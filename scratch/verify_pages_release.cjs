// HISTORICAL (kept for provenance): defaults to release v1.26. For v1.28 run: HEALTH_RELEASE=v1.28 HEALTH_ALL_MODES=1 node scratch/verify_pages_release.cjs (assertions unchanged).
const fs = require('fs');
const path = require('path');
const http = require('http');
const crypto = require('crypto');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = path.resolve(__dirname, '..');
const release = process.env.HEALTH_RELEASE || 'v1.26';
const bundle = path.join(root, 'build/cloudflare-pages-' + release);
const allModes = process.env.HEALTH_ALL_MODES === '1';
const checks = [];
const sha256 = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
function check(name, pass, detail) {
  checks.push({ name, pass, detail });
  console.log(`${pass ? 'PASS' : 'FAIL'} ${name}: ${JSON.stringify(detail)}`);
  if (!pass) throw new Error(name);
}
async function waitForCache(page) {
  const deadline = Date.now() + 180000;
  while (Date.now() < deadline) {
    const result = await page.evaluate(async cacheName => {
      const names = await caches.keys();
      if (!names.includes(cacheName)) return 0;
      return (await (await caches.open(cacheName)).keys()).length;
    }, 'health-poster-' + release);
    if (result === 264) return result;
    await new Promise(resolve => setTimeout(resolve, 500));
  }
  throw new Error('Full precache installation timed out');
}
(async () => {
  let browser, server;
  let url = process.argv[2];
  try {
    if (!url) {
      const mime = { '.html': 'text/html', '.js': 'application/javascript', '.json': 'application/json', '.css': 'text/css', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2' };
      server = http.createServer((req, res) => {
        const rel = decodeURIComponent(new URL(req.url, 'http://localhost').pathname).replace(/^\/+/, '') || 'index.html';
        const file = path.resolve(bundle, rel);
        if (!file.startsWith(bundle + path.sep)) { res.writeHead(403).end(); return; }
        try { res.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream' }); res.end(fs.readFileSync(file)); }
        catch { res.writeHead(404).end(); }
      });
      await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
      url = `http://127.0.0.1:${server.address().port}/index.html`;
    }
    browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 180000 });
    check('page loads', response.status() === 200, response.status());
    await page.waitForFunction(() => !!window.healthPosterApp?.currentDay, null, { timeout: 120000 });
    check('365 calendar dates', await page.evaluate(() => window.HEALTH_CALENDAR_DATA.length === 365), 365);
    check('mobile layout fits', await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), '390x844');
    await page.locator('#searchDayInput').fill('diabetes');
    check('search works', await page.locator('#searchResultsList [role="option"]').count() > 0);
    await page.evaluate(() => window.appStorage.saveSettings({ useDoctorBranding: true, doctorName: 'Pages Offline Check', doctorDegree: 'MD', clinicName: 'Isolated browser', contactInfo: '', city: 'Gujarat' }));
    await page.evaluate(async () => { await navigator.serviceWorker.ready; });
    check('complete ' + release + ' offline cache', await waitForCache(page) === 264, 264);
    const parity = await page.evaluate(async cacheName => {
      const cache = await caches.open(cacheName);
      const hashes = {};
      for (const request of await cache.keys()) {
        const response = await cache.match(request);
        const hash = await crypto.subtle.digest('SHA-256', await response.arrayBuffer());
        hashes[new URL(request.url).pathname.replace(/^\//, '') || 'index.html'] = Array.from(new Uint8Array(hash), b => b.toString(16).padStart(2, '0')).join('');
      }
      return hashes;
    }, 'health-poster-' + release);
    const mismatches = Object.entries(parity).filter(([rel, hash]) => hash !== sha256(fs.readFileSync(path.join(bundle, rel)))).map(([rel]) => rel);
    check('cached files match prepared release', mismatches.length === 0, { files: Object.keys(parity).length, mismatches });
    await context.setOffline(true);
    await page.reload({ waitUntil: 'networkidle', timeout: 120000 });
    await page.waitForFunction(() => window.healthPosterApp?.settings?.doctorName === 'Pages Offline Check', null, { timeout: 120000 });
    check('offline launch preserves settings', true);
    const renders = await page.evaluate(async allModes => {
      const app = window.healthPosterApp;
      let count = 0;
      for (const day of window.HEALTH_CALENDAR_DATA) {
        for (const format of (allModes ? ['square','vertical'] : ['square'])) {
          for (const language of (allModes ? ['english','gujarati','bilingual'] : ['bilingual'])) {
            const canvas = await app.renderer.exportPoster(day, { format, language, settings: app.settings, customPhotos: {} });
            if (canvas.width !== 1080 || canvas.height !== (format === 'square' ? 1080 : 1920)) throw new Error(day.id + ' dimensions');
            count++;
          }
        }
      }
      for (const language of (allModes ? [] : ['english', 'gujarati', 'bilingual'])) {
        await app.renderer.renderPoster(window.HEALTH_CALENDAR_DATA.find(d => d.id === '10-26'), { format: 'vertical', language, settings: app.settings, customPhotos: {} });
        count++;
      }
      return count;
    }, allModes);
    check('offline calendar and vertical language renders', renders === (allModes ? 2190 : 368), renders);
    check('no browser exceptions', errors.length === 0, errors);
  } catch (error) { checks.push({ name: 'run completion', pass: false, detail: error.stack }); console.error(error); process.exitCode = 1; }
  finally {
    if (browser) await browser.close();
    if (server) await new Promise(resolve => server.close(resolve));
    const tag = process.argv[2] ? 'published' : 'prepared';
    const reportPath = process.env.HEALTH_REPORT_PATH || path.join(root, `review/cloudflare_${tag}_verification_2026-10-26.json`);
    fs.writeFileSync(reportPath, JSON.stringify({ created_at: new Date().toISOString(), release, url, checks }, null, 2) + '\n');
  }
})();
