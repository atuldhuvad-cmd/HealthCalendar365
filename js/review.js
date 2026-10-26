/**
 * Annual Calendar 2026 Reference Console Logic
 * Handles 365-day filtering, source/history comparison, keyboard navigation,
 * and mobile-friendly interactions.
 */

class CalendarReviewApp {
  constructor() {
    this.reviewData = null;
    this.selectedDateId = '01-01';
    this.activeFilter = 'all';
    this.searchQuery = '';
    this.selectedMonth = 'all';
    this.currentMode = 'studio'; // 'studio' | 'review'
    
    this.init();
  }

  async init() {
    // 1. Load Review Data
    if (window.ANNUAL_REVIEW_DATA) {
      this.reviewData = window.ANNUAL_REVIEW_DATA;
    } else {
      try {
        const resp = await fetch('./data/annual_review_2026.json');
        this.reviewData = await resp.json();
      } catch (err) {
        console.error('Failed to load review data payload:', err);
        return;
      }
    }

    if (!this.reviewData || !this.reviewData.dates) {
      console.error('Review data payload is empty or invalid.');
      return;
    }

    // 2. Set default date from studio if valid
    const currentStudioDate = window.healthPosterApp ? window.healthPosterApp.currentDayId : '01-01';
    if (this.reviewData.dates.some(d => d.id === currentStudioDate)) {
      this.selectedDateId = currentStudioDate;
    }

    // 3. Setup UI bindings
    this.setupModeSwitcher();
    this.setupFilterChips();
    this.setupSearchAndMonth();
    this.setupNavigationButtons();
    this.setupModals();
    this.setupKeyboardShortcuts();

    // 4. Initial Render
    this.applyFiltersAndRender();
  }

  // View Mode Switcher (Poster Studio <-> Calendar Reference)
  setupModeSwitcher() {
    const studioBtn = document.getElementById('viewStudioBtn');
    const reviewBtn = document.getElementById('viewReviewBtn');
    const studioLayout = document.querySelector('.studio-layout');
    const observanceSearch = document.querySelector('.obs-search');
    const reviewLayout = document.getElementById('calendarReviewView');
    const statusIndicator = document.getElementById('modeStatusIndicator');

    if (!studioBtn || !reviewBtn || !reviewLayout) return;

    const switchMode = (mode) => {
      this.currentMode = mode;
      if (mode === 'review') {
        studioBtn.classList.remove('active');
        reviewBtn.classList.add('active');
        if (studioLayout) studioLayout.style.display = 'none';
        if (observanceSearch) observanceSearch.style.display = 'none';
        reviewLayout.classList.add('active');
        if (statusIndicator) {
          statusIndicator.innerHTML = '<span class="pulse-dot"></span><span class="indicator-text">Calendar Reference Mode</span>';
        }
        // Sync selected date from studio if possible
        if (window.healthPosterApp && window.healthPosterApp.currentDayId) {
          this.selectDate(window.healthPosterApp.currentDayId);
        }
      } else {
        reviewBtn.classList.remove('active');
        studioBtn.classList.add('active');
        if (studioLayout) studioLayout.style.display = '';
        if (observanceSearch) observanceSearch.style.display = '';
        reviewLayout.classList.remove('active');
        if (statusIndicator) {
          statusIndicator.innerHTML = '<span class="pulse-dot"></span><span class="indicator-text">Active Studio Mode</span>';
        }
        // Sync selected date to studio if possible
        if (window.healthPosterApp && this.selectedDateId) {
          window.healthPosterApp.selectDay(this.selectedDateId);
        }
      }
    };

    studioBtn.addEventListener('click', () => switchMode('studio'));
    reviewBtn.addEventListener('click', () => switchMode('review'));
  }

