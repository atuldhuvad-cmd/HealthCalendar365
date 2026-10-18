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
  console.log(`[DIAG SERVER] Running on port ${port}`);

  const browser = await chromium.launch({ headless: true });
  const viewports = [
    { width: 360, height: 740, name: '360x740' },
    { width: 412, height: 915, name: '412x915' }
  ];

  for (const vp of viewports) {
    const page = await browser.newPage();
    await page.setViewportSize({ width: vp.width, height: vp.height });
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(500);

    const docSW = await page.evaluate(() => document.documentElement.scrollWidth);
    const bodySW = await page.evaluate(() => document.body.scrollWidth);
    const innerW = await page.evaluate(() => window.innerWidth);

    console.log(`\n=== Viewport: ${vp.name} ===`);
    console.log(`window.innerWidth: ${innerW}, doc.scrollWidth: ${docSW}, body.scrollWidth: ${bodySW}`);

    const overflowingElements = await page.evaluate((w) => {
      const all = Array.from(document.querySelectorAll('*'));
      const culprits = [];

      for (const el of all) {
        const rect = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        if (rect.right > w + 0.5 || el.scrollWidth > w) {
          culprits.push({
            tag: el.tagName.toLowerCase(),
            id: el.id || null,
            className: el.className || null,
            rectRight: Math.round(rect.right * 10) / 10,
            rectWidth: Math.round(rect.width * 10) / 10,
            scrollWidth: el.scrollWidth,
            clientWidth: el.clientWidth,
            computedWidth: style.width,
            computedMinWidth: style.minWidth,
            computedMaxWidth: style.maxWidth,
            computedPadding: style.padding,
            computedMargin: style.margin,
            computedDisplay: style.display,
            computedFlex: style.flex,
            computedGridCol: style.gridTemplateColumns,
            parentTag: el.parentElement ? el.parentElement.tagName.toLowerCase() : null,
            parentClass: el.parentElement ? el.parentElement.className : null
          });
        }
      }
      return culprits;
    }, vp.width);

    console.log(`Total elements overflowing ${vp.width}px: ${overflowingElements.length}`);
    // Show top-level overflowing ancestors (elements whose parent is body or main or header)
    const topAncestors = overflowingElements.filter(e => 
      e.parentTag === 'body' || e.parentTag === 'html' || e.tag === 'header' || e.tag === 'section' || e.tag === 'main'
    );
    console.log('Top ancestors exceeding viewport:', JSON.stringify(topAncestors, null, 2));

    // Also look at specific containers
    console.log('\nSample overflowing details (first 10):', JSON.stringify(overflowingElements.slice(0, 10), null, 2));

    await page.close();
  }

  await browser.close();
  server.close();
});
