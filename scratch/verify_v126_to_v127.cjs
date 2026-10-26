// HISTORICAL (kept for provenance): upgrade test v1.26->v1.27. Use scratch/verify_v127_to_v128.cjs for v1.28.
const fs = require('fs');
const path = require('path');
const http = require('http');
const crypto = require('crypto');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = path.resolve(__dirname, '..');
let version = 'v1.26';
const checks = [];
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
function check(name, pass, detail) { checks.push({name,pass,detail}); console.log(`${pass?'PASS':'FAIL'} ${name}`); if(!pass) throw new Error(name); }
const mime = {'.html':'text/html','.js':'application/javascript','.json':'application/json','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.woff2':'font/woff2'};
const server = http.createServer((req,res) => {
  const bundle = path.join(root,'build/cloudflare-pages-'+version);
  const rel = decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/+/, '') || 'index.html';
  const file = path.resolve(bundle,rel);
  if(!file.startsWith(bundle+path.sep)) {res.writeHead(403).end();return;}
  try {res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream','Cache-Control':'no-store'});res.end(fs.readFileSync(file));}
  catch {res.writeHead(404).end();}
});
async function waitCache(page, present, absent) {
  const deadline=Date.now()+120000;
  while(Date.now()<deadline) {
    if(await page.evaluate(async ({present,absent})=>{
      const keys=await caches.keys();
      return keys.includes(present)&&(!absent||!keys.includes(absent))&&(await(await caches.open(present)).keys()).length===264;
    },{present,absent})) return;
    await new Promise(resolve=>setTimeout(resolve,250));
  }
  throw new Error('Cache timeout '+present);
}
(async()=>{
  let browser;
  try {
    await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
    browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
    const context=await browser.newContext();const page=await context.newPage();const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.goto(`http://127.0.0.1:${server.address().port}/index.html`,{waitUntil:'networkidle'});
    await page.evaluate(async()=>{await navigator.serviceWorker.ready;});
    await waitCache(page,'health-poster-v1.26');
    check('preserved v1.26 installs completely',true);
    await page.evaluate(()=>window.appStorage.saveSettings({doctorName:'Upgrade Preservation Check',useDoctorBranding:false}));
    version='v1.27';
    await page.evaluate(async()=>{await(await navigator.serviceWorker.getRegistration()).update();});
    await waitCache(page,'health-poster-v1.27','health-poster-v1.26');
    check('v1.27 installs and removes v1.26 cache',true);
    const paths=['js/canvas-renderer.js','photos/cphc_ent_care_oeee_card1.png'];
    const hashes=await page.evaluate(async paths=>{
      const cache=await caches.open('health-poster-v1.27');const result={};
      for(const rel of paths){const response=await cache.match(new URL('/'+rel,location.origin).href);const digest=await crypto.subtle.digest('SHA-256',await response.arrayBuffer());result[rel]=Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');}
      return result;
    },paths);
    check('updated renderer and photograph have release hashes',paths.every(rel=>hashes[rel]===hash(fs.readFileSync(path.join(root,'build/cloudflare-pages-v1.27',rel)))));
    await context.setOffline(true);await page.reload({waitUntil:'networkidle'});
    await page.waitForFunction(()=>window.healthPosterApp?.settings?.doctorName==='Upgrade Preservation Check');
    check('offline restart preserves existing settings',true);
    const renders=await page.evaluate(async()=>{let count=0;for(const id of ['10-26','11-22','11-23'])for(const format of ['square','vertical'])for(const language of ['english','gujarati','bilingual']){await window.healthPosterApp.renderer.exportPoster(window.HEALTH_CALENDAR_DATA.find(d=>d.id===id),{format,language,settings:window.healthPosterApp.settings,customPhotos:{}});count++;}return count;});
    check('corrected posters render offline after upgrade',renders===18,renders);
    check('no browser exceptions',errors.length===0,errors);
  }catch(error){checks.push({name:'completion',pass:false,detail:error.stack});console.error(error);process.exitCode=1;}
  finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));fs.writeFileSync(path.join(root,'review/cphc_framing_2026-10-27/upgrade_verification.json'),JSON.stringify({scope:'Isolated browser upgrade using complete preserved v1.26 and published v1.27 bundles on one local origin; physical mobile upgrade not tested',checks},null,2)+'\n');}
})();
