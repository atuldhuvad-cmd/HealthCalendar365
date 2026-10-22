# Comprehensive Card-Level Audit & Findings Register for 207 Retained Routine Days (2026)

**Document ID:** `AUDIT-RETAINED-207-V2`  
**Clinical Auditor:** Public Health Specialist & Clinical Audit Team (HealthCalendar365)  
**Target Authority:** Dr. Atul Dhuvad (Senior Medical Doctor, Public Health Specialist, District Health Trainer, Gujarat)  
**Scope:** Exhaustive clinical, numerical, translation, and device-specificity review of all 207 retained baseline routine days in `health_365.json` across 34 distinct CPHC topics.  
**Governance Rule:** Review-only proposal. All active files remain untouched; mechanical validation is separated strictly from clinical approval; all proposed copy revisions are registered as pending decisions for Dr. Atul Dhuvad's final consolidated sign-off.  

---

## 1. Executive Summary & Audit Methodology

### 1.1 Scope & Technical Distinction
- **Total Calendar Days Audited:** Exactly 207 retained routine non-observance dates (56.7% of the 365-day calendar).
- **Distinct CPHC Topic Sets:** Exactly 34 distinct topics.
- **Card Content Payload:** 34 unique card templates (each having 4 bilingual cards = 136 distinct cards, repeating to form 828 card occurrences).
- **Technical Hash Distinction:**
  - **Raw Source Record Hash:** Each calendar date entry in `health_365.json` possesses a distinct SHA-256 hash because header fields (`id`, `month`, `day`, `date_en`, `date_gu`) vary daily.
  - **Normalized Card Content Hash:** When extracting the 4-card educational payload (`index`, `title_en`, `desc_en`, `title_gu`, `desc_gu`), repeating occurrences of each topic are **100% byte-identical** across all dates. Consequently, clinical assessments and corrections apply identically across every date sharing that content hash.

### 1.2 Summary of Findings & Reclassification
The previous preliminary audit's blanket 'all medically sound / zero revisions' conclusion has been **completely rescinded**. A rigorous clinical review against current MoHFW, ICMR, WHO, GINA, GOLD, and NAP-SE guidelines identified specific clinical, numerical, device-specificity, and absolute-claim errors in **6 topic sets** (representing 45 calendar dates), alongside the previously flagged schedular gap in Palliative Care (3 dates).

| Assessment Category | Topic Count | Affected Calendar Dates | Governance Action |
| :--- | :--- | :--- | :--- |
| **`PROPOSED_REVISION` (Clinical / Numerical / Absolute Errors)** | **6 Topics** | **45 Dates** | Concrete wording corrections drafted and registered in `PENDING_DECISIONS_REGISTER.md` (`DEC-14` to `DEC-19`). Active files remain frozen. |
| **`PENDING_DECISION_GAP` (Distribution Gap)** | **1 Topic** | **3 Dates** | Palliative Care (`[9a65761e7076]`): Clinically sound text, but 6-month gap between August 21 and March 01 flagged under `DEC-13`. |
| **`RETAIN_CONFIRMED` (Clinically Sound Baseline)** | **27 Topics** | **159 Dates** | Verified sound, evidence-based, safe, and culturally adapted. Maintained without alterations. |
| **Total Retained Routine Calendar** | **34 Topics** | **207 Dates** | Full annual baseline calendar audited card-by-card. |

---

## 2. Priority Clinical Findings & Proposed Wording Register

The following 6 topics contain factual, numerical, translation, or absolute-claim errors that must be reviewed by Dr. Atul Dhuvad:

### Finding DEC-14: Hypertension Screening & Blood Pressure Control
- **Content Hash:** `e59865343a6e`
- **Clinical Status:** **`PROPOSED_REVISION`**
- **Affected Calendar Dates (9 dates):** 01-18, 02-22, 03-26, 04-30, 06-03, 07-07, 08-11, 11-23, 12-27
- **Primary Sourced Authority:** WHO Guideline on Sodium Intake for Adults and Children (2020); MoHFW NP-NCD Operational Guidelines; ICMR Guidelines for Management of Hypertension.
- **Affected Card:** Card 3
- **Clinical Critique:** HIGH-SEVERITY NUMERICAL/CHEMICAL ERROR: Card 3 incorrectly states 'Restrict total daily sodium intake to less than 1 level teaspoon (5g)'. Chemically, 5 g of table salt (NaCl) provides approximately 2 g (2000 mg) of elemental sodium. Confusing salt with sodium suggests 5 g of sodium is permissible, which represents 12.5 g of salt (more than double the safe physiological ceiling).

**Proposed Corrected Bilingual Copy (Registered under `DEC-14`):**

```markdown
English Proposed Correction:
Restrict total daily salt intake to less than 1 level teaspoon (5 g), which corresponds to under 2 g (2000 mg) of sodium. Avoid adding raw salt at the table, and limit pickles, papads, and salted snacks.

Gujarati Proposed Correction:
દૈનિક મીઠાનો વપરાશ ૧ નાની ચમચી (૫ ગ્રામ મીઠું, જે ૨ ગ્રામ સોડિયમ બરાબર છે) થી ઓછો રાખો; જમવામાં ઉપરથી કાચું મીઠું ન નાખો અને અથાણાં, પાપડ કે ખારી વસ્તુઓ મર્યાદિત કરો.
```


### Finding DEC-15: Chronic Respiratory Health (COPD & Asthma)
- **Content Hash:** `ac54dd49cd74`
- **Clinical Status:** **`PROPOSED_REVISION`**
- **Affected Calendar Dates (9 dates):** 01-23, 02-27, 03-31, 05-04, 06-08, 07-12, 08-16, 09-20, 11-28
- **Primary Sourced Authority:** Global Initiative for Chronic Obstructive Lung Disease (GOLD 2024); Global Initiative for Asthma (GINA 2023); National College of Chest Physicians (NCCP) India Consensus Guidelines.
- **Affected Card:** Card 1 & Card 4
- **Clinical Critique:** DEVICE SPECIFICITY ERROR & ABSOLUTE SAFETY CLAIM: (1) Card 1 gives universal spacer advice ('Use Prescribed Inhalers with Spacer Daily'). Spacers/valved holding chambers are specifically indicated for pressurized Metered Dose Inhalers (pMDIs); Dry Powder Inhalers (DPIs like Rotahalers, Accuhalers, Turbuhalers) and Breath-Actuated Inhalers must never be attached to spacers. (2) Card 4 Gujarati text claims inhalers improve breathing 'without side effects' ('આડઅસર વગર'). Inhaled corticosteroids and bronchodilators carry recognized adverse effects (oral candidiasis, dysphonia, reflex coughing, tachycardia). Rinsing mouth/gargling after ICS is clinically mandatory; claiming zero side effects undermines patient vigilance.

**Proposed Corrected Bilingual Copy (Registered under `DEC-15`):**

```markdown
English Proposed Correction:
Card 1: Use prescribed inhalers daily as instructed for your device; for pressurized metered-dose inhalers (pMDIs), a spacer helps deliver medication effectively into the airways.
Card 4: Inhalers deliver targeted, low-dose medicine directly to the lungs with far fewer systemic effects than oral steroid tablets; they are non-addictive maintenance therapies. Always rinse your mouth after steroid inhalers.

Gujarati Proposed Correction:
Card 1: ડૉક્ટરની સલાહ મુજબ યોગ્ય પદ્ધતિથી નિયમિત ઇનહેલર લો; મીટર્ડ-ડોઝ ઇનહેલર (pMDI) સાથે સ્પેસર સાધન વાપરવાથી દવા ફેફસાં સુધી સરળતાથી પહોંચે છે.
Card 4: ઇનહેલરથી દવા સીધી ફેફસાં સુધી પહોંચતી હોવાથી ગોળીઓ કરતાં ઘણી ઓછી આડઅસર થાય છે અને તેની કોઈ આદત પડતી નથી; સ્ટીરોઈડ ઇનહેલર લીધા પછી હંમેશા મોં સાફ કરી કોગળા કરો.
```


### Finding DEC-16: Breast & Cervical Cancer Early Screening
- **Content Hash:** `dc1f8cd74427`
- **Clinical Status:** **`PROPOSED_REVISION`**
- **Affected Calendar Dates (9 dates):** 02-25, 03-29, 05-02, 06-06, 07-10, 08-14, 09-18, 11-26, 12-30
- **Primary Sourced Authority:** Operational Framework for Comprehensive Primary Health Care: Screening of Common NCDs, MoHFW; WHO Cervical Cancer Screening Guidelines.
- **Affected Card:** Card 2 & Card 4
- **Clinical Critique:** ABSOLUTE GUARANTEE CLAIM & TRANSLATION MISMATCH: (1) Card 2 Gujarati copy claims cervical cancer detected early is '100% curable' ('પ્રારંભિક તબક્કે કેન્સર ૧૦૦% સાજું થાય છે'). Absolute 100% cure guarantees are medically untenable in oncology; early detection enables highly successful treatment and dramatically improves survival, but cannot guarantee 100% cure. (2) Card 4 Gujarati copy claims HPV vaccination provides 'lifelong protection' ('આજીવન રક્ષણ'), whereas the English accurately notes it prevents up to 90% of cervical cancers. Suggesting lifelong total immunity may cause women to erroneously skip recommended adult screening.

**Proposed Corrected Bilingual Copy (Registered under `DEC-16`):**

```markdown
English Proposed Correction:
Card 2: Women aged 30-65 should undergo free VIA screening every 5 years at Ayushman Arogya Mandir to detect cervical pre-cancer early, when treatment is most effective.
Card 4: Vaccinating adolescent girls aged 9-14 with Human Papillomavirus (HPV) vaccine prevents up to 90% of cervical cancers; routine adult screening remains recommended.

Gujarati Proposed Correction:
Card 2: ૩૦ થી ૬૫ વર્ષની બહેનો દર ૫ વર્ષે આરોગ્ય કેન્દ્ર પર ગર્ભાશયના મુખની મફત તપાસ (VIA) કરાવો; પ્રારંભિક તબક્કે ઓળખ થવાથી સમયસર સફળ સારવાર શક્ય બને છે.
Card 4: ૯ થી ૧૪ વર્ષની કિશોરીઓને HPV રસી અપાવો; આ રસી મોટાભાગના ગર્ભાશયના કેન્સર સામે મજબૂત સુરક્ષા આપે છે, છતાં પુખ્ત વયે નિયમિત તપાસ કરાવવી જરૂરી છે.
```