  // Filter Chips
  setupFilterChips() {
    const chips = document.querySelectorAll('.filter-chip');
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this.activeFilter = chip.getAttribute('data-filter') || 'all';
        this.applyFiltersAndRender();
      });
    });
  }

  // Search and Month Filter
  setupSearchAndMonth() {
    const searchInput = document.getElementById('reviewSearchInput');
    const clearBtn = document.getElementById('reviewClearSearchBtn');
    const monthSelect = document.getElementById('reviewMonthSelect');

    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.searchQuery = e.target.value.trim().toLowerCase();
        if (clearBtn) clearBtn.style.display = this.searchQuery ? 'block' : 'none';
        this.applyFiltersAndRender();
      });
    }

    if (clearBtn && searchInput) {
      clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        this.searchQuery = '';
        clearBtn.style.display = 'none';
        this.applyFiltersAndRender();
      });
    }

    if (monthSelect) {
      monthSelect.addEventListener('change', (e) => {
        this.selectedMonth = e.target.value;
        this.applyFiltersAndRender();
      });
    }
  }

  // Navigation Buttons
  setupNavigationButtons() {
    const prevBtn = document.getElementById('reviewPrevDayBtn');
    const nextBtn = document.getElementById('reviewNextDayBtn');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => this.navigateDay(-1));
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', () => this.navigateDay(1));
    }
  }

  // Keyboard Shortcuts
  setupKeyboardShortcuts() {
    window.addEventListener('keydown', (e) => {
      if (this.currentMode !== 'review') return;
      
      // Do not trigger shortcuts when typing inside an input
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
        if (e.key === 'Escape') {
          e.target.blur();
        }
        return;
      }

      if (e.key === 'ArrowLeft' || e.key === 'j') {
        e.preventDefault();
        this.navigateDay(-1);
      } else if (e.key === 'ArrowRight' || e.key === 'k') {
        e.preventDefault();
        this.navigateDay(1);
      } else if (e.key === '/') {
        e.preventDefault();
        const searchInput = document.getElementById('reviewSearchInput');
        if (searchInput) searchInput.focus();
      } else if (e.key === 'Escape') {
        this.closeModals();
      }
    });
  }

  // Modals setup
  setupModals() {
    const openLegBtn = document.getElementById('openLegendModalBtn');
    const closeLegBtn = document.getElementById('closeLegendModalBtn');
    const legModal = document.getElementById('legendModal');

    if (openLegBtn && legModal) {
      openLegBtn.addEventListener('click', () => legModal.classList.add('open'));
    }
    if (closeLegBtn && legModal) {
      closeLegBtn.addEventListener('click', () => legModal.classList.remove('open'));
    }

    // Close on backdrop click
    [legModal].forEach(m => {
      if (m) {
        m.addEventListener('click', (e) => {
          if (e.target === m) m.classList.remove('open');
        });
      }
    });
  }

  closeModals() {
    const legModal = document.getElementById('legendModal');
    if (legModal) legModal.classList.remove('open');
  }

  // Filter Algorithm
  applyFiltersAndRender() {
    if (!this.reviewData || !this.reviewData.dates) return;

    let filtered = this.reviewData.dates.filter(d => {
      // 1. Month filter
      if (this.selectedMonth !== 'all') {
        if (d.month !== parseInt(this.selectedMonth, 10)) return false;
      }

      // 2. Active filter chip
      if (this.activeFilter === 'placement_conflict') {
        if (!d.flags.placement_conflict) return false;
      } else if (this.activeFilter === 'evidence_concern') {
        if (!d.flags.evidence_concern) return false;
      } else if (this.activeFilter === 'retained_correction') {
        if (!d.flags.retained_content_correction) return false;
      }

      // 3. Search query
      if (this.searchQuery) {
        const q = this.searchQuery;
        const inId = d.id.toLowerCase().includes(q);
        const inDate = d.date_en.toLowerCase().includes(q) || d.date_gu.includes(q);
        const inCurTitle = (d.current_content.title_en + ' ' + d.current_content.title_gu).toLowerCase().includes(q);
        const inPropTitle = d.proposed_content ? (d.proposed_content.title_en + ' ' + d.proposed_content.title_gu).toLowerCase().includes(q) : false;
        if (!inId && !inDate && !inCurTitle && !inPropTitle) return false;
      }

      return true;
    });

    this.matchingDates = filtered;

    // Update count in header
    const countBadge = document.getElementById('reviewListCount');
    if (countBadge) {
      countBadge.textContent = `${filtered.length} / 365`;
    }

    // Render list
    this.renderDateList(filtered);

    // If current selected date is in filtered, keep it; else pick first
    if (!filtered.some(d => d.id === this.selectedDateId) && filtered.length > 0) {
      this.selectDate(filtered[0].id);
    } else if (filtered.length > 0) {
      this.renderDateDetail(this.selectedDateId);
    } else {
      this.renderEmptyDetail();
    }
  }

  // Render Date Navigation List
  renderDateList(dates) {
    const listContainer = document.getElementById('reviewDateList');
    if (!listContainer) return;

    if (dates.length === 0) {
      listContainer.innerHTML = '<div style="padding:20px;text-align:center;color:var(--rev-text-muted);">No matching dates found for current filter.</div>';
      return;
    }

    listContainer.innerHTML = '';
    dates.forEach(d => {
      const item = document.createElement('div');
      item.className = `date-list-item ${d.id === this.selectedDateId ? 'selected' : ''}`;
      item.setAttribute('data-date-id', d.id);

      // All dates are active for personal use; retain placement context.
      let pillClass = 'pill-active';
      let pillText = 'Active';
      if (d.placement_status === 'COEXISTING_DUAL_TRACK' || d.placement_status === 'SCHEDULE_CONFLICT_RECORDED') {
        pillClass = 'pill-conflict';
        pillText = 'Multi-Track';
      }

      // Title to show
      const title = d.proposed_content ? d.proposed_content.title_en : d.current_content.title_en;

      item.innerHTML = `
        <div class="item-left">
          <div class="item-date-line">
            <span>${d.id}</span>
            <span class="item-weekday">${d.weekday_2026.slice(0, 3)}</span>
            <span>• ${d.date_en}</span>
          </div>
          <div class="item-topic-title" title="${title}">${title}</div>
        </div>
        <div class="item-right">
          <span class="item-status-pill ${pillClass}">${pillText}</span>
        </div>
      `;

      item.addEventListener('click', () => {
        this.selectDate(d.id);
      });

      listContainer.appendChild(item);
    });
  }

  // Select a Date
  selectDate(dateId) {
    this.selectedDateId = dateId;

    // Highlight in list
    const items = document.querySelectorAll('.date-list-item');
    items.forEach(it => {
      if (it.getAttribute('data-date-id') === dateId) {
        it.classList.add('selected');
        it.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      } else {
        it.classList.remove('selected');
      }
    });

    this.renderDateDetail(dateId);
  }

  // Navigate Prev / Next Day
  navigateDay(step) {
    if (!this.matchingDates || this.matchingDates.length === 0) return;
    const currentIndex = this.matchingDates.findIndex(d => d.id === this.selectedDateId);
    let newIndex = currentIndex + step;
    if (newIndex < 0) newIndex = this.matchingDates.length - 1;
    if (newIndex >= this.matchingDates.length) newIndex = 0;
    this.selectDate(this.matchingDates[newIndex].id);
  }

  // Render Date Detail Workspace
  renderDateDetail(dateId) {
    const detailContainer = document.getElementById('reviewDetailContent');
    if (!detailContainer) return;

    const d = this.reviewData.dates.find(x => x.id === dateId);
    if (!d) return;

    // Status Ribbon
    let statusBadgesHtml = '';
    
    statusBadgesHtml += `<span class="ribbon-badge badge-emerald">✅ ACTIVE PERSONAL USE</span>`;
    if (d.flags.retained_content_correction) {
      statusBadgesHtml += `<span class="ribbon-badge" style="background:rgba(249,115,22,0.2);color:#f97316;border:1px solid #f97316;">🔧 CORRECTION HISTORY RETAINED</span>`;
    }

    // Placement Status
    if (d.placement_status === 'COEXISTING_DUAL_TRACK') {
      statusBadgesHtml += `<span class="ribbon-badge badge-blue">⚠️ COEXISTING MULTI-CAMPAIGN TRACK</span>`;
    } else if (d.placement_status === 'SCHEDULE_CONFLICT_RECORDED') {
      statusBadgesHtml += `<span class="ribbon-badge" style="background:rgba(239,68,68,0.2);color:#ef4444;border:1px solid #ef4444;">⚖️ DATE CONFLICT RECORDED</span>`;
    } else if (d.placement_status === 'DISTRIBUTION_GAP') {
      statusBadgesHtml += `<span class="ribbon-badge badge-amber">📅 CALENDAR DISTRIBUTION NOTE</span>`;
    } else if (d.placement_status === 'PROPOSED_REPLACEMENT') {
      statusBadgesHtml += `<span class="ribbon-badge" style="background:rgba(139,92,246,0.2);color:#c4b5fd;border:1px solid #8b5cf6;">🔄 ROUTINE REFERENCE OPTION</span>`;
    } else if (d.placement_status === 'PROPOSED_ADDITION') {
      statusBadgesHtml += `<span class="ribbon-badge" style="background:rgba(139,92,246,0.2);color:#c4b5fd;border:1px solid #8b5cf6;">🌱 OBSERVANCE REFERENCE OPTION</span>`;
    }

    // Visual Status
    if (d.visual_status === 'CURRENT_ACTIVE_ASSET') {
      statusBadgesHtml += `<span class="ribbon-badge badge-emerald">📷 CURRENT ACTIVE ASSET</span>`;
    } else {
      statusBadgesHtml += `<span class="ribbon-badge badge-blue">📷 EXISTING ASSET ACTIVE; OPTIONAL BRIEF AVAILABLE</span>`;
    }

    // Build Current Baseline Cards HTML
    let currentCardsHtml = '';
    d.current_content.cards.forEach(c => {
      currentCardsHtml += `
        <div class="review-card-item">
          <div class="card-item-header">
            <span class="card-num-badge">Card #${c.index}</span>
            <span class="card-visual-pill pill-asset-active">CURRENT_ACTIVE_ASSET</span>
          </div>
          <div class="card-content-bilingual">
            <div class="card-lang-block en">
              <strong>${this.escapeHtml(c.title_en)}</strong>
              <div>${this.escapeHtml(c.desc_en)}</div>
            </div>
            <div class="card-lang-block gu">
              <strong>${this.escapeHtml(c.title_gu)}</strong>
              <div>${this.escapeHtml(c.desc_gu)}</div>
            </div>
          </div>
          ${c.image_url ? `
            <div class="card-image-preview">
              <img src="${c.image_url}" alt="Active Card Photo" onerror="this.style.display='none'" />
            </div>
          ` : ''}
        </div>
      `;
    });

    // Build Proposed Cards HTML
    let proposedColumnHtml = '';
    if (d.proposed_content) {
      const p = d.proposed_content;
      let propCardsHtml = '';
      p.cards.forEach(c => {
        propCardsHtml += `
          <div class="review-card-item">
            <div class="card-item-header">
              <span class="card-num-badge">${c.badge_en ? this.escapeHtml(c.badge_en) : `Card #${c.index}`}</span>
              <span class="card-visual-pill pill-asset-draft">OPTIONAL REFERENCE</span>
            </div>
            <div class="card-content-bilingual">
              <div class="card-lang-block en">
                <strong>${this.escapeHtml(c.title_en)}</strong>
                <div>${this.escapeHtml(c.desc_en)}</div>
              </div>
              <div class="card-lang-block gu">
                <strong>${this.escapeHtml(c.title_gu)}</strong>
                <div>${this.escapeHtml(c.desc_gu)}</div>
              </div>
            </div>
            <div class="card-visual-prompt-box">
              <div class="prompt-box-header">
                <span>✨ Optional Visual Brief & AI Prompt</span>
                <button class="prompt-copy-btn" onclick="window.calendarReviewApp.copyText('${this.escapeHtml(c.ai_prompt)}')">Copy Prompt</button>
              </div>
              <div class="prompt-content-text">${this.escapeHtml(c.visual_brief)}</div>
              <div class="prompt-warning-banner">
                Reference only. The existing photo remains active until the doctor-owner replaces it.
              </div>
            </div>
          </div>
        `;
      });

      let sourcesHtml = '';
      if (p.authority_sources && p.authority_sources.length > 0) {
        sourcesHtml = `
          <div class="authority-box">
            <div class="authority-label">📚 Sourced Clinical / Policy Guidance:</div>
            <div class="authority-sources">
              ${p.authority_sources.map(s => s.url ? `<a href="${s.url}" target="_blank" rel="noopener noreferrer">${this.escapeHtml(s.title)} ↗</a>` : `<span>${this.escapeHtml(s.title)}</span>`).join(' • ')}
            </div>
          </div>
        `;
      }

      proposedColumnHtml = `
        <div class="comparison-column">
          <div class="column-header-bar">
            <h3>✨ Reference Option / Correction History</h3>
            <span class="column-tag badge-blue">REFERENCE</span>
          </div>
          <div class="topic-meta-box">
            <div class="topic-meta-title-en">${this.escapeHtml(p.title_en)}</div>
            <div class="topic-meta-title-gu">${this.escapeHtml(p.title_gu)}</div>
            <div class="topic-meta-desc">${this.escapeHtml(p.clinical_rationale)}</div>
          </div>
          ${sourcesHtml}
          <div class="comparison-cards-list">
            ${propCardsHtml}
          </div>
        </div>
      `;
    } else {
      // No replacement proposed -> Retained sound baseline
      proposedColumnHtml = `
          <div class="comparison-column" style="background:#071a2e;border:1px solid #06b6d4;">
          <div class="column-header-bar">
            <h3 style="color:#06b6d4;">🛡️ Retained Sound Baseline</h3>
            <span class="column-tag" style="background:rgba(6,182,212,0.2);color:#06b6d4;">ACTIVE PERSONAL USE</span>
          </div>
          <div class="topic-meta-box">
            <div class="topic-meta-title-en">No Content Alterations Proposed</div>
            <div class="topic-meta-desc" style="color:#a5f3fc;">
              No alternate content is recorded for this date. The current local poster remains active and may be corrected directly when the doctor-owner identifies an issue.
            </div>
          </div>
          <div style="padding:24px;text-align:center;color:var(--rev-text-muted);background:#051322;border-radius:8px;border:1px dashed var(--rev-border);">
            <div style="font-size:2rem;margin-bottom:8px;">✅</div>
            <strong style="color:#ffffff;">Current local content</strong>
            <p style="margin:4px 0 0 0;font-size:0.85rem;">Active in the poster studio as it stands.</p>
          </div>
        </div>
      `;
    }

    detailContainer.innerHTML = `
      <div class="detail-date-header-bar">
        <div class="detail-date-titles">
          <h2>📅 ${d.date_en}, 2026 (${d.weekday_2026})</h2>
          <p>${d.date_gu} ૨૦૨૬ • ${d.current_content.title_gu || d.current_content.title_en}</p>
        </div>
        <div class="detail-nav-buttons">
          <button id="reviewPrevDayBtn" class="btn-nav-day" title="Previous Date">◀ Prev Day <kbd>← / j</kbd></button>
          <button id="reviewNextDayBtn" class="btn-nav-day" title="Next Date">Next Day ▶ <kbd>→ / k</kbd></button>
        </div>
      </div>

      <div class="detail-status-ribbon">
        ${statusBadgesHtml}
      </div>

      <div class="comparison-grid">
        <!-- Current Baseline Column -->
        <div class="comparison-column">
          <div class="column-header-bar">
            <h3>📌 Current Active Content</h3>
            <span class="column-tag badge-emerald">ACTIVE ASSET</span>
          </div>
          <div class="topic-meta-box">
            <div class="topic-meta-title-en">${this.escapeHtml(d.current_content.title_en)}</div>
            <div class="topic-meta-title-gu">${this.escapeHtml(d.current_content.title_gu)}</div>
            <div class="topic-meta-desc">${this.escapeHtml(d.current_content.theme_en || '')}</div>
          </div>
          <div class="comparison-cards-list">
            ${currentCardsHtml}
          </div>
        </div>

        <!-- Proposed Content Column -->
        ${proposedColumnHtml}
      </div>

    `;

    // Re-bind prev/next day buttons in detail header
    const pBtn = document.getElementById('reviewPrevDayBtn');
    const nBtn = document.getElementById('reviewNextDayBtn');
    if (pBtn) pBtn.addEventListener('click', () => this.navigateDay(-1));
    if (nBtn) nBtn.addEventListener('click', () => this.navigateDay(1));
  }

  renderEmptyDetail() {
    const detailContainer = document.getElementById('reviewDetailContent');
    if (!detailContainer) return;
    detailContainer.innerHTML = `
      <div style="padding:60px 20px;text-align:center;color:var(--rev-text-muted);">
        <div style="font-size:3rem;margin-bottom:12px;">🔍</div>
        <h3 style="color:#ffffff;">No dates match your selected filters</h3>
        <p>Try resetting the search query or selecting "All Dates" above.</p>
      </div>
    `;
  }

  // Utility: Copy prompt text to clipboard
  copyText(text) {
    if (!text) return;
    navigator.clipboard.writeText(text).then(() => {
      if (window.healthPosterApp && window.healthPosterApp.showToast) {
        window.healthPosterApp.showToast('✨ Gemini Imagen 3 prompt copied to clipboard!', 'success');
      } else {
        alert('Prompt copied to clipboard!');
      }
    }).catch(err => {
      console.error('Failed to copy text:', err);
    });
  }

  escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
}

// Auto-initialize when DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.calendarReviewApp = new CalendarReviewApp();
});
