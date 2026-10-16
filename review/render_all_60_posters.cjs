const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

// Robust root and output path resolution
const args = process.argv.slice(2);
let customAppRoot = null;
let customOutDir = null;
let singleTest = false;

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--out-dir' && args[i + 1]) {
    customOutDir = path.resolve(args[i + 1]);
    i++;
  } else if (args[i] === '--app-root' && args[i + 1]) {
    customAppRoot = path.resolve(args[i + 1]);
    i++;
  } else if (args[i] === '--test-one') {
    singleTest = true;
  }
}

const APP_ROOT = customAppRoot || path.resolve(__dirname, '..');
const OUTPUT_DIR = customOutDir || path.join(__dirname, 'rendered_posters');

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

const MIME = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.woff2': 'font/woff2'
};

const server = http.createServer((req, res) => {
  let cleanUrl = req.url.split('?')[0];
  let p = path.join(APP_ROOT, cleanUrl);
  if (p.endsWith(path.sep)) p = path.join(p, 'index.html');
  if (fs.existsSync(p) && fs.statSync(p).isFile()) {
    const ext = path.extname(p).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'Access-Control-Allow-Origin': '*'
    });
    fs.createReadStream(p).pipe(res);
  } else {
    res.writeHead(404);
    res.end('Not found: ' + req.url);
  }
});

const ALL_DAYS = ['10-15', '10-15-cane', '10-16', '10-16-spine', '10-17', '10-18', '10-19', '10-19-oral', '10-20', '10-21'];
const DAYS = singleTest ? ['10-15'] : ALL_DAYS;
const FORMATS = singleTest ? ['square'] : ['square', 'vertical'];
const LANGUAGES = singleTest ? ['bilingual'] : ['english', 'gujarati', 'bilingual'];

