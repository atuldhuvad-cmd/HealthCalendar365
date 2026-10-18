"""
Calendar Data Builder for 365-Day Health Poster Studio (India)
Populates full 365-day bilingual dataset with exact details for Oct 15-21
and 3-tier hierarchy for all other days.
"""

import json
import os

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_NAMES_EN = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
MONTH_NAMES_GU = [
    "જાન્યુઆરી", "ફેબ્રુઆરી", "માર્ચ", "એપ્રિલ", "મે", "જૂન",
    "જુલાઈ", "ઓગસ્ટ", "સપ્ટેમ્બર", "ઓક્ટોબર", "નવેમ્બર", "ડિસેમ્બર"
]
GUJARATI_NUMERALS = {
    '0': '૦', '1': '૧', '2': '૨', '3': '૩', '4': '૪',
    '5': '૫', '6': '૬', '7': '૭', '8': '૮', '9': '૯'
}

def to_gu_num(n):
    return "".join(GUJARATI_NUMERALS.get(c, c) for c in str(n))

# Curated High-Priority Health Observances (WHO & India MoHFW)
KNOWN_OBSERVANCES = {
    # October 15-21 (Exact User Specifications)
    (10, 15): {
        "tier": 1,
        "title_en": "Global Handwashing Day & World White Cane Day",
        "title_gu": "ગ્લોબલ હેન્ડવોશિંગ ડે અને વિશ્વ સફેદ લાકડી દિવસ",
        "theme_en": "Clean Hands Save Lives | Dignity & Safe Mobility for the Visually Impaired",
        "theme_gu": "સ્વચ્છ હાથ, નિરોગી જીવન | પ્રજ્ઞાચક્ષુઓનું સન્માન અને સુરક્ષિત દ્રષ્ટિ",
        "cards": [
            {
                "type": "do", "index": 1,
                "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                "title_en": "20-Sec Soap Handwash",
                "title_gu": "સાબુથી ૨૦ સેકન્ડ હાથ ઘસીને ધોવા",
                "desc_en": "Wash palms, back of hands, fingers & nails under running water for 20+ seconds before meals.",
                "desc_gu": "જમતા પહેલાં અને શૌચ પછી ઓછામાં ઓછી ૨૦ સેકન્ડ સાબુથી હથેળી, આંગળીઓ અને કાંડાં વ્યવસ્થિત ધોવો.",
                "photo": "photos/oct15_do1.png",
                "ai_prompt": "Indian doctor demonstrating proper 20-second hand washing technique with rich soap lather under a modern chrome tap, warm clinical lighting, cinematic medical education photo, hyper-detailed."
            },
            {
                "type": "do", "index": 2,
                "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                "title_en": "Annual Eye Checks & Guide Cane Care",
                "title_gu": "નિયમિત આંખની તપાસ અને સફેદ લાકડીનો સહારો",
                "desc_en": "Get an annual eye test. Respect white cane users and ensure unobstructed walkways.",
                "desc_gu": "વર્ષે એક વાર આંખની તપાસ કરાવો. પ્રજ્ઞાચક્ષુ વ્યક્તિઓને રસ્તો ઓળંગવામાં મદદ કરો અને રસ્તા ખુલ્લા રાખો.",
                "photo": "photos/oct15_do2.png",
                "ai_prompt": "Close-up photorealistic shot of an Indian individual with a white cane with red safety band walking on tactile yellow pavement, morning sunlight, compassionate community, 8k resolution."
            },
            {
                "type": "dont", "index": 3,
                "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                "title_en": "Touching Face With Unwashed Hands",
                "title_gu": "ધોયા વગરના ગંદા હાથે મોં કે ખોરાકને અડવું નહીં",
                "desc_en": "Never touch eyes, nose or street food with unwashed hands; hand contaminants spread gastro & respiratory bugs.",
                "desc_gu": "ગંદા હાથે ક્યારેય આંખ, નાક કે ખાવાની વસ્તુઓને અડવું નહીં; રોગચાળો અને ઝાડા-ઊલટીનું મુખ્ય કારણ છે.",
                "photo": "photos/oct15_dont1.png",
                "ai_prompt": "Cinematic photography showing grimy unwashed hand reaching for street snacks with germ overlay warning, red prohibition tone, high contrast Indian market background, 8k."
            },
            {
                "type": "dont", "index": 4,
                "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                "title_en": "Violent Eye Rubbing & OTC Drops",
                "title_gu": "આંખ જોરથી ચોળવી નહીં કે જાતે ટીપાં નાખવા નહીં",
                "desc_en": "Do not rub irritated eyes with knuckles or use unprescribed steroid eye drops for redness.",
                "desc_gu": "આંખ લાલ થાય કે ખંજવાળ આવે ત્યારે જોરથી ચોળવી નહીં અને ડોક્ટર પૂછ્યા વગર સ્ટીરોઈડ ટીપાં ન વાપરવા.",
                "photo": "photos/oct15_dont2.png",
                "ai_prompt": "Dramatic photo of person aggressively rubbing red irritated eye, crimson warning lighting, danger aura, medical caution visual, hyper-realistic."
            }
        ]
    },
    (10, 16): {
        "tier": 1,
        "title_en": "World Food Day & World Spine Day",
        "title_gu": "વિશ્વ ખાદ્ય દિવસ અને વિશ્વ કરોડરજ્જુ દિવસ",
        "theme_en": "Traditional Indian Balanced Thali & Ergonomic Spine Care",
        "theme_gu": "સંતુલિત દેશી આહાર અને કરોડરજ્જુનું સાચું પોશ્ચર",
        "cards": [
            {
                "type": "do", "index": 1,
                "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                "title_en": "Eat Balanced Desi Thali",
                "title_gu": "સંતુલિત દેશી થાળી આરોગો",
                "desc_en": "Include 50% vegetables/salad, 25% protein (dal/paneer/curd), and 25% whole grains/millets (bajra, jowar).",
                "desc_gu": "રોજિંદા ભોજનમાં ૫૦% શાકભાજી-સલાડ, ૨૫% કઠોળ-દાળ-દહીં અને ૨૫% બાજરી-જુવાર જેવા જાડા અનાજ સામેલ કરો.",
                "photo": "photos/oct16_do1.png",
                "ai_prompt": "Appetizing photorealistic Indian bronze thali with colorful bowls of yellow dal, spinach paneer, fresh dahi, sprouted pulses, bajra rotis, brass tableware, warm home lighting, 8k."
            },
            {
                "type": "do", "index": 2,
                "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                "title_en": "Erect Spine & Lumbar Support",
                "title_gu": "બેસતી-ચાલતી વખતે પીઠ સીધી રાખો",
                "desc_en": "Keep screen at eye level, sit tall with lower back support, and take 2-minute stretch breaks hourly.",
                "desc_gu": "કમ્પ્યુટર-મોબાઈલ વાપરતી વખતે સ્ક્રીન આંખની સામે રાખો, પીઠને ટેકો આપો અને દર કલાકે ઊભા થઈ સ્ટ્રેચિંગ કરો.",
                "photo": "photos/oct16_do2.png",
                "ai_prompt": "Ergonomic workspace photograph of an Indian professional sitting with perfect spine alignment, lumbar cushion support, monitor at eye level, green spine checkmark glow, realistic 8k."
            },
            {
                "type": "dont", "index": 3,
                "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                "title_en": "Deep-Fried Street Fast Food & Soda",
                "title_gu": "વધારે પડતો તળેલો ફાસ્ટફૂડ અને કોલ્ડડ્રિંક્સ",
                "desc_en": "Avoid repeated consumption of re-heated trans-fat fried snacks, ultra-processed junk, and sugary colas.",
                "desc_gu": "વારંવાર તળેલા તેલના સમોસા, ગાંઠિયા, મેંદાના પ્રોસેસ્ડ નાસ્તા અને ખાંડવાળા સોડા-કોલ્ડડ્રિંક્સથી દૂર રહો.",
                "photo": "photos/oct16_dont1.png",
                "ai_prompt": "High realism photograph of dripping oily samosas and fizzy dark cola glass with unhealthy greasy sheen, red warning filter, vivid detail, street vendor setup."
            },
            {
                "type": "dont", "index": 4,
                "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                "title_en": "Slouching & Heavy Lifting with Bent Back",
                "title_gu": "વાંકા વળીને વજન ઊંચકવું કે ઝૂકીને બેસવું નહીં",
                "desc_en": "Never bend spine forward to lift heavy loads; bend your knees instead. Avoid 60° text-neck over phones.",
                "desc_gu": "કરોડરજ્જુ પર વજન ન આવે તે માટે ઘૂંટણ વાળીને વજન ઊંચકો; પથારીમાં વાંકા વળી મોબાઈલ મથાળવો નહીં.",
                "photo": "photos/oct16_dont2.png",
                "ai_prompt": "Photorealistic side view of a person with severe hunched text-neck slouching over a phone, biomechanical spine strain red glow, warning signs, 8k."
            }
        ]
    },
    (10, 17): {
        "tier": 1,
        "title_en": "World Trauma Day (Road Safety & Golden Hour)",
        "title_gu": "વિશ્વ ટ્રોમા દિવસ (માર્ગ સુરક્ષા અને ૧૦૮ ગોલ્ડન અવર)",
        "theme_en": "Certified Helmets, Seatbelts & Rapid 108 Emergency Action",
        "theme_gu": "ISI હેલ્મેટ, સીટબેલ્ટ અને અકસ્માતમાં તાત્કાલિક ૧૦૮ સેવાનો ઉપયોગ",
        "cards": [
            {
                "type": "do", "index": 1,
                "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                "title_en": "Wear ISI-Marked Full-Face Helmet & Seatbelt",
                "title_gu": "ISI ચિહ્નિત ફુલ-ફેસ હેલ્મેટ અને સીટબેલ્ટ પહેરો",
                "desc_en": "Fasten chin strap on two-wheelers; click three-point seatbelt in cars for front and rear passengers.",
                "desc_gu": "બાઇક-સ્કૂટર પર ચિન-સ્ટ્રેપ સાથે ISI ચિહ્નિત હેલ્મેટ પહેરો; કારમાં આગળ-પાછળ બેસનાર દરેક વ્યક્તિ સીટબેલ્ટ અવશ્ય બાંધો.",
                "photo": "photos/oct17_do1.png",
                "ai_prompt": "Sharp commercial photograph of high-grade matte black ISI motorcycle helmet with fastened chin strap and car 3-point seatbelt buckle clicked, safety aesthetic, 8k."
            },
            {
                "type": "do", "index": 2,
                "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                "title_en": "Call 108 in Golden Hour (First 60 Mins)",
                "title_gu": "ગોલ્ડન અવરમાં તરત ૧૦૮ એમ્બ્યુલન્સ બોલાવો",
                "desc_en": "Trauma victims have maximum survival if emergency trauma care begins within the first 60 minutes.",
                "desc_gu": "અકસ્માત વખતે પહેલા ૬૦ મિનિટ 'ગોલ્ડન અવર' છે; સમય બગાડ્યા વગર તરત ૧૦૮ ડાયલ કરો અને રસ્તો આપો.",
                "photo": "photos/oct17_do2.png",
                "ai_prompt": "Emergency scene photograph of Indian 108 ambulance with flashing beacons arriving swiftly on highway, golden hour sunlight, paramedics, heroic lighting, 8k."
            },
            {
                "type": "dont", "index": 3,
                "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                "title_en": "Triple Riding, Speeding & Mobile Driving",
                "title_gu": "ત્રિપલ સવારી, ઓવરસ્પીડ અને ડ્રાઇવિંગમાં ફોન",
                "desc_en": "Never operate vehicles while holding mobile phones; avoid stunt riding, overspeeding, and drunk driving.",
                "desc_gu": "વાહન ચલાવતી વખતે ક્યારેય ફોન પર વાત ન કરો કે મેસેજ ન કરો; વધુ પડતી સ્પીડ અને ત્રિપલ સવારીથી બચો.",
                "photo": "photos/oct17_dont1.png",
                "ai_prompt": "Dramatic photo of 3 young people cramped on scooter with no helmets and driver holding phone, motion blur danger, red warning cross, hyper-realistic."
            },
            {
                "type": "dont", "index": 4,
                "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                "title_en": "Rough Mishandling of Trauma Victims",
                "title_gu": "ઈજાગ્રસ્તને આડેધડ ખસેડવો કે પાણી પીવડાવવું નહીં",
                "desc_en": "Do not jerk spine/neck of crash victims or force water down unconscious throats (choking risk).",
                "desc_gu": "ગંભીર અકસ્માતગ્રસ્ત વ્યક્તિની ગરદન ખેંચવી નહીં કે બેભાન દર્દીના મોંમાં પાણી રેડવું નહીં - શ્વાસનળી બંધ થઈ શકે છે.",
                "photo": "photos/oct17_dont2.png",
                "ai_prompt": "Medical trauma awareness photo showing dangerous improper bystander handling of crash victim, danger warning slash, realistic road accident scene."
            }
        ]
    },
    (10, 18): {
        "tier": 1,
        "title_en": "World Menopause Day",
        "title_gu": "વિશ્વ મેનોપોઝ દિવસ",
        "theme_en": "Women's Bone Health, Sunlight, Calcium & Mindful Pranayama",
        "theme_gu": "મહિલાઓના હાડકાંની સુરક્ષા, કુમળો તડકો, કેલ્શિયમ અને પ્રાણાયામ",
        "cards": [
            {
                "type": "do", "index": 1,
                "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                "title_en": "Morning Sun (Vit D) & Calcium Diet",
                "title_gu": "સવારનો કુમળો તડકો અને કેલ્શિયમ આહાર",
                "desc_en": "Get 20 mins morning sun. Eat milk, curd, ragi, white sesame seeds (til), and dark leafy greens.",
                "desc_gu": "રોજ સવારે ૨૦ મિનિટ કુમળો તડકો લો. દૂધ, દહીં, રાગી, સફેદ તલ અને લીલા શાકભાજીથી હાડકાં મજબૂત રાખો.",
                "photo": "photos/oct18_do1.png",
                "ai_prompt": "Inspiring photograph of an Indian woman in her 50s absorbing warm morning sunlight in garden, healthy bowl of sesame seeds and dairy milk, glowing health, 8k."
            },
            {
                "type": "do", "index": 2,
                "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                "title_en": "Daily Brisk Walk & Anulom-Vilom",
                "title_gu": "રોજ ૩૦ મિનિટ ચાલવું અને અનુલોમ-વિલોમ",
                "desc_en": "30 mins brisk walking preserves bone density; daily slow pranayama balances vasomotor symptoms and stress.",
                "desc_gu": "દરરોજ ૩૦ મિનિટ મોર્નિંગ વોક કરો; અનુલોમ-વિલોમ અને ભ્રામરી પ્રાણાયામથી માનસિક શાંતિ અને ઊંઘ સુધરે છે.",
                "photo": "photos/oct18_do2.png",
                "ai_prompt": "Serene outdoor photograph of an Indian woman practicing pranayama breathing on a yoga mat in lush park, morning mist, sunrise rays, zen aesthetic, 8k."
            },
            {
                "type": "dont", "index": 3,
                "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                "title_en": "Ignoring Hot Flashes & Mood Changes",
                "title_gu": "હોટ ફ્લેશ કે હતાશાને મનમાં દબાવી રાખવા નહીં",
                "desc_en": "Menopause is a natural transition, not an illness. Do not suffer night sweats or mood swings in silence; consult your gynecologist.",
                "desc_gu": "મેનોપોઝ કુદરતી તબક્કો છે; અતિશય ગરમી લાગવી, અનિદ્રા કે ચિંતાને અવગણવા નહીં, ગાયનેકોલોજિસ્ટની સલાહ લો.",
                "photo": "photos/oct18_dont1.png",
                "ai_prompt": "Empathetic realistic photo of a middle-aged woman feeling exhausted with hot flashes, clinical mental health awareness, red distress tone, high detail."
            },
            {
                "type": "dont", "index": 4,
                "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                "title_en": "Heavy Caffeine, High Sugar & Sedentary Habit",
                "title_gu": "વધારે ચા-કૉફી, મીઠાઈ અને નિષ્ક્રિય જીવનશૈલી",
                "desc_en": "Excess tea, coffee, and sugary Indian sweets trigger severe hot flashes and accelerate bone calcium loss.",
                "desc_gu": "વધુ પડતી ચા-કૉફી અને ખાંડવાળી ભારતીય મીઠાઈઓથી તીવ્ર હોટ ફ્લશ થઈ શકે છે અને હાડકાંમાં કેલ્શિયમનું નુકસાન ઝડપથી વધી શકે છે.",
                "photo": "photos/oct18_dont2.png",
                "ai_prompt": "Realistic still life of multiple empty coffee cups, overflowing sugar cubes, and couch silhouette, red prohibited stamp, clear educational visual."
            }
        ]
    },
    (10, 19): {
        "tier": 3,
        "title_en": "Preventive Health: Ear & Hearing Care + Oral Hygiene",
        "title_gu": "નિવારક આરોગ્ય: કાન-શ્રવણ સંભાળ અને મુખની સ્વચ્છતા",
        "theme_en": "Zero Gutkha/Mawa/Tobacco & Safe Ear Cleaning Practices",
        "theme_gu": "ગુટખા-માવા-તમાકુ મુક્તિ અને કાનની સાચી સારસંભાળ",
        "cards": [
            {
                "type": "do", "index": 1,
                "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                "title_en": "Brush Twice Daily & Gargle After Meals",
                "title_gu": "દિવસમાં બે વાર બ્રશ કરો અને જમીને કોગળા કરો",
                "desc_en": "Use soft bristles with fluoridated paste morning and night. Rinse mouth vigorously after every meal.",
                "desc_gu": "સવારે અને રાત્રે સૂતા પહેલાં સોફ્ટ બ્રશથી દાંત સાફ કરો. કંઈપણ ખાધા પછી મોંમાં સ્વચ્છ પાણીના કોગળા કરો.",
                "photo": "photos/oct19_do1.png",
                "ai_prompt": "Clean professional macro photograph of a healthy sparkling white tooth model and soft toothbrush with pea-sized blue fluoride paste, water splashes, clinical hygiene, 8k."
            },
            {
                "type": "do", "index": 2,
                "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                "title_en": "Consult ENT for Ear Wax & Keep Ears Dry",
                "title_gu": "કાન માટે ENT ડોક્ટરની સલાહ લો અને કાન સૂકા રાખો",
                "desc_en": "Ears are self-cleaning organs. Consult an ENT specialist for stubborn wax, pain, or muffled hearing.",
                "desc_gu": "કાનમાં આપમેળે મેલ બહાર નીકળે છે; કાનમાં દુખાવો કે બહેરાશ જણાય તો માત્ર કાનના ડોક્ટર (ENT) પાસે તપાસ કરાવો.",
                "photo": "photos/oct19_do2.png",
                "ai_prompt": "Medical clinic photograph of ENT specialist doctor examining ear using Welch-Allyn illuminated otoscope, caring atmosphere, sharp focus, 8k."
            },
            {
                "type": "dont", "index": 3,
                "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                "title_en": "Chewing Gutkha, Mawa, Khaini or Smoking",
                "title_gu": "ગુટખા, માવો, બીડી કે તમાકુનું સેવન ક્યારેય ન કરો",
                "desc_en": "Betel quid, gutkha, and tobacco are #1 causes of mouth cancer (oral submucous fibrosis) and tooth loss in India.",
                "desc_gu": "ગુટખા, માવો, બીડી કે ખૈનીથી મોઢાનું કેન્સર થાય છે અને જડબું જકડાઈ જાય છે; આ વ્યસનથી સદંતર દૂર રહો.",
                "photo": "photos/oct19_dont1.png",
                "ai_prompt": "Realistic photo of gutkha pouch, tobacco flakes and betel nut with dramatic red warning spit splatter, prohibition symbol, powerful anti-tobacco visual."
            },
            {
                "type": "dont", "index": 4,
                "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                "title_en": "Poking Matchsticks, Pins or Cotton Buds in Ears",
                "title_gu": "કાનમાં દિવાસળી, પીન કે રૂ વાળી સળી નાખવી નહીં",
                "desc_en": "Never insert buds, keys or matchsticks; they push wax deeper and can permanently puncture the eardrum.",
                "desc_gu": "કાનમાં ક્યારેય દિવાસળી, હેરપિન કે બડ્સ ન નાખો; પડદામાં કાણું પડી શકે છે અને કાયમી બહેરાશ આવી શકે છે.",
                "photo": "photos/oct19_dont2.png",
                "ai_prompt": "Close-up medical caution shot of a wooden matchstick touching human ear canal with eardrum damage illustration, red danger cross, hyper-realistic."
            }
        ]
    },
    (10, 20): {
        "tier": 1,
        "title_en": "World Osteoporosis Day",
        "title_gu": "વિશ્વ ઓસ્ટીયોપોરોસીસ દિવસ",
        "theme_en": "Bone Strength, Morning Walks & Fall Prevention in Seniors",
        "theme_gu": "મજબૂત હાડકાં, મોર્નિંગ વૉક અને વડીલોને લપસી પડવાથી બચાવો",
        "cards": [
            {
                "type": "do", "index": 1,
                "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                "title_en": "Bright Lighting & Bathroom Grab Bars",
                "title_gu": "ઘરમાં પૂરતો પ્રકાશ અને બાથરૂમમાં ગ્રેબ-બાર",
                "desc_en": "Install sturdy stainless steel grab bars beside toilets, keep night lights on, and remove throw rugs.",
                "desc_gu": "વડીલો માટે બાથરૂમમાં મજબૂત ગ્રેબ-બાર લગાવો, રાત્રે અજવાળું રાખો અને લપસી જાય તેવી સાદડીઓ હટાવો.",
                "photo": "photos/oct20_do1.png",
                "ai_prompt": "Modern bathroom photograph showing senior-friendly stainless steel grab bar securely anchored to ceramic wall, anti-skid floor mat, bright warm illumination, 8k."
            },
            {
                "type": "do", "index": 2,
                "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                "title_en": "Weight-Bearing Walks & Ragi / Sesame Nutrition",
                "title_gu": "રોજિંદી ચાલવાની કસરત અને રાગી-તલનો આહાર",
                "desc_en": "Daily walking stimulates osteoblasts to build bone. Include calcium-rich ragi, sesame, paneer and curd.",
                "desc_gu": "દરરોજ પગપાળા ચાલવાથી હાડકાં મજબૂત થાય છે. આહારમાં રાગીની રોટલી, સફેદ તલ અને પનીરનો ઉપયોગ વધારો.",
                "photo": "photos/oct20_do2.png",
                "ai_prompt": "Healthy elderly Indian couple smiling joyfully during a morning park walk in fresh air, sunrise background, healthy bone structure graphic, 8k."
            },
            {
                "type": "dont", "index": 3,
                "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                "title_en": "Eliminate Slip, Trip & Fall Hazards at Home",
                "title_gu": "ઘરમાં લપસી પડવાના અને ઠોકર ખાવાના જોખમો દૂર કરો",
                "desc_en": "Slippery wet floors and loose cords are a leading avoidable cause of falls and hip fractures in elders.",
                "desc_gu": "ભીનો ફ્લોર અને છૂટા વાયરો વડીલોમાં થાપાના ફ્રેક્ચરનું એક મુખ્ય ટાળી શકાય તેવું કારણ છે.",
                "photo": "photos/oct20_dont1.png",
                "ai_prompt": "Ultra-photorealistic 4:3 photograph of an Indian elder living room demonstrating fall hazard prevention: completely clear, uncluttered walkways with electrical cords safely bound and secured along the wall baseboard. A senior Indian grandfather is standing steadily near a firm armchair, wearing non-slip footwear. Warm indoor daylight, dry matte tiled flooring, authentic Indian domestic setting, 8k resolution. No text, no warning icons, no injured bodies."
            },
            {
                "type": "dont", "index": 4,
                "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                "title_en": "Limit Excessive Salt Intake & Choose Wholesome Hydration",
                "title_gu": "વધુ પડતું મીઠું ટાળો અને પૂરતું પાણી-છાશ પીઓ",
                "desc_en": "Excessive dietary salt increases urinary calcium loss. For adults, keep total salt from all foods below 5 g/day (equivalent to less than 2 g/day sodium). Choose water or traditional unsalted buttermilk.",
                "desc_gu": "વધારે પડતું મીઠું ખાવાથી પેશાબ વાટે કેલ્શિયમ નીકળી જાય છે; પુખ્ત વયના લોકો માટે દિવસભરના બધા ખોરાકમાંથી મળતું કુલ મીઠું ૫ ગ્રામથી ઓછું રાખો (આશરે ૨ ગ્રામથી ઓછું સોડિયમ). પાણી અથવા મીઠું ઉમેર્યા વગરની છાશ પસંદ કરો.",
                "photo": "photos/oct20_dont2.png",
                "ai_prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian dining table setting demonstrating healthy bone nutrition: a glass of fresh homemade buttermilk (chaas) and clean water in focus, with an open salt shaker pushed away to the background. Wholesome Indian meal setting with brass or stainless steel plate, warm natural daylight, 8k resolution. Strictly no brand logos, no text labels."
            }
        ]
    },
    (10, 21): {
        "tier": 1,
        "title_en": "World Iodine Deficiency Disorders Prevention Day",
        "title_gu": "વિશ્વ આયોડિન અલ્પતા નિવારણ દિવસ",
        "theme_en": "Proper Storage of Iodized Salt & Healthy Thyroid Care",
        "theme_gu": "આયોડિનયુક્ત મીઠાનો સાચો સંગ્રહ અને થાઇરોઇડનું રક્ષણ",
        "cards": [
            {
                "type": "do", "index": 1,
                "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                "title_en": "Store Iodized Salt in Airtight Jars",
                "title_gu": "આયોડાઇઝ્ડ મીઠું હવાચુસ્ત બરણીમાં ઢાંકીને રાખો",
                "desc_en": "Always buy sealed packets with the smiling sun iodized logo. Store in airtight ceramic or glass jars.",
                "desc_gu": "હંમેશા પેક કરેલું આયોડાઇઝ્ડ મીઠું ખરીદો અને તેને કાચ કે ચિનાઈ માટીની હવાચુસ્ત બરણીમાં ઢાંકીને રાખો.",
                "photo": "photos/oct21_do1.png",
                "ai_prompt": "Kitchen counter photo of blue branded iodized salt packet pouring into an airtight ceramic jar with rubber seal lid, thyroid care badge, pristine clarity, 8k."
            },
            {
                "type": "do", "index": 2,
                "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                "title_en": "Add Iodized Salt Towards the End of Cooking",
                "title_gu": "રાંધતી વખતે મીઠું છેલ્લે ઉમેરવાની ટેવ પાડો",
                "desc_en": "Prolonged high-heat boiling can degrade and leach fortified iodine compounds. Adding iodized salt towards the end of cooking helps retain full micronutrient value.",
                "desc_gu": "લાંબા સમય સુધી વધુ ગરમીમાં ઉકાળવાથી આયોડિનનું પ્રમાણ ઘટી શકે છે; રસોઈ પૂરી થવાના સમયે મીઠું ઉમેરવાથી આયોડિનનું મૂલ્ય જળવાય છે.",
                "photo": "photos/oct21_do2.png",
                "ai_prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian home cook gently sprinkling a measured pinch of iodized salt into a stainless steel kadai of freshly cooked vegetables near the end of cooking, warm steam, 8k resolution. No text, no logos."
            },
            {
                "type": "dont", "index": 3,
                "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                "title_en": "Avoid Unbranded Loose Coarse Salt",
                "title_gu": "ખુલ્લું અને બિન-આયોડાઇઝ્ડ મીઠું વાપરવાનું ટાળો",
                "desc_en": "Unbranded loose coarse salt lacks iodine; iodine deficiency in pregnant mothers leads to child mental retardation.",
                "desc_gu": "ખુલ્લું બિન-આયોડાઇઝ્ડ મીઠું વાપરશો નહીં; આયોડિનની કમીથી બાળકોમાં માનસિક મંદતા અને ગલગંડ (ગોઇટર) થાય છે.",
                "photo": "photos/oct21_dont1.png",
                "ai_prompt": "Ultra-photorealistic 4:3 photo showing packaged sealed iodized salt with smiling sun logo selected while unbranded loose coarse salt in an open sack is pushed aside, medical awareness, 8k."
            },
            {
                "type": "dont", "index": 4,
                "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                "title_en": "Keep Iodized Salt Dry & Covered",
                "title_gu": "આયોડાઇઝ્ડ મીઠું સૂકું અને ઢાંકેલું રાખો",
                "desc_en": "Store iodized salt in a tightly closed container in a cool, dry place away from moisture.",
                "desc_gu": "આયોડાઇઝ્ડ મીઠું હવાચુસ્ત બરણીમાં, ઠંડી અને સૂકી જગ્યાએ ભેજથી દૂર રાખો.",
                "photo": "photos/oct21_dont2.png",
                "ai_prompt": "Realistic Indian kitchen pantry photo showing iodized salt in a tightly closed ceramic or glass container on a clean, cool, dry shelf away from moisture, 8k."
            }
        ]
    }
}

