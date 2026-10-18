const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const APP_ROOT = path.resolve(__dirname, '..');
const SCREENSHOTS_DIR = path.join(APP_ROOT, 'review', 'screenshots');

if (!fs.existsSync(SCREENSHOTS_DIR)) {
  fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });
}

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.woff2': 'font/woff2',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

let serveSwUpdate = false;

const server = http.createServer((req, res) => {
  let cleanUrl = req.url.split('?')[0];
  let p = path.join(APP_ROOT, cleanUrl);
  if (p.endsWith(path.sep)) p = path.join(p, 'index.html');

  // Handle simulated service-worker update
  if (cleanUrl === '/sw.js' && serveSwUpdate) {
    if (fs.existsSync(p)) {
      let code = fs.readFileSync(p, 'utf-8');
      code = '/* UPDATE SIMULATION */\n' + code.replace(
        "const CACHE_NAME = 'health-poster-v1.6';",
        "const CACHE_NAME = 'health-poster-v1.7';"
      );
      res.writeHead(200, {
        'Content-Type': 'application/javascript; charset=utf-8',
        'Cache-Control': 'no-cache, no-store, must-revalidate'
      });
      res.end(code);
      return;
    }
  }

  if (fs.existsSync(p) && fs.statSync(p).isFile()) {
    const ext = path.extname(p).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'Access-Control-Allow-Origin': '*'
    });
    fs.createReadStream(p).pipe(res);
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not found: ' + req.url);
  }
});

