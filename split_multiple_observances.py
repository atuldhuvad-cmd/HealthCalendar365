"""
Split Multiple Observances Across 365-Day Health Calendar
Ensures dates with multiple observances produce independent dedicated posters
instead of merged/Frankenstein posters.
"""

import json
import os
import shutil

PROJECT_DIR = r"D:\HealthCalendar365"
JSON_PATH = os.path.join(PROJECT_DIR, "data", "health_365.json")
JS_PATH = os.path.join(PROJECT_DIR, "js", "calendar-data.js")
PHOTOS_DIR = os.path.join(PROJECT_DIR, "photos")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    cal = json.load(f)

# Define dedicated posters for days that had merged observances
# 1. October 15: Global Handwashing Day (Already updated!) + World White Cane Day (New Poster B)
white_cane_day = {
    "id": "10-15-cane",
    "month": 10,
    "day": 15,
    "date_en": "October 15",
    "date_gu": "૧૫ ઓક્ટોબર",
    "tier": 2,
    "tier_en": "Global Inclusion & Health Observance",
    "tier_gu": "વિશ્વ દ્રષ્ટિ સુરક્ષા અને સમાવેશી આરોગ્ય દિવસ",
    "title_en": "World White Cane Day",
    "title_gu": "વિશ્વ સફેદ લાકડી દિવસ (પ્રજ્ઞાચક્ષુ સન્માન)",
    "theme_en": "Dignity, Accessible Pathways & Blindness Prevention",
    "theme_gu": "પ્રજ્ઞાચક્ષુઓનું સન્માન, સુરક્ષિત રસ્તા અને અંધત્વ નિવારણ",
    "cards": [
        {
            "type": "message",
            "index": 1,
            "badge_en": "Action #1",
            "badge_gu": "માર્ગદર્શન #૧",
            "title_en": "Annual Comprehensive Eye Examination",
            "title_gu": "વર્ષે એક વાર સંપૂર્ણ આંખની તપાસ કરાવો",
            "desc_en": "Regular dilated eye exams detect glaucoma, cataracts, and diabetic retinopathy early before permanent sight loss.",
            "desc_gu": "ગ્લુકોમા, મોતિયો અને ડાયાબિટીક રેટીનોપથીની વહેલી ખબર પડે તે માટે વર્ષે એક વાર નેત્ર નિષ્ણાત પાસે આંખની તપાસ કરાવો.",
            "photo": "photos/oct15_cane_card1.png",
            "ai_prompt": "Ultra-photorealistic 4:3 photograph of an Indian ophthalmologist carefully examining an Indian patient's eyes using a modern slit lamp biomicroscope in a well-lit clinic, 8k."
        },
        {
            "type": "message",
            "index": 2,
            "badge_en": "Action #2",
            "badge_gu": "માર્ગદર્શન #૨",
            "title_en": "Respect White Cane & Clear Walkways",
            "title_gu": "સફેદ લાકડીનું સન્માન અને ખુલ્લા રસ્તા",
            "desc_en": "White cane is a symbol of independence. Never park or leave obstacles on yellow tactile paving or footpaths.",
            "desc_gu": "સફેદ લાકડી પ્રજ્ઞાચક્ષુઓની આત્મનિર્ભરતાનું પ્રતીક છે. ફૂટપાથ અને પીળા ટેક્ટાઈલ રસ્તાઓ પર વાહન કે સામાન મૂકશો નહીં.",
            "photo": "photos/oct15_cane_card2.png",
            "ai_prompt": "Ultra-photorealistic 4:3 shot of an Indian person walking with confidence using a white cane along clean yellow textured tactile pavement, morning sunlight, 8k."
        },
        {
            "type": "message",
            "index": 3,
            "badge_en": "Action #3",
            "badge_gu": "માર્ગદર્શન #૩",
            "title_en": "Assist Pedestrians Respectfully",
            "title_gu": "રસ્તો ઓળંગવામાં સન્માનપૂર્વક મદદ કરો",
            "desc_en": "Offer verbal assistance before helping. Let them hold your elbow rather than pulling their arm or cane.",
            "desc_gu": "પ્રજ્ઞાચક્ષુ વ્યક્તિને રસ્તો ઓળંગાવતા પહેલાં પૂછો. હાથ ખેંચવાને બદલે તેમને તમારી કોણી પકડવા દો.",
            "photo": "photos/oct15_cane_card3.png",
            "ai_prompt": "Ultra-photorealistic 4:3 compassionate photograph of an Indian pedestrian guiding a visually impaired person crossing an Indian street zebra crossing respectfully, 8k."
        },
        {
            "type": "message",
            "index": 4,
            "badge_en": "Action #4",
            "badge_gu": "માર્ગદર્શન #૪",
            "title_en": "Protect Eyes from Hazards & Never Rub",
            "title_gu": "આંખને ઈજા અને ધૂળથી બચાવો",
            "desc_en": "Wear protective glasses during outdoor work or dust. Never rub irritated eyes or self-medicate with steroid drops.",
            "desc_gu": "ધૂળ કે કેમિકલવાળા કામ વખતે રક્ષણાત્મક ચશ્મા પહેરો. આંખમાં કચરો પડે ત્યારે ઘસવાને બદલે સ્વચ્છ પાણીથી ધોવો.",
            "photo": "photos/oct15_cane_card4.png",
            "ai_prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian person wearing safety eye protection glasses outdoors, clean healthy eye closeup, clinical safety, 8k."
        }
    ]
}

