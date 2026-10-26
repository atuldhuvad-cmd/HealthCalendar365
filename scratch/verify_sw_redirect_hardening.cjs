// Verifies the sw.js hardening: the cache must hold a NON-redirected navigation entry at rest,
// on a host that 308-redirects /index.html to / (Cloudflare Pages) and on a plain host.
// Also checks offline start and upgrade from the deployed v1.28 / v1.29 workers.
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const BUNDLES = { 'v1.28': process.env.B128, 'v1.29': process.env.B129, 'v1.30': process.env.B130 };
const mime = { '.html': 'text/html', '.js': 'application/javascript', '.json': 'application/json', '.css': 'text/css', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2' };
let serving = 'v1.30', redirecting = true;
const srv = http.createServer((q, r) => {
  let u = decodeURIComponent(new URL(q.url, 'http://x').pathname);
  if (redirecting && u === '/index.html') { r.writeHead(308, { Location: '/' }); return r.end(); }
  if (u === '/') u = '/index.html';
  const f = path.join(BUNDLES[serving], u);
  try { r.writeHead(200, { 'Content-Type': mime[path.extname(f)] || 'application/octet-stream', 'Cache-Control': 'no-cache' }); r.end(fs.readFileSync(f)); }
  catch { r.writeHead(404).end(); }
});

const results = [];
function check(name, pass, detail) { results.push({ name, pass, detail }); console.log(`${pass ? 'PASS' : 'FAIL'} ${name}${detail !== undefined ? ' ' + JSON.stringify(detail) : ''}`); }
const caches_ = p => p.evaluate(async () => { const k = await caches.keys(); const o = {}; for (const n of k) o[n] = (await (await caches.open(n)).keys()).length; return o; }).catch(() => 'no-page-context');
async function waitCache(p, name, n = 264) {
  for (let i = 0; i < 180; i++) { const k = await caches_(p); if (k && k[name] === n) return true; await p.waitForTimeout(1000); }
  return false;
}
// The assertion that matters: what is stored, not what is served.
const storedFlags = (p, name = 'health-poster-v1.30') => p.evaluate(async (n) => {
  const c = await caches.open(n); const o = {};
  for (const u of ['./', './index.html']) { const r = await c.match(u); o[u] = r ? { status: r.status, redirected: r.redirected } : null; }
  return o;
}, name);
// The new worker activates (and deletes old caches) once the old one releases control.
async function waitActivated(p) {
  for (let i = 0; i < 120; i++) {
    const k = await caches_(p);
    if (k && Object.keys(k).length === 1 && k['health-poster-v1.30'] === 264) return true;
    await p.reload({ waitUntil: 'load' }).catch(() => { });
    await p.waitForTimeout(1000);
  }
  return false;
}
const nav = (p, base, u) => p.goto(base + u, { waitUntil: 'load' }).then(() => 'OK').catch(e => 'ERR ' + e.message.slice(0, 50));

(async () => {
  await new Promise(r => srv.listen(0, '127.0.0.1', r));
  const base = 'http://127.0.0.1:' + srv.address().port;
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  try {
    // ---- A. fresh install on a redirecting host ----
    for (const redir of [true, false]) {
      redirecting = redir; serving = 'v1.30';
      const ctx = await browser.newContext(); const p = await ctx.newPage();
      await p.goto(base + '/', { waitUntil: 'load' });
      await p.evaluate(() => navigator.serviceWorker.ready);
      const label = redir ? 'redirecting host' : 'plain host';
      check(`[${label}] installs 264 entries as v1.30`, await waitCache(p, 'health-poster-v1.30'));
      const flags = await storedFlags(p);
      check(`[${label}] cached navigation entries stored NOT redirected`,
        flags['./'] && flags['./'].redirected === false && flags['./index.html'] && flags['./index.html'].redirected === false, flags);
      check(`[${label}] launch /index.html online`, await nav(p, base, '/index.html') === 'OK');
      check(`[${label}] launch / online`, await nav(p, base, '/') === 'OK');
      await ctx.setOffline(true);
      check(`[${label}] launch /index.html offline`, await nav(p, base, '/index.html') === 'OK');
      check(`[${label}] launch / offline`, await nav(p, base, '/') === 'OK');
      const dates = await p.evaluate(() => window.HEALTH_CALENDAR_DATA.length).catch(() => -1);
      check(`[${label}] offline app has 365 dates`, dates === 365, dates);
      await ctx.setOffline(false); await ctx.close();
    }
    // ---- B. upgrade from each deployed worker, on the redirecting host ----
    redirecting = true;
    for (const from of ['v1.28', 'v1.29']) {
      serving = from;
      const ctx = await browser.newContext(); const p = await ctx.newPage();
      await p.goto(base + '/', { waitUntil: 'load' });
      await p.evaluate(() => navigator.serviceWorker.ready);
      check(`[upgrade ${from}->v1.30] old worker installed`, await waitCache(p, 'health-poster-' + from));
      await p.evaluate(() => window.appStorage.saveSettings({ doctorName: 'Hardening Check', useDoctorBranding: false }));
      await p.evaluate(() => window.appStorage.savePhoto('10-26', 2, 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=='));
      if (from === 'v1.28') check('[upgrade v1.28->v1.30] broken worker fails /index.html (reproduces the report)', await nav(p, base, '/index.html') !== 'OK');
      serving = 'v1.30';
      const probe = await ctx.newPage(); await probe.goto(base + '/', { waitUntil: 'load' });
      await probe.evaluate(async () => { const r = await navigator.serviceWorker.getRegistration(); await r.update(); });
      check(`[upgrade ${from}->v1.30] v1.30 cache installed`, await waitCache(probe, 'health-poster-v1.30'));
      const activated = await waitActivated(probe);
      const keys = await caches_(probe);
      check(`[upgrade ${from}->v1.30] old cache removed after activation`, activated && !keys['health-poster-' + from], keys);
      const flags = await storedFlags(probe);
      check(`[upgrade ${from}->v1.30] navigation entries stored NOT redirected`, flags['./index.html'] && flags['./index.html'].redirected === false, flags);
      check(`[upgrade ${from}->v1.30] launch /index.html`, await nav(probe, base, '/index.html') === 'OK');
      await ctx.setOffline(true);
      await probe.goto(base + '/index.html', { waitUntil: 'load' }).catch(() => { });
      await probe.waitForFunction(() => !!window.appStorage).catch(() => { });
      const kept = await probe.evaluate(async () => ({
        name: (await window.appStorage.getSettings() || {}).doctorName,
        photo: await window.appStorage.getPhoto('10-26', 2)
      })).catch(e => ({ err: e.message }));
      check(`[upgrade ${from}->v1.30] settings preserved`, kept.name === 'Hardening Check', kept.name);
      check(`[upgrade ${from}->v1.30] uploaded photo preserved exactly`, kept.photo === 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==');
      await ctx.setOffline(false); await ctx.close();
    }
  } finally {
    fs.writeFileSync(process.env.OUT, JSON.stringify({ scope: 'sw.js hardening: cache stores non-redirected navigation entries', results }, null, 2) + '\n');
    console.log('\n' + results.filter(r => !r.pass).length + ' failed of ' + results.length);
    await browser.close(); srv.close();
  }
})();