# General 365-day health calendar builder
CALENDAR_THEMES = [
    {
        "tier": 1, "cat": "cardio",
        "title_en": "Cardiovascular Health & BP Control",
        "title_gu": "હૃદય સ્વાસ્થ્ય અને બ્લડપ્રેશર નિયંત્રણ",
        "theme_en": "Keep Blood Pressure < 120/80 mmHg | Healthy Heart Habits",
        "theme_gu": "બીપી ૧૨૦/૮૦ સામાન્ય રાખો | તંદુરસ્ત હૃદયની આદતો",
        "do1": ("Check BP Regularly", "દર મહિને બીપી મપાવો", "Check blood pressure once a month; keep systolic under 120.", "મહિને એક વાર બીપી ચેક કરાવો અને નોંધ રાખો.", "photos/cat_cardio.png"),
        "do2": ("45-Min Daily Aerobic Exercise", "દરરોજ ૪૫ મિનિટ કસરત", "Brisk walking, cycling or swimming strengthens the myocardium.", "રોજ ઝડપી ચાલવું કે સાયકલ ચલાવવાથી હૃદય સશક્ત બને છે.", "photos/cat_cardio.png"),
        "dont1": ("Smoking & Excessive Salt", "ધૂમ્રપાન અને વધુ પડતું મીઠું", "Tobacco narrows coronary arteries and high sodium elevates BP.", "તમાકુ અને વધારાનું મીઠું હૃદયની નળીઓ બ્લોક કરે છે.", "photos/cat_cardio.png"),
        "dont2": ("Ignoring Chest Heaviness", "છાતીમાં દબાણ અવગણવું નહીં", "Never dismiss unexplained chest tightness, jaw pain or sweating.", "છાતીમાં ભાર કે પરસેવો થાય તો તરત ECG કરાવો.", "photos/cat_cardio.png")
    },
    {
        "tier": 1, "cat": "nutrition",
        "title_en": "Diabetes Care & Blood Sugar Balance",
        "title_gu": "ડાયાબિટીસ સંભાળ અને બ્લડ શુગર નિયંત્રણ",
        "theme_en": "Maintain HbA1c < 6.5% | Smart Low-Glycemic Indian Diet",
        "theme_gu": "HbA1c ૬.૫% થી ઓછો રાખો | પૌષ્ટિક દેશી ખોરાક",
        "do1": ("High Fiber & Methi Seeds", "મેથી અને ફાઇબરયુક્ત ખોરાક", "Soak methi seeds overnight; eat sprouts and greens before meals.", "સવારે પલાળેલી મેથી લો અને જમતા પહેલાં સલાડ-કઠોળ ખાઓ.", "photos/cat_nutrition.png"),
        "do2": ("Daily Foot Inspection", "રોજ પગના તળિયા તપાસો", "Inspect feet daily for cuts, dry cracks or fungal infection.", "ડાયાબિટીસમાં પગના તળિયા રોજ તપાસો અને મોજાં પહેરો.", "photos/cat_nutrition.png"),
        "dont1": ("Refined Sugar & Fruit Juices", "ખાંડ, ગોળ અને પેક્ડ જ્યુસ", "Liquid sugars cause sudden glucose spikes; eat whole fruits instead.", "ગોળ, ખાંડ અને જ્યુસ ન લો; આખો ફળ ચાવીને ખાઓ.", "photos/cat_nutrition.png"),
        "dont2": ("Skipping Prescribed Medication", "દવાઓ જાતે બંધ ન કરવી", "Never skip insulin or metformin without consulting your physician.", "સુગર નોર્મલ દેખાય તો પણ ડોક્ટર વગર દવા બંધ ન કરો.", "photos/cat_nutrition.png")
    },
    {
        "tier": 2, "cat": "infection",
        "title_en": "Vector-Borne Disease Prevention (Dengue & Malaria)",
        "title_gu": "મચ્છરજન્ય રોગો (ડેન્ગ્યુ અને મેલેરિયા) નિયંત્રણ",
        "theme_en": "Zero Water Stagnation | Dry Day Once a Week",
        "theme_gu": "ક્યાંય પાણી ભરાવા ન દો | અઠવાડિયે એક દિવસ ડ્રાય-ડે",
        "do1": ("Empty Coolers & Flower Pots", "કૂલર અને કૂંડાં સાફ કરી સૂકવો", "Scrub and dry all indoor water containers every Sunday.", "દર રવિવારે કૂલર, ટાંકી અને કૂંડાં સૂકવીને સાફ કરો.", "photos/cat_infection.png"),
        "do2": ("Mosquito Nets & Repellents", "મચ્છરદાનીનો ઉપયોગ કરો", "Sleep under bed nets and wear full-sleeve clothes at dusk/dawn.", "રાત્રે મચ્છરદાની વાપરો અને આખી બાંયના કપડાં પહેરો.", "photos/cat_infection.png"),
        "dont1": ("Stagnant Water on Terraces", "ધાબા પર ભરાયેલું પાણી", "Discard old tyres, broken pots and coconut shells outdoors.", "ધાબા પર ભંગાર, જૂના ટાયર કે નાળિયેરના કોચલા ન રાખો.", "photos/cat_infection.png"),
        "dont2": ("Self-Medicating with Aspirin", "ડેન્ગ્યુમાં જાતે દવા ન લેવી", "Never take Brufen or Aspirin during viral fevers; consult doctor.", "તાવમાં ડોક્ટરની સલાહ વગર પેઈનકિલર ન લેવી.", "photos/cat_infection.png")
    },
    {
        "tier": 3, "cat": "yoga",
        "title_en": "Daily Yoga, Pranayama & Stress Relief",
        "title_gu": "દૈનિક યોગ, પ્રાણાયામ અને માનસિક શાંતિ",
        "theme_en": "Mind-Body Harmony | 20 Mins Surya Namaskar & Dhyana",
        "theme_gu": "તન અને મનની સુખાકારી | ૨૦ મિનિટ સૂર્યનમસ્કાર અને ધ્યાન",
        "do1": ("Surya Namaskar at Sunrise", "સૂર્યોદય સમયે સૂર્યનમસ્કાર", "12 rounds of Surya Namaskar improve flexibility and circulation.", "સવારે ૧૨ સૂર્યનમસ્કાર કરવાથી શરીર સ્ફૂર્તિલું રહે છે.", "photos/cat_yoga.png"),
        "do2": ("Deep Diaphragmatic Breathing", "ઊંડા શ્વાસ અને ભ્રામરી", "Practice 10 mins of Bhramari pranayama before sleeping.", "રાત્રે સૂતા પહેલાં ૧૦ મિનિટ ભ્રામરી પ્રાણાયામ કરો.", "photos/cat_yoga.png"),
        "dont1": ("Jerking Body During Asanas", "ઝટકા સાથે આસનો ન કરવા", "Never force spinal twists or overstretch stiff hamstrings.", "શરીરને ઝટકો આપી આસન ન કરો; ધીમે ધીમે ક્ષમતા વધારો.", "photos/cat_yoga.png"),
        "dont2": ("Eating Heavy Meals Before Yoga", "ભરેલા પેટે યોગાસન ન કરો", "Maintain at least 3-4 hours gap between food and yogic practice.", "જમ્યા પછી તરત યોગાસન ન કરો; ૩-૪ કલાકનું અંતર રાખો.", "photos/cat_yoga.png")
    },
    {
        "tier": 3, "cat": "mental",
        "title_en": "Mental Health & Sleep Hygiene",
        "title_gu": "માનસિક સ્વાસ્થ્ય અને ગાઢ ઊંઘની આદતો",
        "theme_en": "Prioritize 7-8 Hours Restorative Sleep | Open Conversation",
        "theme_gu": "૭ થી ૮ કલાકની શાંત ઊંઘ | મનની વાત નિખાલસપણે રજૂ કરો",
        "do1": ("Consistent Sleep Schedule", "નિયમિત સૂવાનો અને જાગવાનો સમય", "Go to bed and wake up at the exact same hour every day.", "રોજ રાત્રે એક જ સમયે સૂવાની અને સવારે ઊઠવાની ટેવ પાડો.", "photos/cat_mental.png"),
        "do2": ("Talk to Loved Ones / Counselor", "સ્નેહીજનો સાથે મનની વાત કરો", "Share feelings openly; seek professional counseling for anxiety.", "ચિંતા કે ઉદાસી જણાય તો કાઉન્સેલર કે પરિવારજન સાથે વાત કરો.", "photos/cat_mental.png"),
        "dont1": ("Screen Time in Bed", "પથારીમાં સ્માર્ટફોન વાપરવો નહીં", "Blue screen light suppresses melatonin; put phones away 1 hr before sleep.", "સૂતા પહેલાં ૧ કલાક મોબાઈલ સ્ક્રીનથી દૂર રહો.", "photos/cat_mental.png"),
        "dont2": ("Alcohol / Sleeping Pills Dependency", "દારૂ કે ઊંઘની ગોળીઓની લત", "Never self-medicate with sedatives or alcohol to induce sleep.", "ઊંઘ માટે ક્યારેય જાતે ઊંઘની ગોળીઓ કે નશો ન કરવો.", "photos/cat_mental.png")
    }
]