# 2. October 16: Separate into World Food Day AND World Spine Day
world_food_day = {
    "id": "10-16",
    "month": 10,
    "day": 16,
    "date_en": "October 16",
    "date_gu": "૧૬ ઓક્ટોબર",
    "tier": 1,
    "tier_en": "WHO / FAO Global Health Day",
    "tier_gu": "વિશ્વ આરોગ્ય સંસ્થા (WHO / FAO) દિવસ",
    "title_en": "World Food Day",
    "title_gu": "વિશ્વ ખાદ્ય દિવસ (પૌષ્ટિક આહાર સંકલ્પ)",
    "theme_en": "Traditional Balanced Thali, Millets & Zero Food Waste",
    "theme_gu": "સંતુલિત દેશી થાળી, પૌષ્ટિક ધાન્ય અને અન્નનો સદુપયોગ",
    "cards": [
        {
            "type": "message",
            "index": 1,
            "badge_en": "Action #1",
            "badge_gu": "માર્ગદર્શન #૧",
            "title_en": "Eat Balanced Desi Thali Daily",
            "title_gu": "રોજ સંતુલિત દેશી થાળી આરોગો",
            "desc_en": "Fill 50% plate with vegetables and fresh salad, 25% plant protein (dal, paneer, sprouts), and 25% whole grains.",
            "desc_gu": "થાળીમાં ૫૦% શાકભાજી-સલાડ, ૨૫% પ્રોટીન (કઠોળ, દાળ, દહીં) અને ૨૫% બાજરી-જુવાર જેવા પોષક ધાન્ય રાખો.",
            "photo": "photos/oct16_food_card1.png",
            "ai_prompt": "Ultra-photorealistic 4:3 authentic Indian bronze thali with vibrant bowls of yellow dal, palak paneer, fresh dahi, sprouted pulses, bajra rotis, brass tableware, warm home lighting, 8k."
        },
        {
            "type": "message",
            "index": 2,
            "badge_en": "Action #2",
            "badge_gu": "માર્ગદર્શન #૨",
            "title_en": "Embrace Traditional Millets (Shree Anna)",
            "title_gu": "શ્રી અન્ન: બાજરી, જુવાર અને રાગીનો ઉપયોગ",
            "desc_en": "Replace polished white rice and refined flour with high-fiber millets for sustained energy and gut microbiome health.",
            "desc_gu": "મેંદો અને પોલિશ્ડ ચોખા ઘટાડી ફાઈબરથી ભરપૂર બાજરી, જુવાર અને રાગી ખાવાની આદત પાડો; પાચન અને ડાયાબિટીસમાં લાભદાયક.",
            "photo": "photos/oct16_food_card2.png",
            "ai_prompt": "Ultra-photorealistic 4:3 rustic Indian kitchen tabletop displaying earthen bowls filled with raw bajra, jowar, and ragi grains, garnished with fresh curry leaves, 8k."
        },
        {
            "type": "message",
            "index": 3,
            "badge_en": "Action #3",
            "badge_gu": "માર્ગદર્શન #૩",
            "title_en": "Limit Re-Heated Fried Foods & Colas",
            "title_gu": "વારંવાર તળેલા ફાસ્ટફૂડ અને સોડાથી દૂર રહો",
            "desc_en": "Avoid repeated consumption of re-heated trans-fat fried street snacks, ultra-processed junk, and high-fructose sodas.",
            "desc_gu": "વારંવાર ઉકાળેલા તેલના સમોસા-ભજિયાં, પ્રોસેસ્ડ નાસ્તા અને ખાંડવાળા સોડા-કોલ્ડડ્રિંક્સ હૃદય અને લીવરને નુકસાન કરે છે.",
            "photo": "photos/oct16_food_card3.png",
            "ai_prompt": "Ultra-photorealistic 4:3 still life of oily deep-fried samosas and a fizzy cola glass beside fresh green apples, dramatic educational lighting, 8k."
        },
        {
            "type": "message",
            "index": 4,
            "badge_en": "Action #4",
            "badge_gu": "માર્ગદર્શન #૪",
            "title_en": "Safe Food Hygiene & Zero Waste",
            "title_gu": "ખોરાકની શુદ્ધતા અને અન્નનો બગાડ અટકાવો",
            "desc_en": "Wash raw produce thoroughly under clean water. Cook freshly, store covered, and practice zero food waste.",
            "desc_gu": "શાકભાજી-ફળોને સ્વચ્છ વહેતા પાણીથી ધોવો. તાજો રાંધેલો ખોરાક ઢાંકીને રાખો અને અન્નનો બગાડ ક્યારેય ન કરો.",
            "photo": "photos/oct16_food_card4.png",
            "ai_prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian mother gently washing fresh tomatoes and leafy spinach in a colander under clean flowing tap water, 8k."
        }
    ]
}

