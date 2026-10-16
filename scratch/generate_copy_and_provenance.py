import json
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

provenance_data = {
    "10-15": {
        "observance_name_en": "Global Handwashing Day",
        "observance_name_gu": "વિશ્વ હાથ ધોવા દિવસ",
        "date": "October 15",
        "official_sponsoring_body": "Global Handwashing Partnership (GHP)",
        "international_status": "Officially designated global health advocacy day",
        "website": "https://globalhandwashing.org/global-handwashing-day/",
        "attribution_type": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "Global Handwashing Partnership (GHP)"
    },
    "10-15-cane": {
        "observance_name_en": "World White Cane Day / White Cane Safety Day",
        "observance_name_gu": "વિશ્વ સફેદ લાકડી દિવસ (પ્રજ્ઞાચક્ષુ સન્માન)",
        "date": "October 15",
        "official_sponsoring_body": "World Blind Union (WBU) / National Federation of the Blind (NFB)",
        "international_status": "Officially established (1964) international awareness day",
        "website": "https://worldblindunion.org/",
        "attribution_type": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "World Blind Union (WBU)"
    },
    "10-16": {
        "observance_name_en": "World Food Day",
        "observance_name_gu": "વિશ્વ ખાદ્ય દિવસ",
        "date": "October 16",
        "official_sponsoring_body": "Food and Agriculture Organization of the United Nations (FAO)",
        "international_status": "Official United Nations International Day (Resolution 34/83)",
        "website": "https://www.fao.org/world-food-day/en",
        "attribution_type": "OFFICIAL_UN_AGENCY_VERIFIED",
        "display_badge": "UN Food & Agriculture Organization (FAO)"
    },
    "10-16-spine": {
        "observance_name_en": "World Spine Day",
        "observance_name_gu": "વિશ્વ કરોડરજ્જુ દિવસ",
        "date": "October 16",
        "official_sponsoring_body": "World Federation of Chiropractic (WFC) / Global Alliance for Musculoskeletal Health",
        "international_status": "Official global health campaign under Bone and Joint Decade",
        "website": "http://www.worldspineday.org/",
        "attribution_type": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "World Spine Day (WFC)"
    },
    "10-17": {
        "observance_name_en": "World Trauma Day (World Trauma Prevention Day)",
        "observance_name_gu": "વિશ્વ ટ્રોમા નિવારણ દિવસ",
        "date": "October 17",
        "official_sponsoring_body": "Initiated 2011 in India (Trauma Association of India / KEM Hospital Mumbai)",
        "international_status": "Grassroots Indian & international clinical awareness initiative (NOT an official UN/WHO day)",
        "website": "http://www.trauma.org.in/",
        "attribution_type": "ORGANIZATION_NEUTRAL_DAILY_GUIDANCE",
        "display_badge": "Emergency Trauma Prevention Initiative",
        "notes": "Verified: Not a WHO/UN mandated day. Must NOT display WHO official logo; use organization-neutral trauma care guidance badge."
    },
    "10-18": {
        "observance_name_en": "World Menopause Day",
        "observance_name_gu": "વિશ્વ મેનોપોઝ દિવસ",
        "date": "October 18",
        "official_sponsoring_body": "International Menopause Society (IMS) in collaboration with WHO",
        "international_status": "Officially designated global awareness day",
        "website": "https://www.imsociety.org/",
        "attribution_type": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "International Menopause Society (IMS)"
    },
    "10-19": {
        "observance_name_en": "Ear & Hearing Health",
        "observance_name_gu": "કાન અને શ્રવણ સ્વાસ્થ્ય",
        "date": "October 19",
        "official_sponsoring_body": "None (Daily Health Guidance)",
        "international_status": "Daily clinical guidance card (World Hearing Day is observed March 3)",
        "website": None,
        "attribution_type": "ORGANIZATION_NEUTRAL_DAILY_GUIDANCE",
        "display_badge": "Daily Health Guidance",
        "notes": "Organization-neutral daily clinical guidance."
    },
    "10-19-oral": {
        "observance_name_en": "Oral Health & Tobacco-Free Life",
        "observance_name_gu": "મુખનું આરોગ્ય અને તમાકુ મુક્તિ",
        "date": "October 19",
        "official_sponsoring_body": "None (Daily Health Guidance)",
        "international_status": "Daily clinical guidance card (World Oral Health Day is observed March 20)",
        "website": None,
        "attribution_type": "ORGANIZATION_NEUTRAL_DAILY_GUIDANCE",
        "display_badge": "Daily Health Guidance",
        "notes": "Organization-neutral daily clinical guidance."
    },
    "10-20": {
        "observance_name_en": "World Osteoporosis Day",
        "observance_name_gu": "વિશ્વ ઓસ્ટીયોપોરોસીસ દિવસ",
        "date": "October 20",
        "official_sponsoring_body": "International Osteoporosis Foundation (IOF)",
        "international_status": "Official global health campaign",
        "website": "https://www.osteoporosis.foundation/",
        "attribution_type": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "International Osteoporosis Foundation (IOF)"
    },
    "10-21": {
        "observance_name_en": "Global Iodine Deficiency Disorders Prevention Day",
        "observance_name_gu": "વિશ્વ આયોડિન અલ્પતા નિવારણ દિવસ",
        "date": "October 21",
        "official_sponsoring_body": "Iodine Global Network (IGN) / WHO / UNICEF",
        "international_status": "Official international public health day",
        "website": "https://www.ign.org/",
        "attribution_type": "OFFICIAL_SPONSOR_VERIFIED",
        "display_badge": "Iodine Global Network (IGN)"
    }
}

