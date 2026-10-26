// Renders every date x format x language and records the SHA-256 of the full PNG bytes.
const fs=require('fs');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const b=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 const p=await (await b.newContext()).newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.goto(process.env.BASE,{waitUntil:'networkidle'}); await p.waitForFunction(()=>!!window.healthPosterApp?.currentDay);
 const r=await p.evaluate(async()=>{
  const R=new window.HealthPosterRenderer(); await R.ensureFontsReady(); const out={};
  for(const d of window.HEALTH_CALENDAR_DATA) for(const f of ['square','vertical']) for(const l of ['english','gujarati','bilingual']){
   const c=await R.renderPoster(d,{format:f,language:l,settings:{},customPhotos:{}});
   const id=c.getContext('2d').getImageData(0,0,c.width,c.height); const buf=id.data.buffer;
   const h=await crypto.subtle.digest('SHA-256',buf); out[d.id+'|'+f+'|'+l]=[...new Uint8Array(h)].map(x=>x.toString(16).padStart(2,'0')).join('')+':'+buf.byteLength;}
  return out;});
 fs.writeFileSync(process.env.OUT,JSON.stringify({base:process.env.BASE,count:Object.keys(r).length,errs,hashes:r}));
 console.log(process.env.OUT,Object.keys(r).length,errs.length); await b.close();})();