world_spine_day = {
    "id": "10-16-spine",
    "month": 10,
    "day": 16,
    "date_en": "October 16",
    "date_gu": "૧૬ ઓક્ટોબર",
    "tier": 1,
    "tier_en": "Global Orthopaedic & Spine Observance",
    "tier_gu": "વિશ્વ કરોડરજ્જુ આરોગ્ય દિવસ",
    "title_en": "World Spine Day",
    "title_gu": "વિશ્વ કરોડરજ્જુ દિવસ (પીઠની સંભાળ)",
    "theme_en": "Straight Spine, Core Strength & Active Movement",
    "theme_gu": "કરોડરજ્જુનું સાચું પોશ્ચર, કસરત અને પીઠના દુખાવાથી મુક્તિ",
    "cards": [
        {
            "type": "message",
            "index": 1,
            "badge_en": "Action #1",
            "badge_gu": "માર્ગદર્શન #૧",
            "title_en": "Erect Spine & Lumbar Support",
            "title_gu": "બેસતી-ચાલતી વખતે કરોડરજ્જુ સીધી રાખો",
            "desc_en": "Keep monitor at eye level, sit with feet flat and lower back firmly supported. Avoid slumping on soft sofas.",
            "desc_gu": "કમ્પ્યુટર વાપરતી વખતે સ્ક્રીન આંખની સામે રાખો, કમર પાછળ ટેકો રાખો અને ઢીલા સોફામાં લાંબો સમય ઝૂકીને બેસશો નહીં.",
            "photo": "photos/oct16_spine_card1.png",
            "ai_prompt": "Ultra-photorealistic 4:3 photograph of an Indian professional sitting with perfect spine ergonomics in a modern ergonomic office chair, monitor at eye level, 8k."
        },
        {
            "type": "message",
            "index": 2,
            "badge_en": "Action #2",
            "badge_gu": "માર્ગદર્શન #૨",
            "title_en": "Take 2-Minute Movement Breaks Hourly",
            "title_gu": "દર કલાકે ૨ મિનિટ ઊભા થઈ સ્ટ્રેચિંગ કરો",
            "desc_en": "Prolonged sitting compresses intervertebral discs. Stand, stretch backwards, and walk 50 steps every 60 minutes.",
            "desc_gu": "સતત બેસી રહેવાથી મણકા પર દબાણ વધે છે; દર કલાકે ઊભા થઈ હળવું સ્ટ્રેચિંગ અને થોડું ચાલવાની ટેવ પાડો.",
            "photo": "photos/oct16_spine_card2.png",
            "ai_prompt": "Ultra-photorealistic 4:3 photograph of an Indian man standing beside a work desk smiling while doing gentle overhead spine extension stretches, warm sunlight, 8k."
        },
        {
            "type": "message",
            "index": 3,
            "badge_en": "Action #3",
            "badge_gu": "માર્ગદર્શન #૩",
            "title_en": "Bend Knees When Lifting Heavy Loads",
            "title_gu": "વજન ઊંચકતી વખતે ઘૂંટણ વાળીને બેસો",
            "desc_en": "Never bend at the waist with straight legs. Keep the load close to your chest and use strong leg muscles.",
            "desc_gu": "વાંકા વળીને ક્યારેય ભારે વજન ન ઊંચકો; ઘૂંટણ વાળીને બેસો અને સાથળના સ્નાયુઓનો ઉપયોગ કરીને વજન ઊંચકો.",
            "photo": "photos/oct16_spine_card3.png",
            "ai_prompt": "Ultra-photorealistic 4:3 instructional photo of an Indian person correctly squatting with bent knees and straight back to lift a heavy parcel safely, 8k."
        },
        {
            "type": "message",
            "index": 4,
            "badge_en": "Action #4",
            "badge_gu": "માર્ગદર્શન #૪",
            "title_en": "Avoid 60° Mobile Text-Neck Slouch",
            "title_gu": "મોબાઈલ જોતી વખતે ગરદન વાંકી ન વાળો",
            "desc_en": "Severe forward neck flexion significantly increases mechanical load on cervical vertebrae. Hold devices closer to eye level and change posture frequently.",
            "desc_gu": "ડોક વધારે પડતી નીચી નમાવવાથી સર્વાઇકલ મણકા પર ભારે દબાણ આવે છે; ફોનને આંખની સામે રાખો અને વચ્ચે-વચ્ચે ગરદન હળવી કરો.",
            "photo": "photos/oct16_spine_card4.png",
            "ai_prompt": "Ultra-photorealistic 4:3 educational photo of an Indian youth holding a smartphone up at eye level with straight upright posture, clean modern aesthetic, 8k."
        }
    ]
}

