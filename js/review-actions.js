/* Local, content-bound copy decisions. No calendar activation or remote writes. */
(() => {
  'use strict';
  const STORAGE = 'healthcalendar2026.card-decisions.v1';
  const fields = ['title_en', 'desc_en', 'title_gu', 'desc_gu'];
  const statuses = ['APPROVED_COPY', 'EDITED_PENDING_APPROVAL', 'PENDING'];
  let decisions = {};
  let recoveryBackup = null;
  let app;
  let lastFocus;
  const sources = new Map();
  const keyFor = (p, c) => `${p.set_or_campaign_id}::${c.index}`;
  const originalFor = c => JSON.stringify(Object.fromEntries(fields.map(f => [f, c[f] || ''])));
  const current = (key, c) => decisions[key]?.original === originalFor(c) ? decisions[key] : null;
  const statusText = r => r?.status === 'APPROVED_COPY' ? 'Copy approved on this device (EN + GU)' : r?.status === 'EDITED_PENDING_APPROVAL' ? 'Edited — approval pending' : 'Your decision: pending';
  function message(text, error = false) {
    const el = document.getElementById('reviewSaveMessage');
    if (el) { el.textContent = text; el.style.color = error ? '#ffb4ab' : '#a7f3d0'; }
  }
  function save(next) {
    if (recoveryBackup !== null) { message('Export the existing saved data before starting new decisions. Your previous data has not been overwritten.',true); return false; }
    try {
      localStorage.setItem(STORAGE, JSON.stringify({schema_version: 1, decisions: next}));
      decisions = next;
      message('Saved on this browser. Export a backup to keep or share your decisions.');
      refreshCount();
      return true;
    } catch (_) {
      message('Could not save. Browser storage may be full or disabled; your decision was not recorded.', true);
      return false;
    }
  }
  function refreshCount() {
    const count = Object.entries(decisions).filter(([k,r]) => sources.has(k) && r.original === originalFor(sources.get(k).card) && r.status === 'APPROVED_COPY').length;
    const el = document.getElementById('reviewApprovalCount');
    if (el) el.textContent = `${count} card copies approved on this device`;
  }
  function validate(payload) {
    if (payload?.schema_version !== 1 || !payload.decisions || Array.isArray(payload.decisions) || typeof payload.decisions !== 'object') throw Error('Unrecognised review file.');
    const out = {};
    for (const [key,r] of Object.entries(payload.decisions)) {
      if (!sources.has(key) || !r || typeof r !== 'object' || !statuses.includes(r.status)) throw Error('File contains an unknown card or decision.');
      if (r.original !== originalFor(sources.get(key).card)) throw Error('A card has changed since this file was exported. Nothing imported.');
      if (r.edited && (typeof r.edited !== 'object' || !fields.every(f => typeof r.edited[f] === 'string' && r.edited[f].trim() && r.edited[f].length <= 12000))) throw Error('Invalid edited card fields.');
      if (r.note != null && (typeof r.note !== 'string' || r.note.length > 12000)) throw Error('Invalid note.');
      out[key] = {status:r.status, original:r.original, ...(r.edited ? {edited:Object.fromEntries(fields.map(f=>[f,r.edited[f]]))}:{}), note:r.note || '', reviewed_at:typeof r.reviewed_at === 'string' ? r.reviewed_at : '', scope:'EN_GU_CLINICAL_COPY_ONLY'};
    }
    return out;
  }
  function record(key, card, status, edited, note) {
    const entry = {original:originalFor(card), status, ...(edited?{edited}:{}), note:note || '', reviewed_at:new Date().toISOString(), scope:'EN_GU_CLINICAL_COPY_ONLY'};
    if (save({...decisions, [key]:entry})) app.renderDateDetail(app.selectedDateId);
  }
  function edit(key, card) {
    const previous = current(key,card);
    const value = previous?.edited || card;
    lastFocus = document.activeElement;
    const dialog = document.createElement('dialog');
    dialog.className = 'review-copy-dialog';
    const title = document.createElement('h2'); title.textContent = 'Edit clinical copy — English and Gujarati';
    dialog.append(title);
    const form = document.createElement('form');
    const inputs = {};
    const labels = {title_en:'English title',desc_en:'English description',title_gu:'ગુજરાતી શીર્ષક',desc_gu:'ગુજરાતી વર્ણન'};
    for (const field of fields) {
      const label = document.createElement('label'); label.textContent = labels[field];
      const input = document.createElement('textarea'); input.name=field; input.value=value[field] || ''; input.rows=field.startsWith('desc')?5:2; input.required=true; input.maxLength=12000;
      input.lang=field.endsWith('gu')?'gu':'en'; label.append(input);form.append(label);inputs[field]=input;
    }
    const noteLabel=document.createElement('label');noteLabel.textContent='Review note (optional)';
    const note=document.createElement('textarea');note.name='note';note.value=previous?.note||'';note.rows=2;note.maxLength=12000;noteLabel.append(note);form.append(noteLabel);
    const hint=document.createElement('p');hint.textContent='Saving an edit leaves copy approval pending. Images and calendar placement are not approved here.';form.append(hint);
    const submit=document.createElement('button');submit.type='submit';submit.textContent='Save edit — pending';
    const cancel=document.createElement('button');cancel.type='button';cancel.textContent='Cancel';cancel.onclick=()=>dialog.close();
    form.append(submit,cancel);
    form.onsubmit=e=>{
      e.preventDefault();
      const edited=Object.fromEntries(fields.map(f=>[f,inputs[f].value.trim()]));
      if (!fields.every(f=>edited[f])) { form.reportValidity(); return; }
      const entry={original:originalFor(card),status:'EDITED_PENDING_APPROVAL',edited,note:note.value.trim(),reviewed_at:new Date().toISOString(),scope:'EN_GU_CLINICAL_COPY_ONLY'};
      if (save({...decisions,[key]:entry})) {dialog.close();app.renderDateDetail(app.selectedDateId);}
    };
    dialog.append(form);document.body.append(dialog);
    dialog.addEventListener('keydown',e=>e.stopPropagation());
    dialog.onclose=()=>{dialog.remove(); if(lastFocus?.isConnected)lastFocus.focus();};
    dialog.showModal();inputs.title_en.focus();
  }
  function enhance(dateId) {
    const day=app.reviewData.dates.find(d=>d.id===dateId);
    const proposal=day?.proposed_content;
    if (!proposal) return;
    const cards=document.querySelectorAll('#reviewDetailContent .comparison-column:nth-child(2) .review-card-item');
    proposal.cards.forEach((card,i)=>{
      const node=cards[i]; if(!node)return;
      const key=keyFor(proposal,card), entry=current(key,card);
      if(entry?.edited){
        for(const [lang,block] of [['en',node.querySelector('.card-lang-block.en')],['gu',node.querySelector('.card-lang-block.gu')]]){
          block.querySelector('strong').textContent=entry.edited['title_'+lang];
          block.querySelector('div').textContent=entry.edited['desc_'+lang];
        }
      }
      const controls=document.createElement('div');controls.className='review-copy-actions';
      const status=document.createElement('p');status.className='review-copy-state';status.textContent=statusText(entry);status.setAttribute('role','status');controls.append(status);
      const approve=document.createElement('button');approve.type='button';approve.textContent=entry?.status==='APPROVED_COPY'?'Copy approved ✓':'Approve copy (EN + GU)';approve.disabled=entry?.status==='APPROVED_COPY';approve.onclick=()=>record(key,card,'APPROVED_COPY',entry?.edited,entry?.note);
      const editBtn=document.createElement('button');editBtn.type='button';editBtn.textContent='Edit copy';editBtn.onclick=()=>edit(key,card);
      const pending=document.createElement('button');pending.type='button';pending.textContent='Keep pending';pending.onclick=()=>record(key,card,'PENDING',entry?.edited,entry?.note);
      controls.append(approve,editBtn,pending);
      if(entry?.note){const p=document.createElement('p');p.textContent='Note: '+entry.note;controls.append(p);}
      const scope=document.createElement('small');scope.textContent='Text decision only. Images and placement stay pending. Repeated identical cards share this decision.';controls.append(scope);node.prepend(controls);
    });
  }
  document.addEventListener('DOMContentLoaded',()=>{
    app=window.calendarReviewApp;
    if(!app?.reviewData)return;
    for(const day of app.reviewData.dates)for(const p of day.proposed_variants || (day.proposed_content?[day.proposed_content]:[]))for(const c of p.cards){
      const key=keyFor(p,c);
      if(sources.has(key)&&originalFor(sources.get(key).card)!==originalFor(c)){
        // Distinct versions must never share approval state.
        p.set_or_campaign_id=p.set_or_campaign_id+'@'+day.id;
      }
      sources.set(keyFor(p,c),{card:c});
    }
    const bar=document.createElement('section');bar.className='review-decision-toolbar';bar.innerHTML='<strong id="reviewApprovalCount"></strong><p>Approve or edit card text below. Decisions stay in this browser; export them to back up or share. No active calendar changes are made.</p><button type="button" id="exportReviewDecisions">Export decisions</button> <button type="button" id="importReviewDecisions">Import decisions</button><input type="file" id="reviewDecisionsFile" accept=".json,application/json" hidden><p id="reviewSaveMessage" role="status" aria-live="polite"></p>';
    document.querySelector('.review-controls-bar').after(bar);
    try { const saved=localStorage.getItem(STORAGE); if(saved){recoveryBackup=saved;decisions=validate(JSON.parse(saved));recoveryBackup=null;} }
    catch(_){message('Saved decisions do not match this content version or could not be read. Export the existing data before starting new decisions.',true);}
    refreshCount();
    document.getElementById('exportReviewDecisions').onclick=()=>{
      const recovering=recoveryBackup!==null;
      const blob=new Blob([recoveryBackup || JSON.stringify({schema_version:1,exported_at:new Date().toISOString(),calendar_year:2026,scope:'EN_GU_CLINICAL_COPY_ONLY',decisions},null,2)],{type:'application/json'});
      const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=recovering?'health-calendar-2026-review-recovery.json':'health-calendar-2026-review-decisions.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);recoveryBackup=null;message(recovering?'Previous saved data exported for recovery. You may now start new decisions.':'Export downloaded. Keep this file as your backup and send it here when ready.');
    };
    const picker=document.getElementById('reviewDecisionsFile');
    document.getElementById('importReviewDecisions').onclick=()=>picker.click();
    picker.onchange=async()=>{try{
      const file=picker.files[0];if(!file)return;if(file.size>5*1024*1024)throw Error('Review file is too large.');
      const imported=validate(JSON.parse(await file.text()));
      const comparable=r=>JSON.stringify([r.status,r.original,r.edited?fields.map(f=>r.edited[f]):null,r.note||'']);
      for(const [key,r] of Object.entries(imported))if(decisions[key]&&comparable(decisions[key])!==comparable(r))throw Error('Import conflicts with existing decisions. Nothing was changed; use the current browser to resolve the card first.');
      if(save({...decisions,...imported})){app.renderDateDetail(app.selectedDateId);message('Compatible decisions imported.');}
    }catch(e){message(e.message || 'Import failed. Nothing changed.',true);}finally{picker.value='';}};
    const render=app.renderDateDetail.bind(app);app.renderDateDetail=(id)=>{render(id);enhance(id);};
    app.renderDateDetail(app.selectedDateId);
    // Unapproved placement must not be represented as already approved.
    for(const d of app.reviewData.dates)for(const p of d.proposed_variants||(d.proposed_content?[d.proposed_content]:[]))if(p.clinical_rationale)p.clinical_rationale=p.clinical_rationale.replace(/Approved for scheduling/gi,'Proposed for scheduling; placement approval pending');
    app.renderDateDetail(app.selectedDateId);
  });
})();
