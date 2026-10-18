/**
 * High-DPI HTML5 Canvas Rendering Engine for 365-Day Health Poster Studio
 * Modern Indian Clinical Editorial Style
 * 
 * Features:
 * - Square 1080x1080 (WhatsApp post / Instagram feed)
 * - Vertical 1080x1920 (WhatsApp Status / Instagram Story)
 * - Dynamic Header: Smooth date pill, WHO / MoHFW Observance badge, bilingual title
 * - Modern 4-Card Visual Grid: Independent 4:3 high-res photos, subtle `#284454` clinical border,
 *   soft shadow, distinct Action Badges (માર્ગદર્શન #૧, #૨, #૩, #૪), bilingual headers & captions
 * - Bottom Footer Bar: Dynamic Public Interest notice or Custom Doctor Branding box
 */

class HealthPosterRenderer {
  constructor() {
    this.canvas = document.createElement('canvas');
    this.ctx = this.canvas.getContext('2d');
    this.imageCache = new Map();
  }

  // Pre-load an image from URL or dataURL
  async loadImage(src) {
    if (!src) return null;
    if (this.imageCache.has(src)) {
      return this.imageCache.get(src);
    }
    return new Promise((resolve) => {
      const img = new Image();
      if (window.location.protocol !== 'file:') {
        img.crossOrigin = 'anonymous';
      }
      img.onload = () => {
        this.imageCache.set(src, img);
        resolve(img);
      };
      img.onerror = () => {
        console.warn('Failed to load image with safe CORS policy:', src);
        resolve(null);
      };
      img.src = src;
    });
  }

  // Ensure Gujarati and English fonts are loaded
  async ensureFontsReady() {
    try {
      if (document.fonts) {
        await Promise.all([
          document.fonts.load('bold 24px "Noto Sans Gujarati"'),
          document.fonts.load('bold 24px "Plus Jakarta Sans"'),
          document.fonts.load('600 18px "Noto Sans Gujarati"'),
          document.fonts.load('600 18px "Plus Jakarta Sans"')
        ]);
        await document.fonts.ready;
      }
    } catch (e) {
      console.warn('Font loading check non-critical warning:', e);
    }
  }