# 3. October 19: Separate into Ear & Hearing Care AND Oral Hygiene
ear_care_day = {
    "id": "10-19",
    "month": 10,
    "day": 19,
    "date_en": "October 19",
    "date_gu": "૧૯ ઓક્ટોબર",
    "tier": 2,
    "tier_en": "Preventive Ear & Hearing Health",
    "tier_gu": "નિવારક કાન અને શ્રવણ સંભાળ દિવસ",
    "title_en": "Ear & Hearing Care",
    "title_gu": "કાન અને શ્રવણ સંભાળ (સુરક્ષિત સાંભળો)",
    "theme_en": "Safe Sound Levels, Dry Ears & Professional ENT Care",
    "theme_gu": "સુરક્ષિત અવાજ, કાનની સ્વચ્છતા અને કાયમી શ્રવણ શક્તિ",
    "cards": [
        {
            "type": "message",
            "index": 1,
            "badge_en": "Action #1",
            "badge_gu": "માર્ગદર્શન #૧",
            "title_en": "Ears Are Self-Cleaning — Consult ENT",
            "title_gu": "કાન માટે માત્ર ENT સ્પેશિયાલિસ્ટની સલાહ લો",
            "desc_en": "Ear canal skin naturally migrates wax outwards. For stubborn wax blockage, earache or reduced hearing, visit an ENT specialist.",
            "desc_gu": "કાન આપમેળે મેલ બહાર કાઢે છે; કાનમાં દુખાવો, રસી કે બહેરાશ જણાય તો ફક્ત કાનના નિષ્ણાત ડોક્ટર પાસે જ તપાસ કરાવો.",
            "photo": "photos/oct19_ear_card1.png",
            "ai_prompt": "Ultra-photorealistic 4:3 photograph of an Indian ENT surgeon examining an Indian patient's ear using an illuminated otoscope in a modern medical clinic, 8k."
        },
        {
            "type": "message",
            "index": 2,
            "badge_en": "Action #2",
            "badge_gu": "માર્ગદર્શન #૨",
            "title_en": "Keep Earphone Volume Below 60%",
            "title_gu": "ઈયરફોનનો અવાજ ૬૦% થી ઓછો રાખો (60-60 નિયમ)",
            "desc_en": "Follow the 60-60 rule: Listen at no more than 60% maximum volume for no longer than 60 minutes at a stretch.",
            "desc_gu": "દરરોજ ઈયરફોન કે હેડફોન ૬૦% થી ઓછા અવાજે સાંભળો અને એકધારું ૬૦ મિનિટથી વધુ સમય ન વાપરો.",
            "photo": "photos/oct19_ear_card2.png",
            "ai_prompt": "Ultra-photorealistic 4:3 shot of an Indian student adjusting volume level safely on a phone with modern over-ear headphones, calm study environment, 8k."
        },
        {
            "type": "message",
            "index": 3,
            "badge_en": "Action #3",
            "badge_gu": "માર્ગદર્શન #૩",
            "title_en": "Never Insert Matchsticks, Pins or Buds",
            "title_gu": "કાનમાં દિવાસળી, પીન કે બડ્સ ક્યારેય ન નાખો",
            "desc_en": "Foreign objects push wax deeper against the eardrum and can cause traumatic perforation or severe infection.",
            "desc_gu": "કાનમાં ક્યારેય દિવાસળી, હેરપિન, ચાવી કે કપાસવાળા બડ્સ ન નાખો; કાનના નાજુક પડદામાં કાણું પડી શકે છે.",
            "photo": "photos/oct19_ear_card3.png",
            "ai_prompt": "Ultra-photorealistic 4:3 close-up medical warning visual showing clean external human ear, educational safety perspective, crisp detail, 8k."
        },
        {
            "type": "message",
            "index": 4,
            "badge_en": "Action #4",
            "badge_gu": "માર્ગદર્શન #૪",
            "title_en": "Protect Ears from Loud Firecrackers & Water",
            "title_gu": "મોટા ફટાકડા, ડીજે અવાજ અને પાણીથી કાન બચાવો",
            "desc_en": "Protect hearing at loud festivals and wedding processions with earplugs. Keep ears gently dry after baths.",
            "desc_gu": "તહેવારો, ડીજે અને ફટાકડાના તીવ્ર ઘોંઘાટથી કાનને બચાવો. સ્નાન કર્યા પછી કાનને હળવા હાથે સૂકા રાખો.",
            "photo": "photos/oct19_ear_card4.png",
            "ai_prompt": "Ultra-photorealistic 4:3 photograph of an Indian child wearing soft foam ear protection plugs outdoors, smiling happily, pristine daytime lighting, 8k."
        }
    ]
}

