// HISTORICAL (kept for provenance): v1.27 test; its renderer-scope assertion targets v1.26->v1.27 and rejects the v1.28 renderer fixes. Use scratch/verify_all_cphc_framing_v1.28.cjs.
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'review/cphc_framing_2026-10-27');
const baseline = fs.readFileSync(path.join(root, 'review/photo_framing_2026-10-26/originals/canvas-renderer.js'), 'utf8').replace(/\r\n/g, '\n');
const current = fs.readFileSync(path.join(root, 'js/canvas-renderer.js'), 'utf8').replace(/\r\n/g, '\n');
let stripped = current.replace(/^  'cphc_[^']+':[^\n]*\n/gm, '')
  .replace('let badgeY = photoY + 12;', 'const badgeY = photoY + 12;')
  .replace('let badgeX = photoX + 12;', 'const badgeX = photoX + 12;')
  .replace(/^    const verticalCorner = .*\n/m, '')
  .replace(/^    if \(verticalCorner === .*\n/gm, '');
if (stripped !== baseline) throw new Error('Unexpected renderer changes beyond CPHC profiles and optional vertical badge corners');
const profiles = JSON.parse(fs.readFileSync(path.join(out, 'profiles.json')));
for (const dir of ['before', 'after', 'posters']) fs.mkdirSync(path.join(out, dir), { recursive: true });
(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const context = await browser.newContext();
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  try {
    await page.goto('http://127.0.0.1:8765/index.html', { waitUntil: 'networkidle' });
    await page.waitForFunction(() => !!window.healthPosterApp?.currentDay);
    const result = await page.evaluate(async ({ records, baseline }) => {
      const CurrentRenderer = window.HealthPosterRenderer;
      const OldRenderer = new Function(baseline+';return HealthPosterRenderer;')();
      window.HealthPosterRenderer = CurrentRenderer;
      const old = new OldRenderer(), next = new CurrentRenderer();
      await next.ensureFontsReady();
      const output = [], failures = [], sourcePhotos = new Set();
      let renders = 0;
      for (const record of records) {
        const day = window.HEALTH_CALENDAR_DATA.find(d => d.cards.some(c => c.photo === record.image));
        const card = day.cards.find(c => c.photo === record.image);
        const image = await next.loadImage(record.image);
        const oldImage = await old.loadImage(record.image);
        if (!image || !oldImage) throw new Error(record.image+' decode');
        sourcePhotos.add(record.image);
        const actualProfile = PHOTO_FOCUS[record.image.split('/').pop()];
        if (JSON.stringify(actualProfile) !== JSON.stringify(record.profile)) failures.push(record.image+': profile mismatch');
        for (const format of ['square','vertical']) {
          for (const language of ['english','gujarati','bilingual']) {
            next.canvas.width = 485;
            next.canvas.height = format === 'square' ? 380 : 786;
            image.photoFocus = actualProfile;
            next.ctx.fillStyle = '#0B1726'; next.ctx.fillRect(0,0,next.canvas.width,next.canvas.height);
            next[format === 'square' ? 'renderClinicalCardSquare' : 'renderClinicalCardVertical'](next.ctx, { x:0,y:0,index:card.index,card,img:image }, language);
            renders++;
            if (language === 'bilingual') {
              const crop = document.createElement('canvas');
              crop.width = 485; crop.height = format === 'square' ? 230 : 365;
              crop.getContext('2d').drawImage(next.canvas,0,0);
              output.push({ file:'after/'+record.image.split('/').pop().replace('.png',`_${format}.png`), data:crop.toDataURL().split(',')[1] });
              old.canvas.width=485;old.canvas.height=format==='square'?380:786;
              oldImage.photoFocus = null;
              old[format === 'square' ? 'renderClinicalCardSquare' : 'renderClinicalCardVertical'](old.ctx, { x:0,y:0,index:card.index,card,img:oldImage }, language);
              crop.getContext('2d').clearRect(0,0,crop.width,crop.height);
              crop.getContext('2d').drawImage(old.canvas,0,0);
              output.push({ file:'before/'+record.image.split('/').pop().replace('.png',`_${format}.png`), data:crop.toDataURL().split(',')[1] });
            }
          }
        }
      }
      for (const id of ['10-26','10-28','11-04','11-22','11-23']) {
        for (const format of ['square','vertical']) {
          for (const language of ['english','gujarati','bilingual']) {
            const canvas=await next.exportPoster(window.HEALTH_CALENDAR_DATA.find(d=>d.id===id),{format,language,settings:{},customPhotos:{}});
            output.push({file:`posters/${id}_${format}_${language}.png`,data:canvas.toDataURL().split(',')[1]});
          }
        }
      }
      return { renders, sourcePhotos:sourcePhotos.size, failures, output };
    }, { records: profiles.records, baseline });
    for (const file of result.output) fs.writeFileSync(path.join(out,file.file),Buffer.from(file.data,'base64'));
    delete result.output;
    result.errors = errors;
    result.rendererScopeCheck = 'PASS: only CPHC photo profiles and optional CPHC vertical badge corners differ from deployed v1.26';
    result.visualReview = 'PENDING';
    fs.writeFileSync(path.join(out,'verification.json'),JSON.stringify(result,null,2)+'\n');
    console.log(JSON.stringify(result));
    if(errors.length || result.failures.length || result.renders !== 840 || result.sourcePhotos !== 140) process.exitCode=1;
  } finally { await browser.close(); }
})().catch(e=>{console.error(e);process.exitCode=1;});
