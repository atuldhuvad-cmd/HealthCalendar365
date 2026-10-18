# HealthCalendar365 — Nine-Candidate Pilot Spending & Generation Authorization Sheet

**Date:** October 16, 2026  
**Document ID:** `AUTH-SHEET-PILOT-20261016`  
**Status:** ZERO-SPEND DIRECTIVE ACTIVE — AUTHORIZED SPENDING STRICTLY USD 0.00  
**Governing Standard:** [`review/RELEASE_GOVERNANCE.md`](file:///d:/HealthCalendar365/review/RELEASE_GOVERNANCE.md)  
**Production Hold:** STRICTLY ACTIVE

> [!IMPORTANT]
> **USER DIRECTIVE (October 16, 2026):** Explicit user instruction received: *"Do not use any paid image-generation API and do not incur any financial charge. Keep authorized spending at USD 0.00. Preserve the four ready candidates as review-only specifications and continue only work that requires no external API expenditure. Report any future paid requirement before taking action."*
>
> In accordance with this directive:
> - **Authorized Spend:** Strictly **USD 0.00**.
> - **Zero External API Calls:** No Gemini / Imagen or other generative image APIs will be called.
> - **Review-Only Specifications:** All 4 ready candidates are preserved as review-only candidate specifications.
> - **Zero Financial Charge:** Work proceeds exclusively on zero-expenditure acceptance, testing, and governance phases.

---

## 1. Provider & Model Availability Verification (October 2026)

Immediately prior to preparing this authorization sheet, provider availability and published pricing were verified against official documentation:

1. **Legacy Model Retirement (`imagen-3.0-generate-002`):**
   - Official Google AI developer documentation confirms that `imagen-3.0-generate-002` was **deprecated and shut down on November 10, 2025**. It is no longer accessible via the Gemini Developer API (`ai.google.dev`).
2. **Current Active Production Models:**
   - Under the Google GenAI SDK (`google-genai`), image generation is supported natively via `client.models.generate_content`:
     - **Primary Candidate Model:** `gemini-3.1-flash-image` (Nano Banana 2) — State-of-the-art native image generation combining prompt comprehension, fine clinical photorealism, and rapid generation.
     - **Alternative High-Efficiency Model:** `gemini-2.5-flash-image` (Nano Banana) — High-efficiency visual generator.
3. **Current Official Pricing:**
   - Google AI Studio standard image generation rate: **~USD 0.039 – 0.040 per generated image** (standard resolution).
   - Planning rate per attempt: **USD 0.04**.

---

## 2. Partitioned Pilot Candidate Breakdown

The 9 replacement candidates are partitioned into two strict operational categories:

### A. Four Candidates `READY_TO_REQUEST_AUTHORIZATION` (Copy-Independent)
These 4 slots have frozen, approved copy in `data/health_365.json` that does not require modification. Their prompts directly reflect the existing active text.

| Slot | Staging ID | Theme / Clinical Focus | Active Spec Hash | Max Attempts | Est. Cost | Spending Cap |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| `10-19-oral_card2` | `pilot-20261016-10-19-oral-card2-a01` | Post-meal clean water mouth swishing at washbasin | `a1c1d3903632...` | 2 | $0.04 | $0.10 |
| `10-20_card1` | `pilot-20261016-10-20-card1-a01` | Indian elder gripping wall-mounted stainless grab bar | `b65c586266f4...` | 2 | $0.04 | $0.10 |
| `10-20_card2` | `pilot-20261016-10-20-card2-a01` | Walking elders & ragi / white sesame / paneer foods | `a32d80035850...` | 2 | $0.04 | $0.10 |
| `10-21_card1` | `pilot-20261016-10-21-card1-a01` | Indian kitchen airtight ceramic barni & glass salt jars | `cde9b141b633...` | 2 | $0.04 | $0.10 |
| **SUBTOTAL (Phase 1 Pilot)** | **4 Candidate Slots** | | | **8 Attempts Max** | **$0.16** | **$0.40** |

### B. Five Candidates `BLOCKED_PENDING_COPY_APPROVAL` (Copy-Dependent)
Image generation for these 5 slots is **STRICTLY BLOCKED** because their visuals depend on unresolved clinical copy changes. Authorized spend for these slots is currently **USD 0.00**.

| Slot | Staging ID | Blocking Dependency | Staged Prospective Spec Hash | Status | Authorized Spend |
| :--- | :--- | :--- | :--- | :---: | :---: |
| `10-20_card3` | `pilot-20261016-10-20-card3-a01` | Requires clinician sign-off on domestic fall hazards title/desc (`REQUIRES_APPROVAL_OF_STAGED_TITLE_10_20_CARD3`) | Pending copy approval | ⛔ **BLOCKED** | $0.00 |
| `10-20_card4` | `pilot-20261016-10-20-card4-a01` | Requires clinician sign-off on revised sodium / soda copy per IOF guidance (`REQUIRES_APPROVAL_OF_STAGED_TITLE_AND_DESC_10_20_CARD4`) | Pending copy approval | ⛔ **BLOCKED** | $0.00 |
| `10-21_card2` | `pilot-20261016-10-21-card2-a01` | Requires clinician sign-off on non-volatile KIO3 thermal food chemistry (`REQUIRES_APPROVAL_OF_STAGED_DESC_10_21_CARD2`) | Pending copy approval | ⛔ **BLOCKED** | $0.00 |
| `10-21_card3` | `pilot-20261016-10-21-card3-a01` | Requires clinician sign-off on unbranded loose salt avoidance title (`REQUIRES_APPROVAL_OF_STAGED_TITLE_10_21_CARD3`) | Pending copy approval | ⛔ **BLOCKED** | $0.00 |
| `10-21_card4` | `pilot-20261016-10-21-card4-a01` | Requires clinician sign-off on revised dry, covered, moisture-protected storage copy (`REQUIRES_CLINICAL_REAPPROVAL_OF_REVISED_COPY_10_21_CARD4`) | Pending copy approval | ⛔ **BLOCKED** | $0.00 |
| **SUBTOTAL (Phase 2 Blocked)** | **5 Candidate Slots** | | | **0 Attempts** | **$0.00** | **$0.00** |

---

## 3. Detailed Specification & Prompt Manifest for the 4 Ready Candidates

### Candidate 1: `10-19-oral_card2`
- **Slot:** `10-19-oral_card2` (Day: `10-19-oral`, Card: 2)
- **Active Title EN/GU:** Rinse Mouth Vigorously After Meals / કંઈપણ ખાધા પછી સ્વચ્છ પાણીના કોગળા કરો
- **Active Image SHA-256:** `8ee897bfa0ea0e3df016e4f34c1aa2194fd0baa80bed4a0a6b10c36925ba1c4a`
- **Active Spec Hash:** `a1c1d3903632a731410e781742bfdeba1dd97ad7a7ce57f437479a0b15d10ad4`
- **Target Output File:** `photos/staging/candidate_10_19_oral_card2_v1.png`
- **Dimensions / Ratio:** Minimum $720\times540$ px, Target $1080\times810$ px ($4:3$)
- **Polarity:** Positive hygiene action
- **Required Visual Elements:** Indian individual actively rinsing mouth with water at clean modern ceramic washbasin after meal; water swishing with puffed cheeks; clean glass tumbler on counter; natural morning light; clean clinical hygiene.
- **Prohibited Elements:** Dental floss thread, plastic flosser picks, toothpicks, commercial toothpaste branding, distorted facial features, text slogans.
- **Generation Prompt:**
  ```text
  Ultra-photorealistic 4:3 close-up photograph of an Indian individual actively rinsing mouth with water at a clean, modern ceramic washbasin after a meal. The person has water in mouth with puffed cheeks during a vigorous swish, leaning slightly forward over the sink. A simple clear glass water tumbler rests on the counter. Natural indoor morning lighting, authentic Indian domestic bathroom or wash area setting, clean clinical hygiene, cinematic depth of field, 8k resolution, editorial medical quality. Strictly NO dental floss, NO flosser picks, NO toothpicks, NO logos, NO text.
  ```

### Candidate 2: `10-20_card1`
- **Slot:** `10-20_card1` (Day: `10-20`, Card: 1)
- **Active Title EN/GU:** Bright Lighting & Bathroom Grab Bars / ઘરમાં પૂરતો પ્રકાશ અને બાથરૂમમાં ગ્રેબ-બાર
- **Active Image SHA-256:** `0c6537680a7c3fd1956ab389e9fadd26342f570c4af87008399f2723cc6bd119`
- **Active Spec Hash:** `b65c586266f47d326e46bd398aecab53e9d861b01c296fffcade1e5ef1948224`
- **Target Output File:** `photos/staging/candidate_10_20_card1_v1.png`
- **Dimensions / Ratio:** Minimum $720\times540$ px, Target $1080\times810$ px ($4:3$)
- **Polarity:** Positive safety action
- **Required Visual Elements:** Elderly Indian senior citizen (65+ years) safely gripping wall-mounted brushed stainless steel grab bar in brightly lit bathroom; dry matte non-slip floor tiles; warm morning light; dignified posture; authentic Indian domestic setting.
- **Prohibited Elements:** Western hospital ward stock look, slippery wet floor puddles, distorted limbs/hands, commercial logos.
- **Generation Prompt:**
  ```text
  Ultra-photorealistic 4:3 close-up photograph of an elderly Indian senior citizen (65+ years) safely gripping a sturdy, wall-mounted brushed stainless steel bathroom grab bar in a brightly lit Indian home bathroom. The bathroom has clean, dry, matte non-slip floor tiles and warm morning lighting. Dignified posture, authentic Indian domestic setting, clean clinical fall-prevention environment, cinematic depth of field, 8k resolution, editorial medical journal quality. No text, no logos, no distorted limbs, no slippery wet puddles.
  ```

### Candidate 3: `10-20_card2`
- **Slot:** `10-20_card2` (Day: `10-20`, Card: 2)
- **Active Title EN/GU:** Weight-Bearing Walks & Ragi / Sesame Nutrition / રોજિંદી ચાલવાની કસરત અને રાગી-તલનો આહાર
- **Active Image SHA-256:** `3076ab20178716f0a52efaa03d6afc653e9bbff7a83ea2a8c1293ec4ace99404`
- **Active Spec Hash:** `a32d80035850373fbe548c5a622732cfa2a3d20f6e6018dc15f482d0b7cf72e0`
- **Target Output File:** `photos/staging/candidate_10_20_card2_v1.png`
- **Dimensions / Ratio:** Minimum $720\times540$ px, Target $1080\times810$ px ($4:3$)
- **Polarity:** Positive nutrition & exercise action
- **Required Visual Elements:** Active elderly Indian couple walking briskly along paved path in sunlit Indian garden park during morning golden hour; comfortable walking shoes; soft natural sunlight; foreground/inset display of traditional Indian calcium staples: ragi grains, bowl of white sesame seeds, fresh artisanal paneer.
- **Prohibited Elements:** Western stock models, pharmaceutical calcium pill bottles, sedentary/frail postures, commercial brand packaging.
- **Generation Prompt:**
  ```text
  Ultra-photorealistic 4:3 photograph of active elderly Indian couple walking briskly along a paved walking path in a sunlit Indian garden park during golden morning hours, wearing comfortable walking shoes and cotton attire. Soft natural morning sunlight illuminating them. A tasteful inset or subtle foreground display of traditional Indian calcium foods: ragi grains, small bowl of white sesame seeds, and fresh paneer. Warm authentic Indian lifestyle, healthy bone aging, cinematic depth of field, 8k resolution, editorial medical quality. No text, no logos, no pills.
  ```

### Candidate 4: `10-21_card1`
- **Slot:** `10-21_card1` (Day: `10-21`, Card: 1)
- **Active Title EN/GU:** Store Iodized Salt in Airtight Jars / આયોડાઇઝ્ડ મીઠું હવાચુસ્ત બરણીમાં ઢાંકીને રાખો
- **Active Image SHA-256:** `96bc7f83487c80996b2b2936808f6d3d4af9a69d7e5c31d5ee1a0e9257625153`
- **Active Spec Hash:** `cde9b141b6339bbc33749b7256fecc4eb7ab325dae1deddcc22aafdd82c1de11`
- **Target Output File:** `photos/staging/candidate_10_21_card1_v1.png`
- **Dimensions / Ratio:** Minimum $720\times540$ px, Target $1080\times810$ px ($4:3$)
- **Polarity:** Positive storage action
- **Required Visual Elements:** Authentic Indian kitchen counter with traditional glazed ceramic barni with airtight lid, clear glass jar with fine white iodized salt, small wooden spoon resting beside, sealed salt packet in background with generic smiling sun iodized logo, warm natural kitchen light.
- **Prohibited Elements:** Refrigerator crisper drawers, open damp containers, commercial trademark brand names, text slogans.
- **Generation Prompt:**
  ```text
  Ultra-photorealistic 4:3 close-up photograph of an authentic Indian kitchen counter featuring a traditional ceramic barni (glazed white and brown porcelain jar) with an airtight lid, and a clear glass jar containing fine white iodized salt. A small wooden spoon is resting beside the open jar showing clean dry powdered salt. In the background sits a sealed salt packet with a generic smiling sun iodized logo. Warm natural kitchen lighting, clean hygiene, authentic Indian domestic setting, cinematic depth of field, 8k resolution, editorial quality. No commercial brand logos, no text.
  ```

---

## 4. Total Budget & Spending Authorization Request

To proceed with generating the 4 copy-independent pilot candidates into `photos/staging/`:

| Item | Specification |
| :--- | :--- |
| **Target Candidate Slots** | `10-19-oral_card2`, `10-20_card1`, `10-20_card2`, `10-21_card1` |
| **Model Recommended** | `gemini-3.1-flash-image` (via Google GenAI API) |
| **Generation Output Directory** | `photos/staging/` (Zero mutation of active `photos/` assets) |
| **Max Attempts per Slot** | 2 attempts |
| **Estimated Initial Spend** | **USD 0.16** (4 candidates × 1 attempt × $0.04) |
| **Maximum Authorized Spend Cap** | **USD 0.40** (Total cap covering retries up to 2 attempts per candidate) |
| **Blocked Slots Spending** | **USD 0.00** (Strictly $0.00 for the 5 copy-dependent slots) |

---

## 5. Required User Authorization Prompt

To authorize this pilot generation batch, the user must provide explicit approval in chat:
> *"I authorize the 4-candidate pilot image generation using model `gemini-3.1-flash-image` into `photos/staging/` with a maximum spending cap of USD 0.40."*

**STOPPING POINT REACHED. Zero API calls executed. Awaiting explicit user spend authorization.**