  // Draw rounded rectangle helper
  drawRoundRect(ctx, x, y, width, height, radius, fill = true, stroke = true) {
    if (typeof radius === 'number') {
      radius = { tl: radius, tr: radius, br: radius, bl: radius };
    }
    ctx.beginPath();
    ctx.moveTo(x + radius.tl, y);
    ctx.lineTo(x + width - radius.tr, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius.tr);
    ctx.lineTo(x + width, y + height - radius.br);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius.br, y + height);
    ctx.lineTo(x + radius.bl, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius.bl);
    ctx.lineTo(x, y + radius.tl);
    ctx.quadraticCurveTo(x, y, x + radius.tl, y);
    ctx.closePath();
    if (fill) ctx.fill();
    if (stroke) ctx.stroke();
  }

  // Draw image with cover aspect ratio inside a bounding box
  drawImageCover(ctx, img, x, y, w, h, radius = 0) {
    if (!img) return;
    ctx.save();
    if (radius > 0) {
      this.drawRoundRect(ctx, x, y, w, h, radius, false, false);
      ctx.clip();
    }
    const imgRatio = img.width / img.height;
    const boxRatio = w / h;
    let sWidth, sHeight, sx, sy;

    if (imgRatio > boxRatio) {
      sHeight = img.height;
      sWidth = img.height * boxRatio;
      sx = (img.width - sWidth) / 2;
      sy = 0;
    } else {
      sWidth = img.width;
      sHeight = img.width / boxRatio;
      sx = 0;
      sy = (img.height - sHeight) / 2;
    }

    ctx.drawImage(img, sx, sy, sWidth, sHeight, x, y, w, h);
    ctx.restore();
  }

  // Word-wrapping text on canvas with optional truncation ellipsis
  wrapText(ctx, text, x, y, maxWidth, lineHeight, maxLines = 3) {
    if (!text) return 0;
    const words = text.split(' ');
    let line = '';
    const lines = [];

    for (let n = 0; n < words.length; n++) {
      const testLine = line + words[n] + ' ';
      const metrics = ctx.measureText(testLine);
      if (metrics.width > maxWidth && n > 0) {
        lines.push(line.trim());
        line = words[n] + ' ';
        if (lines.length >= maxLines) break;
      } else {
        line = testLine;
      }
    }
    if (lines.length < maxLines && line.trim().length > 0) {
      lines.push(line.trim());
    }

    for (let i = 0; i < lines.length; i++) {
      ctx.fillText(lines[i], x, y + (i * lineHeight));
    }
    return lines.length * lineHeight;
  }

  // Gujarati Numerals Helper
  toGuNum(num) {
    const guMap = { '0': '૦', '1': '૧', '2': '૨', '3': '૩', '4': '૪', '5': '૫', '6': '૬', '7': '૭', '8': '૮', '9': '૯' };
    return String(num).split('').map(c => guMap[c] || c).join('');
  }

  /**
   * Main Poster Render Method
   * @param {Object} dayData - The day object from health_365.json
   * @param {Object} options - { format: 'square' | 'vertical', language: 'bilingual' | 'gujarati' | 'english', settings: {...}, customPhotos: {1: '...', 2: '...'} }
   */
  async renderPoster(dayData, options = {}) {
    await this.ensureFontsReady();

    const format = options.format || 'square';
    const language = options.language || 'bilingual';
    const settings = options.settings || {};
    const customPhotos = options.customPhotos || {};

    const isVertical = format === 'vertical';
    const WIDTH = 1080;
    const HEIGHT = isVertical ? 1920 : 1080;

    this.canvas.width = WIDTH;
    this.canvas.height = HEIGHT;
    const ctx = this.ctx;

    // -------------------------------------------------------------
    // 1. DEEP CLINICAL SLATE BACKGROUND WITH EDITORIAL LIGHTING
    // -------------------------------------------------------------
    const bgGrad = ctx.createLinearGradient(0, 0, 0, HEIGHT);
    bgGrad.addColorStop(0, '#061320');
    bgGrad.addColorStop(0.3, '#091b2e');
    bgGrad.addColorStop(0.7, '#071624');
    bgGrad.addColorStop(1, '#030a12');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, WIDTH, HEIGHT);

    // Ambient medical soft glow in upper left and lower right
    const glow1 = ctx.createRadialGradient(120, 120, 20, 120, 120, 500);
    glow1.addColorStop(0, 'rgba(14, 165, 233, 0.12)');
    glow1.addColorStop(1, 'transparent');
    ctx.fillStyle = glow1;
    ctx.fillRect(0, 0, 700, 700);

    const glow2 = ctx.createRadialGradient(WIDTH - 120, HEIGHT - 140, 20, WIDTH - 120, HEIGHT - 140, 550);
    glow2.addColorStop(0, 'rgba(16, 185, 129, 0.10)');
    glow2.addColorStop(1, 'transparent');
    ctx.fillStyle = glow2;
    ctx.fillRect(WIDTH - 700, HEIGHT - 700, 700, 700);

    // Subtle framing border
    ctx.save();
    ctx.strokeStyle = '#284454';
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, 16, 16, WIDTH - 32, HEIGHT - 32, 22, false, true);
    ctx.restore();

    // -------------------------------------------------------------
    // 2. PRELOAD ALL 4 CARD PHOTOS
    // -------------------------------------------------------------
    const failedCards = [];
    const loadedImages = await Promise.all(
      dayData.cards.map(async (card) => {
        const customSrc = customPhotos[card.index];
        const src = customSrc || card.photo;
        const img = await this.loadImage(src);
        if (!img) {
          failedCards.push({
            index: card.index,
            title: card.title_en || `Card #${card.index}`,
            src: src || 'no photo specified'
          });
        }
        return img;
      })
    );
    this.lastRenderFailedCards = failedCards;

    // -------------------------------------------------------------
    // 3. HEADER RENDERING
    // -------------------------------------------------------------
    const headerY = isVertical ? 44 : 34;

    // A. Date Badge (Left Pill)
    // Format: e.g. "15 OCTOBER | ૧૫ ઓક્ટોબર"
    let datePillText = '';
    const upperDateEn = (dayData.date_en || '').toUpperCase();
    if (language === 'gujarati') {
      datePillText = `📅 ${dayData.date_gu}`;
    } else if (language === 'english') {
      datePillText = `📅 ${upperDateEn}`;
    } else {
      datePillText = `📅 ${upperDateEn} | ${dayData.date_gu}`;
    }

    ctx.save();
    ctx.font = 'bold 18px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const dateWidth = ctx.measureText(datePillText).width + 36;
    
    // Smooth pill border with subtle cyan fill
    ctx.fillStyle = 'rgba(11, 30, 48, 0.85)';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, 40, headerY, dateWidth, 38, 19, true, true);
    ctx.fillStyle = '#ffffff';
    ctx.fillText(datePillText, 58, headerY + 25);
    ctx.restore();

    // B. Observance Badge (Right Pill) with Sourced Provenance Verification
    // Badges are derived strictly from verified authority metadata (zero hard-coded ID allowlists).
    // Verified WHO/UN days get gold badges, verified MoHFW days get orange badges,
    // verified global health days get sky blue badges, and rotational guidance gets emerald badges.
    let tierLabel = '';
    let tierColor = '#a7f3d0';
    let tierBg = 'rgba(16, 185, 129, 0.18)';
    let tierBorder = '#10b981';

    const prov = dayData.provenance;
    if (prov && prov.status === 'VERIFIED') {
      const tier = prov.authority_tier;
      if (tier === 'UN_AGENCY' || tier === 'INTERNATIONAL_SOCIETY_WHO' || tier === 'GLOBAL_PARTNERSHIP') {
        tierColor = '#fef08a';
        tierBg = 'rgba(234, 179, 8, 0.22)';
        tierBorder = '#eab308';
      } else if (tier === 'MoHFW_NATIONAL_PROGRAMME') {
        tierColor = '#fed7aa';
        tierBg = 'rgba(249, 115, 22, 0.22)';
        tierBorder = '#f97316';
      } else {
        // Non-governmental accredited global health bodies
        tierColor = '#bae6fd';
        tierBg = 'rgba(14, 165, 233, 0.22)';
        tierBorder = '#0ea5e9';
      }
      tierLabel = language === 'gujarati' ? (prov.badge_gu || '🌐 વિશ્વ આરોગ્ય દિવસ') : (prov.badge_en || '🌐 Global Health Day');
    } else {
      tierColor = '#a7f3d0';
      tierBg = 'rgba(16, 185, 129, 0.18)';
      tierBorder = '#10b981';
      tierLabel = language === 'gujarati' ? '🛡️ દૈનિક આરોગ્ય માર્ગદર્શન' : '🛡️ Daily Health Guidance';
    }

    ctx.save();
    ctx.font = 'bold 17px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const tierWidth = ctx.measureText(tierLabel).width + 36;
    const tierX = WIDTH - tierWidth - 40;
    ctx.fillStyle = tierBg;
    ctx.strokeStyle = tierBorder;
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, tierX, headerY, tierWidth, 38, 19, true, true);
    ctx.fillStyle = tierColor;
    ctx.fillText(tierLabel, tierX + 18, headerY + 25);
    ctx.restore();

    // C. Large Bold Bilingual Title (Center)
    let currentY = headerY + 70;
    ctx.save();
    ctx.textAlign = 'center';

    if (language === 'bilingual') {
      // English Title
      ctx.font = 'bold 28px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(dayData.title_en.toUpperCase(), WIDTH / 2, currentY);

      // Gujarati Title (Hero Font)
      currentY += 38;
      ctx.font = 'bold 34px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
      ctx.shadowBlur = 8;
      ctx.fillText(dayData.title_gu, WIDTH / 2, currentY);
      ctx.shadowBlur = 0;
    } else if (language === 'gujarati') {
      ctx.font = 'bold 40px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
      ctx.shadowBlur = 8;
      ctx.fillText(dayData.title_gu, WIDTH / 2, currentY + 12);
      ctx.shadowBlur = 0;
      currentY += 24;
    } else {
      ctx.font = 'bold 36px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
      ctx.shadowBlur = 8;
      ctx.fillText(dayData.title_en.toUpperCase(), WIDTH / 2, currentY + 12);
      ctx.shadowBlur = 0;
      currentY += 24;
    }

    // D. Theme Subtitle Capsule
    currentY += 28;
    const themeText = language === 'gujarati' ? dayData.theme_gu : (language === 'english' ? dayData.theme_en : `${dayData.theme_en} • ${dayData.theme_gu}`);
    ctx.font = '500 17px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const themeMetrics = ctx.measureText(themeText);
    const themeBoxW = Math.min(WIDTH - 80, themeMetrics.width + 44);
    const themeBoxX = (WIDTH - themeBoxW) / 2;

    ctx.fillStyle = 'rgba(11, 23, 38, 0.85)';
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.35)';
    ctx.lineWidth = 1;
    this.drawRoundRect(ctx, themeBoxX, currentY - 20, themeBoxW, 32, 16, true, true);
    ctx.fillStyle = '#a7f3d0';
    ctx.fillText(themeText, WIDTH / 2, currentY + 3);
    ctx.restore();

    // -------------------------------------------------------------
    // 4. MODERN 4-CARD VISUAL GRID
    // -------------------------------------------------------------
    if (!isVertical) {
      // SQUARE FORMAT (1080 x 1080)
      const gridStartY = currentY + 22;
      const cardW = 485;
      const cardH = 380;
      const gapX = 30;
      const leftX = 40;
      const rightX = leftX + cardW + gapX;

      const cardPositions = [
        { x: leftX, y: gridStartY, index: 1, card: dayData.cards[0], img: loadedImages[0] },
        { x: rightX, y: gridStartY, index: 2, card: dayData.cards[1], img: loadedImages[1] },
        { x: leftX, y: gridStartY + cardH + 16, index: 3, card: dayData.cards[2], img: loadedImages[2] },
        { x: rightX, y: gridStartY + cardH + 16, index: 4, card: dayData.cards[3], img: loadedImages[3] },
      ];

      for (const pos of cardPositions) {
        this.renderClinicalCardSquare(ctx, pos, language);
      }
    } else {
      // VERTICAL FORMAT (1080 x 1920)
      const gridStartY = currentY + 32;
      const cardW = 485;
      const cardH = 725;
      const gapX = 30;
      const leftX = 40;
      const rightX = leftX + cardW + gapX;

      const cardPositions = [
        { x: leftX, y: gridStartY, index: 1, card: dayData.cards[0], img: loadedImages[0] },
        { x: rightX, y: gridStartY, index: 2, card: dayData.cards[1], img: loadedImages[1] },
        { x: leftX, y: gridStartY + cardH + 26, index: 3, card: dayData.cards[2], img: loadedImages[2] },
        { x: rightX, y: gridStartY + cardH + 26, index: 4, card: dayData.cards[3], img: loadedImages[3] },
      ];

      for (const pos of cardPositions) {
        this.renderClinicalCardVertical(ctx, pos, language);
      }
    }

    // -------------------------------------------------------------
    // 5. BOTTOM FOOTER BAR
    // -------------------------------------------------------------
    this.renderFooter(ctx, WIDTH, HEIGHT, isVertical, settings, language);

    return this.canvas;
  }

  /**
   * Render individual card in Square Mode (w: 485, h: 380)
   * Modern Indian Clinical Editorial layout with 4:3 photo and distinct Action Badge
   */
  renderClinicalCardSquare(ctx, pos, language) {
    const { x, y, index, card, img } = pos;
    const w = 485;
    const h = 380;

    ctx.save();

    // 1. Clean rounded container with subtle border (#284454) and soft shadow
    ctx.shadowColor = 'rgba(0, 0, 0, 0.45)';
    ctx.shadowBlur = 14;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 6;

    ctx.fillStyle = '#0B1726';
    ctx.strokeStyle = '#284454';
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, x, y, w, h, 18, true, true);
    ctx.shadowBlur = 0;

    // 2. High-res Photo Box
    const photoMargin = 8;
    const photoX = x + photoMargin;
    const photoY = y + photoMargin;
    const photoW = w - (photoMargin * 2);
    const photoH = 215;

    if (img) {
      this.drawImageCover(ctx, img, photoX, photoY, photoW, photoH, 14);
    } else {
      // Editorial clinical fallback
      ctx.fillStyle = '#112233';
      this.drawRoundRect(ctx, photoX, photoY, photoW, photoH, 14, true, false);
      ctx.fillStyle = '#64748b';
      ctx.font = '15px "Plus Jakarta Sans", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('📷 High-Res Photo', photoX + (photoW / 2), photoY + (photoH / 2) + 5);
      ctx.textAlign = 'left';
    }

    // 3. Distinct Action Badge (e.g. "માર્ગદર્શન #૧" or "ACTION #1 • માર્ગદર્શન #૧")
    const badgeY = photoY + 10;
    const badgeX = photoX + 10;
    const guNum = this.toGuNum(index);
    let badgeText = '';
    if (language === 'gujarati') {
      badgeText = `માર્ગદર્શન #${guNum}`;
    } else if (language === 'english') {
      badgeText = `ACTION #${index}`;
    } else {
      badgeText = `ACTION #${index} • માર્ગદર્શન #${guNum}`;
    }

    ctx.font = 'bold 13px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const badgeW = ctx.measureText(badgeText).width + 24;
    const badgeH = 26;

    // Smooth pill overlay with dark glass background & cyan accent
    ctx.fillStyle = 'rgba(7, 19, 32, 0.90)';
    ctx.strokeStyle = '#0ea5e9';
    ctx.lineWidth = 1.2;
    this.drawRoundRect(ctx, badgeX, badgeY, badgeW, badgeH, 13, true, true);

    ctx.fillStyle = '#38bdf8';
    ctx.fillText(badgeText, badgeX + 12, badgeY + 18);

    // 4. Content Area below photo
    const contentX = x + 14;
    const contentY = photoY + photoH + 18;
    const maxTextW = w - 28;

    // Bilingual Action Header
    if (language === 'bilingual') {
      // English Title
      ctx.font = 'bold 16px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      const enTitle = card.title_en || '';
      ctx.fillText(enTitle, contentX, contentY);

      // Gujarati Title
      ctx.font = 'bold 18px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      const guTitle = card.title_gu || '';
      ctx.fillText(guTitle, contentX, contentY + 22);

      // Medical Caption (Concise)
      ctx.font = '400 13.5px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#cbd5e1';
      this.wrapText(ctx, card.desc_gu || '', contentX, contentY + 44, maxTextW, 18, 2);

      ctx.font = '400 12.5px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#94a3b8';
      this.wrapText(ctx, card.desc_en || '', contentX, contentY + 84, maxTextW, 16, 2);

    } else if (language === 'gujarati') {
      ctx.font = 'bold 20px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.fillText(card.title_gu || '', contentX, contentY + 4);

      ctx.font = '400 14px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#cbd5e1';
      this.wrapText(ctx, card.desc_gu || '', contentX, contentY + 34, maxTextW, 20, 3);

    } else {
      ctx.font = 'bold 19px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(card.title_en || '', contentX, contentY + 4);

      ctx.font = '400 14px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#cbd5e1';
      this.wrapText(ctx, card.desc_en || '', contentX, contentY + 34, maxTextW, 20, 3);
    }

    ctx.restore();
  }

  /**
   * Render individual card in Vertical Mode (w: 485, h: 725)
   * High-impact 4:3 high-res photo with clean clinical typography
   */
  renderClinicalCardVertical(ctx, pos, language) {
    const { x, y, index, card, img } = pos;
    const w = 485;
    const h = 725;

    ctx.save();

    // 1. Clean rounded container with subtle border (#284454) and soft shadow
    ctx.shadowColor = 'rgba(0, 0, 0, 0.50)';
    ctx.shadowBlur = 18;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 8;

    ctx.fillStyle = '#0B1726';
    ctx.strokeStyle = '#284454';
    ctx.lineWidth = 1.8;
    this.drawRoundRect(ctx, x, y, w, h, 22, true, true);
    ctx.shadowBlur = 0;

    // 2. High-res Photo Box (4:3 aspect ratio: 465w x 348h)
    const photoMargin = 10;
    const photoX = x + photoMargin;
    const photoY = y + photoMargin;
    const photoW = w - (photoMargin * 2);
    const photoH = 350; // Exact 4:3 ratio: 465 / 4 * 3 = 348.75 ~ 350px

    if (img) {
      this.drawImageCover(ctx, img, photoX, photoY, photoW, photoH, 16);
    } else {
      ctx.fillStyle = '#112233';
      this.drawRoundRect(ctx, photoX, photoY, photoW, photoH, 16, true, false);
      ctx.fillStyle = '#64748b';
      ctx.font = '18px "Plus Jakarta Sans", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('📷 4:3 High-Res Photo', photoX + (photoW / 2), photoY + (photoH / 2) + 5);
      ctx.textAlign = 'left';
    }

    // 3. Distinct Action Badge
    const badgeY = photoY + 12;
    const badgeX = photoX + 12;
    const guNum = this.toGuNum(index);
    let badgeText = '';
    if (language === 'gujarati') {
      badgeText = `માર્ગદર્શન #${guNum}`;
    } else if (language === 'english') {
      badgeText = `ACTION #${index}`;
    } else {
      badgeText = `ACTION #${index} • માર્ગદર્શન #${guNum}`;
    }

    ctx.font = 'bold 15px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const badgeW = ctx.measureText(badgeText).width + 28;
    const badgeH = 32;

    ctx.fillStyle = 'rgba(7, 19, 32, 0.92)';
    ctx.strokeStyle = '#0ea5e9';
    ctx.lineWidth = 1.4;
    this.drawRoundRect(ctx, badgeX, badgeY, badgeW, badgeH, 16, true, true);

    ctx.fillStyle = '#38bdf8';
    ctx.fillText(badgeText, badgeX + 14, badgeY + 22);

    // 4. Content Area below photo
    const contentX = x + 18;
    const contentY = photoY + photoH + 26;
    const maxTextW = w - 36;

    if (language === 'bilingual') {
      // English Title
      ctx.font = 'bold 21px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(card.title_en || '', contentX, contentY);

      // Gujarati Title
      ctx.font = 'bold 22px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.fillText(card.title_gu || '', contentX, contentY + 28);

      // Gujarati Description
      ctx.font = '400 16px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#e2e8f0';
      const guLinesH = this.wrapText(ctx, card.desc_gu || '', contentX, contentY + 62, maxTextW, 23, 3);

      // English Description
      ctx.font = '400 14px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#94a3b8';
      this.wrapText(ctx, card.desc_en || '', contentX, contentY + 68 + guLinesH, maxTextW, 20, 3);

    } else if (language === 'gujarati') {
      ctx.font = 'bold 24px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.fillText(card.title_gu || '', contentX, contentY + 8);

      ctx.font = '400 17px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#e2e8f0';
      this.wrapText(ctx, card.desc_gu || '', contentX, contentY + 48, maxTextW, 26, 6);

    } else {
      ctx.font = 'bold 23px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(card.title_en || '', contentX, contentY + 8);

      ctx.font = '400 17px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#e2e8f0';
      this.wrapText(ctx, card.desc_en || '', contentX, contentY + 48, maxTextW, 26, 6);
    }

    ctx.restore();
  }

  /**
   * Render Footer Bar (Public Interest vs Custom Doctor Branding)
   */
  renderFooter(ctx, width, height, isVertical, settings, language) {
    ctx.save();
    const useDoctor = settings.useDoctorBranding && settings.doctorName;

    if (!isVertical) {
      // SQUARE FOOTER (y: 1012 to 1062)
      const footerY = 1012;
      const footerH = 50;
      const footerW = width - 80;
      const footerX = 40;

      // Dark clinical container
      ctx.fillStyle = 'rgba(11, 23, 38, 0.95)';
      ctx.strokeStyle = useDoctor ? '#10b981' : '#284454';
      ctx.lineWidth = 1.5;
      this.drawRoundRect(ctx, footerX, footerY, footerW, footerH, 14, true, true);

      ctx.textAlign = 'center';
      if (!useDoctor) {
        ctx.font = 'bold 16px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#38bdf8';
        const msg = language === 'gujarati'
          ? '🏛️ જાહેર આરોગ્ય હિતમાં પ્રસારિત | નિરોગી ભારત અભિયાન'
          : (language === 'english'
            ? '🏛️ Issued in Public Interest for Health Awareness | Healthy India Mission'
            : '🏛️ Issued in Public Interest for Health Awareness | જાહેર આરોગ્ય હિતમાં પ્રસારિત');
        ctx.fillText(msg, width / 2, footerY + 31);
      } else {
        ctx.font = 'bold 16px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#34d399';
        const clinicPart = settings.clinicName ? ` • ${settings.clinicName}` : '';
        const phonePart = settings.contactInfo ? ` • 💬 WhatsApp: ${settings.contactInfo}` : '';
        const line = `🩺 ${settings.doctorName} (${settings.doctorDegree || 'Medical Consultant'})${clinicPart}${phonePart}`;
        ctx.fillText(line, width / 2, footerY + 31);
      }
    } else {
      // VERTICAL FOOTER (y: 1755 to 1890) - WhatsApp Status & Story Bar
      const footerY = 1755;
      const footerH = 135;
      const footerW = width - 80;
      const footerX = 40;

      // Gradient medical container
      const footerGrad = ctx.createLinearGradient(footerX, footerY, footerX + footerW, footerY + footerH);
      footerGrad.addColorStop(0, 'rgba(11, 23, 38, 0.95)');
      footerGrad.addColorStop(1, 'rgba(6, 30, 48, 0.95)');
      ctx.fillStyle = footerGrad;
      ctx.strokeStyle = useDoctor ? '#10b981' : '#284454';
      ctx.lineWidth = 2;
      this.drawRoundRect(ctx, footerX, footerY, footerW, footerH, 20, true, true);

      if (!useDoctor) {
        ctx.textAlign = 'center';
        ctx.font = 'bold 22px "Plus Jakarta Sans", sans-serif';
        ctx.fillStyle = '#38bdf8';
        ctx.fillText('ISSUED IN PUBLIC INTEREST FOR HEALTH AWARENESS', width / 2, footerY + 44);

        ctx.font = 'bold 22px "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#ffffff';
        ctx.fillText('જાહેર જનતાના આરોગ્ય અને સુખાકારીના હિતમાં પ્રસારિત', width / 2, footerY + 80);

        ctx.font = '500 16px "Plus Jakarta Sans", sans-serif';
        ctx.fillStyle = '#94a3b8';
        ctx.fillText('National Health Mission • Preventive Healthcare India • 365 Days Health Calendar', width / 2, footerY + 112);
      } else {
        // High-end Doctor Profile Card in Footer
        // Doctor Icon Circle
        ctx.fillStyle = '#10b981';
        this.drawRoundRect(ctx, footerX + 25, footerY + 25, 85, 85, 42, true, false);
        ctx.font = '42px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('🩺', footerX + 67, footerY + 82);

        // Doctor Name & Degree
        ctx.textAlign = 'left';
        ctx.font = 'bold 24px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#ffffff';
        ctx.fillText(settings.doctorName, footerX + 130, footerY + 46);

        ctx.font = '600 17px "Plus Jakarta Sans", sans-serif';
        ctx.fillStyle = '#34d399';
        ctx.fillText(settings.doctorDegree || 'Medical Specialist', footerX + 130, footerY + 74);

        // Clinic & Contact
        ctx.font = '500 16px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#cbd5e1';
        const contactLine = `${settings.clinicName || 'Clinic'}  |  💬 WhatsApp: ${settings.contactInfo || ''}`;
        ctx.fillText(contactLine, footerX + 130, footerY + 104);
      }
    }
    ctx.restore();
  }

  /**
   * Export Poster Method with Mandatory Image Failure Guard
   * Throws an error and halts export if any required card photo failed to load.
   */
  async exportPoster(dayData, options = {}) {
    const canvas = await this.renderPoster(dayData, options);
    if (this.lastRenderFailedCards && this.lastRenderFailedCards.length > 0) {
      const details = this.lastRenderFailedCards
        .map(c => `Card #${c.index} (${c.title}): ${c.src}`)
        .join(', ');
      throw new Error(`Export blocked: Required card photo assets failed to load: ${details}`);
    }
    return canvas;
  }
}

window.HealthPosterRenderer = HealthPosterRenderer;
