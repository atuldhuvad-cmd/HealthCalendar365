const fs=require('fs'),path=require('path'),http=require('http');
const {chromium}=require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..'),out=path.join(root,'review/installed_start_fix_2026-10-27');fs.mkdirSync(out,{recursive:true});
let version='v1.28';const checks=[];
function check(name,pass,detail){checks.push({name,pass,detail});console.log(`${pass?'PASS':'FAIL'} ${name}`);if(!pass)throw new Error(name);}
const mime={'.html':'text/html','.js':'application/javascript','.json':'application/json','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.woff2':'font/woff2'};
const server=http.createServer((req,res)=>{const u=new URL(req.url,'http://localhost');if(u.pathname==='/index.html'){res.writeHead(308,{Location:'/'}).end();return;}const base=path.join(root,'build/cloudflare-pages-'+version),rel=decodeURIComponent(u.pathname).replace(/^\/+/, '')||'index.html',file=path.resolve(base,rel);if(!file.startsWith(base+path.sep)){res.writeHead(403).end();return;}try{res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream','Cache-Control':'no-store'});res.end(fs.readFileSync(file));}catch{res.writeHead(404).end();}});
async function waitCache(page,name,absent){const until=Date.now()+120000;while(Date.now()<until){if(await page.evaluate(async({name,absent})=>{const keys=await caches.keys();return keys.includes(name)&&(!absent||!keys.includes(absent))&&(await(await caches.open(name)).keys()).length===264;},{name,absent}))return;await new Promise(r=>setTimeout(r,250));}throw new Error('cache timeout');}
(async()=>{let browser;try{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin=`http://127.0.0.1:${server.address().port}`;
 browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 const context=await browser.newContext();let page=await context.newPage();
 await page.goto(origin+'/',{waitUntil:'networkidle'});await page.evaluate(async()=>{await navigator.serviceWorker.ready;});await waitCache(page,'health-poster-v1.28');
 let oldFailed=false;try{await page.goto(origin+'/index.html',{waitUntil:'networkidle'});}catch(e){oldFailed=/ERR_FAILED/.test(e.message);}
 check('v1.28 reproduces installed start ERR_FAILED behind host redirect',oldFailed);
 await page.close();page=await context.newPage();
 await page.goto(origin+'/',{waitUntil:'networkidle'});await page.waitForFunction(()=>!!window.healthPosterApp?.currentDay);
 const photo='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==';
 await page.evaluate(async photo=>{await window.appStorage.saveSettings({doctorName:'Start URL Preservation',useDoctorBranding:false});await window.appStorage.savePhoto('10-26',2,photo);},photo);
 version='v1.29';await page.evaluate(async()=>{await(await navigator.serviceWorker.getRegistration()).update();});await waitCache(page,'health-poster-v1.29','health-poster-v1.28');
 check('upgrade installs v1.29 and removes old cache',true);
 for(const offline of [false,true]){await context.setOffline(offline);for(const suffix of ['/index.html','/','/index.html']){const response=await page.goto(origin+suffix,{waitUntil:'networkidle'});await page.waitForFunction(()=>!!window.healthPosterApp?.currentDay);check(`${offline?'offline':'online'} launch ${suffix}`,response.status()===200);}}
 check('settings retained',await page.evaluate(()=>window.healthPosterApp.settings.doctorName==='Start URL Preservation'));
 check('uploaded photo retained exactly',await page.evaluate(async photo=>(await window.appStorage.getPhoto('10-26',2))===photo,photo));
 const manifest=await page.evaluate(async()=>await(await fetch('./manifest.json')).json());check('canonical launch with preserved original identity',manifest.start_url==='./'&&manifest.id==='./index.html'&&manifest.scope==='./');
 await page.evaluate(async()=>{await(await caches.open('health-poster-v1.29')).delete('./index.html');});const fallback=await page.goto(origin+'/index.html',{waitUntil:'networkidle'});check('offline missing-index fallback uses cached root',fallback.status()===200);
 await page.evaluate(async()=>{const c=await caches.open('health-poster-v1.29');await c.delete('./');await c.delete('./index.html');});const unavailable=await page.goto(origin+'/index.html',{waitUntil:'networkidle'});check('missing offline shell gives readable 503, not ERR_FAILED',unavailable.status()===503&&(await page.locator('body').innerText()).includes('Connect to the internet'));
}catch(e){checks.push({name:'completion',pass:false,detail:e.stack});console.error(e);process.exitCode=1;}finally{if(browser)await browser.close();await new Promise(r=>server.close(r));fs.writeFileSync(path.join(out,'regression_verification.json'),JSON.stringify({checks},null,2)+'\n');}})();