def generate_365_days():
    full_calendar = []
    
    for month_idx in range(12):
        month_num = month_idx + 1
        num_days = DAYS_IN_MONTH[month_idx]
        
        for day_num in range(1, num_days + 1):
            key = (month_num, day_num)
            day_id = f"{month_num:02d}-{day_num:02d}"
            date_en = f"{MONTH_NAMES_EN[month_idx]} {day_num}"
            date_gu = f"{to_gu_num(day_num)} {MONTH_NAMES_GU[month_idx]}"
            
            if key in KNOWN_OBSERVANCES:
                obs = KNOWN_OBSERVANCES[key]
                tier = obs["tier"]
                tier_en = "WHO Global Health Observance" if tier == 1 else ("India MoHFW National Health Day" if tier == 2 else "Preventive Health Awareness")
                tier_gu = "વિશ્વ આરોગ્ય સંસ્થા (WHO) દિવસ" if tier == 1 else ("રાષ્ટ્રીય આરોગ્ય મિશન (MoHFW)" if tier == 2 else "નિવારક આરોગ્ય માર્ગદર્શિકા")
                
                entry = {
                    "id": day_id,
                    "month": month_num,
                    "day": day_num,
                    "date_en": date_en,
                    "date_gu": date_gu,
                    "tier": tier,
                    "tier_en": tier_en,
                    "tier_gu": tier_gu,
                    "title_en": obs["title_en"],
                    "title_gu": obs["title_gu"],
                    "theme_en": obs["theme_en"],
                    "theme_gu": obs["theme_gu"],
                    "cards": obs["cards"]
                }
            else:
                # Rotate among curated Indian preventive themes
                theme_template = CALENDAR_THEMES[(month_num * 31 + day_num) % len(CALENDAR_THEMES)]
                tier = theme_template["tier"]
                tier_en = "WHO Global Health Observance" if tier == 1 else ("India MoHFW National Health Day" if tier == 2 else "Preventive Health Awareness")
                tier_gu = "વિશ્વ આરોગ્ય સંસ્થા (WHO) દિવસ" if tier == 1 else ("રાષ્ટ્રીય આરોગ્ય મિશન (MoHFW)" if tier == 2 else "નિવારક આરોગ્ય માર્ગદર્શિકા")
                
                d1 = theme_template["do1"]
                d2 = theme_template["do2"]
                dn1 = theme_template["dont1"]
                dn2 = theme_template["dont2"]
                
                entry = {
                    "id": day_id,
                    "month": month_num,
                    "day": day_num,
                    "date_en": date_en,
                    "date_gu": date_gu,
                    "tier": tier,
                    "tier_en": tier_en,
                    "tier_gu": tier_gu,
                    "title_en": theme_template["title_en"],
                    "title_gu": theme_template["title_gu"],
                    "theme_en": theme_template["theme_en"],
                    "theme_gu": theme_template["theme_gu"],
                    "cards": [
                        {
                            "type": "do", "index": 1,
                            "badge_en": "DO #1", "badge_gu": "આટલું જરૂર કરો #૧",
                            "title_en": d1[0], "title_gu": d1[1],
                            "desc_en": d1[2], "desc_gu": d1[3],
                            "photo": d1[4],
                            "ai_prompt": f"Realistic photographic Indian health awareness visual of {d1[0]}, warm clinical lighting, clean aesthetic, 8k quality."
                        },
                        {
                            "type": "do", "index": 2,
                            "badge_en": "DO #2", "badge_gu": "આટલું જરૂર કરો #૨",
                            "title_en": d2[0], "title_gu": d2[1],
                            "desc_en": d2[2], "desc_gu": d2[3],
                            "photo": d2[4],
                            "ai_prompt": f"Photorealistic Indian context photo representing {d2[0]}, golden sunlight, healthy lifestyle, 8k resolution."
                        },
                        {
                            "type": "dont", "index": 3,
                            "badge_en": "DON'T #1", "badge_gu": "આટલું ક્યારેય ન કરો #૧",
                            "title_en": dn1[0], "title_gu": dn1[1],
                            "desc_en": dn1[2], "desc_gu": dn1[3],
                            "photo": dn1[4],
                            "ai_prompt": f"High realism medical warning photography depicting {dn1[0]}, dramatic red warning lighting, educational caution."
                        },
                        {
                            "type": "dont", "index": 4,
                            "badge_en": "DON'T #2", "badge_gu": "આટલું ક્યારેય ન કરો #૨",
                            "title_en": dn2[0], "title_gu": dn2[1],
                            "desc_en": dn2[2], "desc_gu": dn2[3],
                            "photo": dn2[4],
                            "ai_prompt": f"Clinical warning photo showing danger of {dn2[0]}, crimson prohibition overlay, hyper-detailed."
                        }
                    ]
                }
            full_calendar.append(entry)
            
    return full_calendar

def main():
    print("Building full 365-day health calendar database...")
    calendar = generate_365_days()
    print(f"Total days generated: {len(calendar)}")
    
    # Save as JSON
    json_path = os.path.join("data", "health_365.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(calendar, f, ensure_ascii=False, indent=2)
    print(f"Saved {json_path}")
    
    # Also save as JS global variable for instant zero-CORS / offline local file inclusion
    js_path = os.path.join("js", "calendar-data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("// 365-Day Indian Health Calendar Data (Preloaded)\n")
        f.write("window.HEALTH_CALENDAR_DATA = ")
        json.dump(calendar, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Saved {js_path}")

if __name__ == "__main__":
    main()