### Finding DEC-17: Snakebite First Aid & Poisoning Management
- **Content Hash:** `1b4fee7365be`
- **Clinical Status:** **`PROPOSED_REVISION`**
- **Affected Calendar Dates (6 dates):** 02-01, 03-05, 04-09, 05-13, 06-17, 11-02
- **Primary Sourced Authority:** National Action Plan for Prevention and Control of Snakebite Envenoming (NAP-SE), MoHFW, Government of India (2024); WHO Guidelines for the Clinical Management of Snakebites in the South-East Asia Region.
- **Affected Card:** Card 4
- **Clinical Critique:** ABSOLUTE SURVIVAL GUARANTEE: Card 4 Gujarati text states 'સમયસર હોસ્પિટલ પહોંચવાથી દર્દીનો જીવ ૧૦૦% બચે છે' ('reaching hospital on time 100% saves the patient's life'). While prompt antivenom and supportive care (mechanical ventilation, dialysis) reduce mortality drastically, envenoming may still lead to fatality due to severe neurotoxicity, acute tubular necrosis, or venom-induced consumptive coagulopathy. Clinical communication must avoid 100% guarantees.

**Proposed Corrected Bilingual Copy (Registered under `DEC-17`):**

```markdown
English Proposed Correction:
Over 70% of snakes are non-venomous; never waste critical minutes on faith healers. Reaching a capable hospital promptly for anti-snake venom is life-saving.

Gujarati Proposed Correction:
સાપ કરડવા પર ઝાડ-ફૂંક કે પથ્થર ઘસવામાં એક મિનિટ પણ ન બગાડો; સમયસર સક્ષમ હોસ્પિટલ પહોંચી એન્ટિ-સ્નેક વેનમ લેવાથી દર્દીનો જીવ બચાવી શકાય છે.
```


### Finding DEC-18: Child Health Screening & Early Intervention (RBSK)
- **Content Hash:** `727476e5a39f`
- **Clinical Status:** **`PROPOSED_REVISION`**
- **Affected Calendar Dates (4 dates):** 03-19, 05-27, 09-08, 12-20
- **Primary Sourced Authority:** Operational Guidelines on Rashtriya Bal Swasthya Karyakram (RBSK), MoHFW; DEIC Operational Manual.
- **Affected Card:** Card 4
- **Clinical Critique:** SURGICAL OUTCOME GUARANTEE: Card 4 states 'Conditions like cleft lip, clubfoot, and congenital cataract are 100% surgically correctable for free under government RBSK program'. Surgical outcomes vary based on tissue anatomy, associated syndromes, and post-operative therapy. Promising '100% surgical correction' contradicts national public health guidelines.

**Proposed Corrected Bilingual Copy (Registered under `DEC-18`):**

```markdown
English Proposed Correction:
Conditions like cleft lip, clubfoot, and congenital cataract can be effectively treated with government-supported corrective surgeries and therapy under RBSK.

Gujarati Proposed Correction:
હોઠ ફાટેલો હોય, પગનો પંજો વળેલો હોય કે જન્મજાત મોતિયો હોય તો અંધશ્રદ્ધામાં ન પડો; સરકારી RBSK યોજના હેઠળ નિષ્ણાત સર્જરી અને થેરાપી દ્વારા સુધારાત્મક સારવાર ઉપલબ્ધ છે.
```


### Finding DEC-19: Diabetes Management & Glycemic Balance
- **Content Hash:** `218d778d421c`
- **Clinical Status:** **`PROPOSED_REVISION`**
- **Affected Calendar Dates (8 dates):** 01-19, 02-23, 03-27, 06-04, 08-12, 09-16, 11-24, 12-28
- **Primary Sourced Authority:** ICMR Guidelines for Management of Type 2 Diabetes; Research Society for the Study of Diabetes in India (RSSDI) Clinical Practice Recommendations.
- **Affected Card:** Card 1
- **Clinical Critique:** RIGID TARGET QUALIFICATION: Card 1 specifies an absolute target 'Maintain HbA1c under 7%'. While standard for non-pregnant adults without severe comorbidities, clinical guidelines require individualizing HbA1c targets (e.g. 7.5%–8.0% for elderly patients, long-standing diabetes, or those with cardiovascular disease or hypoglycemia unawareness).

**Proposed Corrected Bilingual Copy (Registered under `DEC-19`):**

```markdown
English Proposed Correction:
Monitor fasting blood sugar and quarterly HbA1c; work with your doctor toward your individualized target (typically under 7% for most adults) to prevent microvascular damage.

Gujarati Proposed Correction:
દર ૩ મહિને સુગર અને HbA1c તપાસ કરાવો; ડૉક્ટરે નક્કી કરેલા વ્યક્તિગત લક્ષ્ય (સામાન્ય રીતે ૭% ની અંદર) મુજબ સુગર નિયંત્રણમાં રાખી કિડની, નસો અને આંખો સુરક્ષિત રાખો.
```


### Finding DEC-13: Palliative Care & Chronic Pain Relief (EPMNS)
- **Content Hash:** `9a65761e7076`
- **Clinical Status:** **`PENDING_DECISION_GAP`**
- **Affected Calendar Dates (3 dates):** 03-01, 04-05, 08-21
- **Primary Sourced Authority:** National Programme for Palliative Care (NPPC) Operational Guidelines, MoHFW; WHO Guidelines for the Pharmacological and Radiotherapeutic Management of Cancer Pain.
- **Affected Card:** Calendar Distribution
- **Clinical Critique:** SCHEDULAR GAP: Card copy is clinically sound (promotes holistic pain relief, oral morphine access, home nursing, and removes 'giving up hope' misconceptions). However, retaining only 3 occurrences (03-01, 04-05, 08-21) creates a 6-month multi-quarter gap from late August to March 2027.

**Proposed Corrected Bilingual Copy (Registered under `DEC-13`):**

```markdown
English Proposed Correction:
Preserve clinically sound baseline cards; evaluate swapping one repetitive Q4 hypertension or diabetes slot (e.g. in November) to Palliative Care.

Gujarati Proposed Correction:
હાલનું લખાણ યોગ્ય છે; કેલેન્ડરમાં ઓગસ્ટથી માર્ચ વચ્ચેના ૬ મહિનાના અંતરાલને ઘટાડવા ચોથા ક્વાર્ટરમાં એક સ્લોટ ફાળવવાનો નિર્ણય પેન્ડિંગ છે.
```


---

## 3. Comprehensive Topic-by-Topic Card-Level Audit (All 34 Sets)

Detailed card-level assessment of all 34 topic sets across 207 calendar days:


### Set 1. Hypertension Screening & Blood Pressure Control
- **Content Hash:** `e59865343a6e`
- **Clinical Assessment:** **`PROPOSED_REVISION`**
- **Occurrence Count in 2026:** 9 dates
- **Affected Dates:** 01-18, 02-22, 03-26, 04-30, 06-03, 07-07, 08-11, 11-23, 12-27
- **Primary Sourced Authority:** WHO Guideline on Sodium Intake for Adults and Children (2020); MoHFW NP-NCD Operational Guidelines; ICMR Guidelines for Management of Hypertension.
- **Clinical Audit Notes:** HIGH-SEVERITY NUMERICAL/CHEMICAL ERROR: Card 3 incorrectly states 'Restrict total daily sodium intake to less than 1 level teaspoon (5g)'. Chemically, 5 g of table salt (NaCl) provides approximately 2 g (2000 mg) of elemental sodium. Confusing salt with sodium suggests 5 g of sodium is permissible, which represents 12.5 g of salt (more than double the safe physiological ceiling).

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Check Blood Pressure Monthly Above Age 30**<br>Visit Ayushman Arogya Mandir monthly for digital BP measurement; hypertension is a silent killer showing zero symptoms until crisis. | **૩૦ વર્ષ પછી નિયમિત બીપી ચેક કરાવો**<br>કોઈ તકલીફ ન હોય તો પણ ૩૦ વર્ષની ઉંમર પછી દર મહિને આરોગ્ય કેન્દ્ર પર બીપી મપાવો; સાયલન્ટ કિલર બીપીથી સાવધાન રહો. | Verified sound; safe preventive advice. |
| **Card 2** | **Engage in 45 Minutes Daily Brisk Walking**<br>Moderate aerobic activity like brisk walking or cycling improves arterial elasticity and naturally reduces systolic BP by 5-8 mmHg. | **દરરોજ ૪૫ મિનિટ ઝડપી ચાલો**<br>રોજ સવારે ખુલ્લી હવામાં ૪૫ મિનિટ ઝડપી ચાલવાની ટેવ પાડો; તેનાથી નળીઓ સ્વસ્થ રહે છે અને બીપી કાબૂમાં રહે છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Sprinkle Extra Raw Salt on Cooked Food**<br>Restrict total daily sodium intake to less than 1 level teaspoon (5g). Avoid pickles, papads, salted farsan, and packaged namkeen. | **જમતી વખતે ઉપરથી કાચું મીઠું ન ભભરાવવું**<br>જમવામાં ઉપરથી મીઠું નાખવાની ટેવ સદંતર બંધ કરો; અથાણાં, પાપડ અને ખારી વસ્તુઓ નળીઓમાં દબાણ વધારી હૃદય પર ભાર વધારે છે. | **CONCERN (DEC-14):** Conflates 5g salt with 5g sodium. Correction proposed. |
| **Card 4** | **Never Discontinue Prescribed BP Medication**<br>Hypertension requires continuous lifelong therapy. Stopping medicines abruptly causes rebound malignant hypertension and strokes. | **બીપી નોર્મલ આવે તો દવા બંધ ન કરવી**<br>બીપી કાબૂમાં આવી જાય તેનો અર્થ દવા કામ કરી રહી છે; ડોક્ટરની સલાહ વગર ક્યારેય દવા બંધ ન કરો જેથી લકવો ન થાય. | Verified sound; safe preventive advice. |

### Set 2. Chronic Respiratory Health (COPD & Asthma)
- **Content Hash:** `ac54dd49cd74`
- **Clinical Assessment:** **`PROPOSED_REVISION`**
- **Occurrence Count in 2026:** 9 dates
- **Affected Dates:** 01-23, 02-27, 03-31, 05-04, 06-08, 07-12, 08-16, 09-20, 11-28
- **Primary Sourced Authority:** Global Initiative for Chronic Obstructive Lung Disease (GOLD 2024); Global Initiative for Asthma (GINA 2023); National College of Chest Physicians (NCCP) India Consensus Guidelines.
- **Clinical Audit Notes:** DEVICE SPECIFICITY ERROR & ABSOLUTE SAFETY CLAIM: (1) Card 1 gives universal spacer advice ('Use Prescribed Inhalers with Spacer Daily'). Spacers/valved holding chambers are specifically indicated for pressurized Metered Dose Inhalers (pMDIs); Dry Powder Inhalers (DPIs like Rotahalers, Accuhalers, Turbuhalers) and Breath-Actuated Inhalers must never be attached to spacers. (2) Card 4 Gujarati text claims inhalers improve breathing 'without side effects' ('આડઅસર વગર'). Inhaled corticosteroids and bronchodilators carry recognized adverse effects (oral candidiasis, dysphonia, reflex coughing, tachycardia). Rinsing mouth/gargling after ICS is clinically mandatory; claiming zero side effects undermines patient vigilance.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Use Prescribed Inhalers with Spacer Daily**<br>Inhaled bronchodilators deliver micro-grams directly to airways with minimal bodily side effects. Use a transparent spacer for maximum lung reach. | **ઇનહેલર સ્પેસર સાથે નિયમિત વાપરો**<br>ડોક્ટરે આપેલું ઇનહેલર સ્પેસર સાધન સાથે દરરોજ નિયમિત લો; તેનાથી દવા સીધી શ્વાસનળીમાં જઈ ફેફસાં ખુલ્લા રાખે છે. | **CONCERN (DEC-15):** Universal spacer instruction. Device-specific guidance proposed. |
| **Card 2** | **Shift to Clean LPG Gas & Ensure Kitchen Ventilation**<br>Replace wood and dung chulhas with clean LPG stoves; keep kitchen windows open to eliminate chronic biomass smoke lung destruction. | **ચૂલાના ધુમાડાથી બચી એલપીજી ગેસ વાપરો**<br>લાકડાંના ચૂલાનો ધુમાડો ફેફસાંને બગાડે છે; રસોડામાં બારી ખુલ્લી રાખો અને ઉજ્જવલા યોજનાનો ગેસ ચૂલો વાપરો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Smoke Bidis, Cigarettes or Inhale Chillum Smoke**<br>Smoking destroys delicate lung alveoli, causing irreversible COPD and chronic breathlessness. Quitting halts rapid lung decline. | **બીડી, સિગારેટ કે હુક્કો સદંતર બંધ કરો**<br>બીડી-સિગારેટનો ધુમાડો શ્વાસનળીઓ કાયમ માટે સંકોચી નાખે છે; તમાકુ મુક્ત બનો જેથી ઉંમર વધતા ઓક્સિજન સિલિન્ડરનો સહારો ન લેવો પડે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Fear Inhaler Dependence or Addiction**<br>Inhalers are safe, targeted medical delivery systems; they are not addictive drugs. Delaying inhalers causes permanent airway remodeling. | **ઇનહેલરની ટેવ પડી જાય તેવો ડર ન રાખવો**<br>ઇનહેલરની આદત પડી જાય તેવી ખોટી માન્યતામાં ન પડો; ગોળીઓ કરતાં ઇનહેલર વધુ સુરક્ષિત છે અને આડઅસર વગર શ્વાસ સુધારે છે. | **CONCERN (DEC-15):** Gujarati claims 'zero side effects'. Correction proposed. |

### Set 3. Breast & Cervical Cancer Early Screening
- **Content Hash:** `dc1f8cd74427`
- **Clinical Assessment:** **`PROPOSED_REVISION`**
- **Occurrence Count in 2026:** 9 dates
- **Affected Dates:** 02-25, 03-29, 05-02, 06-06, 07-10, 08-14, 09-18, 11-26, 12-30
- **Primary Sourced Authority:** Operational Framework for Comprehensive Primary Health Care: Screening of Common NCDs, MoHFW; WHO Cervical Cancer Screening Guidelines.
- **Clinical Audit Notes:** ABSOLUTE GUARANTEE CLAIM & TRANSLATION MISMATCH: (1) Card 2 Gujarati copy claims cervical cancer detected early is '100% curable' ('પ્રારંભિક તબક્કે કેન્સર ૧૦૦% સાજું થાય છે'). Absolute 100% cure guarantees are medically untenable in oncology; early detection enables highly successful treatment and dramatically improves survival, but cannot guarantee 100% cure. (2) Card 4 Gujarati copy claims HPV vaccination provides 'lifelong protection' ('આજીવન રક્ષણ'), whereas the English accurately notes it prevents up to 90% of cervical cancers. Suggesting lifelong total immunity may cause women to erroneously skip recommended adult screening.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Conduct Monthly Breast Self-Examination (BSE)**<br>Every woman above 20 should inspect and palpate breasts monthly after menstruation for painless lumps, dimpling, or nipple discharge. | **માસિક પછી સ્તનની જાતે તપાસ કરો**<br>દર મહિને સ્તનમાં કોઈ નવી ગાંઠ, ચામડી ખેંચાતી હોય કે સ્તનની ડીંટડીમાંથી પ્રવાહી નીકળતું હોય તો જાતે તપાસી તુરંત ડોક્ટરને બતાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Undergo Visual Inspection with Acetic Acid (VIA)**<br>Women aged 30-65 should undergo free VIA screening every 5 years at Ayushman Arogya Mandir to detect cervical pre-cancer early. | **આરોગ્ય કેન્દ્ર પર ગર્ભાશય મુખની તપાસ કરાવો**<br>૩૦ વર્ષથી વધુ ઉંમરની બહેનો આરોગ્ય કેન્દ્ર પર ગર્ભાશયના મુખની સરળ તપાસ (VIA) કરાવો; પ્રારંભિક તબક્કે કેન્સર ૧૦૦% સાજું થાય છે. | **CONCERN (DEC-16):** Gujarati claims 100% cancer cure. Nuanced wording proposed. |
| **Card 3** | **Never Conceal Intimate Symptoms Due to Shyness**<br>Abnormal vaginal bleeding between periods, post-menopausal spotting, or persistent foul discharge require immediate evaluation. | **ખચકાટ રાખી લક્ષણો છુપાવવા નહીં**<br>માસિક બંધ થયા પછી અચાનક રક્તસ્ત્રાવ થાય કે દુર્ગંધયુક્ત પાણી પડે તો શરમ રાખ્યા વગર મહિલા ડોક્ટરની સલાહ લો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Delay HPV Vaccination for Adolescent Girls**<br>Vaccinating adolescent girls aged 9-14 with Human Papillomavirus (HPV) vaccine prevents up to 90% of cervical cancers in adulthood. | **કિશોરીઓને HPV રસી અપાવવામાં વિલંબ ન કરવો**<br>૯ થી ૧૪ વર્ષની દીકરીઓને એચપીવી રસી અપાવો; આ રસી મોટા થયા પછી ગર્ભાશયના મુખના કેન્સર સામે આજીવન રક્ષણ આપે છે. | **CONCERN (DEC-16):** Gujarati claims lifelong protection from HPV vaccine. Correction proposed. |

### Set 4. Childhood Diarrhea & Pneumonia Control (IDCF / SAANS)
- **Content Hash:** `f4bd17c31c47`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 8 dates
- **Affected Dates:** 01-09, 02-13, 03-17, 04-21, 06-29, 08-02, 09-06, 12-18
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Prepare WHO-ORS & Give 14 Days Zinc**<br>Dissolve 1 WHO-ORS packet in 1L clean water. Give frequent sips during diarrhea plus dispersible zinc tablets daily for 14 full days. | **ઓ.આર.એસ. અને ૧૪ દિવસ ઝિંક આપો**<br>૧ લીટર સ્વચ્છ પાણીમાં આખું ઓઆરએસ ઓગાળો; ઝાડા બંધ થાય તો પણ ૧૪ દિવસ પૂરા ઝિંકની ગોળી આપો જેથી આંતરડાં મજબૂત થાય. | Verified sound; safe preventive advice. |
| **Card 2** | **Spot Fast Breathing & Chest Indrawing**<br>Count breaths for 1 minute: >50/min (2-11m) or >40/min (1-5y) or lower chest indrawing signals pneumonia; seek urgent medical clinic. | **ઝડપી શ્વાસ અને પાંસળી ખેંચાવી ઓળખો**<br>બાળકની પાંસળી અંદર ખાડા પડતી હોય કે શ્વાસ ઝડપથી ચાલતો હોય તો ન્યુમોનિયા હોઈ શકે છે; તાત્કાલિક પ્રાથમિક આરોગ્ય કેન્દ્ર જાઓ. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Withhold Fluids During Diarrhea**<br>Never stop breastfeeding or fluids during loose motions; withholding fluids causes rapid life-threatening dehydration and shock. | **માંદગીમાં ધાવણ કે પ્રવાહી બંધ ન કરવું**<br>ઝાડામાં બાળકનું ધાવણ કે પાણી ક્યારેય રોકવું નહીં; પ્રવાહી બંધ કરવાથી શરીરમાં પાણી ખૂટી જઈ જીવનું જોખમ થાય છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Give Adult Cough Syrups to Infants**<br>Over-the-counter adult cold syrups cause respiratory depression in children. Always get respiratory infections evaluated by doctor. | **બાળકોને જાતે કફ સિરપ ન આપવી**<br>બાળકને મેડિકલ સ્ટોરમાંથી જાતે કફ સિરપ લાવીને ન પીવડાવો; ફેફસાંના ચેપ માટે ડોક્ટર પાસે સાચી સારવાર કરાવો. | Verified sound; safe preventive advice. |

### Set 5. Leprosy Eradication & Disability Prevention (NLEP)
- **Content Hash:** `f09439622914`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 8 dates
- **Affected Dates:** 01-16, 02-20, 04-28, 06-01, 07-05, 08-09, 11-21, 12-25
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Inspect Skin for Numb Hypopigmented Patches**<br>Check for pale or reddish skin patches with complete loss of sensation to light touch, heat, or cold. Report early for free tests. | **સંવેદના વગરના આછા ડાઘ તપાસાવો**<br>ચામડી પર આછો કે લાલાશ પડતો ડાઘ હોય અને ત્યાં અડવાથી ખબર ન પડે તો તે રક્તપિત્ત હોઈ શકે છે; તુરંત તપાસ કરાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Complete Full Multi-Drug Therapy (MDT) Course**<br>Free blister-pack MDT cures leprosy in 6 to 12 months. The disease becomes completely non-infectious after the very first dose. | **સરકારી હોસ્પિટલમાંથી મફત MDT કોર્સ કરો**<br>સરકારી આરોગ્ય કેન્દ્ર પરથી મફત મળતી એમડીટી (MDT) દવા પૂરા સમય માટે લો; પ્રથમ ડોઝથી જ રોગ બીજામાં ફેલાતો અટકે છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Stigmatize or Isolate Leprosy Patients**<br>Leprosy is not a hereditary curse or punishment; it is caused by simple bacteria (Mycobacterium leprae) and is 100% curable. | **રક્તપિત્તના દર્દી સાથે ભેદભાવ ન કરવો**<br>રક્તપિત્ત કોઈ પાપ કે અસ્પૃશ્ય રોગ નથી; દર્દી સાથે સામાન્ય વ્યવહાર રાખો, ભેદભાવ ન કરો અને પરિવારમાં સન્માન આપો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Neglect Numb Hands & Feet to Prevent Deformity**<br>Wear soft micro-cellular rubber (MCR) footwear; protect numb hands from hot cooking utensils to avoid burns and irreversible disability. | **અનુભૂતિ વગરના હાથ-પગની ઉપેક્ષા ન કરવી**<br>હાથ-પગમાં અહેસાસ ન થતો હોય તો રસોઈમાં ગરમ વાસણ સીધા ન પકડવા અને બહાર નીકળતી વખતે એમસીઆર ચંપલ અવશ્ય પહેરવા. | Verified sound; safe preventive advice. |

### Set 6. Diabetes Management & Glycemic Balance
- **Content Hash:** `218d778d421c`
- **Clinical Assessment:** **`PROPOSED_REVISION`**
- **Occurrence Count in 2026:** 8 dates
- **Affected Dates:** 01-19, 02-23, 03-27, 06-04, 08-12, 09-16, 11-24, 12-28
- **Primary Sourced Authority:** ICMR Guidelines for Management of Type 2 Diabetes; Research Society for the Study of Diabetes in India (RSSDI) Clinical Practice Recommendations.
- **Clinical Audit Notes:** RIGID TARGET QUALIFICATION: Card 1 specifies an absolute target 'Maintain HbA1c under 7%'. While standard for non-pregnant adults without severe comorbidities, clinical guidelines require individualizing HbA1c targets (e.g. 7.5%–8.0% for elderly patients, long-standing diabetes, or those with cardiovascular disease or hypoglycemia unawareness).

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Monitor Fasting Blood Sugar & Quarterly HbA1c**<br>Maintain HbA1c under 7% to prevent irreversible microvascular damage to eyes (retinopathy), kidneys (nephropathy), and nerves. | **દર ૩ મહિને સુગર અને HbA1c તપાસો**<br>માત્ર ખાલી પેટની સુગર નહીં, દર ૩ મહિને HbA1c ટેસ્ટ કરાવી સુગર ૭% થી નીચે રાખો જેથી કિડની અને આંખો સુરક્ષિત રહે. | **CONCERN (DEC-19):** Rigid HbA1c <7% target. Individualized physician advice proposed. |
| **Card 2** | **Inspect Feet Daily with a Mirror for Cuts**<br>Diabetic neuropathy impairs pain sensation. Wash feet in lukewarm water, dry between toes, and check soles daily for painless wounds. | **અરીસામાં પગના તળિયા રોજ તપાસો**<br>ડાયાબિટીસમાં પગની નસો નબળી પડતી હોવાથી ઈજાનો અહેસાસ થતો નથી; રોજ પગના તળિયા અરીસામાં જોઈ ક્યાંય ચાંદું નથી તે તપાસો. | Verified sound; safe preventive advice. |
| **Card 3** | **Eliminate Sugar, Jaggery, Sweets & Fruit Juices**<br>Jaggery and honey cause blood sugar spikes identical to white sugar. Replace them with fiber-rich salads, sprouted pulses, and millets. | **ખાંડ, ગોળ અને પેક્ડ જ્યુસ બંધ કરો**<br>ગોળ અને મધ પણ ખાંડ જેટલી જ સુગર વધારે છે; મીઠાઈઓ અને જ્યુસ બંધ કરી ફણગાવેલા મગ, કાકડી અને મેથીના દાણા લો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Walk Barefoot Even Indoors**<br>Never walk barefoot on hot floors, stones, or temple grounds; minor unnoticed blisters turn rapidly into gangrenous diabetic ulcers. | **ઘરમાં કે બહાર ખુલ્લા પગે ન ચાલવું**<br>ઘરમાં કે બહાર ક્યારેય ઉઘાડા પગે ન ફરો; સોફ્ટ ચંપલ પહેરો જેથી કાંટો કે પથ્થર વાગવાથી થતું ગંભીર ઇન્ફેક્શન અટકે. | Verified sound; safe preventive advice. |

### Set 7. Road Trauma First Aid & 108 Golden Hour Action
- **Content Hash:** `12f3a3426353`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 8 dates
- **Affected Dates:** 02-02, 03-06, 05-14, 06-18, 08-26, 09-30, 11-03, 12-07
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Apply Firm Direct Pressure to Stop Severe Bleeding**<br>Press a clean cloth firmly directly over bleeding wounds for at least 10 continuous minutes. Direct pressure stops 90% of lethal hemorrhage. | **વહેતા લોહી પર સ્વચ્છ કપડાથી દબાણ આપો**<br>અકસ્માતમાં વહેતા લોહી પર સ્વચ્છ કપડું મૂકી હથેળીથી ૧૦ મિનિટ સતત દબાવી રાખો; દબાણ આપવાથી લોહી વહેતું અટકી જાય છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Wear ISI Full-Face Helmet & Click Seatbelts**<br>Fasten chin-strap on two-wheelers and wear 3-point seatbelts in cars. Golden hour hospital care within 60 minutes saves trauma victims. | **ISI હેલ્મેટ અને સીટબેલ્ટ અવશ્ય પહેરો**<br>બાઈક પર ચિન-સ્ટ્રેપ સાથે ISI હેલ્મેટ પહેરો અને કારમાં સીટબેલ્ટ બાંધો; અકસ્માત થાય તો તરત ૧૦૮ બોલાવો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Forcibly Remove Helmet of Crash Victims**<br>Roughly jerking a helmet off an injured rider fractures damaged cervical vertebrae, instantly causing permanent quadriplegia or death. | **અકસ્માત પછી હેલ્મેટ ઝટકાથી ન ખેંચવું**<br>પટકાયેલા વ્યક્તિનું હેલ્મેટ જોરથી ન ખેંચો; ડોક હલવાથી કરોડરજ્જુ તૂટી કાયમી લકવો થઈ શકે છે. ૧૦૮ ટીમને આવવા દો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Transport Trauma Victims Without Spine Support**<br>Do not bundle trauma victims into autos with bent spines. Keep head, neck, and torso aligned in a straight line on a firm stretcher. | **દર્દીને વાંકાચૂંકા ઊંચકીને રિક્ષામાં ન લઈ જવા**<br>અકસ્માતના દર્દીને વાંકા વળીને ઊંચકવા નહીં; ગરદન અને પીઠ સીધી રહે તે રીતે પાટિયા કે ૧૦૮ ના સ્ટ્રેચર પર જ લઈ જાઓ. | Verified sound; safe preventive advice. |

### Set 8. Tuberculosis Elimination & Nikshay Care (NTEP)
- **Content Hash:** `dad2af33baf1`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 8 dates
- **Affected Dates:** 02-18, 03-22, 04-26, 05-30, 07-03, 08-07, 09-11, 12-23
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Screen Persistent Cough >2 Weeks with CBNAAT**<br>Test cough lasting over 2 weeks with free rapid molecular tests (CBNAAT / Truenat) at government centers for early detection. | **ગળફાની મોલેક્યુલર (CBNAAT) તપાસ કરાવો**<br>બે અઠવાડિયાથી વધુ ઉધરસ, સાંજે તાવ કે વજન ઘટતું હોય તો સરકારી હોસ્પિટલમાં ગળફાની સીબીનાટ તપાસ મફત કરાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Avail Nikshay Poshan Direct DBT Support**<br>Every registered TB patient receives direct monthly DBT bank transfers to afford protein-rich nutrition like eggs, pulses, and milk. | **નિક્ષય પોષણ સહાયના નાણાં મેળવો**<br>નિક્ષય પોર્ટલ પર નોંધણી કરાવી પૌષ્ટિક આહાર માટે દર મહિને સરકાર તરફથી સીધા બેંક ખાતામાં પોષણ સહાય મેળવો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Stop TB Medicines Midway When Feeling Better**<br>Stopping DOTS treatment midway after symptoms improve causes lethal multi-drug resistant TB (MDR-TB). Complete all 6 months. | **સારું લાગે તો પણ ટીબીની દવા બંધ ન કરવી**<br>બે મહિનામાં સારું લાગવા માંડે તો પણ દવા અધૂરી ન છોડશો; અધૂરી દવાથી દવા-પ્રતિરોધી (MDR) ટીબી થાય છે જે જીવલેણ છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Spit Openly or Cough Without Covering Mouth**<br>Always cover mouth with a handkerchief while coughing; open spitting spreads live tubercle bacilli into ambient community air. | **ખુલ્લામાં થૂંકવું નહીં, મોં ઢાંકો**<br>ઉધરસ ખાતી વખતે મોં આડે રૂમાલ રાખો અને ગમે ત્યાં ન થૂંકો; તમારા થૂંકવાથી ઘરમાં નાના બાળકો અને વડીલોને ચેપ લાગે છે. | Verified sound; safe preventive advice. |

### Set 9. Rational Drug Use & Antibiotic Stewardship
- **Content Hash:** `3eabb245bc0a`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 7 dates
- **Affected Dates:** 01-03, 03-11, 06-23, 07-27, 08-31, 10-04, 11-08
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Take Antibiotics Only with Qualified Medical Prescription**<br>Antibiotics are precious life-saving drugs that treat bacterial infections only. Take them strictly under registered medical advice. | **એન્ટિબાયોટિક્સ ફક્ત ડોક્ટરની સલાહથી જ લો**<br>એન્ટિબાયોટિક દવાઓ માત્ર લાયકાત ધરાવતા ડોક્ટર લખે ત્યારે જ લો; સાચી બીમારીમાં સાચી દવાથી જ રોગ નાશ પામે છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Always Complete the Entire 5-to-7-Day Antibiotic Course**<br>Stopping antibiotics early because fever subsided allows surviving mutated bacteria to become incurable drug-resistant superbugs. | **સારું લાગે તો પણ એન્ટિબાયોટિકનો પૂરો કોર્સ કરો**<br>બે દિવસમાં તાવ ઊતરી જાય તો પણ ડોક્ટરે લખેલા ૫ કે ૭ દિવસનો પૂરો કોર્સ કરો; અધૂરી દવાથી બચેલા જીવાણુ વધુ ઘાતક બને છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Demand Antibiotics for Common Viral Cold & Cough**<br>Antibiotics do not kill common cold, influenza, or viral dengue viruses. Demanding antibiotics for viral illness produces zero cure. | **સામાન્ય શરદી-ખાંસીમાં એન્ટિબાયોટિક્સ ન માગો**<br>સામાન્ય શરદી, ઉધરસ કે વાયરલ તાવમાં એન્ટિબાયોટિક્સ કોઈ કામ કરતી નથી; ગરમ પાણી, આરામ અને પેરાસિટામોલ જ પૂરતા છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Share Leftover Antibiotics with Family Members**<br>Every infection requires a specific drug class, precise dosing, and duration. Sharing leftover pills causes toxic kidney/liver harm. | **પોતાની જૂની દવાઓ પરિવારમાં બીજાને ન આપવી**<br>ઘરમાં પડેલી જૂની દવાઓ પરિવારના અન્ય સભ્યોને ન આપો; ખોટી દવા લેવાથી એલર્જી અને કિડનીને ગંભીર નુકસાન થઈ શકે છે. | Verified sound; safe preventive advice. |

### Set 10. Universal Immunization Programme (UIP)
- **Content Hash:** `0e1a53cac6f1`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 7 dates
- **Affected Dates:** 01-10, 02-14, 03-18, 05-26, 06-30, 10-11, 12-19
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Complete All Scheduled Vaccines on Mamta Diwas**<br>Ensure on-time administration of BCG, Hep-B, Pentavalent, Rotavirus, fIPV, PCV, and MR vaccines at nearest Anganwadi session. | **મમતા દિવસે સમયસર રસી મુકાવો**<br>દર બુધવારે યોજાતા મમતા દિવસે બાળકને પોલિયો, પેન્ટા, રોટા, પીસીવી અને ઓરી-રૂબેલાની રસી સમયસર અપાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Preserve Mamta Immunization Card Safely**<br>Keep the Mamta card safe in a protective pouch. Bring it to every health visit to record doses and note the next upcoming due date. | **મમતા કાર્ડ સાચવીને સાથે રાખો**<br>મમતા કાર્ડ પ્લાસ્ટિક કવરમાં સાચવીને રાખો અને દરેક મુલાકાતે સાથે લાવો જેથી આગામી રસીની તારીખ યાદ રહે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Skip Vaccine Due to Mild Cold or Fever**<br>Mild cough, runny nose, or minor fever is not a contraindication for vaccines. Postponing leaves your baby vulnerable to fatal diseases. | **સામાન્ય તાવમાં રસી મુલતવી ન રાખવી**<br>સામાન્ય શરદી કે હળવા તાવમાં રસી આપવાનું ટાળશો નહીં; રસી મુલતવી રાખવાથી બાળક જોખમી રોગો સામે અસુરક્ષિત રહે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Leave Missed Booster Doses Incomplete**<br>If any scheduled dose is delayed, do not restart from zero; visit your ANM to resume and complete all remaining booster shots promptly. | **છૂટેલા બુસ્ટર ડોઝમાં વિલંબ ન કરવો**<br>કોઈ કારણસર રસી છૂટી ગઈ હોય તો ચિંતા વગર એએનએમનો સંપર્ક કરો અને બાકીના ડોઝ વહેલી તકે પૂરા કરાવો. | Verified sound; safe preventive advice. |

### Set 11. Vector-Borne Disease Prevention (Malaria & Dengue)
- **Content Hash:** `fef08d617c27`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 7 dates
- **Affected Dates:** 01-15, 02-19, 03-23, 04-27, 07-04, 08-08, 11-20
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Observe Weekly Sunday Dry Day at Home**<br>Scrub, empty, and dry all water containers, air coolers, flower pots, and drums every Sunday to destroy Aedes mosquito larvae. | **દર રવિવારે કૂલર-કૂંડાં સૂકવી સાફ કરો**<br>દર રવિવારે પાણીની ટાંકી, કૂલર, ફ્રિજની ટ્રે અને કૂંડાં સાફ કરી સૂકવી નાખો; તેનાથી ડેન્ગ્યુના મચ્છર પેદા થતા અટકે છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Get Blood Tested for Every Fever Case Within 24h**<br>Visit health sub-centre for rapid diagnostic tests (RDT) and blood smear examination for timely species-specific malaria therapy. | **તાવ આવે ત્યારે લોહીની તપાસ કરાવો**<br>તાવ આવે ત્યારે ઘેર બેઠા રહેવાને બદલે ૨૪ કલાકમાં આરોગ્ય કાર્યકર પાસે લોહીની તપાસ કરાવો અને મેલેરિયાની સાચી દવા લો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Leave Stagnant Water Around Roofs & Tires**<br>Discard discarded tires, coconut shells, and plastic cups outdoors; clear terrace roof drains to prevent mosquito breeding grounds. | **ધાબા પર ભંગાર કે ભરાયેલું પાણી ન રાખો**<br>ધાબા પર કે ઘરની આસપાસ જૂના ટાયર, નાળિયેરના કોચલા કે તૂટેલા ડબ્બા ન રાખો; તેમાં ભરાયેલા વરસાદી પાણીમાં મચ્છર ઈંડા મૂકે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Take Painkillers Like Brufen/Aspirin in Fever**<br>In viral fevers and dengue, never self-medicate with Brufen, Combiflam, or Aspirin; they cause fatal internal gastrointestinal bleeding. | **ડેન્ગ્યુ તાવમાં બ્રુફેન કે એસ્પિરિન ન લેવી**<br>ડેન્ગ્યુ કે વાયરલ તાવમાં માત્ર પેરાસિટામોલ જ લો; દુખાવાની ગોળીઓ લેવાથી પ્લેટલેટ્સ ઘટવા સાથે આંતરિક રક્તસ્ત્રાવ થઈ શકે છે. | Verified sound; safe preventive advice. |

### Set 12. Viral Hepatitis & Waterborne Disease Prevention
- **Content Hash:** `b712699825ba`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 7 dates
- **Affected Dates:** 01-17, 02-21, 03-25, 06-02, 07-06, 11-22, 12-26
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Boil Drinking Water & Maintain Food Hygiene**<br>Boil water rolling for 1 minute or use chlorine tablets. Wash raw salads thoroughly to eliminate fecal-oral Hepatitis A & E viruses. | **પાણી ઉકાળીને પીવો અને સ્વચ્છતા રાખો**<br>પીવાનું પાણી ઉકાળીને કે ક્લોરીનેશન કરીને જ વાપરો અને જમતા પહેલાં હાથ ધોવો; તેનાથી ઝેરી કમળો અને ઝાડા-ઊલટી અટકે છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Screen for Hepatitis B & C at District Centers**<br>Blood screening under National Viral Hepatitis Control Program (NVHCP) is free. Hepatitis C is completely curable with oral antivirals. | **હિપેટાઇટિસ બી અને સી ની લોહી તપાસ કરાવો**<br>સરકારી હોસ્પિટલમાં હિપેટાઇટિસ બી અને સી ની મફત તપાસ કરાવો; હિપેટાઇટિસ સી દવાઓથી માત્ર ૩ મહિનામાં સાજો થઈ શકે છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Drink Street-Side Unhygienic Crushed Ice Drinks**<br>Roadside crushed ice is frequently manufactured with unpotable industrial water, directly transmitting deadly enterically-borne viral hepatitis. | **ખુલ્લામાં વેચાતા બરફ કે જ્યુસ ન પીવા**<br>બહાર ખુલ્લામાં વેચાતા બરફવાળા શરબત કે ગોળા ન ખાવા; અસ્વચ્છ બરફ કમળા અને ટાઇફોઇડનું સૌથી મોટું વાહક છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Rely on Superstition for Jaundice**<br>Never delay medical treatment for jaundice with quack mantras or harmful starvation diets; acute viral hepatitis needs clinical monitoring. | **કમળામાં ભુવા-ભારડી પાછળ ન દોડવું**<br>કમળામાં ઝાડ-ફૂંક કે ભૂખમરા જેવા અયોગ્ય દેશી ઉપચારો ન કરો; સમયસર ડોક્ટર પાસે લીવરની તપાસ કરાવો જેથી લિવર ફેઈલ ન થાય. | Verified sound; safe preventive advice. |

### Set 13. Oral Cancer Screening & Tobacco Control (NTCP)
- **Content Hash:** `46e27ba7915e`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 7 dates
- **Affected Dates:** 01-20, 02-24, 03-28, 05-01, 07-09, 11-25, 12-29
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Perform Monthly Self-Oral 3-Finger Test**<br>Stand before a mirror; verify you can insert 3 fingers vertically into mouth. Check inner cheeks for red/white patches or stiffness. | **દર મહિને મોંમાં ૩ આંગળી નાખી તપાસો**<br>અરીસા સામે મોં ખોલી ઊભી ૩ આંગળીઓ નાખી જુઓ; જો ૩ આંગળી ન જાય કે તીખું ખાતાં બળતરા થાય તો કેન્સરનું પૂર્વ લક્ષણ હોઈ શકે છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Quit Tobacco with National Helpline 1800-11-2356**<br>Seek evidence-based behavioral therapy and nicotine replacement at District Hospital Tobacco Cessation Centers (TCC). | **તમાકુ છોડવા ટોલ-ફ્રી હેલ્પલાઇન વાપરો**<br>ગુટખા કે બીડી છોડવા સરકારી ટોલ-ફ્રી નંબર ૧૮૦૦-૧૧-૨૩૫૬ પર માર્ગદર્શન મેળવો અને જિલ્લા હોસ્પિટલના ટીસીસી સેન્ટરનો સંપર્ક કરો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Chew Gutkha, Mawa, Khaini or Supari**<br>Areca nut and smokeless tobacco release potent nitrosamines causing Oral Submucous Fibrosis (OSMF) and disfiguring mouth cancer. | **ગુટખા, માવો, સોપારી મોંમાં ન દબાવવા**<br>સોપારી અને તમાકુ મોઢાની અંદરની ચામડી બાળી જડબું કાયમ માટે જકડી દે છે; આ જીવલેણ વ્યસનથી આજે જ મુક્ત થાઓ. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Ignore Mouth Ulcers Lasting >14 Days**<br>A painless mouth ulcer, burning patch, or neck lump persisting over 2 weeks requires urgent biopsy by a dental or ENT specialist. | **૧૪ દિવસથી વધુ ન રુઝાતું ચાંદું ન અવગણવું**<br>મોંમાં પડેલું ચાંદું બે અઠવાડિયામાં ન રુઝાય તો માત્ર મલમ લગાડવામાં સમય ન બગાડો; તાત્કાલિક ડેન્ટલ ડોક્ટર પાસે તપાસ કરાવો. | Verified sound; safe preventive advice. |

### Set 14. Cardiovascular Emergency & FAST Stroke Care
- **Content Hash:** `3b2d0496ae8c`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 7 dates
- **Affected Dates:** 01-22, 02-26, 03-30, 05-03, 08-15, 11-27, 12-31
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Spot FAST Stroke Warning Signs Immediately**<br>Face drooping, Arm weakness, Speech slurring = Time to call 108. Thrombolysis in first 4.5 hours reverses brain paralysis. | **લકવાના લક્ષણો FAST પદ્ધતિથી ઓળખો**<br>મોં વાંકું થાય, એક હાથ નબળો પડે કે બોલવામાં જીભ લથડાય તો સમય બગાડ્યા વગર તુરંત ૧૦૮ બોલાવી સીટી સ્કેન વાળી હોસ્પિટલ પહોંચો. | Verified sound; safe preventive advice. |
| **Card 2** | **Act Within Golden Hour for Acute Chest Heaviness**<br>Crushing chest pressure radiating to jaw, left arm, or back with cold sweats needs immediate ECG and hospital emergency care. | **છાતીમાં ભાર કે પરસેવો થાય તો ૧૦૮ બોલાવો**<br>છાતીમાં ભાર, ગભરામણ, ડાબા હાથમાં દુખાવો કે પરસેવો વળે તો તાત્કાલિક હોસ્પિટલ પહોંચો; પ્રથમ એક કલાક ગોલ્ડન અવર છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Dismiss Chest Heaviness as Acidity**<br>Never waste crucial golden hours drinking sodas or antacids; an atypical heart attack can mimic severe indigestion, especially in diabetics. | **છાતીના દુખાવાને સામાન્ય ગેસ ન ગણવો**<br>છાતીના દુખાવાને ગેસ સમજી સોડા પીવામાં સમય ન બગાડો; ખાસ કરીને ડાયાબિટીસના દર્દીઓમાં હૃદયરોગના હુમલામાં ઓછો દુખાવો પણ હોઈ શકે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Feed Water or Food to Acute Stroke Patients**<br>A stroke paralyzes throat swallowing reflexes. Forcing water or tea into mouth causes lethal aspiration directly into lungs. | **લકવાના દર્દીને પાણી કે ખાવાનું ન આપવું**<br>લકવો પડે ત્યારે દર્દીને ક્યારેય પાણી, ચા કે ગોળી ગળાવશો નહીં; ગળાના સ્નાયુઓ શિથિલ હોવાથી પાણી ફેફસાંમાં જઈ દર્દી ગૂંગળાઈ શકે છે. | Verified sound; safe preventive advice. |

### Set 15. Primary Ear, Nose & Throat Health (OEEE)
- **Content Hash:** `e944e3cc9ddb`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 7 dates
- **Affected Dates:** 05-06, 06-10, 07-14, 08-18, 09-22, 10-26, 11-30
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Pinch Nose & Lean Forward During Epistaxis**<br>Pinch soft lower nostrils firmly for 10 minutes, lean forward, and breathe through mouth. Never tilt head back as blood chokes stomach. | **નસકોરીમાં નાક દબાવી સહેજ આગળ નમો**<br>નાકમાંથી લોહી નીકળે ત્યારે માથું પાછળ ન લેશો; આગળ નમીને નાકનો નરમ ભાગ ૧૦ મિનિટ દબાવી રાખો અને મોં વાટે શ્વાસ લો. | Verified sound; safe preventive advice. |
| **Card 2** | **Keep Ears Dry and Seek Doctor for Ear Discharge**<br>Treat chronic suppurative otitis media early at CHC with antibiotic ear drops. Keep ears protected from water during swimming. | **કાન સૂકા રાખો અને રસી થાય તો તપાસ કરાવો**<br>કાનમાંથી રસી કે પરુ નીકળતું હોય તો ENT ડોક્ટર પાસે તપાસ કરાવો અને નાહતી વખતે કાનમાં પાણી ન જવા દો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Poke Matchsticks, Pins or Buds into Ears**<br>Ears are self-cleaning organs. Inserting foreign objects pushes ear wax deeper and punctures delicate tympanic membranes permanently. | **કાનમાં દિવાસળી, પીન કે બડ્સ ક્યારેય ન નાખવા**<br>કાન ખોતરવા માટે દિવાસળી, હેરપિન કે કાનબડ્સ ન વાપરો; તેનાથી કાનના પડદામાં કાણું પડી કાયમી બહેરાશ આવી શકે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Pour Warm Oil or Garlic Juice into Ears**<br>Pouring mustard oil or concoctions into infected ears causes fungal otitis externa and destroys middle ear hearing bones. | **કાનમાં ગરમ તેલ કે ઘરગથ્થુ રસાયણ ન નાખવા**<br>કાનમાં દુખાવો થાય ત્યારે લસણનું તેલ કે પાંદડાંનો રસ ન નાખો; તેનાથી કાનમાં ફૂગ થાય છે અને ચેપ ગંભીર બને છે. | Verified sound; safe preventive advice. |

### Set 16. Water, Sanitation & Hygiene (WASH / NQAS)
- **Content Hash:** `64e9d58a9810`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 6 dates
- **Affected Dates:** 01-02, 02-06, 05-18, 07-26, 10-03, 12-11
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Practice 6-Step 20-Second Soap Handwashing**<br>Wash palms, back of hands, between fingers, thumbs, knuckles, and wrists with soap under running water before eating and after toilet. | **સાબુથી ૨૦ સેકન્ડ સુધી હાથ ઘસીને ધોવો**<br>જમતા પહેલાં અને શૌચ પછી ઓછામાં ઓછી ૨૦ સેકન્ડ સાબુથી હથેળી, આંગળીઓ અને કાંડાં વ્યવસ્થિત ઘસીને પાણીથી ધોવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Store Drinking Water in Clean Covered Tapped Vessels**<br>Store drinking water in narrow-mouthed vessels fitted with a tap. Keep covered with lid and clean containers thoroughly every week. | **પીવાનું પાણી નળવાળા વાસણમાં ઢાંકીને રાખો**<br>પીવાનું પાણી હંમેશા નળવાળા માટલામાં કે વાસણમાં ઢાંકીને રાખો જેથી હાથ અડવાથી પાણી ગંદુ ન થાય. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Dip Unwashed Hands Directly into Water Pots**<br>Dipping unwashed cups or hands into domestic storage pots spreads gastroenteritis, cholera, and hepatitis A through the entire family. | **પીવાના પાણીના માટલામાં સીધો ગ્લાસ ન બોળવો**<br>માટલામાંથી પાણી લેવા હાથ બોળશો નહીં; લાંબા હાથાવાળો ડોયો વાપરો અથવા નળ વાળા વાસણમાંથી જ પાણી લો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Defecate in Open Fields Near Water Bodies**<br>Open defecation contaminates groundwater and soil with parasitic roundworms and hookworms. Always use clean domestic toilets. | **ખુલ્લામાં શૌચ ન જવું, શૌચાલયનો જ ઉપયોગ કરવો**<br>ખુલ્લામાં શૌચ જવાનું સદંતર બંધ કરો; શૌચાલયનો જ ઉપયોગ કરવાથી કરમિયા, ટાઇફોઇડ અને કમળા જેવા રોગોથી ગામ સુરક્ષિત રહે છે. | Verified sound; safe preventive advice. |

### Set 17. Antenatal Care & Safe Motherhood (ANC)
- **Content Hash:** `0f50263ba2f6`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 6 dates
- **Affected Dates:** 01-04, 04-16, 05-20, 06-24, 10-05, 12-13
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Early ANC Registration in 1st Trimester**<br>Register pregnancy within the first 12 weeks at Ayushman Arogya Mandir for early ultrasound and health tracking. | **ગર્ભાવસ્થાની વહેલી નોંધણી કરાવો**<br>ગર્ભાવસ્થાના પહેલા ૧૨ અઠવાડિયામાં નજીકના આરોગ્ય કેન્દ્રમાં નોંધણી કરાવી મમતા કાર્ડ મેળવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Daily IFA & Calcium Adherence**<br>Take 1 red IFA tablet daily after first trimester with lemon water; take calcium separately with water, never with tea. | **આયર્ન અને કેલ્શિયમ નિયમિત લો**<br>બીજા ત્રિમાસિકથી ૧૮૦ દિવસ સુધી રોજ એક આયર્નની ગોળી અને કેલ્શિયમ નિયમિત લો; ચા સાથે ક્યારેય ન લેવી. | Verified sound; safe preventive advice. |
| **Card 3** | **Skipping Scheduled Tests & Scans**<br>Never skip blood pressure check, urine protein test, blood sugar, or anomaly ultrasound scans on PMSMA day (9th of month). | **તપાસ કે સોનોગ્રાફી ટાળવી નહીં**<br>બીપી, પેશાબની તપાસ, સુગર કે સોનોગ્રાફી છોડશો નહીં; દર મહિનાની ૯મી તારીખે પીએમએસએમએ દિવસે તપાસ કરાવો. | Verified sound; safe preventive advice. |
| **Card 4** | **Ignoring Severe Danger Signs**<br>Swelling of face/hands, severe headache, bleeding, convulsions, or reduced fetal movement require immediate 108 hospital transfer. | **જોખમી લક્ષણોની અવગણના ન કરવી**<br>ચહેરા પર સોજો, તીવ્ર માથાનો દુખાવો, રક્તસ્ત્રાવ કે બાળકની હલચલ ઓછી થાય તો વિલંબ વગર ૧૦૮ બોલાવી હોસ્પિટલ પહોંચો. | Verified sound; safe preventive advice. |

### Set 18. Community Mental Health & Tele-MANAS Support (EPMNS)
- **Content Hash:** `6b8552028be2`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 6 dates
- **Affected Dates:** 01-29, 03-02, 04-06, 05-10, 07-18, 10-30
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Call 24/7 Tele-MANAS Toll-Free 14416 Anytime**<br>Government Tele-MANAS helpline provides 24/7 free, confidential psychological counseling in Gujarati by certified mental health experts. | **માનસિક તણાવમાં ૧૪૪૧૬ પર મફત કોલ કરો**<br>ચિંતા, ડિપ્રેશન કે નિરાશા થાય ત્યારે ખચકાયા વગર ૧૪૪૧૬ પર ફોન કરો; ગુજરાતીમાં ગુપ્ત અને નિઃશુલ્ક કાઉન્સેલિંગ ઉપલબ્ધ છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Screen for Depression & Anxiety with PHQ-9 / GAD-7**<br>Community Health Officers screen for common mental disorders at Ayushman Arogya Mandir. Early counseling prevents severe psychiatric crisis. | **પીએચક્યુ-૯ પ્રશ્નાવલીથી માનસિક તપાસ કરાવો**<br>આરોગ્ય મંદિર પર સામાન્ય માનસિક તણાવનું સ્ક્રીનિંગ કરાવો; પ્રારંભિક કાઉન્સેલિંગથી મનની મૂંઝવણ ઝડપથી દૂર થાય છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Chain or Abuse Patients with Mental Disorders**<br>Severe mental disorders like psychosis and schizophrenia are biological brain illnesses. Torturing or chaining patients is a punishable crime. | **માનસિક બીમારીમાં દોરા-ધાગા કે અત્યાચાર ન કરવો**<br>માનસિક બીમારીમાં દર્દીને સાંકળે બાંધવો કે ભૂત-વળગાડ ગણી અત્યાચાર કરવો ગુનો છે; સાયકિયાટ્રિસ્ટની દવાથી દર્દી સંપૂર્ણ સાજો થાય છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Dismiss Expressions of Hopelessness**<br>Statements like 'I want to end it all' are urgent emergency cries for help. Never leave a person in acute suicidal distress alone. | **કોઈની હતાશાને મજાક કે નાટક ન ગણો**<br>જ્યારે કોઈ કહે કે મારું કોઈ નથી અથવા જીવવું નથી, ત્યારે તેને હળવાશથી ન લેશો; તેમની સાથે રહો અને તાત્કાલિક ૧૪૪૧૬ ની મદદ અપાવો. | Verified sound; safe preventive advice. |

### Set 19. Snakebite First Aid & Poisoning Management
- **Content Hash:** `1b4fee7365be`
- **Clinical Assessment:** **`PROPOSED_REVISION`**
- **Occurrence Count in 2026:** 6 dates
- **Affected Dates:** 02-01, 03-05, 04-09, 05-13, 06-17, 11-02
- **Primary Sourced Authority:** National Action Plan for Prevention and Control of Snakebite Envenoming (NAP-SE), MoHFW, Government of India (2024); WHO Guidelines for the Clinical Management of Snakebites in the South-East Asia Region.
- **Clinical Audit Notes:** ABSOLUTE SURVIVAL GUARANTEE: Card 4 Gujarati text states 'સમયસર હોસ્પિટલ પહોંચવાથી દર્દીનો જીવ ૧૦૦% બચે છે' ('reaching hospital on time 100% saves the patient's life'). While prompt antivenom and supportive care (mechanical ventilation, dialysis) reduce mortality drastically, envenoming may still lead to fatality due to severe neurotoxicity, acute tubular necrosis, or venom-induced consumptive coagulopathy. Clinical communication must avoid 100% guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Immobilize Bitten Limb with a Rigid Splint**<br>Immobilize bitten extremity with a splint and crepe bandage just like a fracture. Keep limb below heart level; reassure the victim. | **દંખવાળા હાથ-પગને પાટિયું બાંધી સ્થિર રાખો**<br>સાપ કરડે ત્યારે દર્દીને દોડવા ન દો; દંખવાળા અંગને પાટિયું બાંધી સાવ સ્થિર રાખો જેથી ઝેર આખા શરીરમાં ઝડપથી ન ફેલાય. | Verified sound; safe preventive advice. |
| **Card 2** | **Rush to CHC / District Hospital for Free ASV**<br>Anti-Snake Venom (ASV) is the only scientific, life-saving antidote for Indian cobra, krait, Russell's viper, and saw-scaled viper bites. | **તાત્કાલિક સરકારી હોસ્પિટલ પહોંચી ASV લો**<br>વિલંબ કર્યા વગર ૧૦૮ દ્વારા સીધા સરકારી હોસ્પિટલ પહોંચો; ત્યાં મફત ઉપલબ્ધ એન્ટિ-સ્નેક વેનમ (ASV) જ એકમાત્ર જીવનરક્ષક ઈલાજ છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Cut, Suck, Bleed or Tie Tight Tourniquets**<br>Tight tourniquets stop arterial blood flow causing gangrene and amputation. Cutting with razor blades introduces fatal tetanus and hemorrhage. | **ચીરો મૂકવો, ચૂસવું કે કચકચાવીને દોરી ન બાંધવી**<br>દંખ પર બ્લેડથી ચીરો ન મૂકો, મોંથી ચૂસશો નહીં કે કચકચાવીને દોરી ન બાંધો; તેનાથી અંગ સડી જાય છે અને કાપવું પડી શકે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Waste Golden Time on Snake Stones or Faith Healers**<br>Over 70% of snakes are non-venomous; faith healers claim false credit while venomous bites progress to fatal paralysis during delays. | **ભુવા કે ઝેરમોરા પાછળ કિંમતી સમય ન બગાડવો**<br>સાપ કરડવા પર ઝાડ-ફૂંક કે પથ્થર ઘસવામાં એક મિનિટ પણ ન બગાડો; સમયસર હોસ્પિટલ પહોંચવાથી દર્દીનો જીવ ૧૦૦% બચે છે. | **CONCERN (DEC-17):** Gujarati claims 100% life saved. Sourced correction proposed. |

### Set 20. Dementia Awareness & Fall Prevention in Seniors (EPMNS)
- **Content Hash:** `ab4bc5d6e98c`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 6 dates
- **Affected Dates:** 06-15, 07-19, 08-23, 09-27, 10-31, 12-04
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Install Stainless Steel Grab Bars in All Toilets**<br>Anchor sturdy handrails beside Western commodes and bathing areas. Grab bars prevent devastating hip fractures in senior citizens. | **બાથરૂમ અને શૌચાલયમાં મજબૂત ગ્રેબ-બાર લગાવો**<br>વડીલો લપસી ન પડે તે માટે બાથરૂમમાં મજબૂત સ્ટીલના ગ્રેબ-બાર લગાવો જેથી ઊભા થતાં કે બેસતાં સારો ટેકો મળી રહે. | Verified sound; safe preventive advice. |
| **Card 2** | **Screen Memory with Mini-Cog Test at Age 60+**<br>Mini-Cog evaluates 3-word recall and clock drawing. Early detection of Alzheimer's and vascular dementia allows protective interventions. | **વડીલોની યાદશક્તિની મિની-કોગ તપાસ કરાવો**<br>વડીલો વસ્તુઓ કે રસ્તા ભૂલી જતા હોય તો આરોગ્ય કેન્દ્ર પર મિની-કોગ ટેસ્ટ કરાવો જેથી પ્રારંભિક સ્મૃતિભ્રંશનું નિદાન થઈ શકે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Leave Slippery Floors or Loose Electrical Cords**<br>Wet bathroom tiles and loose extension cords are leading preventable triggers for elder falls, subdural hematomas, and hip fractures. | **ભીનો ફ્લોર કે રસ્તામાં છૂટા વાયરો ન રાખવા**<br>ઘરમાં લાદી ભીની ન રાખો અને ચાલવાના રસ્તે છૂટા વાયરો ન રાખશો; વડીલોમાં લપસી પડવાથી થાપાનું ફ્રેક્ચર જીવલેણ નીવડી શકે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Scold or Argue with Disoriented Elders**<br>Dementia patients experience genuine cognitive distortion. Arguing increases agitation; use calm reassurance, simple words, and patience. | **ભૂલી જતા વડીલો પર ગુસ્સો ન કરવો કે ખીજાવું નહીં**<br>વડીલો વારંવાર એકની એક વાત પૂછે તો ચીડાશો નહીં; સ્નેહ અને ધીરજથી જવાબ આપો જેથી તેઓ સુરક્ષિત અને શાંત અનુભવે. | Verified sound; safe preventive advice. |

### Set 21. Safe Institutional Delivery & Dakshata Care
- **Content Hash:** `145b316b509e`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 01-05, 05-21, 06-25, 07-29, 09-02
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Plan Institutional Birth at FRU / CHC**<br>Pre-identify delivery hospital, arrange 108 transport, and choose a birth companion in advance for peace of mind. | **હોસ્પિટલમાં જ પ્રસૂતિ કરાવો**<br>પ્રસૂતિ માટે સરકારી હોસ્પિટલ અગાઉથી નક્કી રાખો, ૧૦૮ ની વ્યવસ્થા કરો અને સાથે રહેનાર સ્વજન તૈયાર રાખો. | Verified sound; safe preventive advice. |
| **Card 2** | **Respectful Maternity Care in Labor Room**<br>Ensure skilled birth attendants follow Dakshata protocols, active stage 3 management, and provide gentle compassionate care. | **દક્ષતા પ્રોટોકોલ અનુસાર સંભાળ**<br>પ્રસૂતિ ખંડમાં પ્રશિક્ષિત નર્સ દ્વારા સ્વચ્છ, જંતુમુક્ત અને સન્માનપૂર્વક સંભાળ સુનિશ્ચિત કરો. | Verified sound; safe preventive advice. |
| **Card 3** | **Home Delivery by Unskilled Dai**<br>Never attempt home delivery by untrained individuals; it risks lethal postpartum hemorrhage, birth asphyxia, and maternal sepsis. | **ઘેર ડિલિવરી કરાવવાનું જોખમ ન લેશો**<br>અપ્રશિક્ષિત દાઈ દ્વારા ઘેર સુવાવડ કરાવવાથી માતામાં અતિશય રક્તસ્ત્રાવ અને બાળકમાં શ્વાસ રૂંધાવાનું મોટું જોખમ રહે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Administering Labor Inducers at Home**<br>Never purchase or administer oxytocin injections outside hospital to speed up labor; it causes catastrophic uterine rupture. | **જાતે દુખાવાના ઇન્જેક્શન ન અપાવો**<br>સુવાવડ ઝડપી કરાવવા બહારથી કોઈ દવા કે ઇન્જેક્શન ન લેશો; તેનાથી ગર્ભાશય ફાટી જવાની જીવલેણ સમસ્યા થઈ શકે છે. | Verified sound; safe preventive advice. |

### Set 22. Immediate Newborn Care & Navjaat Shishu Suraksha
- **Content Hash:** `57fd68381d41`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 01-06, 04-18, 05-22, 07-30, 09-03
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Immediate Drying & Skin-to-Skin Warmth**<br>Dry newborn immediately with a dry clean towel, discard wet cloth, and place skin-to-skin on mother's chest to prevent hypothermia. | **બાળકને લૂછી માતાની છાતી સરસું રાખો**<br>જન્મતા વેંત બાળકને સ્વચ્છ ગરમ કપડાથી લૂછી ભીનું કપડું હટાવો અને માતાની છાતી સાથે અડાડી ગરમ રાખો. | Verified sound; safe preventive advice. |
| **Card 2** | **Initiate Breastfeeding in First Hour**<br>Give yellow thick colostrum within 60 minutes of delivery; it serves as baby's first natural immunity vaccine against infections. | **પ્રથમ કલાકમાં કોલોસ્ટ્રમ (ધાવણ) આપો**<br>જન્મના પહેલા ૬૦ મિનિટમાં જ માતાનું પીળું ઘટ્ટ ધાવણ આપો; તે બાળકની રોગપ્રતિકારક શક્તિ વધારે છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Delay First Bath for at Least 48 Hours**<br>Never give a bath on the first day; newborns lose body heat rapidly leading to cold stress, respiratory distress, and death. | **૪૮ કલાક સુધી સ્નાન ન કરાવવું**<br>જન્મ પછી ઓછામાં ઓછા બે દિવસ બાળકને નવડાવવું નહીં; તેનાથી શરીર ઠંડુ પડી જઈ શ્વાસની તકલીફ થઈ શકે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Applying Substances to Umbilical Stump**<br>Never apply cow dung, turmeric, kajal, or oil to the umbilical cord. Keep it clean and dry until it drops off naturally. | **નાળ પર કશું જ ન લગાવવું**<br>બાળકની નાળ પર હળદર, છાણ, તેલ કે કાજલ ક્યારેય ન લગાવવું; નાળને સાવ કોરી અને ખુલ્લી રાખો જેથી ધનુર ન થાય. | Verified sound; safe preventive advice. |

### Set 23. Modern Family Planning & Spacing Methods
- **Content Hash:** `251785bf7951`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 01-13, 05-29, 07-02, 08-06, 12-22
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Maintain 3-Year Spacing Between Children**<br>A healthy 3-year gap between births allows mother's body to replenish iron stores and gives every infant dedicated nurturing. | **બે બાળકો વચ્ચે ૩ વર્ષનું અંતર રાખો**<br>બે બાળકો વચ્ચે ઓછામાં ઓછું ૩ વર્ષનું અંતર રાખવાથી માતાનું સ્વાસ્થ્ય જળવાય છે અને બાળકનો વિકાસ સારો થાય છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Choose Antara Injectable or Chhaya Pills**<br>Avail free non-hormonal weekly Chhaya tablets, 3-monthly Antara injections, or long-acting postpartum IUCD at government facilities. | **અંતરા ઇન્જેક્શન કે છાયા ગોળી અપનાવો**<br>સરકારી આરોગ્ય કેન્દ્ર પરથી ૩ મહિને લેવાનું અંતરા ઇન્જેક્શન અથવા બિન-હોર્મોનલ છાયા ગોળીઓ નિઃશુલ્ક મેળવો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Rely on Emergency Pills as Regular Contraception**<br>Emergency contraceptive pills (ECPs) are only for rare unforeseen failures; frequent use disrupts hormonal cycles and fails. | **ઇમરજન્સી પિલ્સનો વારંવાર ઉપયોગ ન કરવો**<br>ઇમરજન્સી ગોળીઓ નિયમિત કુટુંબ નિયોજન માટે નથી; વારંવાર લેવાથી હોર્મોન્સ અસંતુલિત થાય છે અને અનિચ્છનીય ગર્ભ રહે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Discard Myths About Male Vasectomy (NSV)**<br>Non-Scalpel Vasectomy (NSV) is a simple, painless 10-minute procedure with zero impact on physical strength or marital life. | **પુરુષ નસબંધી અંગેની ગેરમાન્યતાઓ દૂર કરો**<br>પુરુષ નસબંધીથી નબળાઈ આવતી નથી; તે માત્ર ૧૦ મિનિટની સાદી, ટાંકા વગરની અને સાવ સલામત પ્રક્રિયા છે. | Verified sound; safe preventive advice. |

### Set 24. Basic Oral & Dental Hygiene (OEEE)
- **Content Hash:** `a199ca92215b`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 01-26, 04-03, 06-11, 08-19, 10-27
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Brush Twice Daily for 2 Minutes with Soft Bristles**<br>Use a pea-sized amount of fluoridated toothpaste. Clean all surfaces with gentle circular motions and scrape tongue gently. | **સવારે અને રાત્રે ૨ મિનિટ બ્રશ કરો**<br>સવારે અને રાત્રે સૂતા પહેલાં સોફ્ટ બ્રશથી દાંત ઉપર-નીચે ગોળાકાર ગતિમાં સાફ કરો અને જીભ પણ સાફ કરવાની ટેવ રાખો. | Verified sound; safe preventive advice. |
| **Card 2** | **Rinse Mouth Vigorously After Every Meal**<br>Swish plain drinking water vigorously after every meal to dislodge sticky carbohydrates and neutralize oral acid enamel decay. | **જમ્યા પછી સ્વચ્છ પાણીથી જોરથી કોગળા કરો**<br>કંઈપણ ખાધા પછી મોંમાં સ્વચ્છ પાણી ભરી જોરથી કોગળા કરો જેથી દાંત વચ્ચે ફસાયેલો ખોરાક નીકળી જાય અને સડો ન થાય. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Poke Safety Pins or Toothpicks into Gums**<br>Using sharp metal objects strips delicate periodontal attachments and creates bleeding gum pockets and bone infection. | **દાંત વચ્ચે સેફ્ટી પીન કે સળી ન ભરાવવી**<br>દાંત ખોતરવા ટાંકણી કે તાર વાપરવાથી પેઢા છોલાઈ જાય છે અને પાયોરિયા થાય છે; દાંત સાફ કરવા ડેન્ટલ ફ્લોસ વાપરો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Go to Sleep with Sugary Sweets in Mouth**<br>Sugars lingering on teeth overnight nourish acid-forming Streptococcus mutans bacteria that dissolve enamel and form deep cavities. | **રાત્રે ચોકલેટ-મીઠાઈ ખાઈને બ્રશ વગર ન સૂવું**<br>રાત્રે ગળી વસ્તુઓ ખાધા પછી બ્રશ કર્યા વગર ન સૂવું; રાત્રે મોંમાં લાળ ઓછી હોવાથી ખાંડથી દાંતમાં ઝડપથી કેવિટી થાય છે. | Verified sound; safe preventive advice. |

### Set 25. Substance Misuse Screening & De-addiction (EPMNS)
- **Content Hash:** `fb2551bb8e88`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 01-31, 03-04, 08-24, 11-01, 12-05
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Screen Alcohol Misuse with AUDIT Scale at HWC**<br>The 10-question AUDIT tool identifies risky drinking patterns early before cirrhosis, pancreatic damage, or domestic harm occur. | **આરોગ્ય મંદિર પર ઓડિટ પ્રશ્નાવલીથી તપાસ કરાવો**<br>દારૂના વ્યસનથી લીવર ખરાબ થાય તે પહેલાં આરોગ્ય કેન્દ્ર પર ઓડિટ સ્કેલ દ્વારા તપાસ કરાવો અને વહેલી કાઉન્સેલિંગ મેળવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Utilize District De-Addiction Centers (DDC)**<br>Access free medical detoxification, psychiatric therapy, and family counseling at government Nasha Mukti rehabilitation centers. | **જિલ્લા વ્યસન મુક્તિ કેન્દ્રની મદદ લો**<br>જિલ્લા હોસ્પિટલના વ્યસન મુક્તિ કેન્દ્ર પરથી સલામત દવાઓ અને કાઉન્સેલિંગ દ્વારા દારૂ કે ડ્રગ્સની લતમાંથી કાયમ માટે મુક્ત થાઓ. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Stop Heavy Alcohol Abruptly Without Medical Supervision**<br>Severe alcohol withdrawal triggers life-threatening Delirium Tremens, seizures, and arrhythmias. Always detoxify under doctor's care. | **ભારે દારૂનું વ્યસન અચાનક જાતે ન છોડવું**<br>વર્ષોથી દારૂ પીતા વ્યક્તિએ જાતે અચાનક બંધ ન કરવો; તેનાથી આંચકી કે ખેંચ આવી શકે છે. ડોક્ટરની દેખરેખ હેઠળ દવા સાથે છોડો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Enable Addiction by Hiding the Problem**<br>Covering up for an addicted family member delays life-saving medical help. Seek compassionate professional healthcare early. | **વ્યસનને શરમ કે ભયથી છુપાવવું નહીં**<br>પરિવારમાં કોઈને વ્યસન હોય તો સમાજના ડરે છુપાવશો નહીં; સમયસર સારવાર અપાવવાથી વ્યક્તિ અને આખો પરિવાર બચી જાય છે. | Verified sound; safe preventive advice. |

### Set 26. Eat Right India: Aaj Se Thoda Kam (Salt, Sugar, Oil)
- **Content Hash:** `0457bbb148a4`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 02-03, 03-07, 07-23, 08-27, 12-08
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Measure Cooking Oil with a Spoon, Not Direct Pouring**<br>Limit household oil consumption to under 500ml per person per month. Measure cooking oil with teaspoons to slash invisible saturated fat. | **તેલ ચમચીથી માપીને વાપરો (મહિને ૫૦૦ મિલી)**<br>શાક-વઘારમાં તેલ ડબ્બામાંથી સીધું રેડવાને બદલે ચમચીથી માપીને નાખો; વ્યક્તિ દીઠ મહિને ૫૦૦ મિલીથી વધુ તેલ ન વાપરવું. | Verified sound; safe preventive advice. |
| **Card 2** | **Satisfy Sweet Tooth with Fresh Seasonal Fruits**<br>Choose whole apples, papayas, oranges, and guavas instead of Indian sweets (mithai). Whole fruits provide protective fiber and antioxidants. | **મીઠાઈને બદલે તાજા મોસમી ફળો ખાઓ**<br>જમ્યા પછી મીઠાઈ ખાવાને બદલે પપૈયું, જામફળ, મોસંબી કે દાડમ જેવા તાજા ફળો ખાવાની ટેવ પાડો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Reheat Cooking Oil Repeatedly for Frying**<br>Reheating vegetable oils creates dangerous Total Polar Compounds (TPC) and industrial trans fats that trigger coronary blockages. | **તળેલું તેલ વારંવાર ગરમ કરીને ન વાપરવું**<br>પૂરી કે ભજીયાં તળ્યા પછી વધેલું તેલ વારંવાર ગરમ ન કરો; કાળું પડેલું તેલ હૃદયની નળીઓ બ્લોક કરે છે અને કેન્સરનું જોખમ વધારે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Avoid Ultra-Processed Packaged Snacks & Colas**<br>Packaged chips, puffs, biscuits, and sodas contain massive amounts of hidden sodium, palm oil, and high-fructose corn syrup. | **પેકેટવાળા નમકીન અને બેકરી આઇટમોથી દૂર રહો**<br>બહારના પડીકાં, વેફર્સ, બિસ્કિટ અને સોડા-કોલ્ડડ્રિંક્સ ખાલી કેલરી આપે છે; બાળકોને શેકેલા ચણા, મખાના અને તાજા ફળ આપો. | Verified sound; safe preventive advice. |

### Set 27. Home-Based Care for Young Child (HBYC)
- **Content Hash:** `5c78c6ad97ff`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 05-24, 06-28, 09-05, 11-13, 12-17
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Welcome Structured ASHA Home Visits**<br>Ensure ASHA conducts scheduled visits at 3, 6, 9, 12, and 15 months to check nutrition, immunization, and child development. | **આશા બહેનની મુલાકાતમાં સહકાર આપો**<br>બાળકના ૩, ૬, ૯, ૧૨ અને ૧૫મા મહિને આશા બહેનને ઘરે બોલાવી વજન અને તબિયતની તપાસ કરાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Stimulate Cognitive & Motor Milestones**<br>Talk, sing, play, and read colorful picture books with your child daily; early loving interaction shapes lifelong brain architecture. | **બાળક સાથે વાતચીત અને રમતો રમો**<br>બાળક સાથે રોજ વાતો કરો, ગીતો ગાઓ અને રંગબેરંગી ચિત્રો બતાવો; તેનાથી બાળકના મગજનો તેજસ્વી વિકાસ થાય છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Zero Screen Time Under Age 2**<br>Do not hand smartphones to infants to make them eat; screen time delays speech, social milestones, and induces irritability. | **નાના બાળકોને મોબાઇલ ન આપવો**<br>જમાડવા માટે બાળકને મોબાઇલની સ્ક્રીન બતાવવાની આદત ન પાડો; તેનાથી બોલવામાં અને સમજવામાં વિલંબ થાય છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Miss Monthly Anganwadi Weighing**<br>Plot your child's weight monthly on MCP green curve; catch growth faltering immediately before severe malnutrition sets in. | **આંગણવાડીમાં વજન કરાવવાનું ન ચૂકવું**<br>દર મહિને આંગણવાડીમાં બાળકના વજનની નોંધ કરાવો; વજનનો કાંટો નીચે જાય તો તુરંત બાલસેવા કેન્દ્રનો સંપર્ક કરો. | Verified sound; safe preventive advice. |

### Set 28. Primary Eye Care & Cataract Prevention (OEEE)
- **Content Hash:** `8cfbad70d58f`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 5 dates
- **Affected Dates:** 06-09, 07-13, 08-17, 10-25, 11-29
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Get Vision Screened Annually for Refractive Errors**<br>Screen schoolchildren for myopia and seniors for glaucoma. Corrective spectacles restore scholastic focus and prevent elder falls. | **બાળકો અને વડીલોની વર્ષે એકવાર આંખ તપાસ**<br>શાળાના બાળકો બોર્ડ પર વાંચી ન શકતા હોય તો ચશ્મા તપાસાવો અને વડીલોમાં ઝામરની વહેલી તપાસ માટે વાર્ષિક નેત્ર પરીક્ષણ કરાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Avail Free Modern Sutureless Cataract Surgery**<br>Do not let elders live in avoidable blindness. Modern sutureless cataract surgery with intraocular lens (IOL) is free at District Hospitals. | **સરકારી હોસ્પિટલમાં મોતિયાનું મફત ઓપરેશન**<br>મોતિયો પાકે ત્યાં સુધી રાહ ન જુઓ; રાષ્ટ્રીય અંધત્વ નિયંત્રણ કાર્યક્રમ હેઠળ આધુનિક પદ્ધતિથી લેન્સ મૂકી મોતિયાનું મફત ઓપરેશન કરાવો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Rub Red Irritated Eyes Aggressively**<br>Rubbing scratches delicate corneal epithelium and spreads bacterial conjunctivitis. Wash face with clean water and blink gently. | **આંખ લાલ થાય ત્યારે જોરથી ચોળવી નહીં**<br>આંખ લાલ થાય કે કચરો પડે ત્યારે જોરથી મસળવી નહીં; સ્વચ્છ પાણીની છાલક મારી આંખ સાફ કરો જેથી કીકી પર ઘસરકો ન પડે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Use Steroid Eye Drops Without Prescription**<br>Over-the-counter red eye drops containing steroids elevate intraocular pressure, causing irreversible blinding steroid glaucoma. | **ડોક્ટર પૂછ્યા વગર સ્ટીરોઈડ ટીપાં ન નાખવા**<br>મેડિકલ સ્ટોરમાંથી જાતે લાવીને આંખમાં ટીપાં ન નાખો; સ્ટીરોઈડ ટીપાં આંખનું પ્રેશર વધારી કાયમી અંધાપો લાવી શકે છે. | Verified sound; safe preventive advice. |

### Set 29. Comprehensive Geriatric Care & Elder Health (EPMNS)
- **Content Hash:** `3e5003b01c1d`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 4 dates
- **Affected Dates:** 01-27, 04-04, 07-16, 09-24
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Avail Monthly Comprehensive Geriatric Review at HWC**<br>Comprehensive Geriatric Assessment evaluates blood pressure, sugar, mobility, cognitive memory, nutrition, and urinary continence. | **આરોગ્ય મંદિર પર વડીલોની માસિક તપાસ**<br>દર મહિને આયુષ્માન આરોગ્ય મંદિર પર વડીલોની બીપી, સુગર, સાંધા, દ્રષ્ટિ અને યાદશક્તિની વ્યાપક તપાસ કરાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Install Bright Night-Lights & Non-Slip Bathroom Mats**<br>Ensure well-lit hallways, sturdy non-slip footwear, and uncluttered walkways to protect fragile bones from debilitating falls. | **ઘરમાં પૂરતો પ્રકાશ અને લપસી ન પડાય તેવી વ્યવસ્થા**<br>વડીલો માટે ઘરમાં રાત્રે પૂરતો પ્રકાશ રાખો, બાથરૂમમાં એન્ટી-સ્કિડ સાદડી પાથરો અને પગ લપસી ન જાય તેવા ચંપલ પહેરાવો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Dismiss Elder Sadness as Natural Old Age**<br>Elderly depression and social isolation are treatable medical conditions. Spend loving daily time talking with senior family members. | **વડીલોની ઉદાસીને માત્ર વૃદ્ધાવસ્થા ન ગણવી**<br>વડીલો એકલા પડી જાય કે ઉદાસ રહે તો તેમની સાથે બેસી વાતો કરો; માનસિક હતાશા એ ઉંમરનો ભાગ નથી પણ સારવારપાત્ર છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Self-Adjust Multiple Chronic Medications**<br>Seniors often take multiple medicines (polypharmacy). Always review pills with a qualified medical officer to prevent toxic drug clashes. | **વડીલોની દવાઓ જાતે બદલવી કે બંધ ન કરવી**<br>બીપી, ડાયાબિટીસ અને સાંધાની વિવિધ દવાઓ જાતે ઓછી-વધતી ન કરો; ડોક્ટર પાસે સમયાંતરે દવાની સમીક્ષા કરાવો. | Verified sound; safe preventive advice. |

### Set 30. Child Health Screening & Early Intervention (RBSK)
- **Content Hash:** `727476e5a39f`
- **Clinical Assessment:** **`PROPOSED_REVISION`**
- **Occurrence Count in 2026:** 4 dates
- **Affected Dates:** 03-19, 05-27, 09-08, 12-20
- **Primary Sourced Authority:** Operational Guidelines on Rashtriya Bal Swasthya Karyakram (RBSK), MoHFW; DEIC Operational Manual.
- **Clinical Audit Notes:** SURGICAL OUTCOME GUARANTEE: Card 4 states 'Conditions like cleft lip, clubfoot, and congenital cataract are 100% surgically correctable for free under government RBSK program'. Surgical outcomes vary based on tissue anatomy, associated syndromes, and post-operative therapy. Promising '100% surgical correction' contradicts national public health guidelines.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Screen for 4Ds with RBSK Mobile Health Teams**<br>Support RBSK doctor teams screening children aged 0-18 for Birth Defects, Deficiencies, Childhood Diseases, and Developmental Delays. | **શાળા-આંગણવાડીમાં RBSK તપાસ કરાવો**<br>શાળા અને આંગણવાડીમાં આવતી આરબીએસકે ટીમ પાસે બાળકની જન્મજાત ખોડખાંપણ, આંખ, કાન અને પોષણની તપાસ કરાવો. | Verified sound; safe preventive advice. |
| **Card 2** | **Utilize District Early Intervention Centers (DEIC)**<br>Refer children with developmental delays or sensory impairments to DEIC for free comprehensive therapy, hearing aids, and surgeries. | **DEIC કેન્દ્ર પર મફત થેરાપી મેળવો**<br>બોલવામાં, સાંભળવામાં કે ચાલવામાં મુશ્કેલી હોય તો જિલ્લા હોસ્પિટલના DEIC સેન્ટર પર મફત ફિઝિયોથેરાપી અને સ્પીચ થેરાપી મેળવો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Ignore Squint, Limp or Delayed Speech**<br>Do not assume children will naturally outgrow crossed eyes or walking delays; early intervention before age 3 produces best outcomes. | **આંખનો ત્રાસાદોષ કે બહેરાશ ન અવગણવી**<br>બાળકની આંખમાં ત્રાસાદોષ હોય કે મોડું બોલે તો આપમેળે મટી જશે તેમ માની બેસી ન રહો; વહેલી તપાસથી ખામી દૂર થાય છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Hide Congenital Cleft Lip or Clubfoot**<br>Conditions like cleft lip, clubfoot, and congenital cataract are 100% surgically correctable for free under government RBSK program. | **જન્મજાત ખોડખાંપણ છુપાવવી નહીં**<br>હોઠ ફાટેલો હોય કે પગનો પંજો વળેલો હોય તો અંધશ્રદ્ધામાં ન પડો; સરકારી યોજના હેઠળ મફત ઓપરેશનથી બાળક સાજું થઈ જાય છે. | **CONCERN (DEC-18):** Absolute claim of 100% surgical correction. Correction proposed. |

### Set 31. Eat Right: Desi Balanced Thali & Shree Anna Millets
- **Content Hash:** `60c52c325cba`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 4 dates
- **Affected Dates:** 04-12, 06-20, 11-05, 12-09
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Adopt the Traditional Rainbow Balanced Thali**<br>Fill 50% of your thali with colorful vegetables and raw salads, 25% with whole dals/curd/paneer, and 25% with wholesome grains. | **થાળીમાં ત્રિરંગો સંતુલિત આહાર સામેલ કરો**<br>રોજિંદા ભોજનમાં અડધી થાળી લીલા શાકભાજી અને કાચા સલાડની, ચોથો ભાગ કઠોળ-દાળ-દહીં અને ચોથો ભાગ અનાજ રાખો. | Verified sound; safe preventive advice. |
| **Card 2** | **Integrate Bajra, Jowar, Ragi & Foxtail Millets**<br>Shree Anna millets offer complex fiber, low glycemic index, magnesium, and calcium that protect against diabetes and obesity. | **બાજરી, જુવાર અને રાગીનો ઉપયોગ વધારો**<br>રોટલીમાં બાજરી, જુવાર અને રાગી જેવા પૌષ્ટિક ધાન્ય ઉમેરો; આ જાડા અનાજ સુગર અને કોલેસ્ટ્રોલને કુદરતી રીતે કાબૂમાં રાખે છે. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Rely Exclusively on Polished White Rice & Maida**<br>Ultra-refined grains lack bran and germ, causing rapid insulin spikes and accelerating visceral abdominal fat accumulation. | **મેંદો અને વધુ પડતા પોલિશ કરેલા ચોખા ન ખાવા**<br>મેંદો, સફેદ બ્રેડ અને વધુ પડતા ભાત ખાવાથી વજન અને સુગર ઝડપથી વધે છે; તેના બદલે આખા અનાજ અને દળેલા લોટનો ઉપયોગ કરો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Skip Daily Pulses, Dals or Sprouts**<br>Vegetarian Indian diets require diverse sprouted pulses (moong, chana) and dals to meet essential amino acid protein requirements. | **રોજના ભોજનમાં દાળ કે કઠોળ ખાવાનું ન ચૂકવું**<br>શાકાહારી ભોજનમાં કઠોળ પ્રોટીનનો મુખ્ય સ્ત્રોત છે; રોજિંદા ભોજનમાં ફણગાવેલા મગ, ચણા કે તુવેર દાળ અવશ્ય સામેલ કરો. | Verified sound; safe preventive advice. |

### Set 32. Infant & Young Child Feeding (IYCF)
- **Content Hash:** `6c3847ad349a`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 4 dates
- **Affected Dates:** 05-23, 06-27, 07-31, 09-04
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Exclusive Breastfeeding for 6 Months**<br>Provide zero water, honey, ghutti, or animal milk for first 6 months. Mother's milk contains 88% water and all essential nutrients. | **૬ મહિના ફક્ત માતાનું દૂધ જ આપો**<br>૬ મહિના સુધી બાળકને પાણી, ઘૂંટી કે મધ કશું જ ન આપો; ગરમીમાં પણ માતાના દૂધમાંથી પૂરતું પાણી મળી રહે છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Start Mashed Complementary Feeds at 6 Months**<br>At completed 6 months, begin thick mashed foods: dal-khichdi with ghee, mashed banana, boiled pumpkin, 2-3 times daily. | **૬ મહિને પૌષ્ટિક ઉપરી આહાર શરૂ કરો**<br>૬ મહિના પૂરા થતાં જ સ્તનપાન સાથે ઘી વાળી મગની દાળ-ખીચડી, કેળું અને બાફેલી શાકભાજી વાટકી-ચમચીથી શરૂ કરો. | Verified sound; safe preventive advice. |
| **Card 3** | **Avoid Bottle Feeding & Packaged Formula**<br>Never use plastic feeding bottles or pacifiers; unhygienic nipples cause recurring diarrhea, ear infections, and malnutrition. | **બોટલ કે ડબ્બાના દૂધથી બચો**<br>પ્લાસ્ટિકની બોટલથી બાળકના પેટમાં જંતુઓ જઈ ઝાડા-ઊલટી થાય છે; ઉપરી આહાર હંમેશા વાટકી-ચમચીથી જ આપો. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Feed Watery Dilute Gruels**<br>Do not feed only watery dal-water or thin liquids; young children need thick, calorie-dense foods to prevent stunting and wasting. | **પાતળી રાબ કે દાળનું પાણી ન આપવું**<br>માત્ર દાળનું પાણી આપવાથી બાળકનું પેટ ભરાય છે પણ પોષણ મળતું નથી; ઘટ્ટ મસળેલો ખોરાક ખવડાવવાની ટેવ પાડો. | Verified sound; safe preventive advice. |

### Set 33. Palliative Care & Chronic Pain Relief (EPMNS)
- **Content Hash:** `9a65761e7076`
- **Clinical Assessment:** **`PENDING_DECISION_GAP`**
- **Occurrence Count in 2026:** 3 dates
- **Affected Dates:** 03-01, 04-05, 08-21
- **Primary Sourced Authority:** National Programme for Palliative Care (NPPC) Operational Guidelines, MoHFW; WHO Guidelines for the Pharmacological and Radiotherapeutic Management of Cancer Pain.
- **Clinical Audit Notes:** SCHEDULAR GAP: Card copy is clinically sound (promotes holistic pain relief, oral morphine access, home nursing, and removes 'giving up hope' misconceptions). However, retaining only 3 occurrences (03-01, 04-05, 08-21) creates a 6-month multi-quarter gap from late August to March 2027.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Turn Bedridden Patients Every 2 Hours**<br>Reposition bedridden patients every 2 hours, use an alternating air mattress, and keep skin dry and moisturized to prevent bed sores. | **પથારીવશ દર્દીનું દર ૨ કલાકે પડખું ફેરવો**<br>લાંબા સમયથી પથારીવશ દર્દીનું દર ૨ કલાકે પડખું બદલો અને એર-મેટ્રેસ વાપરો જેથી પીઠ કે નિતંબ પર બેડસોર (ચાંદાં) ન પડે. | Verified sound; safe preventive advice. |
| **Card 2** | **Manage Chronic Pain with WHO Analgesic Protocol**<br>Advanced cancer and organ failure pain can be safely controlled with prescribed analgesics, restoring sleep and daily comfort. | **દર્દ મુક્તિ માટે ડોક્ટરની સલાહ મુજબ દવા લો**<br>ગંભીર બીમારીઓમાં દર્દીને પીડા સહન ન કરવા દો; સરકારી હોસ્પિટલના પેલિએટિવ કેર સેન્ટર પરથી દર્દ નિવારક દવાઓ મેળવો. | Verified sound; safe preventive advice. |
| **Card 3** | **Never Leave Chronically Ill Patients in Solitude**<br>Palliative care addresses physical pain, mental anxiety, social dignity, and spiritual peace. Involve patient in family daily moments. | **દર્દીને એકલા કે નિરાધાર ન છોડવા**<br>ગંભીર દર્દીને અલાયદા રૂમમાં એકલા ન પાડી દો; પરિવારનો સ્નેહ, હાજરી અને ખુશનુંમા વાતાવરણ તેમના મનને શાંતિ આપે છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Vigorously Massage Swollen Fragile Limbs**<br>Vigorous massage on swollen edematous legs can dislodge deep vein thrombosis (DVT) clots directly to lungs with fatal results. | **સોજાવાળા પગ પર ક્યારેય જોરથી માલિશ ન કરવી**<br>પથારીવશ દર્દીના સોજેલા પગ પર જોરથી તેલ માલિશ ન કરો; નસોમાં જામેલું લોહી છૂટું પડી ફેફસાં કે હૃદયમાં બ્લોકેજ કરી શકે છે. | Verified sound; safe preventive advice. |

### Set 34. Adolescent Health & Wellness (RKSK)
- **Content Hash:** `d449e3b2762e`
- **Clinical Assessment:** **`RETAIN_CONFIRMED`**
- **Occurrence Count in 2026:** 2 dates
- **Affected Dates:** 02-16, 12-21
- **Primary Sourced Authority:** National Health Mission (NHM) / Comprehensive Primary Health Care (CPHC) Operational Guidelines.
- **Clinical Audit Notes:** Card copy is medically sound, safe, and culturally adapted. Free of diagnostic public cut-offs, universal screening claims, or absolute guarantees.

| Card # | English Title & Copy | Gujarati Title & Copy | Card-Level Verification |
| :--- | :--- | :--- | :--- |
| **Card 1** | **Take Weekly Blue WIFS Tablet on Mondays**<br>Adolescent boys and girls aged 10-19 should take one blue Iron-Folic Acid tablet weekly after lunch in schools to conquer anemia. | **દર સોમવારે વાદળી આયર્ન ગોળી લો**<br>શાળામાં દર સોમવારે જમ્યા પછી અપાતી વાદળી આયર્નની ગોળી અવશ્ય લો; તેનાથી શરીરમાં સ્ફૂર્તિ વધે છે અને ભણવામાં ધ્યાન રહે છે. | Verified sound; safe preventive advice. |
| **Card 2** | **Practice Safe Menstrual Hygiene & Pad Disposal**<br>Use clean sanitary pads, change them every 4-6 hours, wash with clean water, and dispose wrapped in paper in dedicated dustbins. | **સ્વચ્છ પેડ વાપરો અને ૬ કલાકે બદલો**<br>માસિક દરમિયાન સ્વચ્છ પેડ વાપરો, દર ૪-૬ કલાકે બદલો અને કાગળમાં લપેટી કચરાપેટીમાં નાખો; ગંદા કપડાનો ઉપયોગ ન કરો. | Verified sound; safe preventive advice. |
| **Card 3** | **Avoid Skipping Meals for Packaged Junk Food**<br>Never replace nutritious home-cooked meals with packaged snacks, chips, or roadside colas; they cause severe micronutrient malnutrition. | **ભોજન છોડી જંકફૂડ ખાવાની ટેવ ટાળો**<br>બહારના તળેલા પેકેટ, મેગી કે કોલ્ડડ્રિંક્સ ખાવાનું ટાળો; દાળ, ભાત, શાક, રોટલી અને સલાડથી શરીર મજબૂત બને છે. | Verified sound; safe preventive advice. |
| **Card 4** | **Never Suffer Mental Anxiety in Silence**<br>Visit the AFHC (Maitri Clinic) at CHC for free, confidential guidance on emotional stress, body changes, and peer pressure. | **માનસિક મૂંઝવણ મનમાં ન દબાવવી**<br>પરીક્ષાનો તણાવ કે શારીરિક ફેરફારોની મૂંઝવણ હોય તો નજીકના મૈત્રી ક્લિનિકના કાઉન્સેલર સાથે ખુલીને વાત કરો. | Verified sound; safe preventive advice. |

---

*End of Card-Level Retained Routine Audit. All findings registered in PENDING_DECISIONS_REGISTER.md (`DEC-14` through `DEC-19`).*