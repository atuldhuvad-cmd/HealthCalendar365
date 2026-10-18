const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const APP_ROOT = path.resolve(__dirname, '..');

const MIME = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.woff2': 'font/woff2',
  '.svg': 'image/svg+xml'
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

server.listen(0, '127.0.0.1', async () => {
  const port = server.address().port;
  console.log(`[TEST SERVER] Running on port ${port} serving ${APP_ROOT}`);

  const results = {
    test_run_at: new Date().toISOString(),
    tests: []
  };

  function record(name, pass, details) {
    results.tests.push({ name, pass, details });
    console.log(`[${pass ? 'PASS' : 'FAIL'}] ${name}: ${details}`);
  }

  let browser;
  try {
    const launchOptions = { headless: true };
    if (process.env.PLAYWRIGHT_EXECUTABLE_PATH) launchOptions.executablePath = process.env.PLAYWRIGHT_EXECUTABLE_PATH;
    browser = await chromium.launch(launchOptions);
    const context = await browser.newContext();
    const page = await context.newPage();

    const consoleErrors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });

    // 1. Root loading & basic HTML
    console.log('\n--- Test 1: Root Loading & Metadata ---');
    const resp = await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });
    const status = resp.status();
    const title = await page.title();
    const hasViewport = await page.evaluate(() => !!document.querySelector('meta[name="viewport"]'));
    record('Root URL Loading', status === 200, `HTTP status ${status}`);
    record('Page Title Present', title.length > 0, `Title: "${title}"`);
    record('Mobile Viewport Tag Present', hasViewport, 'Found meta viewport tag');

    // 2. Web App Manifest
    console.log('\n--- Test 2: Web App Manifest (manifest.json) ---');
    const manifestPath = path.join(APP_ROOT, 'manifest.json');
    if (fs.existsSync(manifestPath)) {
      const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
      const hasName = !!manifest.name;
      const hasDisplay = manifest.display === 'standalone';
      const icons = manifest.icons || [];
      const has192 = icons.some(i => i.sizes === '192x192');
      const has512 = icons.some(i => i.sizes === '512x512');
      record('Manifest Syntax & Identity', hasName && hasDisplay, `name: "${manifest.name}", display: "${manifest.display}"`);
      record('Manifest High-Res Icons', has192 && has512, `Total icons: ${icons.length}, has 192x192: ${has192}, has 512x512: ${has512}`);
    } else {
      record('Manifest Exists', false, 'manifest.json not found on disk');
    }

    // 3. Font Loading in Browser Context
    console.log('\n--- Test 3: Typography & Offline Fonts ---');
    const fontInfo = await page.evaluate(async () => {
      await document.fonts.ready;
      return {
        notoSansGujarati: document.fonts.check('bold 24px "Noto Sans Gujarati"') || document.fonts.check('16px "Noto Sans Gujarati"'),
        plusJakartaSans: document.fonts.check('bold 24px "Plus Jakarta Sans"') || document.fonts.check('16px "Plus Jakarta Sans"'),
        totalFontsLoaded: document.fonts.size
      };
    });
    record('Google Fonts Loaded', fontInfo.notoSansGujarati && fontInfo.plusJakartaSans, `Noto Sans Gujarati: ${fontInfo.notoSansGujarati}, Plus Jakarta Sans: ${fontInfo.plusJakartaSans}, Total fonts: ${fontInfo.totalFontsLoaded}`);

    // 4. Calendar Navigation & Data Binding
    console.log('\n--- Test 4: Calendar Navigation & UI State ---');
    const calendarLoaded = await page.evaluate(() => {
      return !!(window.HEALTH_CALENDAR_DATA && window.HEALTH_CALENDAR_DATA.length === 368);
    });
    record('Full Calendar Dataset Loaded', calendarLoaded, `window.HEALTH_CALENDAR_DATA count: ${calendarLoaded ? 368 : 'FAIL'}`);

    // Check date selector / navigation
    const navOk = await page.evaluate(() => {
      const daySelect = document.getElementById('day-select') || document.querySelector('select');
      return !!daySelect;
    });
    record('Calendar UI Controls Present', navOk, 'Date selector UI controls initialized');

    // 5. Canvas Poster Renderer in all formats & languages
    console.log('\n--- Test 5: Dynamic Canvas Poster Rendering ---');
    const testDay = '10-15';
    const formats = ['square', 'vertical'];
    const languages = ['english', 'gujarati', 'bilingual'];

    for (const fmt of formats) {
      for (const lang of languages) {
        const renderResult = await page.evaluate(async ({ dId, f, l }) => {
          const renderer = new window.HealthPosterRenderer();
          const dayData = window.HEALTH_CALENDAR_DATA.find(d => d.id === dId);
          if (!dayData) return { ok: false, error: 'day not found' };
          const canvas = await renderer.renderPoster(dayData, {
            format: f,
            language: l,
            settings: {},
            customPhotos: {}
          });
          return {
            ok: true,
            width: canvas.width,
            height: canvas.height,
            dataUrlLen: canvas.toDataURL('image/png').length
          };
        }, { dId: testDay, f: fmt, l: lang });

        const expectedW = 1080;
        const expectedH = fmt === 'square' ? 1080 : 1920;
        const dimMatch = renderResult.width === expectedW && renderResult.height === expectedH;
        const validPng = renderResult.dataUrlLen > 50000;
        record(`Render ${testDay} [${fmt}] [${lang}]`, dimMatch && validPng, `Dimensions: ${renderResult.width}x${renderResult.height}, PNG DataURL length: ${renderResult.dataUrlLen}`);
      }
    }

    // 6. Service Worker Syntax & Precache Inspection
    console.log('\n--- Test 6: Service Worker Integrity (sw.js) ---');
    const swPath = path.join(APP_ROOT, 'sw.js');
    if (fs.existsSync(swPath)) {
      const swCode = fs.readFileSync(swPath, 'utf-8');
      const hasPrecache = swCode.includes('PRECACHE_ASSETS');
      const hasCacheName = swCode.includes('CACHE_NAME');
      const hasInstall = swCode.includes("addEventListener('install'");
      const hasActivate = swCode.includes("addEventListener('activate'");
      const hasFetch = swCode.includes("addEventListener('fetch'");

      // Extract PRECACHE_ASSETS list
      const precacheMatch = swCode.match(/const\s+PRECACHE_ASSETS\s*=\s*(\[[^\]]+\]);/s);
      let assetCount = 0;
      if (precacheMatch) {
        try {
          const assets = JSON.parse(precacheMatch[1].replace(/'/g, '"').replace(/,\s*\]/, ']'));
          assetCount = assets.length;
        } catch (_) {}
      }

      record('Service Worker Lifecycle Handlers', hasInstall && hasActivate && hasFetch, 'install, activate, and fetch listeners present');
      record('Service Worker Precache Asset List', hasPrecache && assetCount > 0, `Precache asset count: ${assetCount}`);
      const scopedEviction = swCode.includes("key.startsWith('health-poster-')") || swCode.includes('.startsWith(CACHE_PREFIX)');
      record('Scoped Cache Eviction Logic', scopedEviction, 'Cache deletion strictly scoped to owned cache prefix (health-poster-)');
    } else {
      record('Service Worker Present', false, 'sw.js not found on disk');
    }

    // 7. Responsive Mobile Layout (No Horizontal Overflow)
    console.log('\n--- Test 7: Viewport Overflow & Responsive Layout ---');
    const viewports = [
      { width: 320, height: 640, name: 'Ultra-compact Mobile (320px)' },
      { width: 360, height: 740, name: 'Small Mobile (360px)' },
      { width: 390, height: 844, name: 'Mid Mobile (390px)' },
      { width: 412, height: 915, name: 'Modern Android (412px)' },
      { width: 768, height: 1024, name: 'Tablet Portrait (768px)' },
      { width: 1440, height: 900, name: 'Desktop Wide (1440px)' }
    ];

    for (const vp of viewports) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      await page.reload({ waitUntil: 'networkidle' });
      const docSW = await page.evaluate(() => document.documentElement.scrollWidth);
      const overflow = docSW > vp.width;
      record(`Viewport Overflow [${vp.name}]`, !overflow, `scrollWidth: ${docSW} vs innerWidth: ${vp.width}`);
    }

    // 8. Keyboard Accessibility
    console.log('\n--- Test 8: Keyboard Focus & Accessibility ---');
    const interactiveElements = await page.evaluate(() => {
      const buttons = document.querySelectorAll('button, select, input, a[href]');
      return {
        total: buttons.length,
        hasTabindexNegative: Array.from(buttons).filter(b => b.getAttribute('tabindex') === '-1').length
      };
    });
    record('Interactive Elements Focusability', interactiveElements.total > 0, `Found ${interactiveElements.total} focusable controls, ${interactiveElements.hasTabindexNegative} excluded with tabindex=-1`);

    console.log(`\nConsole Errors during testing: ${consoleErrors.length}`);
    record('Zero Browser Console Errors', consoleErrors.length === 0, consoleErrors.length === 0 ? 'No errors' : consoleErrors.join('; '));

    await browser.close();

    // Persist results
    const outPath = path.join(APP_ROOT, 'review', 'automated_browser_pwa_test_results.json');
    fs.writeFileSync(outPath, JSON.stringify(results, null, 2), 'utf-8');
    console.log(`\nWrote automated test results to ${outPath}`);

  } catch (err) {
    console.error('[FATAL BROWSER TEST ERROR]', err);
  } finally {
    server.close();
  }
});
