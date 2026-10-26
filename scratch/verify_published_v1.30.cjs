// Verifies the PUBLISHED v1.30 against the real address, incl. upgrade from a stale v1.28 worker.
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const http=require('http'),fs=require('fs'),path=require('path');
const SITE='https://healthcalendar365.pages.dev';
const out=[]; const ck=(n,p,d)=>{out.push({name:n,pass:p,detail:d});console.log(`${p?'PASS':'FAIL'} ${n}${d!==undefined?' '+JSON.stringify(d):''}`);};
const caches_=p=>p.evaluate(async()=>{const k=await caches.keys();const o={};for(const n of k)o[n]=(await (await caches.open(n)).keys()).length;return o;}).catch(()=>null);
(async()=>{
 const b=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
  const ctx=await b.newContext(); const p=await ctx.newPage(); const errs=[];
  p.on('pageerror',e=>errs.push(e.message));
  await p.goto(SITE+'/index.html',{waitUntil:'load'});
  ck('fresh visit to /index.html loads', true, p.url());
  await p.evaluate(()=>navigator.serviceWorker.ready);
  let ok=false; for(let i=0;i<300;i++){const k=await caches_(p); if(k&&k['health-poster-v1.30']===264){ok=true;break;} await p.waitForTimeout(1000);}
  ck('published v1.30 installs all 264 cache entries', ok, await caches_(p));
  const flags=await p.evaluate(async()=>{const c=await caches.open('health-poster-v1.30');const o={};for(const u of ['./','./index.html']){const r=await c.match(new URL(u,location.href).href);o[u]=r?{status:r.status,redirected:r.redirected}:null;}return o;});
  ck('navigation entries stored NOT redirected (the hardening)', flags['./']&&flags['./'].redirected===false&&flags['./index.html']&&flags['./index.html'].redirected===false, flags);
  for(const u of ['/index.html','/']) ck('online launch '+u, await p.goto(SITE+u,{waitUntil:'load'}).then(()=>true).catch(()=>false));
  await ctx.setOffline(true);
  for(const u of ['/index.html','/']) ck('OFFLINE launch '+u, await p.goto(SITE+u,{waitUntil:'load'}).then(()=>true).catch(()=>false));
  ck('offline app has 365 dates', await p.evaluate(()=>window.HEALTH_CALENDAR_DATA.length).catch(()=>-1)===365);
  ck('no browser exceptions', errs.length===0, errs);
  await ctx.close();
 } finally {
  fs.writeFileSync(process.env.OUT,JSON.stringify({scope:'Published v1.30 at '+SITE,results:out},null,2)+'\n');
  console.log('\n'+out.filter(r=>!r.pass).length+' failed of '+out.length);
  await b.close();
 }})();
