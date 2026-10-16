/**
 * Main Application Logic for 365-Day Health Poster Studio (India)
 * Handles state, day selection, format & language toggling, photo upload/swap,
 * AI prompt copying, WhatsApp sharing, single download, and batch Oct 15-21 downloads.
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

    // 4. Populate Month/Day selector and Quick Week Bar
    this.setupQuickWeekBar();
    this.populateDateSelect();

    // 5. Load and Display Default Day (October 15)
    await this.selectDay(this.currentDayId);

    // Register Service Worker for Offline PWA
    this.registerServiceWorker();
  }

  // Quick Week Bar (Oct 15 - Oct 21 Observance Posters)
  setupQuickWeekBar() {
    const weekContainer = document.getElementById('quickWeekPills');
    if (!weekContainer) return;

    // Grab all posters for Oct 15-21
    const octPosters = this.calendarData.filter(d => d.month === 10 && d.day >= 15 && d.day <= 21);

    weekContainer.innerHTML = '';
    octPosters.forEach((d) => {
      const btn = document.createElement('button');
      btn.className = `week-pill-btn ${d.id === this.currentDayId ? 'active' : ''}`;
      btn.setAttribute('data-day-id', d.id);
      btn.innerHTML = `
        <span class="pill-date">${d.date_en}</span>
        <span class="pill-topic">${d.title_en}</span>
      `;
      btn.addEventListener('click', () => {
        this.selectDay(d.id);
      });
      weekContainer.appendChild(btn);
    });
  }

  // Populate Month & Day Selectors and Search
  populateDateSelect() {
    const datePicker = document.getElementById('dateSelectInput');
    if (!datePicker) return;

    datePicker.innerHTML = '';
    this.calendarData.forEach((day) => {
      const opt = document.createElement('option');
      opt.value = day.id;
      opt.textContent = `${day.date_en} (${day.date_gu}) - ${day.title_en}`;
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
    document.getElementById('batchDownloadBtn')?.addEventListener('click', () => this.batchDownloadOctWeek());

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

    // Update Quick Week Pills active state
    document.querySelectorAll('.week-pill-btn').forEach((btn) => {
      btn.classList.toggle('active', btn.getAttribute('data-day-id') === dayId);
    });

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

    // Update button states
    document.querySelectorAll('[data-format-toggle]').forEach((btn) => {
      btn.classList.toggle('active', btn.getAttribute('data-format-toggle') === format);
    });

    this.canvasWrapper.setAttribute('data-aspect', format);
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

    const contW = container.clientWidth - 40;
    const contH = container.clientHeight - 40;
    const canvasW = this.previewCanvas.width;
    const canvasH = this.previewCanvas.height;

    const scaleX = contW / canvasW;
    const scaleY = contH / canvasH;
    const fitScale = Math.min(scaleX, scaleY, 1.0);

    const effectiveScale = fitScale * this.zoomLevel;
    this.previewCanvas.style.transform = `scale(${effectiveScale})`;
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
      // Vertical 1080x1920: Left col [40, 525], Right col [555, 1040], Row 1 [250, 975], Row 2 [1005, 1730]
      if (clickX >= 40 && clickX <= 525) {
        if (clickY >= 250 && clickY <= 975) clickedIndex = 1;
        else if (clickY >= 1005 && clickY <= 1730) clickedIndex = 3;
      } else if (clickX >= 555 && clickX <= 1040) {
        if (clickY >= 250 && clickY <= 975) clickedIndex = 2;
        else if (clickY >= 1005 && clickY <= 1730) clickedIndex = 4;
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

  // Share to WhatsApp (Web Share API with image file + bilingual text caption)
  async shareToWhatsApp() {
    if (!this.currentDay) return;

    this.showToast('Preparing WhatsApp Share...', 'info');
    const day = this.currentDay;

    // Build rich bilingual WhatsApp text message
    let whatsappText = `🌟 *${day.date_en} | ${day.date_gu}*\n`;
    whatsappText += `🏥 *${day.title_en}*\n`;
    whatsappText += `✨ *${day.title_gu}*\n\n`;
    whatsappText += `📌 *${day.theme_en}*\n`;
    whatsappText += `📌 *${day.theme_gu}*\n\n`;

    const doCards = day.cards.filter(c => c.type === 'do');
    const dontCards = day.cards.filter(c => c.type === 'dont');
    const infoCards = day.cards.filter(c => c.type !== 'do' && c.type !== 'dont');

    if (doCards.length > 0) {
      whatsappText += `✅ *આટલું જરૂર કરો / DO's:*\n`;
      doCards.forEach((c, idx) => {
        whatsappText += `${idx + 1}. *${c.title_gu}*: ${c.desc_gu}\n`;
      });
      whatsappText += `\n`;
    }

    if (dontCards.length > 0) {
      whatsappText += `❌ *આટલું ક્યારેય ન કરો / DON'Ts:*\n`;
      dontCards.forEach((c, idx) => {
        whatsappText += `${idx + 1}. *${c.title_gu}*: ${c.desc_gu}\n`;
      });
      whatsappText += `\n`;
    }

    if (infoCards.length > 0) {
      whatsappText += `💡 *મુખ્ય આરોગ્ય માર્ગદર્શન / Key Health Guidance:*\n`;
      infoCards.forEach((c, idx) => {
        whatsappText += `${idx + 1}. *${c.title_gu}*: ${c.desc_gu}\n`;
      });
      whatsappText += `\n`;
    }

    if (this.settings.useDoctorBranding && this.settings.doctorName) {
      whatsappText += `🩺 *${this.settings.doctorName}* (${this.settings.doctorDegree || ''})\n`;
      whatsappText += `🏥 ${this.settings.clinicName || ''} • 📞 ${this.settings.contactInfo || ''}\n`;
    } else {
      whatsappText += `📢 *જાહેર જનતાના આરોગ્ય હિતમાં પ્રસારિત* | 365 Days Health Awareness\n`;
    }

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
          await navigator.share({
            title: day.title_en,
            text: whatsappText,
            files: [file]
          });
          this.showToast('Shared successfully!', 'success');
          return;
        } catch (err) {
          if (err.name !== 'AbortError') {
            console.warn('Web Share failed, using direct WhatsApp URL fallback:', err);
          } else {
            return;
          }
        }
      }

      // Fallback: Trigger PNG download & open WhatsApp Web/App with text prefilled
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);

      const encodedText = encodeURIComponent(whatsappText);
      const waUrl = `https://api.whatsapp.com/send?text=${encodedText}`;
      window.open(waUrl, '_blank');
      this.showToast('Downloaded poster & opened WhatsApp message!', 'success');
    }, 'image/png');
  }

  // Batch Download All 7 Days (Oct 15 - Oct 21)
  async batchDownloadOctWeek() {
    const octWeekIds = ['10-15', '10-16', '10-17', '10-18', '10-19', '10-20', '10-21'];
    const weekDays = this.calendarData.filter((d) => octWeekIds.includes(d.id));

    if (weekDays.length === 0) {
      this.showToast('Oct 15-21 days not found', 'error');
      return;
    }

    this.showProgressModal(true, 'Rendering and downloading full week (Oct 15–21)...');

    for (let i = 0; i < weekDays.length; i++) {
      const day = weekDays[i];
      const step = i + 1;
      this.updateProgressModal(step, weekDays.length, `Generating ${day.date_en} (${day.title_en})...`);

      // Check if custom photos exist for this day
      const dayCustomPhotos = {};
      for (let idx = 1; idx <= 4; idx++) {
        const saved = await window.appStorage.getPhoto(day.id, idx);
        if (saved) dayCustomPhotos[idx] = saved;
      }

      // Render canvas with mandatory card image failure guard
      let canvas;
      try {
        canvas = await this.renderer.exportPoster(day, {
          format: this.currentFormat,
          language: this.currentLanguage,
          settings: this.settings,
          customPhotos: dayCustomPhotos
        });
      } catch (err) {
        console.error(`Skipping Day ${day.id}:`, err);
        this.showToast(`⚠️ Skipped Day ${day.id}: card photo missing or unreadable`, 'error');
        continue;
      }

      // Download file with short timeout between downloads to prevent browser throttling
      await new Promise((resolve) => {
        canvas.toBlob((blob) => {
          const safeName = day.title_en.replace(/[^a-zA-Z0-9]/g, '_').substring(0, 25);
          const filename = `${day.id}_${safeName}_${this.currentFormat}.png`;
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = filename;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          URL.revokeObjectURL(url);

          setTimeout(resolve, 600); // 600ms pause between downloads
        }, 'image/png');
      });
    }

    this.showProgressModal(false);
    this.showToast('🎉 All 7 Days (Oct 15–21) downloaded successfully!', 'success');
  }

  // Search filter
  handleSearch(query) {
    if (!query) return;
    const q = query.toLowerCase().trim();
    const match = this.calendarData.find(
      (d) =>
        d.date_en.toLowerCase().includes(q) ||
        d.title_en.toLowerCase().includes(q) ||
        d.title_gu.toLowerCase().includes(q) ||
        d.theme_en.toLowerCase().includes(q)
    );
    if (match) {
      this.selectDay(match.id);
    }
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

  // Progress Modal for Batch Download
  showProgressModal(show, title = '') {
    const modal = document.getElementById('progressModal');
    if (!modal) return;
    if (show) {
      document.getElementById('progressModalTitle').textContent = title;
      modal.classList.add('active');
    } else {
      modal.classList.remove('active');
    }
  }

  updateProgressModal(current, total, detail) {
    const pct = Math.round((current / total) * 100);
    const bar = document.getElementById('progressBarFill');
    const label = document.getElementById('progressDetail');
    if (bar) bar.style.width = `${pct}%`;
    if (label) label.textContent = `${detail} (${current}/${total} - ${pct}%)`;
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
});
