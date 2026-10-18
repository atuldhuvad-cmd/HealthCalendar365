const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('C:/Users/dhuva/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const APP_ROOT = path.resolve(__dirname, '..');
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.woff2': 'font/woff2'
};

const server = http.createServer((req, res) => {
  const cleanUrl = req.url.split('?')[0];
  let filePath = path.join(APP_ROOT, cleanUrl);
  if (filePath.endsWith(path.sep)) filePath = path.join(filePath, 'index.html');
  if (!filePath.startsWith(APP_ROOT) || !fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
    res.writeHead(404);
    res.end('Not found');
    return;
  }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(filePath).toLowerCase()] || 'application/octet-stream' });
  fs.createReadStream(filePath).pipe(res);
});

(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = server.address().port;
  const launchOptions = { headless: true };
  if (process.env.PLAYWRIGHT_EXECUTABLE_PATH) launchOptions.executablePath = process.env.PLAYWRIGHT_EXECUTABLE_PATH;
  const browser = await chromium.launch(launchOptions);
  const page = await browser.newPage();
  try {
    await page.addInitScript(() => {
      window.__canShareFiles = true;
      window.__shareCalls = [];
      window.__downloadClicks = 0;
      window.__windowOpenCalls = 0;
      Object.defineProperty(navigator, 'canShare', {
        configurable: true,
        value: data => window.__canShareFiles && Array.isArray(data.files) && data.files.length === 1
      });
      Object.defineProperty(navigator, 'share', {
        configurable: true,
        value: async data => {
          window.__shareCalls.push({
            keys: Object.keys(data).sort(),
            fileCount: data.files?.length || 0,
            fileName: data.files?.[0]?.name,
            fileType: data.files?.[0]?.type,
            text: data.text,
            title: data.title
          });
        }
      });
      HTMLAnchorElement.prototype.click = function () {
        window.__downloadClicks += 1;
      };
      window.open = () => {
        window.__windowOpenCalls += 1;
        return null;
      };
    });

    await page.goto(`http://127.0.0.1:${port}/index.html`, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => window.healthApp?.currentDay);
    await page.evaluate(() => {
      window.healthApp.renderer.exportPoster = async () => {
        const canvas = document.createElement('canvas');
        canvas.width = 2;
        canvas.height = 2;
        canvas.getContext('2d').fillRect(0, 0, 2, 2);
        return canvas;
      };
    });

    await page.click('#shareWhatsappBtn');
    await page.waitForFunction(() => window.__shareCalls.length === 1);
    const nativeShare = await page.evaluate(() => window.__shareCalls[0]);
    if (JSON.stringify(nativeShare.keys) !== JSON.stringify(['files'])) throw new Error(`Unexpected share keys: ${nativeShare.keys}`);
    if (nativeShare.fileCount !== 1 || nativeShare.fileType !== 'image/png') throw new Error(`Invalid image file payload: ${JSON.stringify(nativeShare)}`);
    if (nativeShare.text !== undefined || nativeShare.title !== undefined) throw new Error('Share payload contains text or title');

    await page.evaluate(async () => {
      window.__canShareFiles = false;
      await window.healthApp.shareToWhatsApp();
    });
    await page.waitForFunction(() => window.__downloadClicks === 1);
    const fallback = await page.evaluate(() => ({
      shareCalls: window.__shareCalls.length,
      downloadClicks: window.__downloadClicks,
      windowOpenCalls: window.__windowOpenCalls
    }));
    if (fallback.shareCalls !== 1 || fallback.downloadClicks !== 1 || fallback.windowOpenCalls !== 0) {
      throw new Error(`Invalid fallback behavior: ${JSON.stringify(fallback)}`);
    }

    console.log(JSON.stringify({ status: 'PASS', nativeShare, fallback }, null, 2));
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
})().catch(err => {
  console.error(err.stack || err);
  process.exit(1);
});