copy_audit = [
    {
        "slot": "10-15_day_title",
        "category": "EDITORIAL_CORRECTION",
        "current_en": "Global Handwashing Day",
        "current_gu": "વિશ્વ હાથ ધોવાના દિવસ (ગ્લોબલ હેન્ડવોશિંગ ડે)",
        "proposed_en": "Global Handwashing Day",
        "proposed_gu": "વિશ્વ હાથ ધોવા દિવસ (ગ્લોબલ હેન્ડવોશિંગ ડે)",
        "rationale": "Corrects Gujarati genitive grammar error ('ધોવાના' -> 'ધોવા'). Purely grammatical editorial correction.",
        "requires_clinician_sign_off": False
    },
    {
        "slot": "10-17_card3",
        "category": "EDITORIAL_CLARIFICATION",
        "current_en": "Controlled Speed & Helmet Discipline",
        "current_gu": "નિયંત્રિત ગતિ અને હેલ્મેટ શિસ્ત",
        "proposed_en": "Controlled Speed & Zero Phone Distraction",
        "proposed_gu": "નિયંત્રિત ગતિ અને ફોનથી સાવધાની",
        "rationale": "Card 1 already covers helmet discipline; Card 3 description covers mobile phones and speeding. Clarifies title to match body copy.",
        "requires_clinician_sign_off": False
    },
    {
        "slot": "10-18_card3_and_card4",
        "category": "CLINICAL_DECISION_REQUIRED",
        "current_en": "Card 3 Title: Bone Density & Joint Care (Desc: hot flashes & consulting gynecologist) | Card 4 Title: Qualified Gynecologist Consultation (Desc: diet & caffeine)",
        "current_gu": "કાર્ડ ૩: હાડકાંની મજબૂતી (વર્ણન: ગાયનેકોલોજિસ્ટની સલાહ) | કાર્ડ ૪: ગાયનેકોલોજિસ્ટની સલાહ (વર્ણન: ચા-કૉફીથી પરેજી)",
        "proposed_en": "Card 3 Title: 'Consult Gynecologist for Menopause Symptoms' | Card 4 Title: 'Moderate Caffeine, Sugar & Spices'",
        "proposed_gu": "કાર્ડ ૩: 'મેનોપોઝના લક્ષણો માટે ગાયનેકોલોજિસ્ટની સલાહ' | કાર્ડ ૪: 'ચા, કૉફી અને વધુ પડતી ખાંડની પરેજી'",
        "rationale": "Severe title/desc semantic inversion. Aligns card titles with their respective medical advice.",
        "requires_clinician_sign_off": True,
        "staging_status": "STAGED_FOR_CLINICAL_REVIEW"
    },
    {
        "slot": "10-20_card3",
        "category": "CLINICAL_DECISION_REQUIRED",
        "current_en": "Regular Movement & Postural Balance",
        "current_gu": "બેઠાડુ જીવન છોડી નિયમિત સક્રિયતા",
        "proposed_en": "Eliminate Slip, Trip & Fall Hazards at Home",
        "proposed_gu": "ઘરમાં લપસી પડવાના અને ઠોકર ખાવાના જોખમો દૂર કરો",
        "rationale": "Title is about exercise/movement, but description is about wet floors, dark pathways, and loose wires causing hip fractures. Staged title precisely aligns with fall prevention instruction.",
        "requires_clinician_sign_off": True,
        "staging_status": "STAGED_FOR_CLINICAL_REVIEW"
    },
    {
        "slot": "10-20_card4",
        "category": "CLINICAL_DECISION_REQUIRED",
        "current_en": "Non-Slip Flooring & Lighting",
        "current_gu": "લપસણા ફ્લોરિંગ સામે સુરક્ષા",
        "proposed_en": "Limit Bone-Depleting Excess Salt & Dark Sodas",
        "proposed_gu": "હાડકાં નબળાં પાડતાં વધુ પડતું મીઠું અને સોડા ટાળો",
        "rationale": "Title is about flooring/lighting (redundant with Card 1 and Card 3), but description is about excessive dietary sodium and phosphoric dark sodas leaching bone calcium. Staged title reflects bone nutrition instruction.",
        "requires_clinician_sign_off": True,
        "staging_status": "STAGED_FOR_CLINICAL_REVIEW"
    },
    {
        "slot": "10-21_card3",
        "category": "CLINICAL_DECISION_REQUIRED",
        "current_en": "Dry & Airtight Salt Storage",
        "current_gu": "મીઠાને ભેજ અને ગરમીથી બચાવો",
        "proposed_en": "Avoid Unbranded Loose Coarse Salt",
        "proposed_gu": "ખુલ્લું અને બિન-આયોડાઇઝ્ડ મીઠું વાપરવાનું ટાળો",
        "rationale": "Title is about storage (redundant with Card 1 & 4), but description warns that unbranded loose coarse salt lacks iodine and causes developmental impairment. Staged title directly targets unfortified loose salt risk.",
        "requires_clinician_sign_off": True,
        "staging_status": "STAGED_FOR_CLINICAL_REVIEW"
    },
    {
        "slot": "10-21_card4",
        "category": "CLINICAL_DECISION_REQUIRED",
        "current_en": "Balanced Micronutrient Diet",
        "current_gu": "પૂરતાં પોષક તત્ત્વોવાળો આહાર",
        "proposed_en": "Protect Salt from Direct Stove Heat & Moisture",
        "proposed_gu": "મીઠાની બરણી ગેસની જ્વાળા અને ભેજથી દૂર રાખો",
        "rationale": "Title is generic 'balanced micronutrient diet', but description specifically warns against stove burner heat and open containers degrading volatile potassium iodate. Staged title reflects thermal and humidity preservation of iodine.",
        "requires_clinician_sign_off": True,
        "staging_status": "STAGED_FOR_CLINICAL_REVIEW"
    }
]

out_path = os.path.join(PROJECT_DIR, 'review', 'proposed_copy_and_provenance_corrections.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({
        "production_hold_notice": "PRODUCTION HOLD ACTIVE: Copy changes are staged for review and have NOT been applied to production datasets. Real datasets remain unchanged.",
        "health_observance_provenance": provenance_data,
        "staged_copy_audit_and_corrections": copy_audit
    }, f, indent=2, ensure_ascii=False)

print(f"Generated {out_path} with {len(provenance_data)} days provenance and {len(copy_audit)} copy audit items.")