server.listen(0, '127.0.0.1', async () => {
  const port = server.address().port;
  console.log(`[HTTP SERVER] Running on port ${port} serving APP_ROOT: ${APP_ROOT}`);
  console.log(`[OUTPUT DIR] Saving posters to: ${OUTPUT_DIR}`);
  if (singleTest) console.log('[MODE] Running single representative render test (--test-one)');

  let browser;
  try {
    browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    const pageErrors = [];
    page.on('pageerror', e => pageErrors.push(e.message));
    page.on('console', msg => {
      if (msg.type() === 'error') pageErrors.push(msg.text());
    });

    console.log(`[BROWSER] Navigating to http://127.0.0.1:${port}/ ...`);
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => window.HEALTH_CALENDAR_DATA && window.HealthPosterRenderer);

    const fontStatus = await page.evaluate(async () => {
      await document.fonts.ready;
      return {
        notoSansGujarati: document.fonts.check('bold 24px "Noto Sans Gujarati"') || document.fonts.check('16px "Noto Sans Gujarati"'),
        plusJakartaSans: document.fonts.check('bold 24px "Plus Jakarta Sans"') || document.fonts.check('16px "Plus Jakarta Sans"'),
        totalFontsLoaded: document.fonts.size
      };
    });
    console.log('[FONTS LOADED IN BROWSER CONTEXT]', fontStatus);

    const manifestResults = [];
    let count = 0;
    const total = DAYS.length * FORMATS.length * LANGUAGES.length;

    for (const dayId of DAYS) {
      for (const format of FORMATS) {
        for (const language of LANGUAGES) {
          count++;
          const filename = `poster_${dayId}_${format}_${language}.png`;
          const filePath = path.join(OUTPUT_DIR, filename);

          const renderInfo = await page.evaluate(async ({ dId, fmt, lang }) => {
            const renderer = new HealthPosterRenderer();
            const dayData = window.HEALTH_CALENDAR_DATA.find(d => d.id === dId);
            if (!dayData) return { error: `Day ${dId} not found in calendar data` };

            const c = await renderer.renderPoster(dayData, {
              format: fmt,
              language: lang,
              settings: {},
              customPhotos: {}
            });

            const cardPhotos = (dayData.cards || []).map(c => c.photo || c.image);
            const imageCacheStatus = cardPhotos.map(p => ({
              path: p,
              cached: renderer.imageCache.has(p),
              loaded: renderer.imageCache.get(p) ? (renderer.imageCache.get(p).naturalWidth > 0) : false
            }));

            const dataUrl = c.toDataURL('image/png');
            return {
              width: c.width,
              height: c.height,
              dataUrl,
              cardPhotos: imageCacheStatus,
              dayTitleEn: dayData.title_en,
              dayTitleGu: dayData.title_gu
            };
          }, { dId: dayId, fmt: format, lang: language });

          if (renderInfo.error) {
            console.error(`[ERROR] (${count}/${total}) ${filename}: ${renderInfo.error}`);
            manifestResults.push({
              file: filename,
              day_id: dayId,
              format,
              language,
              technical_render_status: 'FAIL',
              visual_review_status: 'PENDING_HUMAN_REVIEW',
              clinical_review_status: 'PENDING_CLINICAL_REVIEW',
              mobile_delivery_status: 'NOT_TESTED',
              error: renderInfo.error
            });
            continue;
          }

          const base64Data = renderInfo.dataUrl.replace(/^data:image\/png;base64,/, '');
          const buffer = Buffer.from(base64Data, 'base64');
          fs.writeFileSync(filePath, buffer);

          const expectedWidth = 1080;
          const expectedHeight = (format === 'vertical') ? 1920 : 1080;
          const dimMatch = (renderInfo.width === expectedWidth && renderInfo.height === expectedHeight);
          const allImagesLoaded = renderInfo.cardPhotos.every(p => p.loaded);

          manifestResults.push({
            file: filename,
            day_id: dayId,
            format,
            language,
            width: renderInfo.width,
            height: renderInfo.height,
            dimensions_correct: dimMatch,
            bytes: buffer.length,
            card_photos_loaded: allImagesLoaded,
            photo_details: renderInfo.cardPhotos,
            // Explicitly separated status layers:
            technical_render_status: (dimMatch && allImagesLoaded) ? 'STRUCTURAL_RENDER_PASS' : 'STRUCTURAL_RENDER_WARNING',
            visual_review_status: 'PENDING_HUMAN_REVIEW',
            clinical_review_status: 'PENDING_CLINICAL_REVIEW',
            mobile_delivery_status: 'NOT_TESTED'
          });

          console.log(`[OK] (${count}/${total}) ${filename} [${renderInfo.width}x${renderInfo.height}] ${(buffer.length / 1024).toFixed(1)} KB | Photos loaded: ${allImagesLoaded ? '4/4' : 'PARTIAL'}`);
        }
      }
    }

    const summary = {
      notice: "UNAPPROVED REVIEW ARTIFACTS: Render manifest captures technical rendering parameters. Visual inspection, clinical correctness, and mobile delivery remain separate pending gates.",
      total_renders: count,
      technical_structural_pass: manifestResults.filter(r => r.technical_render_status === 'STRUCTURAL_RENDER_PASS').length,
      technical_structural_warning: manifestResults.filter(r => r.technical_render_status === 'STRUCTURAL_RENDER_WARNING').length,
      technical_structural_fail: manifestResults.filter(r => r.technical_render_status === 'FAIL').length,
      visual_review_pending: manifestResults.length,
      clinical_review_pending: manifestResults.length,
      mobile_delivery_not_tested: manifestResults.length,
      font_status: fontStatus,
      page_errors: pageErrors,
      rendered_at: new Date().toISOString(),
      renders: manifestResults
    };

    fs.writeFileSync(
      path.join(OUTPUT_DIR, 'render_manifest.json'),
      JSON.stringify(summary, null, 2),
      'utf-8'
    );

    console.log('\n======================================================');
    console.log(`COMPLETED ${count} POSTER RENDERS.`);
    console.log(`Technical Structural Status: ${summary.technical_structural_pass} STRUCTURAL_RENDER_PASS, ${summary.technical_structural_warning} WARNING, ${summary.technical_structural_fail} FAIL`);
    console.log(`Governance Status: Visual Review PENDING (${summary.visual_review_pending}), Clinical Review PENDING (${summary.clinical_review_pending}), Mobile Delivery NOT TESTED (${summary.mobile_delivery_not_tested})`);
    console.log(`Manifest saved to ${path.join(OUTPUT_DIR, 'render_manifest.json')}`);
    console.log('======================================================');

    await browser.close();
  } catch (err) {
    console.error('[FATAL RENDER ERROR]', err);
  } finally {
    server.close();
  }
});