oral_health_day = {
    "id": "10-19-oral",
    "month": 10,
    "day": 19,
    "date_en": "October 19",
    "date_gu": "૧૯ ઓક્ટોબર",
    "tier": 2,
    "tier_en": "Oral Hygiene & Anti-Tobacco Health",
    "tier_gu": "મુખની સ્વચ્છતા અને વ્યસન મુક્તિ દિવસ",
    "title_en": "Oral Health & Tobacco-Free Life",
    "title_gu": "મુખનું આરોગ્ય અને તમાકુ મુક્તિ",
    "theme_en": "Brush Twice Daily, Gargle & Zero Gutkha / Mawa",
    "theme_gu": "રોજ બે વાર બ્રશ, જમ્યા પછી કોગળા અને તમાકુ-ગુટખા મુક્તિ",
    "cards": [
        {
            "type": "message",
            "index": 1,
            "badge_en": "Action #1",
            "badge_gu": "માર્ગદર્શન #૧",
            "title_en": "Brush Twice Daily with Soft Bristles",
            "title_gu": "સવાર-સાંજ સોફ્ટ બ્રશથી દાંત સાફ કરો",
            "desc_en": "Brush gently for 2 minutes morning and before sleep using fluoridated toothpaste. Clean gums and tongue.",
            "desc_gu": "સવારે અને રાત્રે સૂતા પહેલાં ૨ મિનિટ સુધી સોફ્ટ બ્રશ અને ફ્લોરાઈડ પેસ્ટથી દાંત અને જીભ બરાબર સાફ કરો.",
            "photo": "photos/oct19_oral_card1.png",
            "ai_prompt": "Ultra-photorealistic 4:3 clean clinical photograph of an Indian woman brushing teeth gently in front of a modern mirror, smiling healthy white teeth, soft lighting, 8k."
        },
        {
            "type": "message",
            "index": 2,
            "badge_en": "Action #2",
            "badge_gu": "માર્ગદર્શન #૨",
            "title_en": "Rinse Mouth Vigorously After Meals",
            "title_gu": "કંઈપણ ખાધા પછી સ્વચ્છ પાણીના કોગળા કરો",
            "desc_en": "Rinsing removes trapped carbohydrate debris, neutralizes plaque acids, and prevents enamel erosion.",
            "desc_gu": "જમ્યા પછી કે નાસ્તો કર્યા પછી મોંમાં સ્વચ્છ પાણી ભરીને જોરથી કોગળા કરો; દાંતમાં સડો થતો અટકે છે.",
            "photo": "photos/oct19_oral_card2.png",
            "ai_prompt": "Ultra-photorealistic 4:3 shot of an Indian individual swishing clear water in mouth and rinsing at a clean washbasin, fresh morning hygiene routine, 8k."
        },
        {
            "type": "message",
            "index": 3,
            "badge_en": "Action #3",
            "badge_gu": "માર્ગદર્શન #૩",
            "title_en": "Zero Gutkha, Mawa, Khaini or Bidi",
            "title_gu": "ગુટખા, માવો, ખૈની કે તમાકુનું સેવન ક્યારેય ન કરો",
            "desc_en": "Chewing tobacco & betel quid causes oral submucous fibrosis (OSMF), restricted mouth opening, and oral cancer.",
            "desc_gu": "ગુટખા, માવો કે બીડીથી મોઢાનું કેન્સર થાય છે અને જડબું ખુલતું બંધ થઈ જાય છે; આ ઘાતક વ્યસનથી સદંતર દૂર રહો.",
            "photo": "photos/oct19_oral_card3.png",
            "ai_prompt": "Ultra-photorealistic 4:3 dramatic public health photograph showing a hand crushing a packet of chewing tobacco over a clean white background, red warning aura, 8k."
        },
        {
            "type": "message",
            "index": 4,
            "badge_en": "Action #4",
            "badge_gu": "માર્ગદર્શન #૪",
            "title_en": "Annual Dental & Oral Cancer Screening",
            "title_gu": "વર્ષે એક વાર ડેન્ટિસ્ટ પાસે તપાસ કરાવો",
            "desc_en": "Visit a qualified dentist yearly for plaque scaling and early screening of non-healing ulcers or white patches.",
            "desc_gu": "વર્ષે એક વાર ડેન્ટિસ્ટ પાસે દાંતની સફાઈ કરાવો અને મોંમાં ન રૂઝાતા ચાંદા કે સફેદ ડાઘની તાત્કાલિક તપાસ કરાવો.",
            "photo": "photos/oct19_oral_card4.png",
            "ai_prompt": "Ultra-photorealistic 4:3 medical photo of an Indian dentist in scrubs using mouth mirror and light probe examining an Indian patient's healthy smile, 8k."
        }
    ]
}