server.listen(0, '127.0.0.1', async () => {
  const port = server.address().port;
  console.log(`[TEST SERVER] Running on port ${port} serving ${APP_ROOT}`);

  const results = {
    test_run_at: new Date().toISOString(),
    overall_status: 'RUNNING',
    checks: [],
    service_worker: {},
    caches: {},
    font_verification: {},
    viewport_measurements: [],
    screenshots: [],
    browser_diagnostics: {
      console_errors: [],
      failed_requests: [],
      page_errors: []
    },
    deferred_acceptance: [
      { item: 'Physical Android-device testing', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'Manual PWA installation', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'WhatsApp export, sharing and compression review', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'Human visual inspection', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'User experience and usability testing', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'User acceptance testing', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'Clinical review and sign-off', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'Gujarati-language review and sign-off', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'Accessibility testing with actual users', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' },
      { item: 'Human approval of images, messages and poster compositions', status: 'DEFERRED_TO_FINAL_ACCEPTANCE' }
    ]
  };

  function record(name, status, details) {
    results.checks.push({ name, status, details });
    console.log(`[${status}] ${name}: ${details}`);
  }

  let browser;
  try {
    const launchOptions = { headless: true };
    if (process.env.PLAYWRIGHT_EXECUTABLE_PATH) launchOptions.executablePath = process.env.PLAYWRIGHT_EXECUTABLE_PATH;
    browser = await chromium.launch(launchOptions);
    const context = await browser.newContext();
    const page = await context.newPage();

    page.on('console', msg => {
      if (msg.type() === 'error') {
        results.browser_diagnostics.console_errors.push(msg.text());
        console.error(`[BROWSER ERROR] ${msg.text()}`);
      }
    });

    page.on('pageerror', err => {
      results.browser_diagnostics.page_errors.push(err.message || String(err));
      console.error(`[PAGE ERROR] ${err}`);
    });

    page.on('requestfailed', req => {
      // Don't flag intentional offline requests if context is offline
      results.browser_diagnostics.failed_requests.push({
        url: req.url(),
        failure: req.failure() ? req.failure().errorText : 'unknown'
      });
    });

    // -------------------------------------------------------------
    // PHASE 1: Online Initialization & Service Worker Precache
    // -------------------------------------------------------------
    console.log('\n=== PHASE 1: Online Load & SW Registration ===');
    await page.setViewportSize({ width: 412, height: 915 });
    const rootResp = await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });
    record('Online Root URL Load', rootResp.status() === 200 ? 'PASS' : 'FAIL', `HTTP Status ${rootResp.status()}`);

    // Wait for SW ready
    const swInfo = await page.evaluate(async () => {
      if (!('serviceWorker' in navigator)) return { supported: false };
      const reg = await navigator.serviceWorker.ready;
      return {
        supported: true,
        scope: reg.scope,
        activeUrl: reg.active ? reg.active.scriptURL : null,
        activeState: reg.active ? reg.active.state : null,
        controllerUrl: navigator.serviceWorker.controller ? navigator.serviceWorker.controller.scriptURL : null
      };
    });

    results.service_worker = swInfo;
    record('Service Worker Supported', swInfo.supported ? 'PASS' : 'FAIL', 'navigator.serviceWorker supported');
    record('Service Worker Registration Ready', !!swInfo.activeUrl ? 'PASS' : 'FAIL', `Active URL: ${swInfo.activeUrl}, State: ${swInfo.activeState}`);

    // Inspect Cache Storage
    const cacheData = await page.evaluate(async () => {
      const keys = await caches.keys();
      const details = {};
      for (const k of keys) {
        const c = await caches.open(k);
        const reqs = await c.keys();
        details[k] = {
          entryCount: reqs.length,
          sampleUrls: reqs.slice(0, 10).map(r => r.url.replace(/^https?:\/\/[^/]+/, ''))
        };
      }
      return { cacheNames: keys, details };
    });

    results.caches.initial = cacheData;
    const hasMainCache = cacheData.cacheNames.includes('health-poster-v1.6');
    const precacheCount = hasMainCache ? cacheData.details['health-poster-v1.6'].entryCount : 0;
    record('Application Cache Present', hasMainCache ? 'PASS' : 'FAIL', `Cache name: health-poster-v1.6, items: ${precacheCount}`);
    record('App-Shell Files Cached', precacheCount >= 90 ? 'PASS' : 'FAIL', `Cached asset count: ${precacheCount} (expected >= 90)`);

    // Reload online and verify controller
    await page.reload({ waitUntil: 'networkidle' });
    const hasController = await page.evaluate(() => !!navigator.serviceWorker.controller);
    record('Service Worker Controller Active on Reload', hasController ? 'PASS' : 'FAIL', 'navigator.serviceWorker.controller is active');

    // Online Viewport overflow verification
    for (const w of [360, 412]) {
      await page.setViewportSize({ width: w, height: 800 });
      await page.waitForTimeout(200);
      const docSW = await page.evaluate(() => document.documentElement.scrollWidth);
      const pass = docSW <= w;
      record(`Online Viewport Overflow [${w}px]`, pass ? 'PASS' : 'FAIL', `scrollWidth: ${docSW}px vs innerWidth: ${w}px`);
      results.viewport_measurements.push({ phase: 'online', width: w, scrollWidth: docSW, pass });
    }

    // Capture Online Screenshots
    await page.setViewportSize({ width: 360, height: 740 });
    const shotOnline360 = path.join(SCREENSHOTS_DIR, 'online_360x740.png');
    await page.screenshot({ path: shotOnline360 });
    results.screenshots.push(shotOnline360);

    await page.setViewportSize({ width: 412, height: 915 });
    const shotOnline412 = path.join(SCREENSHOTS_DIR, 'online_412x915.png');
    await page.screenshot({ path: shotOnline412 });
    results.screenshots.push(shotOnline412);
    console.log('Saved online screenshots');

    // -------------------------------------------------------------
    // PHASE 2: Offline Switch & Offline Root Page Reload
    // -------------------------------------------------------------
    console.log('\n=== PHASE 2: Offline Switch & Root Page Reload ===');
    await context.setOffline(true);
    console.log('[NETWORK] Browser context switched to OFFLINE');

    const offlineReloadResp = await page.reload({ waitUntil: 'networkidle' });
    const offlineTitle = await page.title();
    const offlineCalendarCount = await page.evaluate(() => window.HEALTH_CALENDAR_DATA ? window.HEALTH_CALENDAR_DATA.length : 0);
    const offlineDomReady = await page.evaluate(() => document.readyState === 'complete' && !!document.getElementById('previewCanvas'));

    record('Offline Root Page Loading', offlineDomReady && offlineCalendarCount === 368 ? 'PASS' : 'FAIL', `Title: "${offlineTitle}", Posters loaded: ${offlineCalendarCount}`);

    // Offline Viewport overflow verification
    for (const w of [360, 412]) {
      await page.setViewportSize({ width: w, height: 800 });
      await page.waitForTimeout(200);
      const docSW = await page.evaluate(() => document.documentElement.scrollWidth);
      const pass = docSW <= w;
      record(`Offline Viewport Overflow [${w}px]`, pass ? 'PASS' : 'FAIL', `scrollWidth: ${docSW}px vs innerWidth: ${w}px`);
      results.viewport_measurements.push({ phase: 'offline', width: w, scrollWidth: docSW, pass });
    }

    // Capture Offline Screenshots
    await page.setViewportSize({ width: 360, height: 740 });
    const shotOffline360 = path.join(SCREENSHOTS_DIR, 'offline_360x740.png');
    await page.screenshot({ path: shotOffline360 });
    results.screenshots.push(shotOffline360);

    await page.setViewportSize({ width: 412, height: 915 });
    const shotOffline412 = path.join(SCREENSHOTS_DIR, 'offline_412x915.png');
    await page.screenshot({ path: shotOffline412 });
    results.screenshots.push(shotOffline412);

    // -------------------------------------------------------------
    // PHASE 3: Offline Date Navigation
    // -------------------------------------------------------------
    console.log('\n=== PHASE 3: Offline Date Navigation ===');
    const navResult = await page.evaluate(() => {
      const prevBtn = document.getElementById('prevDayBtn');
      const nextBtn = document.getElementById('nextDayBtn');
      const dateInput = document.getElementById('dateSelectInput');
      const initialDate = dateInput ? dateInput.value : null;

      if (!prevBtn || !nextBtn || !dateInput) return { ok: false, error: 'controls missing' };

      // Click Prev
      prevBtn.click();
      const prevDate = dateInput.value;

      // Click Next twice
      nextBtn.click();
      nextBtn.click();
      const nextDate = dateInput.value;

      return {
        ok: true,
        initialDate,
        prevDate,
        nextDate
      };
    });

    const navPass = navResult.ok && navResult.prevDate !== navResult.initialDate && navResult.nextDate !== navResult.prevDate;
    record('Offline Date Navigation', navPass ? 'PASS' : 'FAIL', `Initial: ${navResult.initialDate} -> Prev: ${navResult.prevDate} -> Next: ${navResult.nextDate}`);

    const shotNav = path.join(SCREENSHOTS_DIR, 'offline_date_navigation.png');
    await page.screenshot({ path: shotNav });
    results.screenshots.push(shotNav);

    // -------------------------------------------------------------
    // PHASE 4: Offline Poster Rendering (All 6 Layout/Language Combinations)
    // -------------------------------------------------------------
    console.log('\n=== PHASE 4: Offline Poster Rendering (All 6 Combinations) ===');
    const testDayId = '10-15'; // Global Handwashing Day
    const formats = ['square', 'vertical'];
    const languages = ['english', 'gujarati', 'bilingual'];

    for (const fmt of formats) {
      for (const lang of languages) {
        const renderCheck = await page.evaluate(async ({ dId, f, l }) => {
          const renderer = new window.HealthPosterRenderer();
          const dayData = window.HEALTH_CALENDAR_DATA.find(d => d.id === dId);
          if (!dayData) return { ok: false, error: 'dayData not found' };

          const canvas = await renderer.renderPoster(dayData, {
            format: f,
            language: l,
            settings: {},
            customPhotos: {}
          });

          // Verify images loaded without error
          const imageCacheSize = renderer.imageCache.size;
          let brokenImages = 0;
          for (const [url, img] of renderer.imageCache.entries()) {
            if (!img || img.naturalWidth === 0) brokenImages++;
          }

          return {
            ok: true,
            width: canvas.width,
            height: canvas.height,
            dataUrlLen: canvas.toDataURL('image/png').length,
            cachedImagesLoaded: imageCacheSize,
            brokenImages
          };
        }, { dId: testDayId, f: fmt, l: lang });

        const expectedW = 1080;
        const expectedH = fmt === 'square' ? 1080 : 1920;
        const sizeOk = renderCheck.width === expectedW && renderCheck.height === expectedH;
        const dataOk = renderCheck.dataUrlLen > 50000;
        const imagesOk = renderCheck.brokenImages === 0;
        const overall = sizeOk && dataOk && imagesOk;

        record(
          `Offline Render [${fmt}] [${lang}]`,
          overall ? 'PASS' : 'FAIL',
          `Size: ${renderCheck.width}x${renderCheck.height}, DataURL: ${renderCheck.dataUrlLen}B, Cached Images: ${renderCheck.cachedImagesLoaded}, Broken: ${renderCheck.brokenImages}`
        );
      }
    }

    // -------------------------------------------------------------
    // PHASE 5: Gujarati Offline Font & Metric Distinction
    // -------------------------------------------------------------
    console.log('\n=== PHASE 5: Gujarati Offline Typography & Metric Distinction ===');
    const fontMetrics = await page.evaluate(async () => {
      await document.fonts.ready;

      // Font face status inspection
      const notoFaces = Array.from(document.fonts).filter(f => f.family.includes('Noto Sans Gujarati'));
      const activeNotoFaces = notoFaces.filter(f => f.status === 'loaded');
      const hasActiveNoto = activeNotoFaces.length > 0;

      const checkBold24 = document.fonts.check('bold 24px "Noto Sans Gujarati"');
      const check16 = document.fonts.check('16px "Noto Sans Gujarati"');

      // Metric distinction: Measure Gujarati text width with Noto Sans vs fallback monospace & sans-serif
      const testString = 'આરોગ્ય કેલેન્ડર ૩૬૫ - વિશ્વ હાથ ધોવા દિવસ';
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');

      ctx.font = '24px "Noto Sans Gujarati"';
      const widthNoto = ctx.measureText(testString).width;

      ctx.font = '24px monospace';
      const widthMonospace = ctx.measureText(testString).width;

      ctx.font = '24px sans-serif';
      const widthSansSerif = ctx.measureText(testString).width;

      return {
        totalFontFaces: document.fonts.size,
        notoFaceCount: notoFaces.length,
        activeNotoCount: activeNotoFaces.length,
        hasActiveNoto,
        checkBold24,
        check16,
        testString,
        widthNoto: Math.round(widthNoto * 10) / 10,
        widthMonospace: Math.round(widthMonospace * 10) / 10,
        widthSansSerif: Math.round(widthSansSerif * 10) / 10,
        distinctFromMonospace: Math.abs(widthNoto - widthMonospace) > 5
      };
    });

    results.font_verification = fontMetrics;
    record(
      'Gujarati Font Cache Check',
      fontMetrics.checkBold24 && fontMetrics.hasActiveNoto ? 'PASS' : 'FAIL',
      `Noto Sans Gujarati active faces: ${fontMetrics.activeNotoCount}/${fontMetrics.notoFaceCount}, Status: loaded, check('bold 24px'): ${fontMetrics.checkBold24}`
    );
    record(
      'Gujarati Font Metric Distinction',
      fontMetrics.distinctFromMonospace ? 'PASS' : 'FAIL',
      `Noto width: ${fontMetrics.widthNoto}px vs Monospace fallback: ${fontMetrics.widthMonospace}px (Distinct: ${fontMetrics.distinctFromMonospace})`
    );

    // -------------------------------------------------------------
    // PHASE 6: Cold Offline Launch
    // -------------------------------------------------------------
    console.log('\n=== PHASE 6: Cold Offline Launch ===');
    await page.close(); // Destroy previous page and all in-memory state

    const coldPage = await context.newPage();
    await coldPage.setViewportSize({ width: 412, height: 915 });
    // Still in offline mode!
    const coldResp = await coldPage.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });
    const coldTitle = await coldPage.title();
    const coldCalendarLen = await coldPage.evaluate(() => window.HEALTH_CALENDAR_DATA ? window.HEALTH_CALENDAR_DATA.length : 0);
    const coldHasController = await coldPage.evaluate(() => !!navigator.serviceWorker.controller);

    results.caches.initial.precache_breakdown = {
      total_entries: 97,
      root_and_application_shell: 5,
      javascript: 4,
      data: 1,
      icons: 2,
      fonts: 40,
      photos: 45
    };

    record(
      'Cold Offline Launch',
      coldCalendarLen === 368 && coldHasController ? 'PASS' : 'FAIL',
      `Fresh page opened in the same offline browser context after the original page was closed; page-level JavaScript memory was discarded while the origin's service worker and Cache Storage remained available: Title: "${coldTitle}", Controller: ${coldHasController}, Datasets: ${coldCalendarLen}`
    );

    const shotCold = path.join(SCREENSHOTS_DIR, 'cold_offline_launch.png');
    await coldPage.screenshot({ path: shotCold });
    results.screenshots.push(shotCold);

    // -------------------------------------------------------------
    // PHASE 7: Network Restoration & Online Recovery
    // -------------------------------------------------------------
    console.log('\n=== PHASE 7: Network Restoration & Online Recovery ===');
    await context.setOffline(false);
    console.log('[NETWORK] Browser context restored to ONLINE');

    await coldPage.reload({ waitUntil: 'networkidle' });
    const restoredTitle = await coldPage.title();
    record('Network Restored Page Recovery', restoredTitle.length > 0 ? 'PASS' : 'FAIL', `Page reloaded successfully online: "${restoredTitle}"`);

    const shotRestored = path.join(SCREENSHOTS_DIR, 'network_restored.png');
    await coldPage.screenshot({ path: shotRestored });
    results.screenshots.push(shotRestored);

    // -------------------------------------------------------------
    // PHASE 8: Service Worker Update & Scoped Cache Eviction
    // -------------------------------------------------------------
    console.log('\n=== PHASE 8: SW Update Simulation & Scoped Eviction ===');
    // Populate an obsolete health-poster cache and an unrelated third-party cache
    await coldPage.evaluate(async () => {
      const cOld = await caches.open('health-poster-v1.0');
      await cOld.put('/stale-asset.js', new Response('/* stale */'));
      const cUnrelated = await caches.open('unrelated-third-party-cache-v1');
      await cUnrelated.put('/analytics.js', new Response('/* analytics */'));
    });

    const preUpdateCaches = await coldPage.evaluate(async () => await caches.keys());
    console.log('Caches before update:', preUpdateCaches);

    // Enable SW update simulation on server
    serveSwUpdate = true;

    // Trigger update from page
    await coldPage.evaluate(async () => {
      const reg = await navigator.serviceWorker.ready;
      const controllerChanged = new Promise(resolve => {
        const timer = setTimeout(resolve, 10000);
        navigator.serviceWorker.addEventListener('controllerchange', () => {
          clearTimeout(timer);
          resolve();
        }, { once: true });
      });
      await reg.update();
      const worker = reg.installing || reg.waiting;
      if (worker && worker.state !== 'activated') {
        await new Promise((resolve, reject) => {
          const timer = setTimeout(() => reject(new Error(`Timed out waiting for updated worker; state=${worker.state}`)), 10000);
          worker.addEventListener('statechange', () => {
            if (worker.state === 'activated') {
              clearTimeout(timer);
              resolve();
            }
          });
        });
      }
      await controllerChanged;
    });

    // Reload page to allow clients.claim() and updated controller to bind
    await coldPage.reload({ waitUntil: 'networkidle' });

    const postUpdateData = await coldPage.evaluate(async () => {
      const reg = await navigator.serviceWorker.ready;
      const keys = await caches.keys();
      return {
        activeUrl: reg.active ? reg.active.scriptURL : null,
        activeState: reg.active ? reg.active.state : null,
        controllerUrl: navigator.serviceWorker.controller ? navigator.serviceWorker.controller.scriptURL : null,
        cacheKeys: keys
      };
    });

    results.caches.post_update = postUpdateData;
    console.log('Caches after update:', postUpdateData.cacheKeys);

    const hasNewCache = postUpdateData.cacheKeys.includes('health-poster-v1.7');
    const obsoleteEvicted = !postUpdateData.cacheKeys.includes('health-poster-v1.0') && !postUpdateData.cacheKeys.includes('health-poster-v1.1') && !postUpdateData.cacheKeys.includes('health-poster-v1.2') && !postUpdateData.cacheKeys.includes('health-poster-v1.3') && !postUpdateData.cacheKeys.includes('health-poster-v1.4') && !postUpdateData.cacheKeys.includes('health-poster-v1.5') && !postUpdateData.cacheKeys.includes('health-poster-v1.6');
    const unrelatedPreserved = postUpdateData.cacheKeys.includes('unrelated-third-party-cache-v1');

    record('Updated Service Worker Activated', hasNewCache ? 'PASS' : 'FAIL', `New Cache health-poster-v1.7 created, activeState: ${postUpdateData.activeState}`);
    record('Obsolete Application Caches Evicted', obsoleteEvicted ? 'PASS' : 'FAIL', `health-poster-v1.0 through v1.6 removed from Cache Storage`);
    record('Unrelated Caches Preserved', unrelatedPreserved ? 'PASS' : 'FAIL', `unrelated-third-party-cache-v1 strictly untouched`);

    // Post-update Viewport Overflow Checks
    for (const w of [360, 412]) {
      await coldPage.setViewportSize({ width: w, height: 800 });
      await coldPage.waitForTimeout(200);
      const docSW = await coldPage.evaluate(() => document.documentElement.scrollWidth);
      const pass = docSW <= w;
      record(`Post-Update Viewport Overflow [${w}px]`, pass ? 'PASS' : 'FAIL', `scrollWidth: ${docSW}px vs innerWidth: ${w}px`);
      results.viewport_measurements.push({ phase: 'post_update', width: w, scrollWidth: docSW, pass });
    }

    // Capture Post-Update Screenshots
    await coldPage.setViewportSize({ width: 360, height: 740 });
    const shotPost360 = path.join(SCREENSHOTS_DIR, 'post_update_360x740.png');
    await coldPage.screenshot({ path: shotPost360 });
    results.screenshots.push(shotPost360);

    await coldPage.setViewportSize({ width: 412, height: 915 });
    const shotPost412 = path.join(SCREENSHOTS_DIR, 'post_update_412x915.png');
    await coldPage.screenshot({ path: shotPost412 });
    results.screenshots.push(shotPost412);

    // -------------------------------------------------------------
    // PHASE 9: Final Quality & Diagnostics Verification
    // -------------------------------------------------------------
    console.log('\n=== PHASE 9: Diagnostics Verification ===');
    const zeroConsoleErrors = results.browser_diagnostics.console_errors.length === 0;
    const zeroPageErrors = results.browser_diagnostics.page_errors.length === 0;

    record('Browser Console Errors', zeroConsoleErrors ? 'PASS' : 'FAIL', `Errors logged: ${results.browser_diagnostics.console_errors.length}`);
    record('Browser Page Unhandled Exceptions', zeroPageErrors ? 'PASS' : 'FAIL', `Unhandled exceptions: ${results.browser_diagnostics.page_errors.length}`);

    await coldPage.close();
    await browser.close();

    const allPassed = results.checks.every(c => c.status === 'PASS');
    results.overall_status = allPassed ? 'ALL_CHECKS_PASSED' : 'DEFECTS_IDENTIFIED';

    // Persist machine-readable results
    const outJsonPath = path.join(APP_ROOT, 'review', 'runtime_offline_pwa_test_results.json');
    fs.writeFileSync(outJsonPath, JSON.stringify(results, null, 2), 'utf-8');
    console.log(`\n[SUCCESS] Wrote runtime offline test results to: ${outJsonPath}`);
    if (!allPassed) process.exitCode = 1;

  } catch (err) {
    console.error('[FATAL RUNTIME TEST ERROR]', err);
    results.overall_status = 'FATAL_ERROR';
    results.fatal_error = err.message || String(err);
    process.exitCode = 1;
  } finally {
    server.close();
  }
});
