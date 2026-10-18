const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const APP_ROOT = path.resolve(__dirname, '..');

const server = http.createServer((req, res) => {
  let p = path.join(APP_ROOT, req.url.split('?')[0]);
  if (p.endsWith(path.sep)) p = path.join(p, 'index.html');
  if (fs.existsSync(p) && fs.statSync(p).isFile()) {
    const ext = path.extname(p).toLowerCase();
    const mime = {
      '.html': 'text/html',
      '.js': 'application/javascript',
      '.css': 'text/css',
      '.json': 'application/json',
      '.woff2': 'font/woff2',
      '.png': 'image/png'
    };
    res.writeHead(200, { 'Content-Type': mime[ext] || 'application/octet-stream' });
    fs.createReadStream(p).pipe(res);
  } else { res.writeHead(404); res.end(); }
});

const candidateCss = `
/* Responsive Media Queries to eliminate mobile horizontal overflow */
@media (max-width: 900px) {
  .header {
    flex-direction: column;
    align-items: stretch;
    padding: 10px 12px;
    gap: 10px;
  }
  .header-left {
    justify-content: center;
    text-align: center;
  }
  .header-center {
    width: 100%;
    justify-content: center;
    gap: 8px;
  }
  .header-right {
    display: flex;
    justify-content: center;
  }
  .studio-layout {
    grid-template-columns: 1fr;
    padding: 12px;
    gap: 16px;
  }
  .preview-column {
    padding: 12px;
  }
  .sidebar-column {
    max-height: none;
    padding: 14px;
  }
  .export-action-bar {
    grid-template-columns: 1fr;
    gap: 10px;
  }
}

@media (max-width: 640px) {
  .quick-week-bar {
    flex-wrap: wrap;
    padding: 8px 12px;
    gap: 8px;
  }
  .quick-week-scroll {
    order: 3;
    width: 100%;
    flex: 1 1 100%;
  }
  .date-search-box {
    flex: 1;
    min-width: 140px;
  }
  .date-select {
    width: 100%;
    max-width: none;
  }
  .preview-toolbar {
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }
  .toolbar-left {
    display: flex;
    gap: 6px;
  }
  .toolbar-center {
    order: 3;
    width: 100%;
    text-align: center;
  }
  .multi-observance-bar {
    flex-wrap: wrap;
  }
}

@media (max-width: 380px) {
  .segmented-control {
    width: 100%;
  }
  .seg-btn {
    padding: 5px 6px;
    font-size: 0.72rem;
    gap: 4px;
  }
  .seg-badge {
    display: none;
  }
  .btn-tool {
    padding: 4px 8px;
    font-size: 0.72rem;
  }
  .format-indicator {
    font-size: 0.72rem;
    padding: 3px 8px;
  }
}
`;

server.listen(0, '127.0.0.1', async () => {
  const launchOptions = { headless: true };
  if (process.env.PLAYWRIGHT_EXECUTABLE_PATH) launchOptions.executablePath = process.env.PLAYWRIGHT_EXECUTABLE_PATH;
  const browser = await chromium.launch(launchOptions);
  const widths = [320, 360, 390, 412, 768, 1440];

  console.log('--- BASELINE (WITHOUT CSS PATCH) ---');
  for (const w of widths) {
    const page = await browser.newPage();
    await page.setViewportSize({ width: w, height: 800 });
    await page.goto(`http://127.0.0.1:${server.address().port}/`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(400);

    const docSW = await page.evaluate(() => document.documentElement.scrollWidth);
    const pass = docSW <= w;
    console.log(`Width ${w}px: scrollWidth = ${docSW}px | ${pass ? 'PASS' : 'FAIL (+ ' + (docSW - w) + 'px)'}`);
    await page.close();
  }

  console.log('\n--- PROTOTYPE TEST (WITH CANDIDATE CSS PATCH) ---');
  for (const w of widths) {
    const page = await browser.newPage();
    await page.setViewportSize({ width: w, height: 800 });
    await page.goto(`http://127.0.0.1:${server.address().port}/`, { waitUntil: 'networkidle' });
    await page.addStyleTag({ content: candidateCss });
    await page.waitForTimeout(400);

    const docSW = await page.evaluate(() => document.documentElement.scrollWidth);
    const bodySW = await page.evaluate(() => document.body.scrollWidth);
    const pass = docSW <= w;

    // Check overflowing elements if any
    const overflowList = await page.evaluate((width) => {
      return Array.from(document.querySelectorAll('*'))
        .filter(el => el.getBoundingClientRect().right > width + 0.5)
        .map(el => ({ tag: el.tagName, cls: el.className, right: el.getBoundingClientRect().right }));
    }, w);

    console.log(`Width ${w}px: scrollWidth = ${docSW}px, bodySW = ${bodySW}px | ${pass ? 'PASS' : 'FAIL (+ ' + (docSW - w) + 'px)'} | Overflows: ${overflowList.length}`);
    if (overflowList.length > 0) {
      console.log('  Overflowing elements:', overflowList.slice(0, 5));
    }
    await page.close();
  }

  await browser.close();
  server.close();
});