# Copy existing photos to seed new dedicated paths
copies = [
    # Food Day
    ("photos/oct16_do1.png", "photos/oct16_food_card1.png"),
    ("photos/oct16_do1.png", "photos/oct16_food_card2.png"),
    ("photos/oct16_dont1.png", "photos/oct16_food_card3.png"),
    ("photos/oct16_do1.png", "photos/oct16_food_card4.png"),
    # Spine Day
    ("photos/oct16_do2.png", "photos/oct16_spine_card1.png"),
    ("photos/oct16_do2.png", "photos/oct16_spine_card2.png"),
    ("photos/oct16_dont2.png", "photos/oct16_spine_card3.png"),
    ("photos/oct16_dont2.png", "photos/oct16_spine_card4.png"),
    # White Cane
    ("photos/cat_cardio.png", "photos/oct15_cane_card1.png"),
    ("photos/cat_cardio.png", "photos/oct15_cane_card2.png"),
    ("photos/cat_cardio.png", "photos/oct15_cane_card3.png"),
    ("photos/cat_cardio.png", "photos/oct15_cane_card4.png"),
    # Ear Care
    ("photos/oct19_do2.png", "photos/oct19_ear_card1.png"),
    ("photos/oct19_do2.png", "photos/oct19_ear_card2.png"),
    ("photos/oct19_dont2.png", "photos/oct19_ear_card3.png"),
    ("photos/oct19_do2.png", "photos/oct19_ear_card4.png"),
    # Oral Health
    ("photos/oct19_do1.png", "photos/oct19_oral_card1.png"),
    ("photos/oct19_do1.png", "photos/oct19_oral_card2.png"),
    ("photos/oct19_dont1.png", "photos/oct19_oral_card3.png"),
    ("photos/oct19_do1.png", "photos/oct19_oral_card4.png"),
]

for src, tgt in copies:
    src_full = os.path.join(PROJECT_DIR, src)
    tgt_full = os.path.join(PROJECT_DIR, tgt)
    if os.path.exists(src_full) and not os.path.exists(tgt_full):
        shutil.copyfile(src_full, tgt_full)

# Rebuild calendar list
new_cal = []
for day in cal:
    day_id = day.get("id")
    if day_id == "10-15":
        new_cal.append(day)
        new_cal.append(white_cane_day)
    elif day_id == "10-16":
        new_cal.append(world_food_day)
        new_cal.append(world_spine_day)
    elif day_id == "10-19":
        new_cal.append(ear_care_day)
        new_cal.append(oral_health_day)
    else:
        new_cal.append(day)

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(new_cal, f, ensure_ascii=False, indent=2)

with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write("// 365-Day Indian Health Calendar Data (Preloaded)\n")
    f.write("window.HEALTH_CALENDAR_DATA = ")
    json.dump(new_cal, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Calendar rebuilt with separated posters! Total posters: {len(new_cal)}")
