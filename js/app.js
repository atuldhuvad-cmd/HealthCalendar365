/**
 * Main Application Logic for 365-Day Health Poster Studio (India)
 * Handles state, day selection, format & language toggling, photo upload/swap,
 * AI prompt copying, WhatsApp sharing, and single-poster downloads.
 */

class HealthPosterApp {
  constructor() {
    this.currentDayId = '10-15'; // Default to October 15 as requested
    this.currentFormat = 'square'; // 'square' | 'vertical'
    this.currentLanguage = 'bilingual'; // 'bilingual' | 'gujarati' | 'english'
    this.calendarData = [];
    this.currentDay = null;
    this.customPhotos = {};
    this.settings = {};
    this.renderer = new HealthPosterRenderer();
    this.isRendering = false;
    this.zoomLevel = 1.0;

    // DOM Elements
    this.previewCanvas = document.getElementById('previewCanvas');
    this.canvasWrapper = document.getElementById('canvasWrapper');
    this.cardsContainer = document.getElementById('cardsContainer');
    this.fileInput = document.getElementById('photoFileInput');
    this.activeSwapSlot = null;

    this.init();
  }

  async init() {
    this.showToast('Loading Health Calendar 365...', 'info');

    // 1. Load Calendar Data (from window global or fetch)
    if (window.HEALTH_CALENDAR_DATA && window.HEALTH_CALENDAR_DATA.length > 0) {
      this.calendarData = window.HEALTH_CALENDAR_DATA;
    } else {
      try {
        const resp = await fetch('./data/health_365.json');
        this.calendarData = await resp.json();
      } catch (err) {
        console.error('Failed to load JSON directly:', err);
      }
    }

    // 2. Load User Branding Settings
    this.settings = await window.appStorage.getSettings();

    // 3. Setup Event Listeners
    this.setupEventListeners();

    // 4. Populate Month/Day selector
    this.populateDateSelect();

    // 5. Load and Display Default Day (October 15)
    await this.selectDay(this.currentDayId);

    // Register Service Worker for Offline PWA
    this.registerServiceWorker();
  }

  // Populate Month & Day Selectors and Search
  populateDateSelect() {
    const datePicker = document.getElementById('dateSelectInput');
    if (!datePicker) return;

    datePicker.innerHTML = '';
    this.calendarData.forEach((day) => {
      const opt = document.createElement('option');
      opt.value = day.id;
      const pending = (day.observance_schedule_2026 || [])
        .filter((item) => item.poster_status === 'PENDING_BILINGUAL_CONTENT_AND_IMAGES')
        .map((item) => item.title_en);
      const pendingSuffix = pending.length
        ? ` | Verified schedule: ${pending.join('; ')} [posters pending]`
        : '';
      opt.textContent = `${day.date_en} (${day.date_gu}) - ${day.title_en}${pendingSuffix}`;
      datePicker.appendChild(opt);
    });
    datePicker.value = this.currentDayId;

    datePicker.addEventListener('change', (e) => {
      this.selectDay(e.target.value);
    });
  }

