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
  '.svg': 'image/svg+xml',
  '.pdf': 'application/pdf'
};

const server = http.createServer((req, res) => {
  let cleanUrl = req.url.split('?')[0];
  let p = path.join(APP_ROOT, cleanUrl);
  if (p.endsWith(path.sep)) p = path.join(p, 'index.html');
  if (fs.existsSync(p) && fs.statSync(p).isFile()) {
    res.writeHead(200, { 'Content-Type': MIME[path.extname(p).toLowerCase()] || 'application/octet-stream' });
    fs.createReadStream(p).pipe(res);
  } else {
    res.writeHead(404);
    res.end();
  }
});

server.listen(0, '127.0.0.1', async () => {
  const port = server.address().port;
  console.log(`Local review server listening on http://127.0.0.1:${port}`);

  try {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    // Set desktop A4 width context
    await page.setViewportSize({ width: 1200, height: 1600 });
    
    const targetUrl = `http://127.0.0.1:${port}/review/scoped-clinical-reapproval.html`;
    console.log(`Navigating to ${targetUrl}...`);
    await page.goto(targetUrl, { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);

    // Validate DOM elements
    const audit = await page.evaluate(() => {
      const cards = document.querySelectorAll('.card-block');
      const results = [];
      for (const card of cards) {
        const id = card.id;
        const img = card.querySelector('.image-preview-box img');
        const imgLoaded = img && img.complete && img.naturalWidth > 0;
        
        const copyApprove = card.querySelector('input[name^="copy_decision_"][value="APPROVE"]');
        const copyReject = card.querySelector('input[name^="copy_decision_"][value="REJECT"]');
        
        const imgApprove = card.querySelector('input[name^="image_decision_"][value="APPROVE"]');
        const imgReject = card.querySelector('input[name^="image_decision_"][value="REJECT"]');
        
        const defectBox = card.querySelector('.defect-box');

        results.push({
          id,
          imgSrc: img ? img.getAttribute('src') : null,
          imgNaturalWidth: img ? img.naturalWidth : 0,
          imgNaturalHeight: img ? img.naturalHeight : 0,
          imgLoaded,
          copyApproveChecked: copyApprove ? copyApprove.checked : false,
          copyRejectChecked: copyReject ? copyReject.checked : false,
          imgApproveChecked: imgApprove ? imgApprove.checked : false,
          imgRejectChecked: imgReject ? imgReject.checked : false,
          hasDefectBox: !!defectBox
        });
      }
      return results;
    });

    console.log('DOM Evaluation Results:', JSON.stringify(audit, null, 2));

    // Assertions
    if (audit.length !== 4) {
      throw new Error(`Expected 4 cards, found ${audit.length}`);
    }

    for (const item of audit) {
      if (!item.imgLoaded) {
        throw new Error(`Image failed to load for card ${item.id}`);
      }
      if (!item.copyApproveChecked) {
        throw new Error(`Clinical copy should be checked APPROVE for card ${item.id}`);
      }
      if (item.copyRejectChecked) {
        throw new Error(`Clinical copy REJECT should NOT be checked for card ${item.id}`);
      }

      if (item.id === 'card-10-17_card1') {
        if (!item.imgRejectChecked) {
          throw new Error(`Image decision for card-10-17_card1 should be checked REJECT`);
        }
        if (item.imgApproveChecked) {
          throw new Error(`Image decision for card-10-17_card1 should NOT be checked APPROVE`);
        }
        if (!item.hasDefectBox) {
          throw new Error(`card-10-17_card1 must display the defect box`);
        }
      } else {
        if (!item.imgApproveChecked) {
          throw new Error(`Image decision for ${item.id} should be checked APPROVE`);
        }
        if (item.imgRejectChecked) {
          throw new Error(`Image decision for ${item.id} should NOT be checked REJECT`);
        }
      }
    }

    const pdfPath = path.join(APP_ROOT, 'review', 'scoped_clinical_reapproval_packet.pdf');
    console.log(`Generating PDF at ${pdfPath}...`);
    
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      margin: {
        top: '12mm',
        bottom: '12mm',
        left: '12mm',
        right: '12mm'
      }
    });

    const stat = fs.statSync(pdfPath);
    console.log(`PDF successfully generated! Size: ${stat.size} bytes (${(stat.size / 1024).toFixed(1)} KB)`);

    await browser.close();
    server.close();
    process.exit(0);
  } catch (err) {
    console.error('Error generating PDF:', err);
    server.close();
    process.exit(1);
  }
});
