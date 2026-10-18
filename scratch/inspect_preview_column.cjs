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
    res.writeHead(200, { 'Content-Type': MIME[path.extname(p).toLowerCase()] || 'application/octet-stream' });
    fs.createReadStream(p).pipe(res);
  } else { res.writeHead(404); res.end(); }
});

server.listen(0, '127.0.0.1', async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 360, height: 740 });
  await page.goto(`http://127.0.0.1:${server.address().port}/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  const analysis = await page.evaluate(() => {
    // Check main layout sections
    const header = document.querySelector('header');
    const quickWeekBar = document.querySelector('.quick-week-bar');
    const studioLayout = document.querySelector('.studio-layout');
    const previewCol = document.querySelector('.preview-column');
    const sidebarCol = document.querySelector('.sidebar-column');

    function elInfo(el, name) {
      if (!el) return null;
      const rect = el.getBoundingClientRect();
      const style = window.getComputedStyle(el);
      return {
        name,
        rectLeft: rect.left,
        rectRight: rect.right,
        rectWidth: rect.width,
        scrollWidth: el.scrollWidth,
        clientWidth: el.clientWidth,
        offsetWidth: el.offsetWidth,
        padding: style.padding,
        margin: style.margin,
        minWidth: style.minWidth,
        maxWidth: style.maxWidth,
        width: style.width
      };
    }

    // Check preview column children
    const previewChildren = Array.from(previewCol.querySelectorAll('*')).map(el => {
      const rect = el.getBoundingClientRect();
      return {
        tag: el.tagName.toLowerCase(),
        id: el.id,
        cls: el.className,
        rectRight: rect.right,
        rectWidth: rect.width,
        scrollWidth: el.scrollWidth
      };
    }).filter(e => e.rectRight > 360 || e.rectWidth > 360);

    // Check header children
    const headerChildren = Array.from(header.querySelectorAll('*')).map(el => {
      const rect = el.getBoundingClientRect();
      return {
        tag: el.tagName.toLowerCase(),
        id: el.id,
        cls: el.className,
        rectRight: rect.right,
        rectWidth: rect.width,
        scrollWidth: el.scrollWidth
      };
    }).filter(e => e.rectRight > 360 || e.rectWidth > 360);

    return {
      docSW: document.documentElement.scrollWidth,
      header: elInfo(header, 'header'),
      quickWeekBar: elInfo(quickWeekBar, 'quick-week-bar'),
      studioLayout: elInfo(studioLayout, 'studio-layout'),
      previewCol: elInfo(previewCol, 'preview-column'),
      sidebarCol: elInfo(sidebarCol, 'sidebar-column'),
      previewWideChildren: previewChildren,
      headerWideChildren: headerChildren
    };
  });

  console.log('Detailed Analysis on 360px:');
  console.log(JSON.stringify(analysis, null, 2));

  await browser.close();
  server.close();
});