  // Setup UI Event Listeners
  setupEventListeners() {
    // Format Toggle (Square vs Vertical)
    document.querySelectorAll('[data-format-toggle]').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const fmt = btn.getAttribute('data-format-toggle');
        this.setFormat(fmt);
      });
    });

    // Language Toggle (Bilingual, Gujarati, English)
    document.querySelectorAll('[data-lang-toggle]').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const lang = btn.getAttribute('data-lang-toggle');
        this.setLanguage(lang);
      });
    });

    // Prev / Next Day Buttons
    document.getElementById('prevDayBtn')?.addEventListener('click', () => this.navigateDay(-1));
    document.getElementById('nextDayBtn')?.addEventListener('click', () => this.navigateDay(1));

    // Export Buttons
    document.getElementById('downloadPosterBtn')?.addEventListener('click', () => this.downloadSinglePoster());
    document.getElementById('shareWhatsappBtn')?.addEventListener('click', () => this.shareToWhatsApp());

    // Settings Modal
    document.getElementById('openSettingsBtn')?.addEventListener('click', () => this.openSettingsModal());
    document.getElementById('closeSettingsBtn')?.addEventListener('click', () => this.closeSettingsModal());
    document.getElementById('cancelSettingsBtn')?.addEventListener('click', () => this.closeSettingsModal());
    document.getElementById('saveSettingsBtn')?.addEventListener('click', () => this.saveSettingsFromModal());

    // Zoom Buttons
    document.getElementById('zoomInBtn')?.addEventListener('click', () => this.adjustZoom(0.15));
    document.getElementById('zoomOutBtn')?.addEventListener('click', () => this.adjustZoom(-0.15));
    document.getElementById('zoomFitBtn')?.addEventListener('click', () => this.resetZoom());

    // Hidden File Input for Custom Photo Upload
    this.fileInput.addEventListener('change', (e) => this.handlePhotoFileSelected(e));

    // Search Input
    const searchInput = document.getElementById('searchDayInput');
    searchInput?.addEventListener('input', (e) => this.handleSearch(e.target.value));
    searchInput?.addEventListener('keydown', (e) => this.handleSearchKeydown(e));
    document.getElementById('searchResultsList')?.addEventListener('click', (e) => {
      const opt = e.target.closest('[data-day-id]');
      if (opt) this.pickSearchResult(opt.getAttribute('data-day-id'));
    });

    // Interactive Canvas Card Click
    this.previewCanvas?.addEventListener('click', (e) => this.handleCanvasClick(e));
    if (this.previewCanvas) {
      this.previewCanvas.style.cursor = 'pointer';
    }

    // Card Action Modal Event Listeners
    document.getElementById('closeCardActionBtn')?.addEventListener('click', () => this.closeCardActionModal());
    document.getElementById('modalSwapPhotoBtn')?.addEventListener('click', () => this.handleModalSwapPhoto());
    document.getElementById('modalCopyPromptBtn')?.addEventListener('click', () => this.handleModalCopyPrompt());
    document.getElementById('modalResetPhotoBtn')?.addEventListener('click', () => this.handleModalResetPhoto());

    // Close modal on click outside
    document.getElementById('cardActionModal')?.addEventListener('click', (e) => {
      if (e.target.id === 'cardActionModal') {
        this.closeCardActionModal();
      }
    });

    // Window resize adjustment
    window.addEventListener('resize', () => this.adjustCanvasScale());
  }

  // Select a Day by ID ('MM-DD')
  async selectDay(dayId) {
    const day = this.calendarData.find((d) => d.id === dayId);
    if (!day) return;

    this.currentDayId = dayId;
    this.currentDay = day;

    // Update Date Picker input
    const datePicker = document.getElementById('dateSelectInput');
    if (datePicker) datePicker.value = dayId;

    // Load any custom swapped photos for this day from IndexedDB
    this.customPhotos = {};
    for (let idx = 1; idx <= 4; idx++) {
      const saved = await window.appStorage.getPhoto(dayId, idx);
      if (saved) {
        this.customPhotos[idx] = saved;
      }
    }

    // Update 4-Cards Interactive Panel
    this.renderCardControlPanels();

    // Update Multi-Observance Selector Bar (if this date has 2+ observances)
    this.updateMultiObservanceBar(day);

    // Render Canvas
    await this.renderPoster();
  }

  // Update Multi-Observance Selector Bar for dates with 2+ dedicated posters
  updateMultiObservanceBar(day) {
    const bar = document.getElementById('multiObservanceBar');
    const container = document.getElementById('multiObsPills');
    if (!bar || !container) return;

    // Find all posters sharing the same month and day
    const sameDatePosters = this.calendarData.filter(d => d.month === day.month && d.day === day.day);
    if (sameDatePosters.length > 1) {
      bar.style.display = 'flex';
      container.innerHTML = '';
      sameDatePosters.forEach((d, i) => {
        const btn = document.createElement('button');
        btn.className = `multi-obs-btn ${d.id === day.id ? 'active' : ''}`;
        btn.innerHTML = `<span class="multi-obs-num">Poster #${i + 1}:</span> <strong>${d.title_en}</strong>`;
        btn.title = `Switch to ${d.title_en} (${d.title_gu})`;
        btn.addEventListener('click', () => {
          this.selectDay(d.id);
        });
        container.appendChild(btn);
      });
    } else {
      bar.style.display = 'none';
      container.innerHTML = '';
    }
  }

  // Navigate Prev / Next Day
  navigateDay(delta) {
    const currIndex = this.calendarData.findIndex((d) => d.id === this.currentDayId);
    if (currIndex === -1) return;
    let nextIndex = currIndex + delta;
    if (nextIndex < 0) nextIndex = this.calendarData.length - 1;
    if (nextIndex >= this.calendarData.length) nextIndex = 0;
    this.selectDay(this.calendarData[nextIndex].id);
  }

  // Set Format (Square / Vertical)
  async setFormat(format) {
    if (this.currentFormat === format) return;
    this.currentFormat = format;
    this.zoomLevel = 1.0;

    // Update button states
    document.querySelectorAll('[data-format-toggle]').forEach((btn) => {
      btn.classList.toggle('active', btn.getAttribute('data-format-toggle') === format);
    });

    this.canvasWrapper.setAttribute('data-aspect', format);
    const aspectBadge = document.getElementById('canvasAspectBadge');
    if (aspectBadge) {
      aspectBadge.textContent = format === 'vertical'
        ? '1080 × 1920 px High-Res'
        : '1080 × 1080 px High-Res';
    }
    await this.renderPoster();
  }

  // Set Language (Bilingual / Gujarati / English)
  async setLanguage(lang) {
    if (this.currentLanguage === lang) return;
    this.currentLanguage = lang;

    // Update button states
    document.querySelectorAll('[data-lang-toggle]').forEach((btn) => {
      btn.classList.toggle('active', btn.getAttribute('data-lang-toggle') === lang);
    });

    this.renderCardControlPanels();
    await this.renderPoster();
  }

  // Render the Live Poster onto the Preview Canvas
  async renderPoster() {
    if (this.isRendering || !this.currentDay) return;
    this.isRendering = true;

    try {
      const renderedCanvas = await this.renderer.renderPoster(this.currentDay, {
        format: this.currentFormat,
        language: this.currentLanguage,
        settings: this.settings,
        customPhotos: this.customPhotos
      });

      // Transfer rendered pixels to preview canvas
      this.previewCanvas.width = renderedCanvas.width;
      this.previewCanvas.height = renderedCanvas.height;
      const pCtx = this.previewCanvas.getContext('2d');
      pCtx.drawImage(renderedCanvas, 0, 0);

      this.adjustCanvasScale();
    } catch (err) {
      console.error('Render error:', err);
      this.showToast('Error rendering poster', 'error');
    } finally {
      this.isRendering = false;
    }
  }

  // Fit canvas smoothly into preview container viewport
  adjustCanvasScale() {
    const container = this.canvasWrapper;
    if (!container || !this.previewCanvas) return;

    const viewport = container.parentElement;
    if (!viewport) return;

    const contW = Math.max(1, viewport.clientWidth - 40);
    const contH = Math.max(1, viewport.clientHeight - 40);
    const canvasW = this.previewCanvas.width;
    const canvasH = this.previewCanvas.height;

    const scaleX = contW / canvasW;
    const scaleY = contH / canvasH;
    const fitScale = Math.min(scaleX, scaleY, 1.0);

    const effectiveScale = fitScale * this.zoomLevel;
    this.previewCanvas.style.width = `${Math.round(canvasW * effectiveScale)}px`;
    this.previewCanvas.style.height = `${Math.round(canvasH * effectiveScale)}px`;
    this.previewCanvas.style.transform = 'none';
  }

  adjustZoom(delta) {
    this.zoomLevel = Math.max(0.4, Math.min(2.5, this.zoomLevel + delta));
    this.adjustCanvasScale();
    this.showToast(`Zoom: ${Math.round(this.zoomLevel * 100)}%`, 'info');
  }

  resetZoom() {
    this.zoomLevel = 1.0;
    this.adjustCanvasScale();
    this.showToast('Fit to Screen', 'info');
  }

  // Handle Click Directly on Live Canvas
  handleCanvasClick(e) {
    if (!this.currentDay || !this.previewCanvas) return;
    const rect = this.previewCanvas.getBoundingClientRect();
    const scaleX = this.previewCanvas.width / rect.width;
    const scaleY = this.previewCanvas.height / rect.height;

    const clickX = (e.clientX - rect.left) * scaleX;
    const clickY = (e.clientY - rect.top) * scaleY;

    const isVertical = this.currentFormat === 'vertical';
    let clickedIndex = null;

    if (!isVertical) {
      // Square 1080x1080: Left col [40, 525], Right col [555, 1040], Row 1 [215, 595], Row 2 [612, 992]
      if (clickX >= 40 && clickX <= 525) {
        if (clickY >= 215 && clickY <= 595) clickedIndex = 1;
        else if (clickY >= 612 && clickY <= 992) clickedIndex = 3;
      } else if (clickX >= 555 && clickX <= 1040) {
        if (clickY >= 215 && clickY <= 595) clickedIndex = 2;
        else if (clickY >= 612 && clickY <= 992) clickedIndex = 4;
      }
    } else {
      // Vertical 1080x1920: Left col [40, 525], Right col [555, 1040], Row 1 [250, 1036], Row 2 [1062, 1848]
      if (clickX >= 40 && clickX <= 525) {
        if (clickY >= 250 && clickY <= 1036) clickedIndex = 1;
        else if (clickY >= 1062 && clickY <= 1848) clickedIndex = 3;
      } else if (clickX >= 555 && clickX <= 1040) {
        if (clickY >= 250 && clickY <= 1036) clickedIndex = 2;
        else if (clickY >= 1062 && clickY <= 1848) clickedIndex = 4;
      }
    }

    if (clickedIndex) {
      const card = this.currentDay.cards.find(c => c.index === clickedIndex);
      if (card) {
        this.openCardActionModal(card);
      }
    }
  }

  // Open Interactive Card Action Modal
  openCardActionModal(card) {
    this.selectedActionCard = card;
    const modal = document.getElementById('cardActionModal');
    if (!modal) return;

    const hasCustomPhoto = !!this.customPhotos[card.index];
    const photoSrc = this.customPhotos[card.index] || card.photo;

    document.getElementById('actionModalTitle').textContent = `Card #${card.index} - ${card.title_en}`;
    document.getElementById('actionModalBadge').textContent = card.badge_gu || `માર્ગદર્શન #${card.index}`;
    document.getElementById('actionModalCardTitle').textContent = `${card.title_en} | ${card.title_gu}`;
    document.getElementById('actionModalDesc').textContent = `${card.desc_gu} (${card.desc_en})`;
    document.getElementById('actionModalImg').src = photoSrc;
    document.getElementById('actionModalPromptText').textContent = card.ai_prompt;

    const resetBtn = document.getElementById('modalResetPhotoBtn');
    if (resetBtn) {
      resetBtn.style.display = hasCustomPhoto ? 'inline-flex' : 'none';
    }

    modal.classList.add('active');
  }

  closeCardActionModal() {
    document.getElementById('cardActionModal')?.classList.remove('active');
    this.selectedActionCard = null;
  }

  handleModalSwapPhoto() {
    if (!this.selectedActionCard) return;
    this.activeSwapSlot = this.selectedActionCard.index;
    this.closeCardActionModal();
    this.fileInput.click();
  }

  handleModalCopyPrompt() {
    if (!this.selectedActionCard) return;
    this.copyGeminiPrompt(this.selectedActionCard);
  }

  async handleModalResetPhoto() {
    if (!this.selectedActionCard) return;
    const slot = this.selectedActionCard.index;
    await window.appStorage.removePhoto(this.currentDayId, slot);
    delete this.customPhotos[slot];
    this.closeCardActionModal();
    this.renderCardControlPanels();
    await this.renderPoster();
    this.showToast(`Reset Card #${slot} to default photo`, 'info');
  }

  // Render the 4 Interactive Card Control Panels
  renderCardControlPanels() {
    if (!this.cardsContainer || !this.currentDay) return;
    this.cardsContainer.innerHTML = '';

    const lang = this.currentLanguage;

    this.currentDay.cards.forEach((card) => {
      const hasCustomPhoto = !!this.customPhotos[card.index];
      const photoSrc = this.customPhotos[card.index] || card.photo;

      let title = card.title_en;
      let desc = card.desc_en;
      if (lang === 'gujarati') {
        title = card.title_gu;
        desc = card.desc_gu;
      } else if (lang === 'bilingual') {
        title = `${card.title_en} / ${card.title_gu}`;
        desc = `${card.desc_gu} (${card.desc_en})`;
      }

      const cardEl = document.createElement('div');
      cardEl.className = 'card-control-item';
      cardEl.setAttribute('data-card-index', card.index);
      cardEl.innerHTML = `
        <div class="card-ctrl-header">
          <span class="badge badge-action">
            ✨ ${card.badge_gu} (${card.badge_en})
          </span>
          ${hasCustomPhoto ? '<span class="custom-photo-badge">Custom Photo</span>' : ''}
        </div>
        
        <div class="card-ctrl-preview" title="Click to swap with your own clinical photo">
          <img src="${photoSrc}" alt="${card.title_en}" class="ctrl-thumb" />
          <div class="thumb-overlay">
            <span class="overlay-icon">📷</span>
            <span class="overlay-text">Click to Swap Photo</span>
          </div>
        </div>

        <div class="card-ctrl-body">
          <h4 class="ctrl-title">${title}</h4>
          <p class="ctrl-desc">${desc}</p>
        </div>

        <div class="card-ctrl-actions">
          <button class="btn-subtle btn-swap-photo" title="Upload custom clinic photo">
            📷 Swap Photo
          </button>
          ${
            hasCustomPhoto
              ? `<button class="btn-subtle btn-reset-photo" title="Reset to default photo">
                  🔄 Reset
                </button>`
              : ''
          }
          <button class="btn-subtle btn-copy-prompt btn-gemini-prompt" title="Copy Gemini Imagen 3 prompt">
            ✨ Copy Gemini Prompt
          </button>
        </div>
      `;

      // Click to Swap Photo (on thumb or button)
      const triggerSwap = () => {
        this.activeSwapSlot = card.index;
        this.fileInput.click();
      };
      cardEl.querySelector('.card-ctrl-preview').addEventListener('click', triggerSwap);
      cardEl.querySelector('.btn-swap-photo').addEventListener('click', triggerSwap);

      // Reset Photo Button
      const resetBtn = cardEl.querySelector('.btn-reset-photo');
      if (resetBtn) {
        resetBtn.addEventListener('click', async () => {
          await window.appStorage.removePhoto(this.currentDayId, card.index);
          delete this.customPhotos[card.index];
          this.renderCardControlPanels();
          await this.renderPoster();
          this.showToast(`Reset Card #${card.index} to default photo`, 'info');
        });
      }

      // Copy Gemini Photo Prompt Button
      cardEl.querySelector('.btn-copy-prompt').addEventListener('click', () => {
        this.copyGeminiPrompt(card);
      });

      this.cardsContainer.appendChild(cardEl);
    });
  }

  // Handle Photo File Upload
  handlePhotoFileSelected(event) {
    const file = event.target.files[0];
    if (!file || !this.activeSwapSlot) return;

    if (!file.type.startsWith('image/')) {
      this.showToast('Please select a valid image file', 'error');
      return;
    }

    const reader = new FileReader();
    reader.onload = async (e) => {
      const dataUrl = e.target.result;
      const slot = this.activeSwapSlot;

      // Save into IndexedDB for persistence
      await window.appStorage.savePhoto(this.currentDayId, slot, dataUrl);
      this.customPhotos[slot] = dataUrl;

      // Update UI and re-render
      this.renderCardControlPanels();
      await this.renderPoster();
      this.showToast(`Custom photo applied to Card #${slot}!`, 'success');

      // Reset input
      this.fileInput.value = '';
      this.activeSwapSlot = null;
    };
    reader.readAsDataURL(file);
  }

  // Copy Gemini Imagen 3 Prompt
  copyGeminiPrompt(card) {
    const prompt = card.ai_prompt;
    const msg = `✨ Copied Gemini Imagen 3 Prompt for Card #${card.index}! Drop it into Gemini Banav.`;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(prompt).then(
        () => {
          this.showToast(msg, 'success');
        },
        () => {
          this.fallbackCopyText(prompt, msg);
        }
      );
    } else {
      this.fallbackCopyText(prompt, msg);
    }
  }

  fallbackCopyText(text, msg = '✨ Copied Gemini Prompt to clipboard!') {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    this.showToast(msg, 'success');
  }

  // Download Single High-Res PNG Poster
  async downloadSinglePoster() {
    if (!this.currentDay) return;
    this.showToast('Generating High-Res PNG Poster...', 'info');

    let canvas;
    try {
      // Render full-res canvas with mandatory card image failure guard
      canvas = await this.renderer.exportPoster(this.currentDay, {
        format: this.currentFormat,
        language: this.currentLanguage,
        settings: this.settings,
        customPhotos: this.customPhotos
      });
    } catch (err) {
      console.error('Poster export halted:', err);
      this.showToast(`❌ ${err.message}`, 'error');
      return;
    }

    const safeTitle = this.currentDay.title_en.replace(/[^a-zA-Z0-9]/g, '_').substring(0, 30);
    const filename = `HealthPoster_${this.currentDay.id}_${safeTitle}_${this.currentFormat}_${this.currentLanguage}.png`;

    canvas.toBlob((blob) => {
      if (!blob) {
        this.showToast('Failed to generate image blob', 'error');
        return;
      }
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      this.showToast(`✅ Downloaded: ${filename}`, 'success');
    }, 'image/png');
  }

  // Share poster image through the native share sheet
  async shareToWhatsApp() {
    if (!this.currentDay) return;

    this.showToast('Preparing WhatsApp Share...', 'info');
    const day = this.currentDay;

    // Try Web Share API with File (with mandatory card image failure guard)
    let canvas;
    try {
      canvas = await this.renderer.exportPoster(day, {
        format: this.currentFormat,
        language: this.currentLanguage,
        settings: this.settings,
        customPhotos: this.customPhotos
      });
    } catch (err) {
      console.error('Share halted:', err);
      this.showToast(`❌ ${err.message}`, 'error');
      return;
    }

    canvas.toBlob(async (blob) => {
      const filename = `HealthPoster_${day.id}.png`;
      const file = new File([blob], filename, { type: 'image/png' });

      if (navigator.canShare && navigator.canShare({ files: [file] })) {
        try {
          await navigator.share({ files: [file] });
          this.showToast('Poster image shared successfully!', 'success');
          return;
        } catch (err) {
          if (err.name !== 'AbortError') {
            console.warn('Image share failed; downloading the poster instead:', err);
          } else {
            return;
          }
        }
      }

      // Fallback: download the PNG so the user can attach it manually
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);

      this.showToast('Poster downloaded. Attach the image in WhatsApp.', 'success');
    }, 'image/png');
  }

  // Search filter
  // Build one search entry per poster title and per pending scheduled observance
  buildSearchEntries() {
    const norm = (s) => String(s || '').normalize('NFC').toLowerCase();
    const entries = [];
    this.calendarData.forEach((d, order) => {
      const dateText = `${d.date_en} ${d.date_gu}`;
      entries.push({
        day: d, order, pending: false, title: d.title_en, titleGu: d.title_gu,
        hay: norm(`${d.title_en} ${d.title_gu} ${d.theme_en} ${dateText}`)
      });
      (d.observance_schedule_2026 || []).forEach((item) => {
        if (item.poster_status === 'PENDING_BILINGUAL_CONTENT_AND_IMAGES') {
          entries.push({
            day: d, order, pending: true, title: item.title_en, titleGu: '',
            hay: norm(`${item.title_en} ${dateText}`)
          });
        } else if (norm(item.title_en) !== norm(d.title_en)) {
          entries.push({
            day: d, order, pending: false, title: item.title_en, titleGu: '',
            hay: norm(`${item.title_en} ${dateText}`)
          });
        }
      });
    });
    return entries;
  }

  // Search observances by English/Gujarati title, theme or date; list every match
  handleSearch(query) {
    const input = document.getElementById('searchDayInput');
    const list = document.getElementById('searchResultsList');
    const status = document.getElementById('searchStatus');
    if (!list || !status) return;

    const q = String(query || '').normalize('NFC').toLowerCase().trim();
    this.searchActive = -1;
    list.innerHTML = '';
    input?.removeAttribute('aria-activedescendant');

    if (!q) {
      list.hidden = true;
      status.textContent = '';
      input?.setAttribute('aria-expanded', 'false');
      return;
    }

    if (!this.searchEntries) this.searchEntries = this.buildSearchEntries();
    const matches = this.searchEntries
      .filter((e) => e.hay.includes(q))
      .sort((a, b) => a.order - b.order);

    list.hidden = false;
    input?.setAttribute('aria-expanded', 'true');

    if (!matches.length) {
      status.textContent = 'No observances match your search.';
      const li = document.createElement('li');
      li.className = 'obs-result-empty';
      li.textContent = 'No observances match your search.';
      list.appendChild(li);
      return;
    }

    status.textContent = `${matches.length} ${matches.length === 1 ? 'result' : 'results'}. Use arrow keys and Enter to open one.`;
    matches.forEach((m, i) => {
      const li = document.createElement('li');
      li.id = `searchResult${i}`;
      li.className = 'obs-result';
      li.setAttribute('role', 'option');
      li.setAttribute('aria-selected', 'false');
      li.setAttribute('data-day-id', m.day.id);
      const badge = m.pending
        ? '<span class="obs-badge obs-badge-pending">Scheduled, poster pending</span>'
        : '<span class="obs-badge obs-badge-ready">Poster available</span>';
      const gu = m.titleGu
        ? `<span class="obs-result-gu">${this.escapeHtml(m.titleGu)}</span>`
        : (m.pending
          ? `<span class="obs-result-gu">No poster for this observance yet. Opens this date's poster: ${this.escapeHtml(m.day.title_en)}</span>`
          : '');
      li.innerHTML = `
        <span class="obs-result-date">${this.escapeHtml(m.day.date_en)} · ${this.escapeHtml(m.day.date_gu)}</span>
        <span class="obs-result-title">${this.escapeHtml(m.title)}</span>
        ${gu}${badge}`;
      list.appendChild(li);
    });
  }

  escapeHtml(s) {
    return String(s ?? '').replace(/[&<>"']/g, (c) => (
      { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
    ));
  }

  handleSearchKeydown(e) {
    const list = document.getElementById('searchResultsList');
    const input = document.getElementById('searchDayInput');
    const opts = list ? [...list.querySelectorAll('[role="option"]')] : [];
    if (e.key === 'Escape') {
      input.value = '';
      this.handleSearch('');
      return;
    }
    if (!opts.length) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      const step = e.key === 'ArrowDown' ? 1 : -1;
      this.searchActive = (this.searchActive + step + opts.length) % opts.length;
      opts.forEach((o, i) => {
        o.classList.toggle('active', i === this.searchActive);
        o.setAttribute('aria-selected', String(i === this.searchActive));
      });
      const cur = opts[this.searchActive];
      input.setAttribute('aria-activedescendant', cur.id);
      cur.scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter' && this.searchActive >= 0) {
      e.preventDefault();
      this.pickSearchResult(opts[this.searchActive].getAttribute('data-day-id'));
    }
  }

  // Load the chosen date through the normal day navigation
  pickSearchResult(dayId) {
    const input = document.getElementById('searchDayInput');
    if (input) input.value = '';
    this.handleSearch('');
    this.selectDay(dayId);
  }

  // Doctor Branding Modal
  openSettingsModal() {
    const modal = document.getElementById('settingsModal');
    if (!modal) return;

    document.getElementById('settingUseDoctor').checked = !!this.settings.useDoctorBranding;
    document.getElementById('settingDoctorName').value = this.settings.doctorName || '';
    document.getElementById('settingDoctorDegree').value = this.settings.doctorDegree || '';
    document.getElementById('settingClinicName').value = this.settings.clinicName || '';
    document.getElementById('settingContactInfo').value = this.settings.contactInfo || '';
    document.getElementById('settingCity').value = this.settings.city || '';

    modal.classList.add('active');
  }

  closeSettingsModal() {
    document.getElementById('settingsModal')?.classList.remove('active');
  }

  async saveSettingsFromModal() {
    this.settings = {
      useDoctorBranding: document.getElementById('settingUseDoctor').checked,
      doctorName: document.getElementById('settingDoctorName').value.trim(),
      doctorDegree: document.getElementById('settingDoctorDegree').value.trim(),
      clinicName: document.getElementById('settingClinicName').value.trim(),
      contactInfo: document.getElementById('settingContactInfo').value.trim(),
      city: document.getElementById('settingCity').value.trim()
    };

    await window.appStorage.saveSettings(this.settings);
    this.closeSettingsModal();
    this.showToast('Doctor branding settings saved!', 'success');
    await this.renderPoster();
  }

  // Toast Notification System
  showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-item toast-${type}`;
    const icon = type === 'success' ? '✅' : type === 'error' ? '⚠️' : 'ℹ️';
    toast.innerHTML = `<span class="toast-icon">${icon}</span> <span class="toast-msg">${message}</span>`;

    container.appendChild(toast);
    setTimeout(() => {
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 400);
    }, 3200);
  }

  // Service Worker Registration for PWA Offline Functionality
  registerServiceWorker() {
    if ('serviceWorker' in navigator) {
      const doRegister = () => {
        navigator.serviceWorker
          .register('./sw.js')
          .then((reg) => console.log('PWA ServiceWorker registered with scope:', reg.scope))
          .catch((err) => console.warn('PWA ServiceWorker registration failed:', err));
      };

      if (document.readyState === 'complete') {
        doRegister();
      } else {
        window.addEventListener('load', doRegister);
      }
    }
  }
}

// Initialize on DOMContentLoaded
window.addEventListener('DOMContentLoaded', () => {
  window.healthApp = new HealthPosterApp();
  window.healthPosterApp = window.healthApp;
});
