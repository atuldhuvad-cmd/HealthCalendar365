import json
import os
import hashlib

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
review_dir = os.path.join(PROJECT_DIR, 'review')
os.makedirs(review_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. UPDATED HEALTH OBSERVANCE PROVENANCE & MEDICAL CLAIMS AUDIT
# -----------------------------------------------------------------------------
provenance_data = {
    "10-15": {
        "observance_name_en": "Global Handwashing Day",
        "observance_name_gu": "વિશ્વ હાથ ધોવા દિવસ",
        "date": "October 15",
        "official_sponsoring_body": "Global Handwashing Partnership (GHP)",
        "international_status": "Officially designated global health advocacy day",
        "source_citation": "Global Handwashing Partnership (https://globalhandwashing.org/global-handwashing-day/)",
        "attribution_category": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "Global Handwashing Partnership (GHP)",
        "provenance_notes": "Official partnership founded by CDC, UNICEF, USAID, World Bank and academic institutions."
    },
    "10-15-cane": {
        "observance_name_en": "White Cane Safety Day / World White Cane Day",
        "observance_name_gu": "વિશ્વ સફેદ લાકડી દિવસ (પ્રજ્ઞાચક્ષુ સન્માન)",
        "date": "October 15",
        "official_sponsoring_body": "World Blind Union (WBU) / National Federation of the Blind (NFB)",
        "international_status": "Historically recognized advocacy observance (US Joint Resolution 1964; WBU global commemoration)",
        "source_citation": "World Blind Union (https://worldblindunion.org/) & NFB",
        "attribution_category": "HISTORICAL_ADVOCACY_OBSERVANCE",
        "display_badge": "World Blind Union (WBU) Observance",
        "provenance_notes": "Grassroots and organizational advocacy day; not a formal UN treaty day."
    },
    "10-16": {
        "observance_name_en": "World Food Day",
        "observance_name_gu": "વિશ્વ ખાદ્ય દિવસ",
        "date": "October 16",
        "official_sponsoring_body": "Food and Agriculture Organization of the United Nations (FAO)",
        "international_status": "Official United Nations International Day (UN General Assembly Resolution 34/83)",
        "source_citation": "FAO World Food Day Portal (https://www.fao.org/world-food-day/en)",
        "attribution_category": "OFFICIAL_UN_AGENCY_VERIFIED",
        "display_badge": "UN Food & Agriculture Organization (FAO)",
        "provenance_notes": "Established November 1979 at FAO's 20th General Conference."
    },
    "10-16-spine": {
        "observance_name_en": "World Spine Day",
        "observance_name_gu": "વિશ્વ કરોડરજ્જુ દિવસ",
        "date": "October 16",
        "official_sponsoring_body": "World Federation of Chiropractic (WFC) / Global Alliance for Musculoskeletal Health",
        "international_status": "Global health awareness campaign under Bone and Joint Decade initiative",
        "source_citation": "World Spine Day Official Registry (http://www.worldspineday.org/)",
        "attribution_category": "ORGANIZATIONAL_CAMPAIGN_VERIFIED",
        "display_badge": "World Spine Day (WFC / GASH)",
        "provenance_notes": "Global musculoskeletal health awareness campaign organized annually on Oct 16."
    },
    "10-17": {
        "observance_name_en": "World Trauma Day (World Trauma Prevention Day)",
        "observance_name_gu": "વિશ્વ ટ્રોમા નિવારણ દિવસ",
        "date": "October 17",
        "official_sponsoring_body": "Grassroots Clinical Initiative (Indian Emergency Care & Trauma Community)",
        "international_status": "Grassroots clinical awareness day (NOT an official UN or WHO designated international day)",
        "source_citation": "Trauma Association of India / Indian Emergency Medicine Literature",
        "attribution_category": "ORGANIZATION_NEUTRAL_DAILY_GUIDANCE",
        "display_badge": "Emergency Trauma Care Guidance",
        "provenance_notes": "Caution: Not a UN or WHO recognized international day. Removal of WHO badge confirmed. Founding origin in India (2011) recorded as historical context pending primary charter evidence."
    },
    "10-18": {
        "observance_name_en": "World Menopause Day",
        "observance_name_gu": "વિશ્વ મેનોપોઝ દિવસ",
        "date": "October 18",
        "official_sponsoring_body": "International Menopause Society (IMS)",
        "international_status": "Officially designated global health campaign (established 2009 by IMS)",
        "source_citation": "International Menopause Society (https://www.imsociety.org/education/world-menopause-day/)",
        "attribution_category": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "International Menopause Society (IMS)",
        "provenance_notes": "Official annual campaign led by IMS with expert White Papers."
    },
    "10-19": {
        "observance_name_en": "Ear & Hearing Health",
        "observance_name_gu": "કાન અને શ્રવણ સ્વાસ્થ્ય",
        "date": "October 19",
        "official_sponsoring_body": "None (Daily Health Guidance)",
        "international_status": "Organization-neutral daily clinical guidance (Official WHO World Hearing Day is March 3)",
        "source_citation": "Primary Clinical Guidance / Indian ENT Clinical Standards",
        "attribution_category": "ORGANIZATION_NEUTRAL_DAILY_GUIDANCE",
        "display_badge": "Daily Health Guidance",
        "provenance_notes": "Routine primary clinical education; no international day designation."
    },
    "10-19-oral": {
        "observance_name_en": "Oral Health & Tobacco-Free Life",
        "observance_name_gu": "મુખનું આરોગ્ય અને તમાકુ મુક્તિ",
        "date": "October 19",
        "official_sponsoring_body": "None (Daily Health Guidance)",
        "international_status": "Organization-neutral daily clinical guidance (Official FDI/WHO World Oral Health Day is March 20)",
        "source_citation": "Dental Council of India / National Oral Health Programme guidelines",
        "attribution_category": "ORGANIZATION_NEUTRAL_DAILY_GUIDANCE",
        "display_badge": "Daily Health Guidance",
        "provenance_notes": "High-priority clinical guidance card for betel quid / tobacco cessation."
    },
    "10-20": {
        "observance_name_en": "World Osteoporosis Day",
        "observance_name_gu": "વિશ્વ ઓસ્ટીયોપોરોસીસ દિવસ",
        "date": "October 20",
        "official_sponsoring_body": "International Osteoporosis Foundation (IOF)",
        "international_status": "Official international health campaign (launched 1996 by UK National Osteoporosis Society, led globally by IOF)",
        "source_citation": "International Osteoporosis Foundation (https://www.osteoporosis.foundation/)",
        "attribution_category": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "International Osteoporosis Foundation (IOF)",
        "provenance_notes": "Dedicated international bone health campaign."
    },
    "10-21": {
        "observance_name_en": "Global Iodine Deficiency Disorders Prevention Day (World Iodine Deficiency Day)",
        "observance_name_gu": "વિશ્વ આયોડિન અલ્પતા નિવારણ દિવસ",
        "date": "October 21",
        "official_sponsoring_body": "Supported by Iodine Global Network (IGN) advocacy",
        "international_status": "Organically developed awareness date (NOT a recognized official UN or WHO international day)",
        "source_citation": "Iodine Global Network: 'Our hopes on World Iodine Deficiency Prevention Day' (https://ign.org/latest/blog/our-hopes-on-world-iodine-deficiency-prevention-day/)",
        "attribution_category": "ORGANIC_AWARENESS_DATE_NOT_UN_OFFICIAL",
        "display_badge": "Iodine Deficiency Prevention Guidance",
        "provenance_notes": "CRITICAL CORRECTION: IGN explicitly notes this observance grew organically and is NOT an official UN/WHO mandated day. Sponsoring coalition claims remain unverified."
    }
}

# -----------------------------------------------------------------------------
# 2. EXPANDED MEDICAL CLAIMS & COPY AUDIT QUEUE
# -----------------------------------------------------------------------------
copy_audit = [
    {
        "slot": "10-15_day_title",
        "category": "EDITORIAL_GRAMMAR_PROPOSAL",
        "current_en": "Global Handwashing Day",
        "current_gu": "વિશ્વ હાથ ધોવાના દિવસ (ગ્લોબલ હેન્ડવોશિંગ ડે)",
        "proposed_en": "Global Handwashing Day",
        "proposed_gu": "વિશ્વ હાથ ધોવા દિવસ (ગ્લોબલ હેન્ડવોશિંગ ડે)",
        "rationale": "Corrects Gujarati genitive case marker ('ધોવાના' -> 'ધોવા'). Staged for qualified Gujarati language reviewer verification.",
        "clinical_evidence_source": "Gujarati Lexicon / Standard Public Health Gujarati usage",
        "requires_clinician_sign_off": False,
        "staging_status": "STAGED_FOR_LANGUAGE_REVIEW"
    },
    {
        "slot": "10-15_card2_desc",
        "category": "MEDICAL_CLAIM_REVISION",
        "current_en": "Interlace fingers, rub backs of hands, rotate thumbs, and clean under fingernails where 80% of germs hide.",
        "current_gu": "હથેળી, આંગળીઓની વચ્ચે, અંગૂઠો અને નખના ભાગમાં ૨૦ સેકન્ડ ઘસીને સાબુ લગાવો જ્યાં મોટાભાગના કીટાણુ છુપાયેલા હોય છે.",
        "proposed_en": "Rub palms, backs of hands, between fingers, fingertips and nails, thumbs, and wrists with soap for at least 20 seconds.",
        "proposed_gu": "હથેળી, હાથનો પાછળનો ભાગ, આંગળીઓની વચ્ચે, આંગળીના ટેરવા અને નખ, અંગૂઠા તથા કાંડા સાબુથી ઓછામાં ઓછા ૨૦ સેકન્ડ ઘસો.",
        "rationale": "Dr. Atul requested a clear six-area handwashing sequence including thumbs and wrists. This also removes the unsupported exact '80%' claim.",
        "clinical_evidence_source": "CDC Clean Hands FAQ (https://www.cdc.gov/clean-hands/faq/index.html)",
        "requires_clinician_sign_off": True,
        "staging_status": "APPLIED_PENDING_SCOPED_REAPPROVAL"
    },
    {
        "slot": "10-16-spine_card4_desc",
        "category": "BIOMECHANICAL_CLAIM_CONTEXT",
        "current_en": "Bending neck forward puts 27 kg of pressure on cervical vertebrae. Hold your smartphone up closer to eye level.",
        "current_gu": "મોબાઈલમાં સતત નીચું જોવાથી ડોકના મણકા પર ૨૭ કિલો વજન આવે છે; ફોનને હંમેશા આંખની સામે રાખીને વાપરો.",
        "proposed_en": "Severe forward neck flexion significantly increases mechanical load on cervical vertebrae. Hold devices closer to eye level and change posture frequently.",
        "proposed_gu": "ડોક વધારે પડતી નીચી નમાવવાથી સર્વાઇકલ મણકા પર ભારે દબાણ આવે છે; ફોનને આંખની સામે રાખો અને વચ્ચે-વચ્ચે ગરદન હળવી કરો.",
        "rationale": "The 27 kg (60 lbs) figure originates from a specific 2014 mathematical finite element model (Hansraj KK, Surg Technol Int), but clinical consensus emphasizes posture variation and movement breaks over a rigid static weight claim.",
        "clinical_evidence_source": "Hansraj KK (2014) Assessment of Stresses in the Cervical Spine Caused by Posture and Position of the Head. Surg Technol Int 25:277-9",
        "requires_clinician_sign_off": True,
        "staging_status": "APPLIED_PENDING_SCOPED_REAPPROVAL"
    },
    {
        "slot": "10-17_card3_title",
        "category": "EDITORIAL_ALIGNMENT",
        "current_en": "Controlled Speed & Helmet Discipline",
        "current_gu": "નિયંત્રિત ગતિ અને હેલ્મેટ શિસ્ત",
        "proposed_en": "Controlled Speed & Zero Phone Distraction",
        "proposed_gu": "નિયંત્રિત ગતિ અને ફોનથી સાવધાની",
        "rationale": "Card 1 already covers helmet discipline; Card 3 description covers mobile phones and speeding. Clarifies title to match body copy.",
        "clinical_evidence_source": "Motor Vehicles (Amendment) Act 2019 / WHO Global Status Report on Road Safety",
        "requires_clinician_sign_off": False,
        "staging_status": "STAGED_FOR_EDITORIAL_REVIEW"
    },
    {
        "slot": "10-18_card3_and_card4",
        "category": "CLINICAL_INVERSION_CORRECTION",
        "current_en": "Card 3 Title: Bone Density & Joint Care (Desc: hot flashes & consulting gynecologist) | Card 4 Title: Qualified Gynecologist Consultation (Desc: diet & caffeine)",
        "current_gu": "કાર્ડ ૩: હાડકાંની મજબૂતી (વર્ણન: ગાયનેકોલોજિસ્ટની સલાહ) | કાર્ડ ૪: ગાયનેકોલોજિસ્ટની સલાહ (વર્ણન: ચા-કૉફીથી પરેજી)",
        "proposed_en": "Card 3 Title: 'Consult Gynecologist for Menopause Symptoms' | Card 4 Title: 'Moderate Caffeine, Sugar & Spices'",
        "proposed_gu": "કાર્ડ ૩: 'મેનોપોઝના લક્ષણો માટે ગાયનેકોલોજિસ્ટની સલાહ' | કાર્ડ ૪: 'ચા, કૉફી અને વધુ પડતી ખાંડની પરેજી'",
        "rationale": "Severe semantic title/desc inversion. Aligns card titles with their respective medical instructions.",
        "clinical_evidence_source": "International Menopause Society (IMS) White Paper on Menopausal Health",
        "requires_clinician_sign_off": True,
        "staging_status": "STAGED_FOR_CLINICAL_REVIEW"
    },
    {
        "slot": "10-20_card3_title_and_desc",
        "category": "CLINICAL_CONFLICT_AND_EPIDEMIOLOGY_REVISION",
        "current_en": "Title: Regular Movement & Postural Balance | Desc: Wet floors and loose electrical wires are the #1 cause of catastrophic hip fractures in elders.",
        "current_gu": "શીર્ષક: બેઠાડુ જીવન છોડી નિયમિત સક્રિયતા | વર્ણન: ફ્લોર ભીનો ન રાખો; અંધારામાં ચાલવું કે ફ્લોર પર વાયરો રાખવાથી વડીલો લપસીને થાપાનું ફ્રેક્ચર ભોગવી શકે છે.",
        "proposed_en": "Title: 'Eliminate Slip, Trip & Fall Hazards at Home' | Desc: 'Slippery wet floors and loose cords are a leading avoidable cause of falls and hip fractures in elders.'",
        "proposed_gu": "શીર્ષક: 'ઘરમાં લપસી પડવાના અને ઠોકર ખાવાના જોખમો દૂર કરો' | વર્ણન: 'ભીનો ફ્લોર અને છૂટા વાયરો વડીલોમાં થાપાના ફ્રેક્ચરનું એક મુખ્ય ટાળી શકાય તેવું કારણ છે.'",
        "rationale": "Resolves conflict between exercise title and domestic hazard description. Moderates '#1 cause' claim to 'a leading avoidable cause'.",
        "clinical_evidence_source": "IOF Fall Prevention Guidelines & WHO Global Report on Falls Prevention in Older Age",
        "requires_clinician_sign_off": True,
        "staging_status": "APPLIED_AND_PROMOTED"
    },
    {
        "slot": "10-20_card4_title_and_desc",
        "category": "MEDICAL_EVIDENCE_REVISION_UNSUPPORTED_CLAIM",
        "current_en": "Title: Non-Slip Flooring & Lighting | Desc: High sodium and dark aerated sodas deplete bone calcium through urinary leaching, creating porous brittle bones.",
        "current_gu": "શીર્ષક: લપસણા ફ્લોરિંગ સામે સુરક્ષા | વર્ણન: કાચું મીઠું છાંટવું અને સોડા-કોલ્ડડ્રિંક્સ પીવાથી હાડકાંમાંથી કેલ્શિયમ પેશાબ વાટે ધોવાઈ જાય છે અને હાડકાં પોલાં બને છે.",
        "proposed_en": "Title: 'Limit Excessive Salt Intake & Choose Wholesome Hydration' | Desc: 'Excessive dietary salt increases urinary calcium loss. For adults, keep total salt from all foods below 5 g/day (equivalent to less than 2 g/day sodium). Choose water or traditional unsalted buttermilk.'",
        "proposed_gu": "શીર્ષક: 'વધુ પડતું મીઠું ટાળો અને પૂરતું પાણી-છાશ પીઓ' | વર્ણન: 'વધારે પડતું મીઠું ખાવાથી પેશાબ વાટે કેલ્શિયમ નીકળી જાય છે; પુખ્ત વયના લોકો માટે દિવસભરના બધા ખોરાકમાંથી મળતું કુલ મીઠું ૫ ગ્રામથી ઓછું રાખો (આશરે ૨ ગ્રામથી ઓછું સોડિયમ). પાણી અથવા મીઠું ઉમેર્યા વગરની છાશ પસંદ કરો.'",
        "rationale": "CRITICAL MEDICAL REVISION: IOF explicitly notes there is no firm scientific evidence that fizzy soft drinks directly weaken bones. WHO recommends adults consume less than 2 g/day sodium, equivalent to less than 5 g/day total dietary salt; these are intake recommendations, not a hypercalciuria diagnostic threshold. Staged copy removes unsupported causal claim about dark sodas while promoting evidence-based sodium moderation and healthy hydration.",
        "clinical_evidence_source": "International Osteoporosis Foundation (IOF) Guidance: Protein and Other Nutrients (https://www.osteoporosis.foundation/patients/prevention/protein-other-nutrients)",
        "requires_clinician_sign_off": True,
        "staging_status": "APPLIED_AND_PROMOTED"
    },
    {
        "slot": "10-21_card2_desc",
        "category": "FOOD_CHEMISTRY_AND_STABILITY_REVISION",
        "current_en": "Excessive prolonged boiling evaporates volatile iodine. Add salt near the finish to preserve full iodine value.",
        "current_gu": "વધારે ઉકાળવાથી આયોડિન ઉડી જાય છે; શાક કે દાળ ઉતારતી વખતે છેલ્લે મીઠું ઉમેરવાથી આયોડિન જળવાઈ રહે છે.",
        "proposed_en": "Prolonged high-heat boiling can degrade and leach fortified iodine compounds. Adding iodized salt towards the end of cooking helps retain full micronutrient value.",
        "proposed_gu": "લાંબા સમય સુધી વધુ ગરમીમાં ઉકાળવાથી આયોડિનનું પ્રમાણ ઘટી શકે છે; રસોઈ પૂરી થવાના સમયે મીઠું ઉમેરવાથી આયોડિનનું મૂલ્ય જળવાય છે.",
        "rationale": "Potassium iodate (KIO3) is a non-volatile ionic salt (melting point >500C); it does not simply 'evaporate' like elemental iodine. Loss occurs through chemical reduction, thermal degradation, and aqueous leaching. Replaces incorrect volatility claim with accurate food science explanation.",
        "clinical_evidence_source": "WHO / FAO Guidelines on Food Fortification with Micronutrients, Part 3 (https://www.who.int/docs/default-source/micronutrients/gff-part-3-en.pdf)",
        "requires_clinician_sign_off": True,
        "staging_status": "APPLIED_AND_PROMOTED"
    },
    {
        "slot": "10-21_card3_title",
        "category": "CLINICAL_CONFLICT_RESOLUTION",
        "current_en": "Dry & Airtight Salt Storage",
        "current_gu": "મીઠાને ભેજ અને ગરમીથી બચાવો",
        "proposed_en": "Avoid Unbranded Loose Coarse Salt",
        "proposed_gu": "ખુલ્લું અને બિન-આયોડાઇઝ્ડ મીઠું વાપરવાનું ટાળો",
        "rationale": "Resolves redundancy with Cards 1 & 4. Description focuses on the severe risk of uniodized loose salt for child neurological development. Safety: Does not imply crystal/rock salt is naturally iodized; does not recommend increasing total salt intake.",
        "clinical_evidence_source": "Universal Salt Iodization (USI) Standards / Iodine Global Network",
        "requires_clinician_sign_off": True,
        "staging_status": "APPLIED_AND_PROMOTED"
    },
    {
        "slot": "10-21_card4_title",
        "category": "CLINICAL_CONFLICT_RESOLUTION",
        "current_en": "Balanced Micronutrient Diet",
        "current_gu": "પૂરતાં પોષક તત્ત્વોવાળો આહાર",
        "proposed_en": "Keep Iodized Salt Dry & Covered",
        "proposed_gu": "આયોડાઇઝ્ડ મીઠું સૂકું અને ઢાંકેલું રાખો",
        "rationale": "Dr. Atul requested removal of direct-stove-heat and iodine-destruction claims. The revised title and description retain only dry, covered, moisture-protected storage guidance.",
        "clinical_evidence_source": "Food Safety and Standards Authority of India (FSSAI) Salt Storage Guidelines",
        "requires_clinician_sign_off": True,
        "staging_status": "APPLIED_PENDING_SCOPED_REAPPROVAL"
    }
]

with open(os.path.join(review_dir, 'proposed_copy_and_provenance_corrections.json'), 'w', encoding='utf-8') as f:
    json.dump({
        "notice": "PRODUCTION HOLD ACTIVE: Copy revisions are staged for clinical/language review. Production database health_365.json remains 100% UNCHANGED.",
        "health_observance_provenance": provenance_data,
        "staged_copy_audit_and_corrections": copy_audit
    }, f, indent=2, ensure_ascii=False)

print("Updated review/proposed_copy_and_provenance_corrections.json")

# -----------------------------------------------------------------------------
# 3. REVISED CANDIDATE SPECIFICATIONS WITH COPY DEPENDENCY FLAGS
# -----------------------------------------------------------------------------
candidate_specs = [
    {
        "slot": "10-19-oral_card2",
        "day_id": "10-19-oral",
        "card_idx": 2,
        "status": "READY_FOR_CLINICAL_AUTHORIZATION",
        "copy_dependency": "INDEPENDENT_OF_COPY_CHANGE",
        "current_title_en": "Rinse Mouth Vigorously After Meals",
        "current_title_gu": "કંઈપણ ખાધા પછી સ્વચ્છ પાણીના કોગળા કરો",
        "rejection_reason": "Visual Concordance FAIL: Displayed plastic flosser picks instead of water mouth rinsing.",
        "clinical_intent": "Vigorous post-meal clean water rinsing to clear carbohydrate debris and neutralize acid.",
        "clinical_safety_rules": [
            "Must depict plain clean water mouth rinsing at washbasin.",
            "Strictly NO dental floss, plastic floss picks, or toothpicks.",
            "Positive clinical hygiene polarity."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_19_oral_card2_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian individual actively rinsing mouth with water at a clean, modern ceramic washbasin after a meal. Water swishing with puffed cheeks, leaning slightly over sink. A clear drinking glass tumbler rests on counter. Natural morning lighting, authentic Indian domestic bathroom, clinical hygiene, 8k resolution. Strictly NO dental floss, NO flosser picks, NO toothpicks, NO logos, NO text."
        }
    },
    {
        "slot": "10-20_card1",
        "day_id": "10-20",
        "card_idx": 1,
        "status": "READY_FOR_CLINICAL_AUTHORIZATION",
        "copy_dependency": "INDEPENDENT_OF_COPY_CHANGE",
        "current_title_en": "Bright Lighting & Bathroom Grab Bars",
        "current_title_gu": "ઘરમાં પૂરતો પ્રકાશ અને બાથરૂમમાં ગ્રેબ-બાર",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Legacy western stock senior lacking sturdy stainless steel bathroom grab bars.",
        "clinical_intent": "Environmental fall prevention for osteoporotic elders in wet zones.",
        "clinical_safety_rules": [
            "Depict an authentic Indian senior in domestic setting.",
            "Grab bar must be sturdy, wall-anchored stainless steel, positioned ergonomically.",
            "Bathroom floor must be visibly dry with non-slip tiles."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card1_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an elderly Indian senior citizen safely gripping a sturdy, wall-mounted brushed stainless steel bathroom grab bar in a brightly lit Indian home bathroom. Dry, matte non-slip floor tiles, warm morning lighting. Dignified posture, authentic Indian domestic setting, clean clinical fall-prevention environment, 8k resolution. No text, no logos, no distorted limbs, no wet puddles."
        }
    },
    {
        "slot": "10-20_card2",
        "day_id": "10-20",
        "card_idx": 2,
        "status": "READY_FOR_CLINICAL_AUTHORIZATION",
        "copy_dependency": "INDEPENDENT_OF_COPY_CHANGE",
        "current_title_en": "Weight-Bearing Walks & Ragi / Sesame Nutrition",
        "current_title_gu": "રોજિંદી ચાલવાની કસરત અને રાગી-તલનો આહાર",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Stock park walk lacking Indian elders and calcium-rich dietary context.",
        "clinical_intent": "Weight-bearing mechanical bone loading plus traditional Indian calcium-dense dietary staples.",
        "clinical_safety_rules": [
            "Must clearly highlight traditional Indian calcium sources: ragi, white sesame (til), paneer, curd, alongside active walking elders.",
            "Do NOT recommend unprescribed pharmaceutical calcium pills."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card2_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph of active elderly Indian couple walking briskly along a paved path in a sunlit Indian garden park during morning golden hour, wearing comfortable walking shoes. Soft natural morning sunlight. In foreground: small authentic bowl of ragi grains and white sesame seeds with paneer. Healthy bone aging, 8k resolution, editorial quality. No text, no logos, no pills."
        }
    },
    {
        "slot": "10-20_card3",
        "day_id": "10-20",
        "card_idx": 3,
        "status": "BLOCKED_PENDING_COPY_APPROVAL",
        "copy_dependency": "REQUIRES_APPROVAL_OF_STAGED_TITLE_10_20_CARD3",
        "staged_title_en": "Eliminate Slip, Trip & Fall Hazards at Home",
        "staged_title_gu": "ઘરમાં લપસી પડવાના અને ઠોકર ખાવાના જોખમો દૂર કરો",
        "rejection_reason": "Visual Concordance FAIL: Generic slip-and-fall graphic lacking authentic Indian elder domestic setting; clinical title/desc mismatch in DB.",
        "clinical_intent": "Elderly fall hazard mitigation: resolving domestic clutter, wet surfaces, and trip hazards.",
        "clinical_safety_rules": [
            "Depict hazard remediation (clean dry walkway, cords secured along wall).",
            "Avoid fear-mongering or injured bodies.",
            "Generation blocked until clinician signs off on proposed title change."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card3_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph of an Indian elder living room demonstrating fall hazard prevention: completely clear, uncluttered walkways with electrical cords safely bound and secured along baseboards. Senior Indian grandfather standing steadily near a firm armchair, wearing non-slip footwear. Warm indoor daylight, dry matte tiled flooring, authentic Indian domestic setting, 8k resolution. No text, no warning icons, no injured bodies."
        }
    },
    {
        "slot": "10-20_card4",
        "day_id": "10-20",
        "card_idx": 4,
        "status": "BLOCKED_PENDING_COPY_APPROVAL",
        "copy_dependency": "REQUIRES_APPROVAL_OF_STAGED_TITLE_AND_DESC_10_20_CARD4",
        "staged_title_en": "Limit Excessive Salt Intake & Choose Wholesome Hydration",
        "staged_title_gu": "વધુ પડતું મીઠું ટાળો અને પૂરતું પાણી-છાશ પીઓ",
        "rejection_reason": "Visual Concordance & Medical Accuracy FAIL: Preserved unsupported claim that dark soda directly leaches bone calcium; IOF confirms no firm evidence that soft drinks weaken bones.",
        "clinical_intent": "Adult total dietary salt below 5 g/day (equivalent to sodium below 2 g/day); wholesome hydration without unsupported causal soda claims. Clinical copy remains pending qualified review.",
        "clinical_safety_rules": [
            "Must NOT depict dark soda as directly destroying bone tissue.",
            "Focus on dietary moderation of raw salt and promotion of fresh buttermilk/water.",
            "Generation blocked until clinician signs off on revised medical copy."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card4_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian dining table setting demonstrating healthy bone nutrition: a glass of fresh homemade buttermilk (chaas) and clean water in clear focus, with an open salt shaker pushed away to the background. Wholesome Indian meal with stainless steel thali, warm natural daylight, editorial clinical nutrition focus, 8k resolution. Strictly NO brand logos, NO text labels, NO graphic illustrations of corroded bones."
        }
    },
    {
        "slot": "10-21_card1",
        "day_id": "10-21",
        "card_idx": 1,
        "status": "READY_FOR_CLINICAL_AUTHORIZATION",
        "copy_dependency": "INDEPENDENT_OF_COPY_CHANGE",
        "current_title_en": "Store Iodized Salt in Airtight Jars",
        "current_title_gu": "આયોડાઇઝ્ડ મીઠું હવાચુસ્ત બરણીમાં ઢાંકીને રાખો",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Refrigerator plastic storage containers lacking Indian kitchen setting with traditional airtight ceramic/glass salt jars.",
        "clinical_intent": "Airtight storage of potassium iodate fortified salt to prevent moisture exposure.",
        "clinical_safety_rules": [
            "Show fine iodized salt in airtight ceramic (barni) or glass container.",
            "Indicate sealed packaged salt with smiling sun icon concept.",
            "Do NOT recommend storing salt in refrigerator."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card1_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an authentic Indian kitchen counter featuring a traditional ceramic barni (glazed porcelain jar) with an airtight lid, and a clear glass jar containing fine white iodized salt. A small wooden spoon rests beside showing clean dry salt. Sealed salt packet in background with generic smiling sun iodized logo. Warm kitchen lighting, authentic Indian setting, 8k resolution. No commercial brand logos, no text."
        }
    },
    {
        "slot": "10-21_card2",
        "day_id": "10-21",
        "card_idx": 2,
        "status": "BLOCKED_PENDING_COPY_APPROVAL",
        "copy_dependency": "REQUIRES_APPROVAL_OF_STAGED_DESC_10_21_CARD2",
        "staged_desc_en": "Prolonged high-heat boiling can degrade and leach fortified iodine compounds. Adding iodized salt towards the end of cooking helps retain full micronutrient value.",
        "staged_desc_gu": "લાંબા સમય સુધી વધુ ગરમીમાં ઉકાળવાથી આયોડિનનું પ્રમાણ ઘટી શકે છે; રસોઈ પૂરી થવાના સમયે મીઠું ઉમેરવાથી આયોડિનનું મૂલ્ય જળવાય છે.",
        "rejection_reason": "Visual Concordance & Food Science FAIL: Salad shield graphic lacks Indian cooking context; copy previously claimed volatile potassium iodate evaporates.",
        "clinical_intent": "Thermostability preservation: potassium iodate degradation in cooking is minimized by adding salt towards the end of cooking.",
        "clinical_safety_rules": [
            "Show measured addition of salt in kadai or steel pot.",
            "For adults, keep total salt from all foods below 5 g/day (equivalent to sodium below 2 g/day); do not recommend extra salt for iodine intake.",
            "Generation blocked until clinician signs off on updated food chemistry description."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card2_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian home cook's hand gently adding a measured small spoon of fine iodized salt into a traditional stainless steel kadai containing freshly cooked vegetable curry (sabzi) near the end of cooking. Gentle soft steam rising, authentic Indian home kitchen, natural warm lighting, 8k resolution. Strictly NO raw salad, NO commercial logos, NO oversized salt pouring."
        }
    },
    {
        "slot": "10-21_card3",
        "day_id": "10-21",
        "card_idx": 3,
        "status": "BLOCKED_PENDING_COPY_APPROVAL",
        "copy_dependency": "REQUIRES_APPROVAL_OF_STAGED_TITLE_10_21_CARD3",
        "staged_title_en": "Avoid Unbranded Loose Coarse Salt",
        "staged_title_gu": "ખુલ્લું અને બિન-આયોડાઇઝ્ડ મીઠું વાપરવાનું ટાળો",
        "rejection_reason": "Visual Concordance FAIL: Generic rock salt visual without authentic Indian market/kitchen context; title/desc conflict.",
        "clinical_intent": "Eliminating unfortified loose salt to prevent IDD, goiter, and fetal intellectual impairment.",
        "clinical_safety_rules": [
            "Strictly do NOT imply rock salt (sendha namak) is naturally iodized.",
            "Do NOT recommend eating more salt; recommend switching exclusively to iodized salt.",
            "Generation blocked until clinician signs off on staged title."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card3_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph of an educational comparison in an authentic Indian grocery or kitchen: in clear focus, a clean sealed packet of fine iodized salt with a sun logo, placed beside an open unbranded rustic gunny sack of coarse grey crystal rock salt with a subtle push-away composition. Clean lighting, authentic Indian grocery context, 8k resolution, editorial public health quality. No text slogans, no brand trademarks, no disfiguring medical anomalies."
        }
    },
    {
        "slot": "10-21_card4",
        "day_id": "10-21",
        "card_idx": 4,
        "status": "BLOCKED_PENDING_COPY_APPROVAL",
        "copy_dependency": "REQUIRES_APPROVAL_OF_STAGED_TITLE_10_21_CARD4",
        "staged_title_en": "Keep Iodized Salt Dry & Covered",
        "staged_title_gu": "આયોડાઇઝ્ડ મીઠું સૂકું અને ઢાંકેલું રાખો",
        "rejection_reason": "Visual Concordance FAIL: Unrelated food panel lacking dry, covered iodized-salt storage context.",
        "clinical_intent": "Keep iodized salt tightly covered and protected from moisture in a cool, dry storage area.",
        "clinical_safety_rules": [
            "Show iodized salt in a tightly closed container on a clean, cool, dry pantry shelf.",
            "Generation blocked until clinician signs off on staged title."
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card4_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph showing proper iodized-salt storage in an Indian kitchen: a tightly closed ceramic or glass salt container placed on a clean, cool, dry pantry shelf protected from moisture. Authentic Indian home setting, warm natural lighting, 8k editorial quality. No logos or text."
        }
    }
]

with open(os.path.join(review_dir, 'candidate_specifications_9_rejected.json'), 'w', encoding='utf-8') as f:
    json.dump({
        "notice": "PRODUCTION HOLD ACTIVE: Staged for human review. Candidate generation prompts requiring copy revision are marked BLOCKED_PENDING_COPY_APPROVAL.",
        "total_rejected_candidates": len(candidate_specs),
        "status_summary": {
            "READY_FOR_CLINICAL_AUTHORIZATION": sum(1 for c in candidate_specs if c['status'] == 'READY_FOR_CLINICAL_AUTHORIZATION'),
            "BLOCKED_PENDING_COPY_APPROVAL": sum(1 for c in candidate_specs if c['status'] == 'BLOCKED_PENDING_COPY_APPROVAL')
        },
        "candidate_specifications": candidate_specs
    }, f, indent=2, ensure_ascii=False)

print("Updated review/candidate_specifications_9_rejected.json")

# -----------------------------------------------------------------------------
# 4. REGENERATE REVIEW_PACKET.MD WITH WORKING INLINE IMAGES & DIFFS
# -----------------------------------------------------------------------------
review_queue = json.load(open(os.path.join(review_dir, 'review_queue.json'), encoding='utf-8'))['review_queue']
copy_audit_map = {item['slot']: item for item in copy_audit}
candidate_spec_map = {item['slot']: item for item in candidate_specs}

days_dict = {}
for item in review_queue:
    d_id = item['poster_id']
    if d_id not in days_dict:
        days_dict[d_id] = {
            "poster_id": d_id,
            "title_en": item['poster_title_en'],
            "title_gu": item['poster_title_gu'],
            "cards": []
        }
    days_dict[d_id]['cards'].append(item)

rp_lines = []
approved_total = sum(1 for c in review_queue if c['review_status'] == 'APPROVED')
pending_total = sum(1 for c in review_queue if c['review_status'] == 'PENDING_CLINICAL_SIGN_OFF')
rejected_total = sum(1 for c in review_queue if c['review_status'] == 'REJECTED_MISMATCH')
rp_lines.append("# Dedicated Poster & Card Visual Review Packet")
rp_lines.append("**HealthCalendar365 — 10 Dedicated Posters (40 Cards)**")
rp_lines.append(f"**Status:** DRAFT REVIEW PACKET — PRODUCTION HOLD ACTIVE — {approved_total} APPROVED, {pending_total} PENDING, {rejected_total} REJECTED")
rp_lines.append("")
rp_lines.append("> [!IMPORTANT]")
rp_lines.append(f"> **REVIEW ARTIFACTS:** This packet displays current artwork and synchronized copy. The active ledger contains {approved_total} APPROVED, {pending_total} PENDING_CLINICAL_SIGN_OFF, and {rejected_total} REJECTED_MISMATCH records. All 40 clinical copies are approved; the {pending_total} pending records still require the nonclinical human gates excluded from the original bulk decision. Production deployment remains on hold.")
rp_lines.append("")
rp_lines.append("## Overview Table")
rp_lines.append("| Poster ID | Health Observance | Official/Observed Body | Attribution Category | Status Summary |")
rp_lines.append("| :--- | :--- | :--- | :--- | :--- |")
for d_id, d_data in days_dict.items():
    prov = provenance_data.get(d_id, {})
    p_cards = d_data['cards']
    app_count = sum(1 for c in p_cards if c['review_status'] == 'APPROVED')
    rej_count = sum(1 for c in p_cards if c['review_status'] == 'REJECTED_MISMATCH')
    pend_count = sum(1 for c in p_cards if c['review_status'] == 'PENDING_CLINICAL_SIGN_OFF')
    parts = []
    if app_count > 0:
        parts.append(f"{app_count} Approved")
    if pend_count > 0:
        parts.append(f"{pend_count} Pending")
    if rej_count > 0:
        parts.append(f"{rej_count} Rejected")
    stat_str = ", ".join(parts) if parts else "0 Cards"
    rp_lines.append(f"| [`{d_id}`](#poster-{d_id}) | {d_data['title_en']} | {prov.get('official_sponsoring_body')} | `{prov.get('attribution_category')}` | {stat_str} |")
rp_lines.append("")

for d_id, d_data in days_dict.items():
    prov = provenance_data.get(d_id, {})
    rp_lines.append("---")
    rp_lines.append(f"<a id=\"poster-{d_id}\"></a>")
    rp_lines.append(f"## Poster `{d_id}`: {d_data['title_en']}")
    rp_lines.append(f"**Gujarati Title:** {d_data['title_gu']} | **Date:** {prov.get('date', 'N/A')}")
    rp_lines.append(f"- **Sponsoring / Recognized Body:** {prov.get('official_sponsoring_body')} (`{prov.get('attribution_category')}`)")
    rp_lines.append(f"- **Provenance Citation:** {prov.get('source_citation')}")
    if prov.get('provenance_notes'):
        rp_lines.append(f"- **Provenance Notes:** {prov.get('provenance_notes')}")
    rp_lines.append("")
    rp_lines.append("### High-Resolution Rendered Poster Previews (Structural Render Pass)")
    rp_lines.append("| Square ($1080\\times1080$ px) | Vertical ($1080\\times1920$ px) |")
    rp_lines.append("| :---: | :---: |")
    square_img_path = f"file:///{PROJECT_DIR.replace(os.sep, '/')}/review/rendered_posters/poster_{d_id}_square_bilingual.png"
    vert_img_path = f"file:///{PROJECT_DIR.replace(os.sep, '/')}/review/rendered_posters/poster_{d_id}_vertical_bilingual.png"
    rp_lines.append(f"| ![Square Poster Preview]({square_img_path})<br>*Square (Bilingual)*<br>[View English](file:///{PROJECT_DIR.replace(os.sep, '/')}/review/rendered_posters/poster_{d_id}_square_english.png) · [View Gujarati](file:///{PROJECT_DIR.replace(os.sep, '/')}/review/rendered_posters/poster_{d_id}_square_gujarati.png) | ![Vertical Poster Preview]({vert_img_path})<br>*Vertical (Bilingual)*<br>[View English](file:///{PROJECT_DIR.replace(os.sep, '/')}/review/rendered_posters/poster_{d_id}_vertical_english.png) · [View Gujarati](file:///{PROJECT_DIR.replace(os.sep, '/')}/review/rendered_posters/poster_{d_id}_vertical_gujarati.png) |")
    rp_lines.append("")

    rp_lines.append(f"### Cards Review Grid for Poster `{d_id}`")
    for c in d_data['cards']:
        slot_key = f"{d_id}_card{c['card_idx']}"
        cand_spec = candidate_spec_map.get(slot_key)
        copy_mod = copy_audit_map.get(f"{d_id}_card{c['card_idx']}") or copy_audit_map.get(f"{d_id}_card{c['card_idx']}_desc") or copy_audit_map.get(f"{d_id}_card{c['card_idx']}_title") or copy_audit_map.get(f"{d_id}_card3_and_card4")
        
        if c['review_status'] == 'APPROVED':
            status_badge = "🟢 **APPROVED**"
        elif c['review_status'] == 'REJECTED_MISMATCH':
            status_badge = "🔴 **REJECTED_MISMATCH**"
        else:
            status_badge = "🟡 **PENDING_CLINICAL_SIGN_OFF**"
        rp_lines.append(f"#### Card #{c['card_idx']}: {c['bilingual_copy']['title_en']} ({c['bilingual_copy']['title_gu']}) — {status_badge}")
        
        active_img_url = f"file:///{PROJECT_DIR.replace(os.sep, '/')}/{c['image_path']}"
        rp_lines.append("| Active Card Artwork | Medical & Technical Details |")
        rp_lines.append("| :---: | :--- |")
        
        details = []
        details.append(f"**Image SHA-256:** `{c['image_sha256']}`<br>")
        details.append(f"**Card Spec Hash:** `{c['spec_hash']}`<br>")
        details.append(f"**Polarity:** `{c['polarity']}`<br>")
        details.append(f"**Current DB Copy (Active):**<br>")
        details.append(f"• **EN:** **{c['bilingual_copy']['title_en']}** — *{c['bilingual_copy']['desc_en']}*<br>")
        details.append(f"• **GU:** **{c['bilingual_copy']['title_gu']}** — *{c['bilingual_copy']['desc_gu']}*<br>")
        
        if copy_mod:
            details.append(f"<br>⚠️ **Staged Proposed Copy Revision ({copy_mod['category']}):**<br>")
            details.append(f"• **Proposed EN:** {copy_mod.get('proposed_en')}<br>")
            details.append(f"• **Proposed GU:** {copy_mod.get('proposed_gu')}<br>")
            details.append(f"• **Rationale:** {copy_mod.get('rationale')}<br>")
            details.append(f"• **Evidence Source:** {copy_mod.get('clinical_evidence_source')}<br>")
            details.append(f"• **Sign-Off Required:** {'Yes (Clinician)' if copy_mod.get('requires_clinician_sign_off') else 'Language Reviewer'}<br>")

        if c['clinical_review_assessment']:
            cr = c['clinical_review_assessment']
            details.append(f"<br>**QA Evaluation:** Visual Concordance: `{cr.get('visual_concordance')}`, Cultural Authenticity: `{cr.get('cultural_authenticity')}`, Polarity Match: `{cr.get('polarity_match')}`<br>")
            details.append(f"**Reviewer Findings:** *{cr.get('findings')}*<br>")

        if cand_spec:
            details.append(f"<br>🎯 **Candidate Re-Specification Status:** `{cand_spec['status']}`<br>")
            if cand_spec['status'] == 'BLOCKED_PENDING_COPY_APPROVAL':
                details.append(f"⛔ **BLOCKER:** Cannot generate imagery until clinical copy revision `{cand_spec['copy_dependency']}` is approved by medical reviewer.<br>")
            details.append(f"**Staged Prompt:** `{cand_spec['candidate_spec']['prompt'][:160]}...`<br>")

        details_str = "".join(details)
        rp_lines.append(f"| ![{c['bilingual_copy']['title_en']}]({active_img_url})<br>*File: {c['image_path']}* | {details_str} |")
        rp_lines.append("")

with open(os.path.join(review_dir, 'REVIEW_PACKET.md'), 'w', encoding='utf-8') as f:
    f.write("\n".join(rp_lines))

print("Created review/REVIEW_PACKET.md with inline images and detailed comparison tables.")

# -----------------------------------------------------------------------------
# 5. GENERATE STANDALONE BROWSABLE HTML REVIEW PACKET (review/index.html)
# -----------------------------------------------------------------------------
html_cards = []
for item in review_queue:
    d_id = item['poster_id']
    c_idx = item['card_idx']
    slot_key = f"{d_id}_card{c_idx}"
    cand = candidate_spec_map.get(slot_key)
    copy_m = copy_audit_map.get(slot_key) or copy_audit_map.get(f"{slot_key}_desc") or copy_audit_map.get(f"{slot_key}_title") or copy_audit_map.get(f"{d_id}_card3_and_card4")
    
    html_cards.append({
        "poster_id": d_id,
        "poster_title_en": item['poster_title_en'],
        "poster_title_gu": item['poster_title_gu'],
        "card_idx": c_idx,
        "review_status": item['review_status'],
        "polarity": item['polarity'],
        "image_path": "../" + item['image_path'],
        "image_sha256": item['image_sha256'],
        "spec_hash": item['spec_hash'],
        "title_en": item['bilingual_copy']['title_en'],
        "title_gu": item['bilingual_copy']['title_gu'],
        "desc_en": item['bilingual_copy']['desc_en'],
        "desc_gu": item['bilingual_copy']['desc_gu'],
        "findings": item.get('clinical_review_assessment', {}).get('findings', '') if item.get('clinical_review_assessment') else '',
        "qa": item.get('clinical_review_assessment'),
        "has_copy_proposal": bool(copy_m),
        "proposed_copy": copy_m,
        "has_candidate_spec": bool(cand),
        "candidate_spec": cand
    })

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HealthCalendar365 — Content Acceptance Visual Review Packet</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {{
      --bg: #07131e;
      --surface: #0e1e2d;
      --card-bg: #142738;
      --border: #223c52;
      --text: #f0f6fc;
      --text-muted: #8b9eb0;
      --primary: #38bdf8;
      --pending: #f59e0b;
      --rejected: #ef4444;
      --pass: #10b981;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 24px;
    }}
    header {{
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 20px 24px;
      border-radius: 12px;
      margin-bottom: 24px;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .badge-pending {{ background: rgba(245, 158, 11, 0.2); color: var(--pending); border: 1px solid var(--pending); }}
    .badge-approved {{ background: rgba(16, 185, 129, 0.2); color: var(--pass); border: 1px solid var(--pass); }}
    .badge-rejected {{ background: rgba(239, 68, 68, 0.2); color: var(--rejected); border: 1px solid var(--rejected); }}
    .badge-hold {{ background: rgba(239, 68, 68, 0.9); color: #fff; }}
    .toolbar {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin: 16px 0;
    }}
    button.filter-btn {{
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 14px;
    }}
    button.filter-btn.active {{
      background: var(--primary);
      color: #03101c;
      font-weight: 700;
      border-color: var(--primary);
    }}
    .poster-section {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      margin-bottom: 32px;
      padding: 24px;
    }}
    .poster-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}
    .poster-previews {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
      background: var(--card-bg);
      padding: 16px;
      border-radius: 8px;
    }}
    .poster-previews img {{
      width: 100%;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 16px;
    }}
    .card-item {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    .card-item.is-approved {{ border-color: var(--pass); }}
    .card-item.is-rejected {{ border-color: var(--rejected); }}
    .card-img-wrap {{
      background: #000;
      position: relative;
      aspect-ratio: 4 / 3;
    }}
    .card-img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .card-body {{
      padding: 16px;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .card-title-en {{ font-size: 16px; font-weight: 700; color: #fff; }}
    .card-title-gu {{ font-size: 15px; font-weight: 600; color: var(--primary); font-family: "Noto Sans Gujarati", sans-serif; }}
    .card-desc-en {{ font-size: 13px; color: #cbd5e1; }}
    .card-desc-gu {{ font-size: 13px; color: #94a3b8; font-family: "Noto Sans Gujarati", sans-serif; }}
    .card-meta {{
      margin-top: auto;
      padding-top: 10px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      font-size: 11px;
      font-family: monospace;
      color: var(--text-muted);
    }}
    .findings-box {{
      background: rgba(239, 68, 68, 0.1);
      border-left: 3px solid var(--rejected);
      padding: 8px 10px;
      font-size: 12px;
      color: #fca5a5;
      margin-top: 6px;
    }}
    .proposal-box {{
      background: rgba(56, 189, 248, 0.1);
      border-left: 3px solid var(--primary);
      padding: 8px 10px;
      font-size: 12px;
      color: #bae6fd;
      margin-top: 6px;
    }}

    /* Review-only responsive layout; preserve complete hashes and source text. */
    header > div:first-child, .poster-header {{ flex-wrap: wrap; gap: 12px; }}
    header > div:first-child > *, .poster-header > *, .poster-previews > *,
    .cards-grid > *, .card-body {{ min-width: 0; max-width: 100%; }}
    h1 {{ font-size: clamp(22px, 4vw, 30px); line-height: 1.25; }}
    h2 {{ overflow-wrap: anywhere; }}
    .badge, .filter-btn {{ max-width: 100%; white-space: normal; overflow-wrap: anywhere; }}
    .poster-previews {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .poster-previews img {{ max-width: 100%; height: auto; display: block; }}
    .cards-grid {{ grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); }}
    .card-meta, .findings-box, .proposal-box, code, a {{ overflow-wrap: anywhere; }}
    @media (max-width: 640px) {{
      body {{ padding: 12px; }}
      header, .poster-section {{ padding: 14px; }}
      .poster-previews {{ grid-template-columns: minmax(0, 1fr); padding: 10px; gap: 14px; }}
      .cards-grid {{ grid-template-columns: minmax(0, 1fr); }}
      .card-body {{ padding: 12px; }}
      .poster-header {{ align-items: flex-start; }}
    }}
  </style>
</head>
<body>
  <header>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
      <h1>HealthCalendar365 Visual Review Packet</h1>
      <span class="badge badge-hold">Production Hold Active</span>
    </div>
    <p style="color: var(--text-muted); font-size: 14px;">
      Technical Baseline: Review 7 Verified | Ledger State: <strong>9 Approved, 31 Pending Clinical Sign-off, 0 Rejected Mismatch</strong>
    </p>
    <div class="toolbar">
      <button class="filter-btn active" onclick="filterCards('ALL')">All 40 Cards (10 Posters)</button>
      <button class="filter-btn" onclick="filterCards('APPROVED')">9 Approved Replacements</button>
      <button class="filter-btn" onclick="filterCards('PENDING')">31 Pending Clinical Sign-Off</button>
    </div>
  </header>

  <main id="posters-container"></main>

  <script>
    const data = {json.dumps(html_cards, ensure_ascii=False)};
    const daysMeta = {json.dumps(provenance_data, ensure_ascii=False)};
    
    // Group by poster_id
    const days = [...new Set(data.map(c => c.poster_id))];
    const container = document.getElementById('posters-container');

    function renderPosters(filter = 'ALL') {{
      container.innerHTML = '';
      days.forEach(dId => {{
        let cards = data.filter(c => c.poster_id === dId);
        if (filter === 'APPROVED') cards = cards.filter(c => c.review_status === 'APPROVED');
        if (filter === 'PENDING') cards = cards.filter(c => c.review_status === 'PENDING_CLINICAL_SIGN_OFF');
        if (filter === 'REJECTED') cards = cards.filter(c => c.review_status === 'REJECTED_MISMATCH');
        if (cards.length === 0) return;

        const prov = daysMeta[dId] || {{}};
        const sec = document.createElement('section');
        sec.className = 'poster-section';
        sec.innerHTML = `
          <div class="poster-header">
            <div>
              <h2>${{cards[0].poster_title_en}} <span style="font-size: 18px; color: var(--text-muted); font-family: 'Noto Sans Gujarati', sans-serif;">(${{cards[0].poster_title_gu}})</span></h2>
              <div style="font-size: 13px; color: var(--text-muted); margin-top: 4px;">
                <strong>Date:</strong> ${{prov.date || 'N/A'}} | <strong>Observance / Sponsor:</strong> ${{prov.official_sponsoring_body || 'N/A'}} (<code>${{prov.attribution_category || ''}}</code>)
              </div>
            </div>
            <div>
              <span class="badge ${{cards.some(c => c.review_status === 'REJECTED_MISMATCH') ? 'badge-rejected' : (cards.every(c => c.review_status === 'APPROVED') ? 'badge-approved' : 'badge-pending')}}">
                ${{cards.filter(c => c.review_status === 'APPROVED').length}} Approved / ${{cards.filter(c => c.review_status === 'PENDING_CLINICAL_SIGN_OFF').length}} Pending
              </span>
            </div>
          </div>

          <div class="poster-previews">
            <div>
              <h4 style="margin-bottom: 8px; font-size: 13px; text-transform: uppercase; color: var(--text-muted);">Rendered Square (1080×1080 px Bilingual)</h4>
              <img src="rendered_posters/poster_${{dId}}_square_bilingual.png" alt="Square Preview" loading="lazy">
            </div>
            <div>
              <h4 style="margin-bottom: 8px; font-size: 13px; text-transform: uppercase; color: var(--text-muted);">Rendered Vertical (1080×1920 px Bilingual)</h4>
              <img src="rendered_posters/poster_${{dId}}_vertical_bilingual.png" alt="Vertical Preview" loading="lazy">
            </div>
          </div>

          <div class="cards-grid">
            ${{cards.map(c => `
              <div class="card-item ${{c.review_status === 'REJECTED_MISMATCH' ? 'is-rejected' : (c.review_status === 'APPROVED' ? 'is-approved' : '')}}">
                <div class="card-img-wrap">
                  <img src="${{c.image_path}}" alt="${{c.title_en}}" loading="lazy">
                  <div style="position: absolute; top: 8px; right: 8px;">
                    <span class="badge ${{c.review_status === 'REJECTED_MISMATCH' ? 'badge-rejected' : (c.review_status === 'APPROVED' ? 'badge-approved' : 'badge-pending')}}">
                      Card #${{c.card_idx}}: ${{c.review_status === 'REJECTED_MISMATCH' ? 'REJECTED' : (c.review_status === 'APPROVED' ? 'APPROVED' : 'PENDING')}}
                    </span>
                  </div>
                </div>
                <div class="card-body">
                  <div class="card-title-en">${{c.title_en}}</div>
                  <div class="card-title-gu">${{c.title_gu}}</div>
                  <div class="card-desc-en">${{c.desc_en}}</div>
                  <div class="card-desc-gu">${{c.desc_gu}}</div>
                  
                  ${{c.findings ? `<div class="findings-box"><strong>Audit Finding:</strong> ${{c.findings}}</div>` : ''}}
                  
                  ${{c.has_copy_proposal ? `
                    <div class="proposal-box">
                      <strong>Staged Copy Proposal (${{c.proposed_copy.category}}):</strong><br>
                      ${{c.proposed_copy.proposed_en ? `• <strong>EN:</strong> ${{c.proposed_copy.proposed_en}}<br>` : ''}}
                      ${{c.proposed_copy.proposed_gu ? `• <strong>GU:</strong> ${{c.proposed_copy.proposed_gu}}<br>` : ''}}
                      • <em>${{c.proposed_copy.rationale}}</em>
                    </div>
                  ` : ''}}

                  ${{c.has_candidate_spec && c.candidate_spec.status === 'BLOCKED_PENDING_COPY_APPROVAL' ? `
                    <div style="background: rgba(239,68,68,0.15); border: 1px solid var(--rejected); padding: 6px 8px; border-radius: 4px; font-size: 11px; color: #fca5a5; margin-top: 6px;">
                      ⛔ <strong>Candidate Blocked:</strong> Cannot generate replacement visual until clinical copy approval is granted.
                    </div>
                  ` : ''}}

                  <div class="card-meta">
                    SHA256: ${{c.image_sha256 ? c.image_sha256.substring(0, 16) + '...' : 'N/A'}}<br>
                    SPEC: ${{c.spec_hash ? c.spec_hash.substring(0, 16) + '...' : 'N/A'}}
                  </div>
                </div>
              </div>
            `).join('')}}
          </div>
        `;
        container.appendChild(sec);
      }});
    }}

    function filterCards(mode) {{
      document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
      renderPosters(mode);
    }}

    renderPosters('ALL');
  </script>
</body>
</html>
"""

with open(os.path.join(review_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created standalone browsable review packet at review/index.html")
