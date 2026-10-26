r"""35 Comprehensive Primary Health Care (CPHC) modules for District Health Training Calendar.
Drawn from Dr. Atul Dhuvad's official training repository at D:\Training Material:
- CHO Induction Modules & NQAS Work Instructions (6 CD, 7 NCD, 17 RMNCHA)
- OEEE Package (Oral, Eye, ENT, Emergency)
- EPMNS Package (Elderly CGA, Palliative, Mental Tele-MANAS, Substance AUDIT)
- Eat Right Tool Kit (ERT FSSAI / NHSRC)
- SASHAKT / NHSRC Comprehensive Primary Health Care Guidelines.
"""

CPHC_THEMES = [
    {
        "tier": 2, "cat": "anc_care",
        "title_en": "Antenatal Care & Safe Motherhood (ANC)",
        "title_gu": "સગર્ભાવસ્થા સંભાળ અને સુરક્ષિત માતૃત્વ",
        "theme_en": "Minimum 4 Quality ANC Visits | Daily IFA & Calcium",
        "theme_gu": "ઓછામાં ઓછી ૪ ગુણવત્તાયુક્ત તપાસ | નિયમિત આયર્ન-કેલ્શિયમ",
        "do1": (
            "Early ANC Registration in 1st Trimester",
            "ગર્ભાવસ્થાની વહેલી નોંધણી કરાવો",
            "Register pregnancy within the first 12 weeks at Ayushman Arogya Mandir for early ultrasound and health tracking.",
            "ગર્ભાવસ્થાના પહેલા ૧૨ અઠવાડિયામાં નજીકના આરોગ્ય કેન્દ્રમાં નોંધણી કરાવી મમતા કાર્ડ મેળવો.",
            "photos/cphc_anc_care_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A pregnant Indian woman in clean traditional saree consulting an ANM nurse at a rural health centre, receiving her official maternal child protection card. Soft clinic daylight, natural documentary realism."
        ),
        "do2": (
            "Daily IFA & Calcium Adherence",
            "આયર્ન અને કેલ્શિયમ નિયમિત લો",
            "Take 1 red IFA tablet daily after first trimester with lemon water; take calcium separately with water, never with tea.",
            "બીજા ત્રિમાસિકથી ૧૮૦ દિવસ સુધી રોજ એક આયર્નની ગોળી અને કેલ્શિયમ નિયમિત લો; ચા સાથે ક્યારેય ન લેવી.",
            "photos/cphc_anc_care_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian expectant mother seated on a veranda happily taking her daily prenatal nutrient tablet with a glass of clean water, family member smiling beside her. Warm morning home lighting."
        ),
        "dont1": (
            "Skipping Scheduled Tests & Scans",
            "તપાસ કે સોનોગ્રાફી ટાળવી નહીં",
            "Never skip blood pressure check, urine protein test, blood sugar, or anomaly ultrasound scans on PMSMA day (9th of month).",
            "બીપી, પેશાબની તપાસ, સુગર કે સોનોગ્રાફી છોડશો નહીં; દર મહિનાની ૯મી તારીખે પીએમએસએમએ દિવસે તપાસ કરાવો.",
            "photos/cphc_anc_care_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A lady doctor in white coat carefully conducting an abdominal ultrasound examination of an expectant mother in a clean primary health centre sonography room. Professional clinical lighting."
        ),
        "dont2": (
            "Ignoring Severe Danger Signs",
            "જોખમી લક્ષણોની અવગણના ન કરવી",
            "Swelling of face/hands, severe headache, bleeding, convulsions, or reduced fetal movement require immediate 108 hospital transfer.",
            "ચહેરા પર સોજો, તીવ્ર માથાનો દુખાવો, રક્તસ્ત્રાવ કે બાળકની હલચલ ઓછી થાય તો વિલંબ વગર ૧૦૮ બોલાવી હોસ્પિટલ પહોંચો.",
            "photos/cphc_anc_care_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian 108 emergency ambulance standing ready outside a community health centre, medical team escorting a patient with urgent care. Realistic daytime documentary."
        )
    },
    {
        "tier": 2, "cat": "delivery_dakshata",
        "title_en": "Safe Institutional Delivery & Dakshata Care",
        "title_gu": "સુરક્ષિત સંસ્થાકીય પ્રસૂતિ અને દક્ષતા સંભાળ",
        "theme_en": "100% Institutional Deliveries | Skilled Birth Attendance",
        "theme_gu": "૧૦૦% હોસ્પિટલ પ્રસૂતિ | પ્રશિક્ષિત સ્ટાફ દ્વારા સુરક્ષિત સુવાવડ",
        "do1": (
            "Plan Institutional Birth at FRU / CHC",
            "હોસ્પિટલમાં જ પ્રસૂતિ કરાવો",
            "Pre-identify delivery hospital, arrange 108 transport, and choose a birth companion in advance for peace of mind.",
            "પ્રસૂતિ માટે સરકારી હોસ્પિટલ અગાઉથી નક્કી રાખો, ૧૦૮ ની વ્યવસ્થા કરો અને સાથે રહેનાર સ્વજન તૈયાર રાખો.",
            "photos/cphc_delivery_dakshata_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian family and expectant mother arriving at a clean, well-lit hospital maternity registration counter, assisted by a smiling staff nurse. Optimistic institutional healthcare."
        ),
        "do2": (
            "Respectful Maternity Care in Labor Room",
            "દક્ષતા પ્રોટોકોલ અનુસાર સંભાળ",
            "Ensure skilled birth attendants follow Dakshata protocols, active stage 3 management, and provide gentle compassionate care.",
            "પ્રસૂતિ ખંડમાં પ્રશિક્ષિત નર્સ દ્વારા સ્વચ્છ, જંતુમુક્ત અને સન્માનપૂર્વક સંભાળ સુનિશ્ચિત કરો.",
            "photos/cphc_delivery_dakshata_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A skilled Indian midwife in clean surgical scrubs comforting a mother in a modern well-equipped government hospital labor room. Compassionate, professional healthcare realism."
        ),
        "dont1": (
            "Home Delivery by Unskilled Dai",
            "ઘેર ડિલિવરી કરાવવાનું જોખમ ન લેશો",
            "Never attempt home delivery by untrained individuals; it risks lethal postpartum hemorrhage, birth asphyxia, and maternal sepsis.",
            "અપ્રશિક્ષિત દાઈ દ્વારા ઘેર સુવાવડ કરાવવાથી માતામાં અતિશય રક્તસ્ત્રાવ અને બાળકમાં શ્વાસ રૂંધાવાનું મોટું જોખમ રહે છે.",
            "photos/cphc_delivery_dakshata_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean sterile delivery tray with sterile instruments prepared neatly on a trolley in an authorized medical facility, showing standard of hygiene. Clinical documentary photography."
        ),
        "dont2": (
            "Administering Labor Inducers at Home",
            "જાતે દુખાવાના ઇન્જેક્શન ન અપાવો",
            "Never purchase or administer oxytocin injections outside hospital to speed up labor; it causes catastrophic uterine rupture.",
            "સુવાવડ ઝડપી કરાવવા બહારથી કોઈ દવા કે ઇન્જેક્શન ન લેશો; તેનાથી ગર્ભાશય ફાટી જવાની જીવલેણ સમસ્યા થઈ શકે છે.",
            "photos/cphc_delivery_dakshata_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A doctor in consultation explaining safe medical procedures to an attentive rural couple at a desk, reinforcing safe institutional delivery practices. Clear daylight."
        )
    },
    {
        "tier": 2, "cat": "newborn_nssk",
        "title_en": "Immediate Newborn Care & Navjaat Shishu Suraksha",
        "title_gu": "નવજાત શિશુની તાત્કાલિક સંભાળ અને સુરક્ષા",
        "theme_en": "Dry & Wrap Promptly | Colostrum in First Hour",
        "theme_gu": "બાળકને તુરંત લૂછી ગરમ રાખો | પ્રથમ કલાકમાં ધાવણ",
        "do1": (
            "Immediate Drying & Skin-to-Skin Warmth",
            "બાળકને લૂછી માતાની છાતી સરસું રાખો",
            "Dry newborn immediately with a dry clean towel, discard wet cloth, and place skin-to-skin on mother's chest to prevent hypothermia.",
            "જન્મતા વેંત બાળકને સ્વચ્છ ગરમ કપડાથી લૂછી ભીનું કપડું હટાવો અને માતાની છાતી સાથે અડાડી ગરમ રાખો.",
            "photos/cphc_newborn_nssk_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A newborn infant wrapped snugly in a clean warm cotton cloth resting gently on its mother's chest in a hospital post-delivery bed, serene atmosphere. Natural soft window lighting."
        ),
        "do2": (
            "Initiate Breastfeeding in First Hour",
            "પ્રથમ કલાકમાં કોલોસ્ટ્રમ (ધાવણ) આપો",
            "Give yellow thick colostrum within 60 minutes of delivery; it serves as baby's first natural immunity vaccine against infections.",
            "જન્મના પહેલા ૬૦ મિનિટમાં જ માતાનું પીળું ઘટ્ટ ધાવણ આપો; તે બાળકની રોગપ્રતિકારક શક્તિ વધારે છે.",
            "photos/cphc_newborn_nssk_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian mother in a maternity ward nursing her newborn calmly with guidance from a supportive female healthcare worker. Warm, authentic maternal care."
        ),
        "dont1": (
            "Delay First Bath for at Least 48 Hours",
            "૪૮ કલાક સુધી સ્નાન ન કરાવવું",
            "Never give a bath on the first day; newborns lose body heat rapidly leading to cold stress, respiratory distress, and death.",
            "જન્મ પછી ઓછામાં ઓછા બે દિવસ બાળકને નવડાવવું નહીં; તેનાથી શરીર ઠંડુ પડી જઈ શ્વાસની તકલીફ થઈ શકે છે.",
            "photos/cphc_newborn_nssk_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A newborn sleeping peacefully in a cot wearing a warm woolen knitted bonnet and soft socks, snugly swaddled. Cozy domestic simplicity."
        ),
        "dont2": (
            "Applying Substances to Umbilical Stump",
            "નાળ પર કશું જ ન લગાવવું",
            "Never apply cow dung, turmeric, kajal, or oil to the umbilical cord. Keep it clean and dry until it drops off naturally.",
            "બાળકની નાળ પર હળદર, છાણ, તેલ કે કાજલ ક્યારેય ન લગાવવું; નાળને સાવ કોરી અને ખુલ્લી રાખો જેથી ધનુર ન થાય.",
            "photos/cphc_newborn_nssk_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A nurse using clean dry cotton to gently inspect a newborn's dry umbilical area on an examination table, demonstrating clean cord management. Clinical clarity."
        )
    },
    {
        "tier": 2, "cat": "iycf_nutrition",
        "title_en": "Infant & Young Child Feeding (IYCF)",
        "title_gu": "શિશુ અને બાળ આહાર (IYCF) માર્ગદર્શિકા",
        "theme_en": "Exclusive Breastfeeding 6 Months | Complementary Feeds",
        "theme_gu": "૬ મહિના ફક્ત ધાવણ | ૬ મહિના પછી ઉપરી પૌષ્ટિક આહાર",
        "do1": (
            "Exclusive Breastfeeding for 6 Months",
            "૬ મહિના ફક્ત માતાનું દૂધ જ આપો",
            "Provide zero water, honey, ghutti, or animal milk for first 6 months. Mother's milk contains 88% water and all essential nutrients.",
            "૬ મહિના સુધી બાળકને પાણી, ઘૂંટી કે મધ કશું જ ન આપો; ગરમીમાં પણ માતાના દૂધમાંથી પૂરતું પાણી મળી રહે છે.",
            "photos/cphc_iycf_nutrition_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A happy healthy 4-month-old Indian baby lying on a colorful cotton quilt on a village veranda, smiling cheerfully. Vibrant, joyful natural light."
        ),
        "do2": (
            "Start Mashed Complementary Feeds at 6 Months",
            "૬ મહિને પૌષ્ટિક ઉપરી આહાર શરૂ કરો",
            "At completed 6 months, begin thick mashed foods: dal-khichdi with ghee, mashed banana, boiled pumpkin, 2-3 times daily.",
            "૬ મહિના પૂરા થતાં જ સ્તનપાન સાથે ઘી વાળી મગની દાળ-ખીચડી, કેળું અને બાફેલી શાકભાજી વાટકી-ચમચીથી શરૂ કરો.",
            "photos/cphc_iycf_nutrition_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian mother sitting in a clean kitchen feeding thick mashed khichdi to her smiling 7-month-old infant using a small stainless steel spoon. Homely warmth."
        ),
        "dont1": (
            "Avoid Bottle Feeding & Packaged Formula",
            "બોટલ કે ડબ્બાના દૂધથી બચો",
            "Never use plastic feeding bottles or pacifiers; unhygienic nipples cause recurring diarrhea, ear infections, and malnutrition.",
            "પ્લાસ્ટિકની બોટલથી બાળકના પેટમાં જંતુઓ જઈ ઝાડા-ઊલટી થાય છે; ઉપરી આહાર હંમેશા વાટકી-ચમચીથી જ આપો.",
            "photos/cphc_iycf_nutrition_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean stainless steel bowl, spoon and fresh homemade infant meal neatly arranged on a clean kitchen counter. Wholesome nutrition focus."
        ),
        "dont2": (
            "Never Feed Watery Dilute Gruels",
            "પાતળી રાબ કે દાળનું પાણી ન આપવું",
            "Do not feed only watery dal-water or thin liquids; young children need thick, calorie-dense foods to prevent stunting and wasting.",
            "માત્ર દાળનું પાણી આપવાથી બાળકનું પેટ ભરાય છે પણ પોષણ મળતું નથી; ઘટ્ટ મસળેલો ખોરાક ખવડાવવાની ટેવ પાડો.",
            "photos/cphc_iycf_nutrition_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An Anganwadi worker demonstrating nutritious recipe preparation with boiled pulses and vegetables to a circle of village mothers in an Anganwadi centre. Educational community spirit."
        )
    },
    {
        "tier": 2, "cat": "hbyc_childcare",
        "title_en": "Home-Based Care for Young Child (HBYC)",
        "title_gu": "બાળ સંભાળ ગૃહ મુલાકાત (HBYC)",
        "theme_en": "Growth Monitoring & Early Milestone Tracking",
        "theme_gu": "બાળકની ઊંચાઈ-વજન માપન અને વિકાસ પર દેખરેખ",
        "do1": (
            "Welcome Structured ASHA Home Visits",
            "આશા બહેનની મુલાકાતમાં સહકાર આપો",
            "Ensure ASHA conducts scheduled visits at 3, 6, 9, 12, and 15 months to check nutrition, immunization, and child development.",
            "બાળકના ૩, ૬, ૯, ૧૨ અને ૧૫મા મહિને આશા બહેનને ઘરે બોલાવી વજન અને તબિયતની તપાસ કરાવો.",
            "photos/cphc_hbyc_childcare_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An ASHA worker in uniform visiting an Indian home courtyard, interacting with a smiling mother holding her energetic toddler. Warm village community healthcare."
        ),
        "do2": (
            "Stimulate Cognitive & Motor Milestones",
            "બાળક સાથે વાતચીત અને રમતો રમો",
            "Talk, sing, play, and read colorful picture books with your child daily; early loving interaction shapes lifelong brain architecture.",
            "બાળક સાથે રોજ વાતો કરો, ગીતો ગાઓ અને રંગબેરંગી ચિત્રો બતાવો; તેનાથી બાળકના મગજનો તેજસ્વી વિકાસ થાય છે.",
            "photos/cphc_hbyc_childcare_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian father sitting on a wooden bench playing interactive clapping games with his giggling one-year-old child in sunny afternoon light. Tender family moment."
        ),
        "dont1": (
            "Zero Screen Time Under Age 2",
            "નાના બાળકોને મોબાઇલ ન આપવો",
            "Do not hand smartphones to infants to make them eat; screen time delays speech, social milestones, and induces irritability.",
            "જમાડવા માટે બાળકને મોબાઇલની સ્ક્રીન બતાવવાની આદત ન પાડો; તેનાથી બોલવામાં અને સમજવામાં વિલંબ થાય છે.",
            "photos/cphc_hbyc_childcare_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A young child happily stacking colorful wooden toy blocks on a floor mat instead of digital screens, focused creative play. Bright natural room light."
        ),
        "dont2": (
            "Never Miss Monthly Anganwadi Weighing",
            "આંગણવાડીમાં વજન કરાવવાનું ન ચૂકવું",
            "Plot your child's weight monthly on MCP green curve; catch growth faltering immediately before severe malnutrition sets in.",
            "દર મહિને આંગણવાડીમાં બાળકના વજનની નોંધ કરાવો; વજનનો કાંટો નીચે જાય તો તુરંત બાલસેવા કેન્દ્રનો સંપર્ક કરો.",
            "photos/cphc_hbyc_childcare_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An Anganwadi worker weighing a toddler gently using a hanging spring scale while the mother holds the child's hands reassuringly. Clear documentary realism."
        )
    },
    {
        "tier": 2, "cat": "childhood_idcf",
        "title_en": "Childhood Diarrhea & Pneumonia Control (IDCF / SAANS)",
        "title_gu": "બાળ ઝાડા અને ન્યુમોનિયા નિયંત્રણ",
        "theme_en": "ORS + 14 Days Zinc | Spot Fast Breathing",
        "theme_gu": "ઝાડામાં ઓઆરએસ + ઝિંક | ન્યુમોનિયામાં ઝડપી શ્વાસ ઓળખો",
        "do1": (
            "Prepare WHO-ORS & Give 14 Days Zinc",
            "ઓ.આર.એસ. અને ૧૪ દિવસ ઝિંક આપો",
            "Dissolve 1 WHO-ORS packet in 1L clean water. Give frequent sips during diarrhea plus dispersible zinc tablets daily for 14 full days.",
            "૧ લીટર સ્વચ્છ પાણીમાં આખું ઓઆરએસ ઓગાળો; ઝાડા બંધ થાય તો પણ ૧૪ દિવસ પૂરા ઝિંકની ગોળી આપો જેથી આંતરડાં મજબૂત થાય.",
            "photos/cphc_childhood_idcf_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A mother preparing fresh ORS in a one-litre clean glass jug with clean water on an Indian kitchen table. Calm, clear domestic hygiene focus."
        ),
        "do2": (
            "Spot Fast Breathing & Chest Indrawing",
            "ઝડપી શ્વાસ અને પાંસળી ખેંચાવી ઓળખો",
            "Count breaths for 1 minute: >50/min (2-11m) or >40/min (1-5y) or lower chest indrawing signals pneumonia; seek urgent medical clinic.",
            "બાળકની પાંસળી અંદર ખાડા પડતી હોય કે શ્વાસ ઝડપથી ચાલતો હોય તો ન્યુમોનિયા હોઈ શકે છે; તાત્કાલિક પ્રાથમિક આરોગ્ય કેન્દ્ર જાઓ.",
            "photos/cphc_childhood_idcf_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A Community Health Officer (CHO) gently using a stethoscope to listen to a child's lungs in a clean rural health clinic room, mother supporting child. Reassuring clinical care."
        ),
        "dont1": (
            "Never Withhold Fluids During Diarrhea",
            "માંદગીમાં ધાવણ કે પ્રવાહી બંધ ન કરવું",
            "Never stop breastfeeding or fluids during loose motions; withholding fluids causes rapid life-threatening dehydration and shock.",
            "ઝાડામાં બાળકનું ધાવણ કે પાણી ક્યારેય રોકવું નહીં; પ્રવાહી બંધ કરવાથી શરીરમાં પાણી ખૂટી જઈ જીવનું જોખમ થાય છે.",
            "photos/cphc_childhood_idcf_card3.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian mother tenderly nursing and hydrating her infant on a cot in a comfortable shaded room. Loving maternal care documentary style."
        ),
        "dont2": (
            "Never Give Adult Cough Syrups to Infants",
            "બાળકોને જાતે કફ સિરપ ન આપવી",
            "Over-the-counter adult cold syrups cause respiratory depression in children. Always get respiratory infections evaluated by doctor.",
            "બાળકને મેડિકલ સ્ટોરમાંથી જાતે કફ સિરપ લાવીને ન પીવડાવો; ફેફસાંના ચેપ માટે ડોક્ટર પાસે સાચી સારવાર કરાવો.",
            "photos/cphc_childhood_idcf_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A doctor reviewing a child's medical case paper in an OPD room, explaining proper treatment without harmful unprescribed syrups. Professional clinical atmosphere."
        )
    },
    {
        "tier": 2, "cat": "uip_vaccination",
        "title_en": "Universal Immunization Programme (UIP)",
        "title_gu": "સાર્વત્રિક રસીકરણ કાર્યક્રમ (UIP)",
        "theme_en": "Complete Protection from 12 Vaccine-Preventable Diseases",
        "theme_gu": "૧૨ જીવલેણ રોગો સામે રસીકરણનું મજબૂત સુરક્ષા કવચ",
        "do1": (
            "Complete All Scheduled Vaccines on Mamta Diwas",
            "મમતા દિવસે સમયસર રસી મુકાવો",
            "Ensure on-time administration of BCG, Hep-B, Pentavalent, Rotavirus, fIPV, PCV, and MR vaccines at nearest Anganwadi session.",
            "દર બુધવારે યોજાતા મમતા દિવસે બાળકને પોલિયો, પેન્ટા, રોટા, પીસીવી અને ઓરી-રૂબેલાની રસી સમયસર અપાવો.",
            "photos/cphc_uip_vaccination_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An ANM nurse gently administering a routine immunization injection to a calm infant seated on mother's lap during a village health day session. Professional maternal-child healthcare."
        ),
        "do2": (
            "Preserve Mamta Immunization Card Safely",
            "મમતા કાર્ડ સાચવીને સાથે રાખો",
            "Keep the Mamta card safe in a protective pouch. Bring it to every health visit to record doses and note the next upcoming due date.",
            "મમતા કાર્ડ પ્લાસ્ટિક કવરમાં સાચવીને રાખો અને દરેક મુલાકાતે સાથે લાવો જેથી આગામી રસીની તારીખ યાદ રહે.",
            "photos/cphc_uip_vaccination_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An organized Indian mother holding an official Mamta card folder while an ANM notes dates in a register. Methodical public healthcare documentation."
        ),
        "dont1": (
            "Never Skip Vaccine Due to Mild Cold or Fever",
            "સામાન્ય તાવમાં રસી મુલતવી ન રાખવી",
            "Mild cough, runny nose, or minor fever is not a contraindication for vaccines. Postponing leaves your baby vulnerable to fatal diseases.",
            "સામાન્ય શરદી કે હળવા તાવમાં રસી આપવાનું ટાળશો નહીં; રસી મુલતવી રાખવાથી બાળક જોખમી રોગો સામે અસુરક્ષિત રહે છે.",
            "photos/cphc_uip_vaccination_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean vaccine cold box with ice packs and properly arranged vials in a primary health sub-centre, showing pristine cold-chain management. Sharp medical focus."
        ),
        "dont2": (
            "Never Leave Missed Booster Doses Incomplete",
            "છૂટેલા બુસ્ટર ડોઝમાં વિલંબ ન કરવો",
            "If any scheduled dose is delayed, do not restart from zero; visit your ANM to resume and complete all remaining booster shots promptly.",
            "કોઈ કારણસર રસી છૂટી ગઈ હોય તો ચિંતા વગર એએનએમનો સંપર્ક કરો અને બાકીના ડોઝ વહેલી તકે પૂરા કરાવો.",
            "photos/cphc_uip_vaccination_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An ANM reviewing a village due-list register and explaining upcoming vaccine schedule to a group of rural mothers. Engaging community healthcare realism."
        )
    },
    {
        "tier": 2, "cat": "rbsk_screening",
        "title_en": "Child Health Screening & Early Intervention (RBSK)",
        "title_gu": "રાષ્ટ્રીય બાળ સ્વાસ્થ્ય કાર્યક્રમ (RBSK 4Ds)",
        "theme_en": "Detect Defects, Deficiencies, Diseases & Delays Early",
        "theme_gu": "જન્મજાત ખામીઓ અને વિકાસ વિલંબનું વહેલું નિદાન",
        "do1": (
            "Screen for 4Ds with RBSK Mobile Health Teams",
            "શાળા-આંગણવાડીમાં RBSK તપાસ કરાવો",
            "Support RBSK doctor teams screening children aged 0-18 for Birth Defects, Deficiencies, Childhood Diseases, and Developmental Delays.",
            "શાળા અને આંગણવાડીમાં આવતી આરબીએસકે ટીમ પાસે બાળકની જન્મજાત ખોડખાંપણ, આંખ, કાન અને પોષણની તપાસ કરાવો.",
            "photos/cphc_rbsk_screening_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A dedicated RBSK doctor examining a young school student in a brightly lit primary school classroom, child smiling confidently. Uplifting public school health check."
        ),
        "do2": (
            "Utilize District Early Intervention Centers (DEIC)",
            "DEIC કેન્દ્ર પર મફત થેરાપી મેળવો",
            "Refer children with developmental delays or sensory impairments to DEIC for free comprehensive therapy, hearing aids, and surgeries.",
            "બોલવામાં, સાંભળવામાં કે ચાલવામાં મુશ્કેલી હોય તો જિલ્લા હોસ્પિટલના DEIC સેન્ટર પર મફત ફિઝિયોથેરાપી અને સ્પીચ થેરાપી મેળવો.",
            "photos/cphc_rbsk_screening_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A child therapist gently assisting a young child in a colorful therapy room equipped with sensory toys and balance balls. Compassionate pediatric rehabilitation."
        ),
        "dont1": (
            "Never Ignore Squint, Limp or Delayed Speech",
            "આંખનો ત્રાસાદોષ કે બહેરાશ ન અવગણવી",
            "Do not assume children will naturally outgrow crossed eyes or walking delays; early intervention before age 3 produces best outcomes.",
            "બાળકની આંખમાં ત્રાસાદોષ હોય કે મોડું બોલે તો આપમેળે મટી જશે તેમ માની બેસી ન રહો; વહેલી તપાસથી ખામી દૂર થાય છે.",
            "photos/cphc_rbsk_screening_card3.png",
            "Editorial realistic photograph, authentic Indian setting. An optometrist gently checking the vision alignment of a young child with colorful fixation targets in a child eye clinic. Focused medical examination."
        ),
        "dont2": (
            "Never Hide Congenital Cleft Lip or Clubfoot",
            "જન્મજાત ખોડખાંપણ છુપાવવી નહીં",
            "Conditions like cleft lip, clubfoot, and congenital cataract are 100% surgically correctable for free under government RBSK program.",
            "હોઠ ફાટેલો હોય કે પગનો પંજો વળેલો હોય તો અંધશ્રદ્ધામાં ન પડો; સરકારી યોજના હેઠળ મફત ઓપરેશનથી બાળક સાજું થઈ જાય છે.",
            "photos/cphc_rbsk_screening_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A smiling recovered child with parents thanking a pediatric surgeon in an outpatient clinic room, radiant hopeful mood. Uplifting documentary realism."
        )
    },
    {
        "tier": 2, "cat": "rksk_adolescent",
        "title_en": "Adolescent Health & Wellness (RKSK)",
        "title_gu": "કિશોર-કિશોરી સ્વાસ્થ્ય અને સુખાકારી (RKSK)",
        "theme_en": "Weekly Iron Folic Acid (WIFS) | Menstrual Dignity",
        "theme_gu": "સાપ્તાહિક આયર્ન (WIFS) | માસિક ધર્મની સ્વચ્છતા",
        "do1": (
            "Take Weekly Blue WIFS Tablet on Mondays",
            "દર સોમવારે વાદળી આયર્ન ગોળી લો",
            "Adolescent boys and girls aged 10-19 should take one blue Iron-Folic Acid tablet weekly after lunch in schools to conquer anemia.",
            "શાળામાં દર સોમવારે જમ્યા પછી અપાતી વાદળી આયર્નની ગોળી અવશ્ય લો; તેનાથી શરીરમાં સ્ફૂર્તિ વધે છે અને ભણવામાં ધ્યાન રહે છે.",
            "photos/cphc_rksk_adolescent_card1.png",
            "Editorial realistic photograph, authentic Indian setting. Indian adolescent school students in uniforms sitting at desks, receiving iron nutritional supplements with clean drinking water. Cheerful adolescent health focus."
        ),
        "do2": (
            "Practice Safe Menstrual Hygiene & Pad Disposal",
            "સ્વચ્છ પેડ વાપરો અને ૬ કલાકે બદલો",
            "Use clean sanitary pads, change them every 4-6 hours, wash with clean water, and dispose wrapped in paper in dedicated dustbins.",
            "માસિક દરમિયાન સ્વચ્છ પેડ વાપરો, દર ૪-૬ કલાકે બદલો અને કાગળમાં લપેટી કચરાપેટીમાં નાખો; ગંદા કપડાનો ઉપયોગ ન કરો.",
            "photos/cphc_rksk_adolescent_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A female health educator conducting a friendly, informative menstrual health awareness session with teenage girls in an airy community hall. Dignified, supportive empowerment."
        ),
        "dont1": (
            "Avoid Skipping Meals for Packaged Junk Food",
            "ભોજન છોડી જંકફૂડ ખાવાની ટેવ ટાળો",
            "Never replace nutritious home-cooked meals with packaged snacks, chips, or roadside colas; they cause severe micronutrient malnutrition.",
            "બહારના તળેલા પેકેટ, મેગી કે કોલ્ડડ્રિંક્સ ખાવાનું ટાળો; દાળ, ભાત, શાક, રોટલી અને સલાડથી શરીર મજબૂત બને છે.",
            "photos/cphc_rksk_adolescent_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A healthy snack spread on a study desk: roasted chana, seasonal guava slices, and roasted foxnuts (makhana) in small clean bowls. Wholesome adolescent nutrition."
        ),
        "dont2": (
            "Never Suffer Mental Anxiety in Silence",
            "માનસિક મૂંઝવણ મનમાં ન દબાવવી",
            "Visit the AFHC (Maitri Clinic) at CHC for free, confidential guidance on emotional stress, body changes, and peer pressure.",
            "પરીક્ષાનો તણાવ કે શારીરિક ફેરફારોની મૂંઝવણ હોય તો નજીકના મૈત્રી ક્લિનિકના કાઉન્સેલર સાથે ખુલીને વાત કરો.",
            "photos/cphc_rksk_adolescent_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An adolescent counselor in a friendly clinic consulting a teenager attentively, empathetic and respectful atmosphere. Natural indoor clinic lighting."
        )
    },
    {
        "tier": 2, "cat": "family_planning",
        "title_en": "Modern Family Planning & Spacing Methods",
        "title_gu": "આધુનિક કુટુંબ કલ્યાણ અને અંતર રાખવાની પદ્ધતિઓ",
        "theme_en": "Safe Spacing with Antara, Chhaya & PPIUCD",
        "theme_gu": "અંતરા, છાયા અને પીપીઆઈયુસીડીથી સુરક્ષિત અંતર",
        "do1": (
            "Maintain 3-Year Spacing Between Children",
            "બે બાળકો વચ્ચે ૩ વર્ષનું અંતર રાખો",
            "A healthy 3-year gap between births allows mother's body to replenish iron stores and gives every infant dedicated nurturing.",
            "બે બાળકો વચ્ચે ઓછામાં ઓછું ૩ વર્ષનું અંતર રાખવાથી માતાનું સ્વાસ્થ્ય જળવાય છે અને બાળકનો વિકાસ સારો થાય છે.",
            "photos/cphc_family_planning_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian couple happily spending time with their healthy energetic toddler in a home courtyard, peaceful family life. Warm domestic documentary."
        ),
        "do2": (
            "Choose Antara Injectable or Chhaya Pills",
            "અંતરા ઇન્જેક્શન કે છાયા ગોળી અપનાવો",
            "Avail free non-hormonal weekly Chhaya tablets, 3-monthly Antara injections, or long-acting postpartum IUCD at government facilities.",
            "સરકારી આરોગ્ય કેન્દ્ર પરથી ૩ મહિને લેવાનું અંતરા ઇન્જેક્શન અથવા બિન-હોર્મોનલ છાયા ગોળીઓ નિઃશુલ્ક મેળવો.",
            "photos/cphc_family_planning_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A female Community Health Officer (CHO) at an Ayushman Arogya Mandir counseling a married couple about modern spacing methods using informational brochures. Respectful, professional counseling."
        ),
        "dont1": (
            "Never Rely on Emergency Pills as Regular Contraception",
            "ઇમરજન્સી પિલ્સનો વારંવાર ઉપયોગ ન કરવો",
            "Emergency contraceptive pills (ECPs) are only for rare unforeseen failures; frequent use disrupts hormonal cycles and fails.",
            "ઇમરજન્સી ગોળીઓ નિયમિત કુટુંબ નિયોજન માટે નથી; વારંવાર લેવાથી હોર્મોન્સ અસંતુલિત થાય છે અને અનિચ્છનીય ગર્ભ રહે છે.",
            "photos/cphc_family_planning_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean healthcare dispensary desk with organized modern family planning commodities neatly displayed for counseling. Professional healthcare realism."
        ),
        "dont2": (
            "Discard Myths About Male Vasectomy (NSV)",
            "પુરુષ નસબંધી અંગેની ગેરમાન્યતાઓ દૂર કરો",
            "Non-Scalpel Vasectomy (NSV) is a simple, painless 10-minute procedure with zero impact on physical strength or marital life.",
            "પુરુષ નસબંધીથી નબળાઈ આવતી નથી; તે માત્ર ૧૦ મિનિટની સાદી, ટાંકા વગરની અને સાવ સલામત પ્રક્રિયા છે.",
            "photos/cphc_family_planning_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A male health worker speaking reassuringly with an adult Indian man during a health camp, building awareness on male participation in family planning. Natural daylight."
        )
    },
    {
        "tier": 2, "cat": "tb_elimination",
        "title_en": "Tuberculosis Elimination & Nikshay Care (NTEP)",
        "title_gu": "ક્ષય (ટીબી) મુક્તિ અને નિક્ષય યોજના",
        "theme_en": "2-Week Cough Check | Complete 6-Month DOTS",
        "theme_gu": "૨ અઠવાડિયાની ખાંસી તપાસાવો | ૬ મહિના પૂરી દવા લો",
        "do1": (
            "Screen Persistent Cough >2 Weeks with CBNAAT",
            "ગળફાની મોલેક્યુલર (CBNAAT) તપાસ કરાવો",
            "Test cough lasting over 2 weeks with free rapid molecular tests (CBNAAT / Truenat) at government centers for early detection.",
            "બે અઠવાડિયાથી વધુ ઉધરસ, સાંજે તાવ કે વજન ઘટતું હોય તો સરકારી હોસ્પિટલમાં ગળફાની સીબીનાટ તપાસ મફત કરાવો.",
            "photos/cphc_tb_elimination_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A laboratory technician wearing protective mask and gloves processing a sputum specimen in a clean, certified government TB diagnostic lab. Precision clinical lighting."
        ),
        "do2": (
            "Avail Nikshay Poshan Direct DBT Support",
            "નિક્ષય પોષણ સહાયના નાણાં મેળવો",
            "Every registered TB patient receives direct monthly DBT bank transfers to afford protein-rich nutrition like eggs, pulses, and milk.",
            "નિક્ષય પોર્ટલ પર નોંધણી કરાવી પૌષ્ટિક આહાર માટે દર મહિને સરકાર તરફથી સીધા બેંક ખાતામાં પોષણ સહાય મેળવો.",
            "photos/cphc_tb_elimination_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A recovered patient in good health holding a bowl of wholesome food and milk, chatting gratefully with a community health volunteer. Uplifting public health recovery."
        ),
        "dont1": (
            "Never Stop TB Medicines Midway When Feeling Better",
            "સારું લાગે તો પણ ટીબીની દવા બંધ ન કરવી",
            "Stopping DOTS treatment midway after symptoms improve causes lethal multi-drug resistant TB (MDR-TB). Complete all 6 months.",
            "બે મહિનામાં સારું લાગવા માંડે તો પણ દવા અધૂરી ન છોડશો; અધૂરી દવાથી દવા-પ્રતિરોધી (MDR) ટીબી થાય છે જે જીવલેણ છે.",
            "photos/cphc_tb_elimination_card3.png",
            "Editorial realistic photograph, authentic Indian setting. An adult patient carefully organizing their daily 4-FDC blister strip calendar pack on a side table with a glass of water. Disciplined healthcare routine."
        ),
        "dont2": (
            "Never Spit Openly or Cough Without Covering Mouth",
            "ખુલ્લામાં થૂંકવું નહીં, મોં ઢાંકો",
            "Always cover mouth with a handkerchief while coughing; open spitting spreads live tubercle bacilli into ambient community air.",
            "ઉધરસ ખાતી વખતે મોં આડે રૂમાલ રાખો અને ગમે ત્યાં ન થૂંકો; તમારા થૂંકવાથી ઘરમાં નાના બાળકો અને વડીલોને ચેપ લાગે છે.",
            "photos/cphc_tb_elimination_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An adult using a clean handkerchief to cover mouth and nose while coughing in a well-ventilated room, responsible hygiene practice. Documentary realism."
        )
    },
    {
        "tier": 2, "cat": "vector_malaria_dengue",
        "title_en": "Vector-Borne Disease Prevention (Malaria & Dengue)",
        "title_gu": "મચ્છરજન્ય રોગો (મેલેરિયા, ડેન્ગ્યુ) નિયંત્રણ",
        "theme_en": "Dry Day Weekly | Sleep Under LLIN Bed Nets",
        "theme_gu": "અઠવાડિયે એક દિવસ ડ્રાય-ડે | મચ્છરદાનીનો ઉપયોગ",
        "do1": (
            "Observe Weekly Sunday Dry Day at Home",
            "દર રવિવારે કૂલર-કૂંડાં સૂકવી સાફ કરો",
            "Scrub, empty, and dry all water containers, air coolers, flower pots, and drums every Sunday to destroy Aedes mosquito larvae.",
            "દર રવિવારે પાણીની ટાંકી, કૂલર, ફ્રિજની ટ્રે અને કૂંડાં સાફ કરી સૂકવી નાખો; તેનાથી ડેન્ગ્યુના મચ્છર પેદા થતા અટકે છે.",
            "photos/cphc_vector_malaria_dengue_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian family actively scrubbing and drying an outdoor air cooler and cleaning flower pots in a sunny courtyard on Sunday morning. Positive domestic sanitation."
        ),
        "do2": (
            "Get Blood Tested for Every Fever Case Within 24h",
            "તાવ આવે ત્યારે લોહીની તપાસ કરાવો",
            "Visit health sub-centre for rapid diagnostic tests (RDT) and blood smear examination for timely species-specific malaria therapy.",
            "તાવ આવે ત્યારે ઘેર બેઠા રહેવાને બદલે ૨૪ કલાકમાં આરોગ્ય કાર્યકર પાસે લોહીની તપાસ કરાવો અને મેલેરિયાની સાચી દવા લો.",
            "photos/cphc_vector_malaria_dengue_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A multi-purpose health worker (MPHW) performing a rapid finger-prick diagnostic test for malaria on an adult villager at a community health desk. Authentic rural field healthcare."
        ),
        "dont1": (
            "Never Leave Stagnant Water Around Roofs & Tires",
            "ધાબા પર ભંગાર કે ભરાયેલું પાણી ન રાખો",
            "Discard discarded tires, coconut shells, and plastic cups outdoors; clear terrace roof drains to prevent mosquito breeding grounds.",
            "ધાબા પર કે ઘરની આસપાસ જૂના ટાયર, નાળિયેરના કોચલા કે તૂટેલા ડબ્બા ન રાખો; તેમાં ભરાયેલા વરસાદી પાણીમાં મચ્છર ઈંડા મૂકે છે.",
            "photos/cphc_vector_malaria_dengue_card3.png",
            "Editorial realistic photograph, authentic Indian setting. Clean swept terrace rooftop under blue sky with clear unobstructed drains and no standing water, showing good municipal vector control. Documentary perspective."
        ),
        "dont2": (
            "Never Take Painkillers Like Brufen/Aspirin in Fever",
            "ડેન્ગ્યુ તાવમાં બ્રુફેન કે એસ્પિરિન ન લેવી",
            "In viral fevers and dengue, never self-medicate with Brufen, Combiflam, or Aspirin; they cause fatal internal gastrointestinal bleeding.",
            "ડેન્ગ્યુ કે વાયરલ તાવમાં માત્ર પેરાસિટામોલ જ લો; દુખાવાની ગોળીઓ લેવાથી પ્લેટલેટ્સ ઘટવા સાથે આંતરિક રક્તસ્ત્રાવ થઈ શકે છે.",
            "photos/cphc_vector_malaria_dengue_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A doctor in consultation examining an adult patient with fever, calmly reviewing prescription medication and emphasizing plenty of hydration. Clinical documentary."
        )
    },
    {
        "tier": 2, "cat": "leprosy_nlep",
        "title_en": "Leprosy Eradication & Disability Prevention (NLEP)",
        "title_gu": "રક્તપિત્ત (લેપ્રસી) મુક્તિ અને વિકલાંગતા નિવારણ",
        "theme_en": "Early MDT Treatment Cures Leprosy Completely",
        "theme_gu": "પ્રારંભિક MDT સારવારથી રક્તપિત્ત સંપૂર્ણ મટે છે",
        "do1": (
            "Inspect Skin for Numb Hypopigmented Patches",
            "સંવેદના વગરના આછા ડાઘ તપાસાવો",
            "Check for pale or reddish skin patches with complete loss of sensation to light touch, heat, or cold. Report early for free tests.",
            "ચામડી પર આછો કે લાલાશ પડતો ડાઘ હોય અને ત્યાં અડવાથી ખબર ન પડે તો તે રક્તપિત્ત હોઈ શકે છે; તુરંત તપાસ કરાવો.",
            "photos/cphc_leprosy_nlep_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A dermatologist gently using a sterile cotton wisp to test light sensation on a patient's forearm patch in a bright clinic room. Careful clinical examination."
        ),
        "do2": (
            "Complete Full Multi-Drug Therapy (MDT) Course",
            "સરકારી હોસ્પિટલમાંથી મફત MDT કોર્સ કરો",
            "Free blister-pack MDT cures leprosy in 6 to 12 months. The disease becomes completely non-infectious after the very first dose.",
            "સરકારી આરોગ્ય કેન્દ્ર પરથી મફત મળતી એમડીટી (MDT) દવા પૂરા સમય માટે લો; પ્રથમ ડોઝથી જ રોગ બીજામાં ફેલાતો અટકે છે.",
            "photos/cphc_leprosy_nlep_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An adult patient receiving official blister-packed MDT medication from a courteous healthcare provider in an outpatient clinic. Dignified public health support."
        ),
        "dont1": (
            "Never Stigmatize or Isolate Leprosy Patients",
            "રક્તપિત્તના દર્દી સાથે ભેદભાવ ન કરવો",
            "Leprosy is not a hereditary curse or punishment; it is caused by simple bacteria (Mycobacterium leprae) and is 100% curable.",
            "રક્તપિત્ત કોઈ પાપ કે અસ્પૃશ્ય રોગ નથી; દર્દી સાથે સામાન્ય વ્યવહાર રાખો, ભેદભાવ ન કરો અને પરિવારમાં સન્માન આપો.",
            "photos/cphc_leprosy_nlep_card3.png",
            "Editorial realistic photograph, authentic Indian setting. An inclusive community gathering in an Indian village where community members sit warmly together on a veranda sharing tea, breaking social stigma. Heartwarming social cohesion."
        ),
        "dont2": (
            "Never Neglect Numb Hands & Feet to Prevent Deformity",
            "અનુભૂતિ વગરના હાથ-પગની ઉપેક્ષા ન કરવી",
            "Wear soft micro-cellular rubber (MCR) footwear; protect numb hands from hot cooking utensils to avoid burns and irreversible disability.",
            "હાથ-પગમાં અહેસાસ ન થતો હોય તો રસોઈમાં ગરમ વાસણ સીધા ન પકડવા અને બહાર નીકળતી વખતે એમસીઆર ચંપલ અવશ્ય પહેરવા.",
            "photos/cphc_leprosy_nlep_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An adult stepping into a pair of comfortable, certified soft MCR protective footwear on a clean doorstep. Practical disability prevention."
        )
    },
    {
        "tier": 2, "cat": "hepatitis_waterborne",
        "title_en": "Viral Hepatitis & Waterborne Disease Prevention",
        "title_gu": "ઝેરી કમળો (હિપેટાઇટિસ) અને જળજન્ય રોગ નિવારણ",
        "theme_en": "Boil Drinking Water | Hepatitis B Birth Dose",
        "theme_gu": "પીવાનું પાણી ઉકાળીને પીવો | હિપેટાઇટિસ બી રસી",
        "do1": (
            "Boil Drinking Water & Maintain Food Hygiene",
            "પાણી ઉકાળીને પીવો અને સ્વચ્છતા રાખો",
            "Boil water rolling for 1 minute or use chlorine tablets. Wash raw salads thoroughly to eliminate fecal-oral Hepatitis A & E viruses.",
            "પીવાનું પાણી ઉકાળીને કે ક્લોરીનેશન કરીને જ વાપરો અને જમતા પહેલાં હાથ ધોવો; તેનાથી ઝેરી કમળો અને ઝાડા-ઊલટી અટકે છે.",
            "photos/cphc_hepatitis_waterborne_card1.png",
            "Editorial realistic photograph, authentic Indian setting. Water boiling vigorously in a clean stainless steel pot on an Indian kitchen stove, with clean filtered water jugs nearby. Clean domestic sanitation."
        ),
        "do2": (
            "Screen for Hepatitis B & C at District Centers",
            "હિપેટાઇટિસ બી અને સી ની લોહી તપાસ કરાવો",
            "Blood screening under National Viral Hepatitis Control Program (NVHCP) is free. Hepatitis C is completely curable with oral antivirals.",
            "સરકારી હોસ્પિટલમાં હિપેટાઇટિસ બી અને સી ની મફત તપાસ કરાવો; હિપેટાઇટિસ સી દવાઓથી માત્ર ૩ મહિનામાં સાજો થઈ શકે છે.",
            "photos/cphc_hepatitis_waterborne_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A lab technician in blue gloves drawing a blood sample from an adult patient's arm for viral screening in a bright public hospital diagnostic lab. Clinical precision."
        ),
        "dont1": (
            "Never Drink Street-Side Unhygienic Crushed Ice Drinks",
            "ખુલ્લામાં વેચાતા બરફ કે જ્યુસ ન પીવા",
            "Roadside crushed ice is frequently manufactured with unpotable industrial water, directly transmitting deadly enterically-borne viral hepatitis.",
            "બહાર ખુલ્લામાં વેચાતા બરફવાળા શરબત કે ગોળા ન ખાવા; અસ્વચ્છ બરફ કમળા અને ટાઇફોઇડનું સૌથી મોટું વાહક છે.",
            "photos/cphc_hepatitis_waterborne_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A person at home pouring fresh coconut water from a tender green coconut into a glass, choosing safe natural hydration over contaminated ice. Healthy lifestyle focus."
        ),
        "dont2": (
            "Never Rely on Superstition for Jaundice",
            "કમળામાં ભુવા-ભારડી પાછળ ન દોડવું",
            "Never delay medical treatment for jaundice with quack mantras or harmful starvation diets; acute viral hepatitis needs clinical monitoring.",
            "કમળામાં ઝાડ-ફૂંક કે ભૂખમરા જેવા અયોગ્ય દેશી ઉપચારો ન કરો; સમયસર ડોક્ટર પાસે લીવરની તપાસ કરાવો જેથી લિવર ફેઈલ ન થાય.",
            "photos/cphc_hepatitis_waterborne_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A physician in an outpatient clinic reviewing liver function test reports and prescribing evidence-based clinical diet and rest to a seated patient. Reassuring medical care."
        )
    },
    {
        "tier": 1, "cat": "hypertension_ncd",
        "title_en": "Hypertension Screening & Blood Pressure Control",
        "title_gu": "હાઈ બ્લડપ્રેશર સ્ક્રીનિંગ અને નિયંત્રણ",
        "theme_en": "Keep BP Under 120/80 mmHg | Limit Daily Salt < 5g",
        "theme_gu": "બીપી ૧૨૦/૮૦ સામાન્ય રાખો | મીઠું દિવસમાં ૫ ગ્રામથી ઓછું",
        "do1": (
            "Check Blood Pressure Monthly Above Age 30",
            "૩૦ વર્ષ પછી નિયમિત બીપી ચેક કરાવો",
            "Visit Ayushman Arogya Mandir monthly for digital BP measurement; hypertension is a silent killer showing zero symptoms until crisis.",
            "કોઈ તકલીફ ન હોય તો પણ ૩૦ વર્ષની ઉંમર પછી દર મહિને આરોગ્ય કેન્દ્ર પર બીપી મપાવો; સાયલન્ટ કિલર બીપીથી સાવધાન રહો.",
            "photos/cphc_hypertension_ncd_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A Community Health Officer (CHO) measuring the blood pressure of a middle-aged villager with a validated digital monitor in an Ayushman Arogya Mandir. Professional community health setting."
        ),
        "do2": (
            "Engage in 45 Minutes Daily Brisk Walking",
            "દરરોજ ૪૫ મિનિટ ઝડપી ચાલો",
            "Moderate aerobic activity like brisk walking or cycling improves arterial elasticity and naturally reduces systolic BP by 5-8 mmHg.",
            "રોજ સવારે ખુલ્લી હવામાં ૪૫ મિનિટ ઝડપી ચાલવાની ટેવ પાડો; તેનાથી નળીઓ સ્વસ્થ રહે છે અને બીપી કાબૂમાં રહે છે.",
            "photos/cphc_hypertension_ncd_card2.png",
            "Editorial realistic photograph, authentic Indian setting. Two Indian adults in comfortable clothes and walking shoes walking briskly along a tree-shaded park path in warm morning sunlight. Active, healthy outdoor lifestyle."
        ),
        "dont1": (
            "Never Sprinkle Extra Raw Salt on Cooked Food",
            "જમતી વખતે ઉપરથી કાચું મીઠું ન ભભરાવવું",
            "Restrict total daily sodium intake to less than 1 level teaspoon (5g). Avoid pickles, papads, salted farsan, and packaged namkeen.",
            "જમવામાં ઉપરથી મીઠું નાખવાની ટેવ સદંતર બંધ કરો; અથાણાં, પાપડ અને ખારી વસ્તુઓ નળીઓમાં દબાણ વધારી હૃદય પર ભાર વધારે છે.",
            "photos/cphc_hypertension_ncd_card3.png",
            "Editorial realistic photograph, authentic Indian setting. Close-up of a measured half-teaspoon of salt being added to a large pot of freshly cooked vegetable stew, demonstrating conscious salt moderation. Natural kitchen daylight."
        ),
        "dont2": (
            "Never Discontinue Prescribed BP Medication",
            "બીપી નોર્મલ આવે તો દવા બંધ ન કરવી",
            "Hypertension requires continuous lifelong therapy. Stopping medicines abruptly causes rebound malignant hypertension and strokes.",
            "બીપી કાબૂમાં આવી જાય તેનો અર્થ દવા કામ કરી રહી છે; ડોક્ટરની સલાહ વગર ક્યારેય દવા બંધ ન કરો જેથી લકવો ન થાય.",
            "photos/cphc_hypertension_ncd_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A doctor reviewing a patient's organized home BP monitoring logbook and praising their consistent daily compliance. Supportive clinical consultation."
        )
    },
    {
        "tier": 1, "cat": "diabetes_care",
        "title_en": "Diabetes Management & Glycemic Balance",
        "title_gu": "ડાયાબિટીસ સંભાળ અને બ્લડ શુગર નિયંત્રણ",
        "theme_en": "Target HbA1c < 7.0% | Daily Foot Inspection",
        "theme_gu": "HbA1c ૭% થી ઓછો રાખો | રોજ પગના તળિયા તપાસો",
        "do1": (
            "Monitor Fasting Blood Sugar & Quarterly HbA1c",
            "દર ૩ મહિને સુગર અને HbA1c તપાસો",
            "Maintain HbA1c under 7% to prevent irreversible microvascular damage to eyes (retinopathy), kidneys (nephropathy), and nerves.",
            "માત્ર ખાલી પેટની સુગર નહીં, દર ૩ મહિને HbA1c ટેસ્ટ કરાવી સુગર ૭% થી નીચે રાખો જેથી કિડની અને આંખો સુરક્ષિત રહે.",
            "photos/cphc_diabetes_care_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An adult Indian testing capillary blood glucose using a modern digital glucometer on a tidy desk, noting the reading in a small diary. Methodical personal self-care."
        ),
        "do2": (
            "Inspect Feet Daily with a Mirror for Cuts",
            "અરીસામાં પગના તળિયા રોજ તપાસો",
            "Diabetic neuropathy impairs pain sensation. Wash feet in lukewarm water, dry between toes, and check soles daily for painless wounds.",
            "ડાયાબિટીસમાં પગની નસો નબળી પડતી હોવાથી ઈજાનો અહેસાસ થતો નથી; રોજ પગના તળિયા અરીસામાં જોઈ ક્યાંય ચાંદું નથી તે તપાસો.",
            "photos/cphc_diabetes_care_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An elderly Indian man seated on a cot inspecting the underside of his bare foot carefully using a handheld mirror in morning window light. Mindful preventive health care."
        ),
        "dont1": (
            "Eliminate Sugar, Jaggery, Sweets & Fruit Juices",
            "ખાંડ, ગોળ અને પેક્ડ જ્યુસ બંધ કરો",
            "Jaggery and honey cause blood sugar spikes identical to white sugar. Replace them with fiber-rich salads, sprouted pulses, and millets.",
            "ગોળ અને મધ પણ ખાંડ જેટલી જ સુગર વધારે છે; મીઠાઈઓ અને જ્યુસ બંધ કરી ફણગાવેલા મગ, કાકડી અને મેથીના દાણા લો.",
            "photos/cphc_diabetes_care_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A healthy diabetic thali on a steel plate: bitter gourd sabzi, sprouted moong salad, fresh curd, and a warm jowar roti in natural light. Wholesome nutritional focus."
        ),
        "dont2": (
            "Never Walk Barefoot Even Indoors",
            "ઘરમાં કે બહાર ખુલ્લા પગે ન ચાલવું",
            "Never walk barefoot on hot floors, stones, or temple grounds; minor unnoticed blisters turn rapidly into gangrenous diabetic ulcers.",
            "ઘરમાં કે બહાર ક્યારેય ઉઘાડા પગે ન ફરો; સોફ્ટ ચંપલ પહેરો જેથી કાંટો કે પથ્થર વાગવાથી થતું ગંભીર ઇન્ફેક્શન અટકે.",
            "photos/cphc_diabetes_care_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A senior citizen stepping into soft, cushioned supportive footwear at home, demonstrating protective foot care. Grounded domestic realism."
        )
    },
    {
        "tier": 2, "cat": "oral_cancer_ntcp",
        "title_en": "Oral Cancer Screening & Tobacco Control (NTCP)",
        "title_gu": "મુખના કેન્સરની તપાસ અને તમાકુ મુક્તિ",
        "theme_en": "3-Finger Test Monthly | Zero Gutkha, Mawa & Supari",
        "theme_gu": "મોંમાં ૩ આંગળીની તપાસ | ગુટખા, માવો, સોપારી બંધ",
        "do1": (
            "Perform Monthly Self-Oral 3-Finger Test",
            "દર મહિને મોંમાં ૩ આંગળી નાખી તપાસો",
            "Stand before a mirror; verify you can insert 3 fingers vertically into mouth. Check inner cheeks for red/white patches or stiffness.",
            "અરીસા સામે મોં ખોલી ઊભી ૩ આંગળીઓ નાખી જુઓ; જો ૩ આંગળી ન જાય કે તીખું ખાતાં બળતરા થાય તો કેન્સરનું પૂર્વ લક્ષણ હોઈ શકે છે.",
            "photos/cphc_oral_cancer_ntcp_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An adult demonstrating the standard medical three-finger vertical mouth opening check in front of a well-lit bathroom mirror. Clear educational demonstration."
        ),
        "do2": (
            "Quit Tobacco with National Helpline 1800-11-2356",
            "તમાકુ છોડવા ટોલ-ફ્રી હેલ્પલાઇન વાપરો",
            "Seek evidence-based behavioral therapy and nicotine replacement at District Hospital Tobacco Cessation Centers (TCC).",
            "ગુટખા કે બીડી છોડવા સરકારી ટોલ-ફ્રી નંબર ૧૮૦૦-૧૧-૨૩૫૬ પર માર્ગદર્શન મેળવો અને જિલ્લા હોસ્પિટલના ટીસીસી સેન્ટરનો સંપર્ક કરો.",
            "photos/cphc_oral_cancer_ntcp_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A counselor at a hospital de-addiction desk providing supportive encouragement to an adult seeking to quit tobacco. Positive, encouraging clinical setting."
        ),
        "dont1": (
            "Never Chew Gutkha, Mawa, Khaini or Supari",
            "ગુટખા, માવો, સોપારી મોંમાં ન દબાવવા",
            "Areca nut and smokeless tobacco release potent nitrosamines causing Oral Submucous Fibrosis (OSMF) and disfiguring mouth cancer.",
            "સોપારી અને તમાકુ મોઢાની અંદરની ચામડી બાળી જડબું કાયમ માટે જકડી દે છે; આ જીવલેણ વ્યસનથી આજે જ મુક્ત થાઓ.",
            "photos/cphc_oral_cancer_ntcp_card3.png",
            "Editorial realistic photograph, authentic Indian setting. An adult decisively dropping sealed tobacco pouches into a dustbin with determination, choosing a healthy future. Resolute documentary realism."
        ),
        "dont2": (
            "Never Ignore Mouth Ulcers Lasting >14 Days",
            "૧૪ દિવસથી વધુ ન રુઝાતું ચાંદું ન અવગણવું",
            "A painless mouth ulcer, burning patch, or neck lump persisting over 2 weeks requires urgent biopsy by a dental or ENT specialist.",
            "મોંમાં પડેલું ચાંદું બે અઠવાડિયામાં ન રુઝાય તો માત્ર મલમ લગાડવામાં સમય ન બગાડો; તાત્કાલિક ડેન્ટલ ડોક્ટર પાસે તપાસ કરાવો.",
            "photos/cphc_oral_cancer_ntcp_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A dental surgeon using an illuminated mouth mirror to examine the oral cavity of a seated patient in an OPD clinic room. Precise clinical focus."
        )
    },
    {
        "tier": 2, "cat": "breast_cervical_cancer",
        "title_en": "Breast & Cervical Cancer Early Screening",
        "title_gu": "સ્તન અને ગર્ભાશયના મુખના કેન્સરની તપાસ",
        "theme_en": "Monthly Breast Self-Exam | VIA Screening at 30+",
        "theme_gu": "દર મહિને સ્તનની જાતે તપાસ | ૩૦ વર્ષે VIA તપાસ",
        "do1": (
            "Conduct Monthly Breast Self-Examination (BSE)",
            "માસિક પછી સ્તનની જાતે તપાસ કરો",
            "Every woman above 20 should inspect and palpate breasts monthly after menstruation for painless lumps, dimpling, or nipple discharge.",
            "દર મહિને સ્તનમાં કોઈ નવી ગાંઠ, ચામડી ખેંચાતી હોય કે સ્તનની ડીંટડીમાંથી પ્રવાહી નીકળતું હોય તો જાતે તપાસી તુરંત ડોક્ટરને બતાવો.",
            "photos/cphc_breast_cervical_cancer_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A female physician in consultation with an adult woman in a private, respectful clinic room, explaining preventive health check protocols. Dignified, warm atmosphere."
        ),
        "do2": (
            "Undergo Visual Inspection with Acetic Acid (VIA)",
            "આરોગ્ય કેન્દ્ર પર ગર્ભાશય મુખની તપાસ કરાવો",
            "Women aged 30-65 should undergo free VIA screening every 5 years at Ayushman Arogya Mandir to detect cervical pre-cancer early.",
            "૩૦ વર્ષથી વધુ ઉંમરની બહેનો આરોગ્ય કેન્દ્ર પર ગર્ભાશયના મુખની સરળ તપાસ (VIA) કરાવો; પ્રારંભિક તબક્કે કેન્સર ૧૦૦% સાજું થાય છે.",
            "photos/cphc_breast_cervical_cancer_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A trained female healthcare officer preparing an organized, clean gynecological examination trolley in an Ayushman Arogya Mandir. Professional clinical hygiene."
        ),
        "dont1": (
            "Never Conceal Intimate Symptoms Due to Shyness",
            "ખચકાટ રાખી લક્ષણો છુપાવવા નહીં",
            "Abnormal vaginal bleeding between periods, post-menopausal spotting, or persistent foul discharge require immediate evaluation.",
            "માસિક બંધ થયા પછી અચાનક રક્તસ્ત્રાવ થાય કે દુર્ગંધયુક્ત પાણી પડે તો શરમ રાખ્યા વગર મહિલા ડોક્ટરની સલાહ લો.",
            "photos/cphc_breast_cervical_cancer_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A compassionate lady gynecologist listening thoughtfully to a patient in a private consultation room, encouraging open dialogue. Respectful medical realism."
        ),
        "dont2": (
            "Never Delay HPV Vaccination for Adolescent Girls",
            "કિશોરીઓને HPV રસી અપાવવામાં વિલંબ ન કરવો",
            "Vaccinating adolescent girls aged 9-14 with Human Papillomavirus (HPV) vaccine prevents up to 90% of cervical cancers in adulthood.",
            "૯ થી ૧૪ વર્ષની દીકરીઓને એચપીવી રસી અપાવો; આ રસી મોટા થયા પછી ગર્ભાશયના મુખના કેન્સર સામે આજીવન રક્ષણ આપે છે.",
            "photos/cphc_breast_cervical_cancer_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A mother and her teenage daughter consulting a female pediatrician with confidence in an immunization clinic. Optimistic public healthcare."
        )
    },
    {
        "tier": 1, "cat": "cardio_stroke_fast",
        "title_en": "Cardiovascular Emergency & FAST Stroke Care",
        "title_gu": "હૃદયરોગનો હુમલો અને લકવો (સ્ટ્રોક) તાત્કાલિક સંભાળ",
        "theme_en": "Chest Pain Golden Hour | FAST: Face, Arm, Speech, Time",
        "theme_gu": "ગોલ્ડન અવરમાં ૧૦૮ | FAST: મોં, હાથ, વાણી અને સમય",
        "do1": (
            "Spot FAST Stroke Warning Signs Immediately",
            "લકવાના લક્ષણો FAST પદ્ધતિથી ઓળખો",
            "Face drooping, Arm weakness, Speech slurring = Time to call 108. Thrombolysis in first 4.5 hours reverses brain paralysis.",
            "મોં વાંકું થાય, એક હાથ નબળો પડે કે બોલવામાં જીભ લથડાય તો સમય બગાડ્યા વગર તુરંત ૧૦૮ બોલાવી સીટી સ્કેન વાળી હોસ્પિટલ પહોંચો.",
            "photos/cphc_cardio_stroke_fast_card1.png",
            "Editorial realistic photograph, authentic Indian setting. Paramedics safely assisting an adult patient onto a stretcher gurney outside an emergency reception, moving swiftly with organized care. Urgent, professional healthcare."
        ),
        "do2": (
            "Act Within Golden Hour for Acute Chest Heaviness",
            "છાતીમાં ભાર કે પરસેવો થાય તો ૧૦૮ બોલાવો",
            "Crushing chest pressure radiating to jaw, left arm, or back with cold sweats needs immediate ECG and hospital emergency care.",
            "છાતીમાં ભાર, ગભરામણ, ડાબા હાથમાં દુખાવો કે પરસેવો વળે તો તાત્કાલિક હોસ્પિટલ પહોંચો; પ્રથમ એક કલાક ગોલ્ડન અવર છે.",
            "photos/cphc_cardio_stroke_fast_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An emergency doctor reviewing a 12-lead ECG strip on a clipboard beside an alert patient in an emergency triage unit. Sharp medical realism."
        ),
        "dont1": (
            "Never Dismiss Chest Heaviness as Acidity",
            "છાતીના દુખાવાને સામાન્ય ગેસ ન ગણવો",
            "Never waste crucial golden hours drinking sodas or antacids; an atypical heart attack can mimic severe indigestion, especially in diabetics.",
            "છાતીના દુખાવાને ગેસ સમજી સોડા પીવામાં સમય ન બગાડો; ખાસ કરીને ડાયાબિટીસના દર્દીઓમાં હૃદયરોગના હુમલામાં ઓછો દુખાવો પણ હોઈ શકે છે.",
            "photos/cphc_cardio_stroke_fast_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A hospital emergency entrance corridor with clear signage and triage reception, illuminated in daylight. Clean public emergency care."
        ),
        "dont2": (
            "Never Feed Water or Food to Acute Stroke Patients",
            "લકવાના દર્દીને પાણી કે ખાવાનું ન આપવું",
            "A stroke paralyzes throat swallowing reflexes. Forcing water or tea into mouth causes lethal aspiration directly into lungs.",
            "લકવો પડે ત્યારે દર્દીને ક્યારેય પાણી, ચા કે ગોળી ગળાવશો નહીં; ગળાના સ્નાયુઓ શિથિલ હોવાથી પાણી ફેફસાંમાં જઈ દર્દી ગૂંગળાઈ શકે છે.",
            "photos/cphc_cardio_stroke_fast_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A nurse keeping an unconscious patient's head safely elevated and turned to the side on an emergency gurney, maintaining clear open airway. Life-saving first-aid realism."
        )
    },
    {
        "tier": 2, "cat": "copd_asthma",
        "title_en": "Chronic Respiratory Health (COPD & Asthma)",
        "title_gu": "શ્વાસનળી અને ફેફસાંનું આરોગ્ય (દમ અને સીઓપીડી)",
        "theme_en": "Spirometry for Chronic Cough | Proper Inhaler Technique",
        "theme_gu": "સ્પાયરોમેટ્રી તપાસ | ઇનહેલરનો સાચો ઉપયોગ",
        "do1": (
            "Use Prescribed Inhalers with Spacer Daily",
            "ઇનહેલર સ્પેસર સાથે નિયમિત વાપરો",
            "Inhaled bronchodilators deliver micro-grams directly to airways with minimal bodily side effects. Use a transparent spacer for maximum lung reach.",
            "ડોક્ટરે આપેલું ઇનહેલર સ્પેસર સાધન સાથે દરરોજ નિયમિત લો; તેનાથી દવા સીધી શ્વાસનળીમાં જઈ ફેફસાં ખુલ્લા રાખે છે.",
            "photos/cphc_copd_asthma_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An adult seated in a clinic office, correctly demonstrating the use of a metered-dose inhaler with a transparent spacer device, doctor observing approvingly. Clear clinical guidance."
        ),
        "do2": (
            "Shift to Clean LPG Gas & Ensure Kitchen Ventilation",
            "ચૂલાના ધુમાડાથી બચી એલપીજી ગેસ વાપરો",
            "Replace wood and dung chulhas with clean LPG stoves; keep kitchen windows open to eliminate chronic biomass smoke lung destruction.",
            "લાકડાંના ચૂલાનો ધુમાડો ફેફસાંને બગાડે છે; રસોડામાં બારી ખુલ્લી રાખો અને ઉજ્જવલા યોજનાનો ગેસ ચૂલો વાપરો.",
            "photos/cphc_copd_asthma_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A smiling rural homemaker cooking happily on a modern clean double-burner LPG stove in a bright kitchen with fresh morning air streaming through an open window. Clean domestic energy."
        ),
        "dont1": (
            "Never Smoke Bidis, Cigarettes or Inhale Chillum Smoke",
            "બીડી, સિગારેટ કે હુક્કો સદંતર બંધ કરો",
            "Smoking destroys delicate lung alveoli, causing irreversible COPD and chronic breathlessness. Quitting halts rapid lung decline.",
            "બીડી-સિગારેટનો ધુમાડો શ્વાસનળીઓ કાયમ માટે સંકોચી નાખે છે; તમાકુ મુક્ત બનો જેથી ઉંમર વધતા ઓક્સિજન સિલિન્ડરનો સહારો ન લેવો પડે.",
            "photos/cphc_copd_asthma_card3.png",
            "Editorial realistic photograph, authentic Indian setting. An elderly man standing in an open agricultural field at sunrise taking deep breaths of fresh clean rural air, resolute expression. Empowering outdoor realism."
        ),
        "dont2": (
            "Never Fear Inhaler Dependence or Addiction",
            "ઇનહેલરની ટેવ પડી જાય તેવો ડર ન રાખવો",
            "Inhalers are safe, targeted medical delivery systems; they are not addictive drugs. Delaying inhalers causes permanent airway remodeling.",
            "ઇનહેલરની આદત પડી જાય તેવી ખોટી માન્યતામાં ન પડો; ગોળીઓ કરતાં ઇનહેલર વધુ સુરક્ષિત છે અને આડઅસર વગર શ્વાસ સુધારે છે.",
            "photos/cphc_copd_asthma_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A pulmonologist in an OPD consultation room reviewing a spirometry lung test report and explaining treatment clearly to an attentive patient. Reassuring medical care."
        )
    },
    {
        "tier": 2, "cat": "eye_care_oeee",
        "title_en": "Primary Eye Care & Cataract Prevention (OEEE)",
        "title_gu": "પ્રાથમિક નેત્ર સંભાળ અને મોતિયા નિયંત્રણ (OEEE)",
        "theme_en": "Annual Vision Screening | Free Sutureless Cataract Op",
        "theme_gu": "વાર્ષિક આંખની તપાસ | સરકારી હોસ્પિટલમાં મફત મોતિયા ઓપરેશન",
        "do1": (
            "Get Vision Screened Annually for Refractive Errors",
            "બાળકો અને વડીલોની વર્ષે એકવાર આંખ તપાસ",
            "Screen schoolchildren for myopia and seniors for glaucoma. Corrective spectacles restore scholastic focus and prevent elder falls.",
            "શાળાના બાળકો બોર્ડ પર વાંચી ન શકતા હોય તો ચશ્મા તપાસાવો અને વડીલોમાં ઝામરની વહેલી તપાસ માટે વાર્ષિક નેત્ર પરીક્ષણ કરાવો.",
            "photos/cphc_eye_care_oeee_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An optometrist testing the visual acuity of a young student using a trial lens frame and distance letter chart in a clean eye screening clinic. Focused educational healthcare."
        ),
        "do2": (
            "Avail Free Modern Sutureless Cataract Surgery",
            "સરકારી હોસ્પિટલમાં મોતિયાનું મફત ઓપરેશન",
            "Do not let elders live in avoidable blindness. Modern sutureless cataract surgery with intraocular lens (IOL) is free at District Hospitals.",
            "મોતિયો પાકે ત્યાં સુધી રાહ ન જુઓ; રાષ્ટ્રીય અંધત્વ નિયંત્રણ કાર્યક્રમ હેઠળ આધુનિક પદ્ધતિથી લેન્સ મૂકી મોતિયાનું મફત ઓપરેશન કરાવો.",
            "photos/cphc_eye_care_oeee_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An elderly Indian grandmother wearing a clear protective eye shield smiling happily after successful cataract surgery in an eye ward. Uplifting recovery."
        ),
        "dont1": (
            "Never Rub Red Irritated Eyes Aggressively",
            "આંખ લાલ થાય ત્યારે જોરથી ચોળવી નહીં",
            "Rubbing scratches delicate corneal epithelium and spreads bacterial conjunctivitis. Wash face with clean water and blink gently.",
            "આંખ લાલ થાય કે કચરો પડે ત્યારે જોરથી મસળવી નહીં; સ્વચ્છ પાણીની છાલક મારી આંખ સાફ કરો જેથી કીકી પર ઘસરકો ન પડે.",
            "photos/cphc_eye_care_oeee_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A person carefully washing their face and eyes with clean running water over a clean washbasin, gentle hygiene focus. Calm domestic realism."
        ),
        "dont2": (
            "Never Use Steroid Eye Drops Without Prescription",
            "ડોક્ટર પૂછ્યા વગર સ્ટીરોઈડ ટીપાં ન નાખવા",
            "Over-the-counter red eye drops containing steroids elevate intraocular pressure, causing irreversible blinding steroid glaucoma.",
            "મેડિકલ સ્ટોરમાંથી જાતે લાવીને આંખમાં ટીપાં ન નાખો; સ્ટીરોઈડ ટીપાં આંખનું પ્રેશર વધારી કાયમી અંધાપો લાવી શકે છે.",
            "photos/cphc_eye_care_oeee_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An ophthalmologist using a slit lamp microscope to examine a patient's anterior eye segment in a dimly lit, professional clinic. Medical precision."
        )
    },
    {
        "tier": 2, "cat": "ent_care_oeee",
        "title_en": "Primary Ear, Nose & Throat Health (OEEE)",
        "title_gu": "પ્રાથમિક કાન, નાક અને ગળાની સંભાળ (OEEE)",
        "theme_en": "Safe Ear Cleaning | Forward Lean for Epistaxis",
        "theme_gu": "કાનની સુરક્ષિત સફાઈ | નસકોરી ફૂટે ત્યારે આગળ નમો",
        "do1": (
            "Pinch Nose & Lean Forward During Epistaxis",
            "નસકોરીમાં નાક દબાવી સહેજ આગળ નમો",
            "Pinch soft lower nostrils firmly for 10 minutes, lean forward, and breathe through mouth. Never tilt head back as blood chokes stomach.",
            "નાકમાંથી લોહી નીકળે ત્યારે માથું પાછળ ન લેશો; આગળ નમીને નાકનો નરમ ભાગ ૧૦ મિનિટ દબાવી રાખો અને મોં વાટે શ્વાસ લો.",
            "photos/cphc_ent_care_oeee_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An adult seated demonstrating correct epistaxis first aid by leaning slightly forward and pinching the soft nostrils with thumb and forefinger calmly. Clear first-aid guidance."
        ),
        "do2": (
            "Keep Ears Dry and Seek Doctor for Ear Discharge",
            "કાન સૂકા રાખો અને રસી થાય તો તપાસ કરાવો",
            "Treat chronic suppurative otitis media early at CHC with antibiotic ear drops. Keep ears protected from water during swimming.",
            "કાનમાંથી રસી કે પરુ નીકળતું હોય તો ENT ડોક્ટર પાસે તપાસ કરાવો અને નાહતી વખતે કાનમાં પાણી ન જવા દો.",
            "photos/cphc_ent_care_oeee_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A doctor using an illuminated otoscope to carefully inspect the external auditory canal and eardrum of a patient in a consultation room. Clinical accuracy."
        ),
        "dont1": (
            "Never Poke Matchsticks, Pins or Buds into Ears",
            "કાનમાં દિવાસળી, પીન કે બડ્સ ક્યારેય ન નાખવા",
            "Ears are self-cleaning organs. Inserting foreign objects pushes ear wax deeper and punctures delicate tympanic membranes permanently.",
            "કાન ખોતરવા માટે દિવાસળી, હેરપિન કે કાનબડ્સ ન વાપરો; તેનાથી કાનના પડદામાં કાણું પડી કાયમી બહેરાશ આવી શકે છે.",
            "photos/cphc_ent_care_oeee_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A bathroom cabinet with organized personal care items, free from dangerous pins or matchsticks. Safe domestic hygiene focus."
        ),
        "dont2": (
            "Never Pour Warm Oil or Garlic Juice into Ears",
            "કાનમાં ગરમ તેલ કે ઘરગથ્થુ રસાયણ ન નાખવા",
            "Pouring mustard oil or concoctions into infected ears causes fungal otitis externa and destroys middle ear hearing bones.",
            "કાનમાં દુખાવો થાય ત્યારે લસણનું તેલ કે પાંદડાંનો રસ ન નાખો; તેનાથી કાનમાં ફૂગ થાય છે અને ચેપ ગંભીર બને છે.",
            "photos/cphc_ent_care_oeee_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An ENT specialist explaining safe ear hygiene to an attentive family with visual ear anatomy charts in a clinic. Professional health education."
        )
    },
    {
        "tier": 2, "cat": "oral_dental_oeee",
        "title_en": "Basic Oral & Dental Hygiene (OEEE)",
        "title_gu": "દાંત અને મુખની સ્વચ્છતા (OEEE)",
        "theme_en": "Brush Twice Daily with Fluoride | 6-Month Dental Check",
        "theme_gu": "દિવસમાં બે વાર બ્રશ કરો | દર ૬ મહિને દાંતની તપાસ",
        "do1": (
            "Brush Twice Daily for 2 Minutes with Soft Bristles",
            "સવારે અને રાત્રે ૨ મિનિટ બ્રશ કરો",
            "Use a pea-sized amount of fluoridated toothpaste. Clean all surfaces with gentle circular motions and scrape tongue gently.",
            "સવારે અને રાત્રે સૂતા પહેલાં સોફ્ટ બ્રશથી દાંત ઉપર-નીચે ગોળાકાર ગતિમાં સાફ કરો અને જીભ પણ સાફ કરવાની ટેવ રાખો.",
            "photos/cphc_oral_dental_oeee_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A smiling father and son standing side by side at a bathroom sink, brushing teeth properly with soft toothbrushes in morning light. Warm domestic routine."
        ),
        "do2": (
            "Rinse Mouth Vigorously After Every Meal",
            "જમ્યા પછી સ્વચ્છ પાણીથી જોરથી કોગળા કરો",
            "Swish plain drinking water vigorously after every meal to dislodge sticky carbohydrates and neutralize oral acid enamel decay.",
            "કંઈપણ ખાધા પછી મોંમાં સ્વચ્છ પાણી ભરી જોરથી કોગળા કરો જેથી દાંત વચ્ચે ફસાયેલો ખોરાક નીકળી જાય અને સડો ન થાય.",
            "photos/cphc_oral_dental_oeee_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A child holding a glass of water, cheerfully swishing water in cheeks to rinse mouth over a clean washbasin after lunch. Healthy pediatric routine."
        ),
        "dont1": (
            "Never Poke Safety Pins or Toothpicks into Gums",
            "દાંત વચ્ચે સેફ્ટી પીન કે સળી ન ભરાવવી",
            "Using sharp metal objects strips delicate periodontal attachments and creates bleeding gum pockets and bone infection.",
            "દાંત ખોતરવા ટાંકણી કે તાર વાપરવાથી પેઢા છોલાઈ જાય છે અને પાયોરિયા થાય છે; દાંત સાફ કરવા ડેન્ટલ ફ્લોસ વાપરો.",
            "photos/cphc_oral_dental_oeee_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean bathroom shelf showing a spool of dental floss, tongue cleaner, and soft toothbrushes stored upright cleanly. Pristine dental care tools."
        ),
        "dont2": (
            "Never Go to Sleep with Sugary Sweets in Mouth",
            "રાત્રે ચોકલેટ-મીઠાઈ ખાઈને બ્રશ વગર ન સૂવું",
            "Sugars lingering on teeth overnight nourish acid-forming Streptococcus mutans bacteria that dissolve enamel and form deep cavities.",
            "રાત્રે ગળી વસ્તુઓ ખાધા પછી બ્રશ કર્યા વગર ન સૂવું; રાત્રે મોંમાં લાળ ઓછી હોવાથી ખાંડથી દાંતમાં ઝડપથી કેવિટી થાય છે.",
            "photos/cphc_oral_dental_oeee_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A dentist examining a young patient's healthy teeth in a dental clinic operatory, patient smiling comfortably in the dental chair. Reassuring clinical care."
        )
    },
    {
        "tier": 2, "cat": "elderly_cga_epmns",
        "title_en": "Comprehensive Geriatric Care & Elder Health (EPMNS)",
        "title_gu": "વરિષ્ઠ નાગરિક આરોગ્ય અને સંભાળ (EPMNS)",
        "theme_en": "Comprehensive Geriatric Assessment (CGA) | Respect & Dignity",
        "theme_gu": "વૃદ્ધાવસ્થા મૂલ્યાંકન (CGA) | વડીલોનું સન્માન અને સેવા",
        "do1": (
            "Avail Monthly Comprehensive Geriatric Review at HWC",
            "આરોગ્ય મંદિર પર વડીલોની માસિક તપાસ",
            "Comprehensive Geriatric Assessment evaluates blood pressure, sugar, mobility, cognitive memory, nutrition, and urinary continence.",
            "દર મહિને આયુષ્માન આરોગ્ય મંદિર પર વડીલોની બીપી, સુગર, સાંધા, દ્રષ્ટિ અને યાદશક્તિની વ્યાપક તપાસ કરાવો.",
            "photos/cphc_elderly_cga_epmns_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A female Community Health Officer gently checking the vitals and speaking warmly with an elderly Indian woman seated in an Ayushman Arogya Mandir. Respectful elder healthcare."
        ),
        "do2": (
            "Install Bright Night-Lights & Non-Slip Bathroom Mats",
            "ઘરમાં પૂરતો પ્રકાશ અને લપસી ન પડાય તેવી વ્યવસ્થા",
            "Ensure well-lit hallways, sturdy non-slip footwear, and uncluttered walkways to protect fragile bones from debilitating falls.",
            "વડીલો માટે ઘરમાં રાત્રે પૂરતો પ્રકાશ રાખો, બાથરૂમમાં એન્ટી-સ્કિડ સાદડી પાથરો અને પગ લપસી ન જાય તેવા ચંપલ પહેરાવો.",
            "photos/cphc_elderly_cga_epmns_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A bright, safe domestic hallway with warm lighting and clear uncluttered floors, an elderly couple walking comfortably with walking sticks. Safe home environment."
        ),
        "dont1": (
            "Never Dismiss Elder Sadness as Natural Old Age",
            "વડીલોની ઉદાસીને માત્ર વૃદ્ધાવસ્થા ન ગણવી",
            "Elderly depression and social isolation are treatable medical conditions. Spend loving daily time talking with senior family members.",
            "વડીલો એકલા પડી જાય કે ઉદાસ રહે તો તેમની સાથે બેસી વાતો કરો; માનસિક હતાશા એ ઉંમરનો ભાગ નથી પણ સારવારપાત્ર છે.",
            "photos/cphc_elderly_cga_epmns_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A multi-generational family sitting together on a veranda, adult daughter serving tea to her smiling elderly mother, engaged in warm conversation. Loving family solidarity."
        ),
        "dont2": (
            "Never Self-Adjust Multiple Chronic Medications",
            "વડીલોની દવાઓ જાતે બદલવી કે બંધ ન કરવી",
            "Seniors often take multiple medicines (polypharmacy). Always review pills with a qualified medical officer to prevent toxic drug clashes.",
            "બીપી, ડાયાબિટીસ અને સાંધાની વિવિધ દવાઓ જાતે ઓછી-વધતી ન કરો; ડોક્ટર પાસે સમયાંતરે દવાની સમીક્ષા કરાવો.",
            "photos/cphc_elderly_cga_epmns_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A doctor reviewing an organized medication organizer box with an elderly patient and their caregiver, explaining timing clearly. Compassionate clinical consultation."
        )
    },
    {
        "tier": 2, "cat": "palliative_epmns",
        "title_en": "Palliative Care & Chronic Pain Relief (EPMNS)",
        "title_gu": "ઉપશામક સારવાર (પેલિએટિવ કેર) અને દર્દ નિવારણ (EPMNS)",
        "theme_en": "Dignity in Advanced Illness | Bed Sore Prevention",
        "theme_gu": "ગંભીર બીમારીમાં ગૌરવપૂર્ણ સંભાળ | બેડસોર અટકાવો",
        "do1": (
            "Turn Bedridden Patients Every 2 Hours",
            "પથારીવશ દર્દીનું દર ૨ કલાકે પડખું ફેરવો",
            "Reposition bedridden patients every 2 hours, use an alternating air mattress, and keep skin dry and moisturized to prevent bed sores.",
            "લાંબા સમયથી પથારીવશ દર્દીનું દર ૨ કલાકે પડખું બદલો અને એર-મેટ્રેસ વાપરો જેથી પીઠ કે નિતંબ પર બેડસોર (ચાંદાં) ન પડે.",
            "photos/cphc_palliative_epmns_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A trained home palliative healthcare worker gently repositioning a bedridden elder with clean pillows in a clean, sunlit domestic room. Compassionate dignified care."
        ),
        "do2": (
            "Manage Chronic Pain with WHO Analgesic Protocol",
            "દર્દ મુક્તિ માટે ડોક્ટરની સલાહ મુજબ દવા લો",
            "Advanced cancer and organ failure pain can be safely controlled with prescribed analgesics, restoring sleep and daily comfort.",
            "ગંભીર બીમારીઓમાં દર્દીને પીડા સહન ન કરવા દો; સરકારી હોસ્પિટલના પેલિએટિવ કેર સેન્ટર પરથી દર્દ નિવારક દવાઓ મેળવો.",
            "photos/cphc_palliative_epmns_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A compassionate palliative physician seated beside an ill patient's bed holding their hand gently, explaining pain relief therapy to family members. Tender medical empathy."
        ),
        "dont1": (
            "Never Leave Chronically Ill Patients in Solitude",
            "દર્દીને એકલા કે નિરાધાર ન છોડવા",
            "Palliative care addresses physical pain, mental anxiety, social dignity, and spiritual peace. Involve patient in family daily moments.",
            "ગંભીર દર્દીને અલાયદા રૂમમાં એકલા ન પાડી દો; પરિવારનો સ્નેહ, હાજરી અને ખુશનુંમા વાતાવરણ તેમના મનને શાંતિ આપે છે.",
            "photos/cphc_palliative_epmns_card3.png",
            "Editorial realistic photograph, authentic Indian setting. Family members gathered around a recovering elderly patient's bedside, sharing smiles and gentle companionship in natural daylight. Emotional warmth and dignity."
        ),
        "dont2": (
            "Never Vigorously Massage Swollen Fragile Limbs",
            "સોજાવાળા પગ પર ક્યારેય જોરથી માલિશ ન કરવી",
            "Vigorous massage on swollen edematous legs can dislodge deep vein thrombosis (DVT) clots directly to lungs with fatal results.",
            "પથારીવશ દર્દીના સોજેલા પગ પર જોરથી તેલ માલિશ ન કરો; નસોમાં જામેલું લોહી છૂટું પડી ફેફસાં કે હૃદયમાં બ્લોકેજ કરી શકે છે.",
            "photos/cphc_palliative_epmns_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A community nurse gently applying a light soothing moisturizer with feather-light touch on an elder's dry arm in a bedroom. Gentle professional nursing care."
        )
    },
    {
        "tier": 2, "cat": "mental_telemanas_epmns",
        "title_en": "Community Mental Health & Tele-MANAS Support (EPMNS)",
        "title_gu": "માનસિક સ્વાસ્થ્ય અને ટેલિ-માનસ સેવા (EPMNS)",
        "theme_en": "Screen Anxiety & Depression | Dial 14416 Toll-Free",
        "theme_gu": "ચિંતા-ડિપ્રેશનની તપાસ | ટોલ-ફ્રી ૧૪૪૧૬ ટેલિ-માનસ",
        "do1": (
            "Call 24/7 Tele-MANAS Toll-Free 14416 Anytime",
            "માનસિક તણાવમાં ૧૪૪૧૬ પર મફત કોલ કરો",
            "Government Tele-MANAS helpline provides 24/7 free, confidential psychological counseling in Gujarati by certified mental health experts.",
            "ચિંતા, ડિપ્રેશન કે નિરાશા થાય ત્યારે ખચકાયા વગર ૧૪૪૧૬ પર ફોન કરો; ગુજરાતીમાં ગુપ્ત અને નિઃશુલ્ક કાઉન્સેલિંગ ઉપલબ્ધ છે.",
            "photos/cphc_mental_telemanas_epmns_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A female Indian counselor wearing professional audio headset seated at a clean workstation, speaking warmly into microphone in a modern tele-health support centre. Professional, compassionate lighting."
        ),
        "do2": (
            "Screen for Depression & Anxiety with PHQ-9 / GAD-7",
            "પીએચક્યુ-૯ પ્રશ્નાવલીથી માનસિક તપાસ કરાવો",
            "Community Health Officers screen for common mental disorders at Ayushman Arogya Mandir. Early counseling prevents severe psychiatric crisis.",
            "આરોગ્ય મંદિર પર સામાન્ય માનસિક તણાવનું સ્ક્રીનિંગ કરાવો; પ્રારંભિક કાઉન્સેલિંગથી મનની મૂંઝવણ ઝડપથી દૂર થાય છે.",
            "photos/cphc_mental_telemanas_epmns_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A Community Health Officer (CHO) having an empathetic, confidential one-on-one discussion with a seated adult villager in a consultation room. Calm community mental healthcare."
        ),
        "dont1": (
            "Never Chain or Abuse Patients with Mental Disorders",
            "માનસિક બીમારીમાં દોરા-ધાગા કે અત્યાચાર ન કરવો",
            "Severe mental disorders like psychosis and schizophrenia are biological brain illnesses. Torturing or chaining patients is a punishable crime.",
            "માનસિક બીમારીમાં દર્દીને સાંકળે બાંધવો કે ભૂત-વળગાડ ગણી અત્યાચાર કરવો ગુનો છે; સાયકિયાટ્રિસ્ટની દવાથી દર્દી સંપૂર્ણ સાજો થાય છે.",
            "photos/cphc_mental_telemanas_epmns_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A qualified psychiatrist in an OPD clinic discussing treatment respectfully with a patient and their caring family, promoting scientific understanding. Dignified clinical setting."
        ),
        "dont2": (
            "Never Dismiss Expressions of Hopelessness",
            "કોઈની હતાશાને મજાક કે નાટક ન ગણો",
            "Statements like 'I want to end it all' are urgent emergency cries for help. Never leave a person in acute suicidal distress alone.",
            "જ્યારે કોઈ કહે કે મારું કોઈ નથી અથવા જીવવું નથી, ત્યારે તેને હળવાશથી ન લેશો; તેમની સાથે રહો અને તાત્કાલિક ૧૪૪૧૬ ની મદદ અપાવો.",
            "photos/cphc_mental_telemanas_epmns_card4.png",
            "Editorial realistic photograph, authentic Indian setting. Two friends seated together on a garden bench in warm afternoon light, one listening with deep empathy with a comforting hand on the other's shoulder. Compassionate emotional support."
        )
    },
    {
        "tier": 2, "cat": "dementia_falls_epmns",
        "title_en": "Dementia Awareness & Fall Prevention in Seniors (EPMNS)",
        "title_gu": "ડિમેન્શિયા (સ્મૃતિભ્રંશ) અને વડીલોને લપસી પડવાથી બચાવો",
        "theme_en": "Mini-Cog Memory Screen | Bathroom Grab Bars",
        "theme_gu": "યાદશક્તિની મિની-કોગ તપાસ | બાથરૂમમાં ગ્રેબ-બાર",
        "do1": (
            "Install Stainless Steel Grab Bars in All Toilets",
            "બાથરૂમ અને શૌચાલયમાં મજબૂત ગ્રેબ-બાર લગાવો",
            "Anchor sturdy handrails beside Western commodes and bathing areas. Grab bars prevent devastating hip fractures in senior citizens.",
            "વડીલો લપસી ન પડે તે માટે બાથરૂમમાં મજબૂત સ્ટીલના ગ્રેબ-બાર લગાવો જેથી ઊભા થતાં કે બેસતાં સારો ટેકો મળી રહે.",
            "photos/cphc_dementia_falls_epmns_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A modern senior-friendly bathroom showing a stainless steel safety grab bar securely mounted beside a clean wall, with anti-skid floor tiles in warm lighting. Safe elder home design."
        ),
        "do2": (
            "Screen Memory with Mini-Cog Test at Age 60+",
            "વડીલોની યાદશક્તિની મિની-કોગ તપાસ કરાવો",
            "Mini-Cog evaluates 3-word recall and clock drawing. Early detection of Alzheimer's and vascular dementia allows protective interventions.",
            "વડીલો વસ્તુઓ કે રસ્તા ભૂલી જતા હોય તો આરોગ્ય કેન્દ્ર પર મિની-કોગ ટેસ્ટ કરાવો જેથી પ્રારંભિક સ્મૃતિભ્રંશનું નિદાન થઈ શકે.",
            "photos/cphc_dementia_falls_epmns_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A doctor gently guiding an elderly Indian gentleman through a simple cognitive clock-drawing screening test on paper in a clinic. Respectful, patient clinical care."
        ),
        "dont1": (
            "Never Leave Slippery Floors or Loose Electrical Cords",
            "ભીનો ફ્લોર કે રસ્તામાં છૂટા વાયરો ન રાખવા",
            "Wet bathroom tiles and loose extension cords are leading preventable triggers for elder falls, subdural hematomas, and hip fractures.",
            "ઘરમાં લાદી ભીની ન રાખો અને ચાલવાના રસ્તે છૂટા વાયરો ન રાખશો; વડીલોમાં લપસી પડવાથી થાપાનું ફ્રેક્ચર જીવલેણ નીવડી શકે છે.",
            "photos/cphc_dementia_falls_epmns_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean, completely dry and unobstructed domestic living room floor with neat furniture arrangement and no trailing wires, demonstrating fall safety. Bright daylight."
        ),
        "dont2": (
            "Never Scold or Argue with Disoriented Elders",
            "ભૂલી જતા વડીલો પર ગુસ્સો ન કરવો કે ખીજાવું નહીં",
            "Dementia patients experience genuine cognitive distortion. Arguing increases agitation; use calm reassurance, simple words, and patience.",
            "વડીલો વારંવાર એકની એક વાત પૂછે તો ચીડાશો નહીં; સ્નેહ અને ધીરજથી જવાબ આપો જેથી તેઓ સુરક્ષિત અને શાંત અનુભવે.",
            "photos/cphc_dementia_falls_epmns_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An adult son gently smiling and walking arm-in-arm with his elderly father in a peaceful garden pathway, offering calm companionship. Tender generational respect."
        )
    },
    {
        "tier": 2, "cat": "substance_audit_epmns",
        "title_en": "Substance Misuse Screening & De-addiction (EPMNS)",
        "title_gu": "વ્યસન મુક્તિ અને દારૂ-તમાકુ નિવારણ (EPMNS)",
        "theme_en": "Screen with AUDIT & ASSIST | Rehabilitation Support",
        "theme_gu": "ઓડિટ (AUDIT) તપાસ | વ્યસન મુક્તિ કેન્દ્રનો સહયોગ",
        "do1": (
            "Screen Alcohol Misuse with AUDIT Scale at HWC",
            "આરોગ્ય મંદિર પર ઓડિટ પ્રશ્નાવલીથી તપાસ કરાવો",
            "The 10-question AUDIT tool identifies risky drinking patterns early before cirrhosis, pancreatic damage, or domestic harm occur.",
            "દારૂના વ્યસનથી લીવર ખરાબ થાય તે પહેલાં આરોગ્ય કેન્દ્ર પર ઓડિટ સ્કેલ દ્વારા તપાસ કરાવો અને વહેલી કાઉન્સેલિંગ મેળવો.",
            "photos/cphc_substance_audit_epmns_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A healthcare officer conducting a structured AUDIT health assessment questionnaire with an adult villager in a quiet clinic room. Professional, non-judgmental atmosphere."
        ),
        "do2": (
            "Utilize District De-Addiction Centers (DDC)",
            "જિલ્લા વ્યસન મુક્તિ કેન્દ્રની મદદ લો",
            "Access free medical detoxification, psychiatric therapy, and family counseling at government Nasha Mukti rehabilitation centers.",
            "જિલ્લા હોસ્પિટલના વ્યસન મુક્તિ કેન્દ્ર પરથી સલામત દવાઓ અને કાઉન્સેલિંગ દ્વારા દારૂ કે ડ્રગ્સની લતમાંથી કાયમ માટે મુક્ત થાઓ.",
            "photos/cphc_substance_audit_epmns_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A recovered adult smiling with pride, holding hands with supportive family members in an outdoor community park, celebrating sobriety. Optimistic documentary realism."
        ),
        "dont1": (
            "Never Stop Heavy Alcohol Abruptly Without Medical Supervision",
            "ભારે દારૂનું વ્યસન અચાનક જાતે ન છોડવું",
            "Severe alcohol withdrawal triggers life-threatening Delirium Tremens, seizures, and arrhythmias. Always detoxify under doctor's care.",
            "વર્ષોથી દારૂ પીતા વ્યક્તિએ જાતે અચાનક બંધ ન કરવો; તેનાથી આંચકી કે ખેંચ આવી શકે છે. ડોક્ટરની દેખરેખ હેઠળ દવા સાથે છોડો.",
            "photos/cphc_substance_audit_epmns_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clinical physician monitoring vitals of a patient in a hospital medical recovery ward, ensuring stable clinical detoxification. Reassuring medical supervision."
        ),
        "dont2": (
            "Never Enable Addiction by Hiding the Problem",
            "વ્યસનને શરમ કે ભયથી છુપાવવું નહીં",
            "Covering up for an addicted family member delays life-saving medical help. Seek compassionate professional healthcare early.",
            "પરિવારમાં કોઈને વ્યસન હોય તો સમાજના ડરે છુપાવશો નહીં; સમયસર સારવાર અપાવવાથી વ્યક્તિ અને આખો પરિવાર બચી જાય છે.",
            "photos/cphc_substance_audit_epmns_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A compassionate family counselor sitting with a supportive spouse and adult in a guidance centre, engaged in healing dialogue. Respectful and hopeful."
        )
    },
    {
        "tier": 2, "cat": "emergency_snakebite",
        "title_en": "Snakebite First Aid & Poisoning Management",
        "title_gu": "સર્પદંશ પ્રાથમિક સારવાર અને ઝેર વ્યવસ્થાપન",
        "theme_en": "Immobilize Limb Promptly | Rush for Free ASV",
        "theme_gu": "દંખવાળા અંગને હલનચલન વગર રાખો | તાત્કાલિક ASV સારવાર",
        "do1": (
            "Immobilize Bitten Limb with a Rigid Splint",
            "દંખવાળા હાથ-પગને પાટિયું બાંધી સ્થિર રાખો",
            "Immobilize bitten extremity with a splint and crepe bandage just like a fracture. Keep limb below heart level; reassure the victim.",
            "સાપ કરડે ત્યારે દર્દીને દોડવા ન દો; દંખવાળા અંગને પાટિયું બાંધી સાવ સ્થિર રાખો જેથી ઝેર આખા શરીરમાં ઝડપથી ન ફેલાય.",
            "photos/cphc_emergency_snakebite_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A trained first responder gently immobilizing a patient's lower leg with a padded wooden splint and bandage on an emergency gurney. Clear, accurate first-aid procedure."
        ),
        "do2": (
            "Rush to CHC / District Hospital for Free ASV",
            "તાત્કાલિક સરકારી હોસ્પિટલ પહોંચી ASV લો",
            "Anti-Snake Venom (ASV) is the only scientific, life-saving antidote for Indian cobra, krait, Russell's viper, and saw-scaled viper bites.",
            "વિલંબ કર્યા વગર ૧૦૮ દ્વારા સીધા સરકારી હોસ્પિટલ પહોંચો; ત્યાં મફત ઉપલબ્ધ એન્ટિ-સ્નેક વેનમ (ASV) જ એકમાત્ર જીવનરક્ષક ઈલાજ છે.",
            "photos/cphc_emergency_snakebite_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An emergency doctor in a government hospital casualty room administering life-saving intravenous infusion therapy to a stabilized patient. Professional medical urgency."
        ),
        "dont1": (
            "Never Cut, Suck, Bleed or Tie Tight Tourniquets",
            "ચીરો મૂકવો, ચૂસવું કે કચકચાવીને દોરી ન બાંધવી",
            "Tight tourniquets stop arterial blood flow causing gangrene and amputation. Cutting with razor blades introduces fatal tetanus and hemorrhage.",
            "દંખ પર બ્લેડથી ચીરો ન મૂકો, મોંથી ચૂસશો નહીં કે કચકચાવીને દોરી ન બાંધો; તેનાથી અંગ સડી જાય છે અને કાપવું પડી શકે છે.",
            "photos/cphc_emergency_snakebite_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean medical first-aid kit with sterile bandages, scissors, and clean splints neatly arranged on a table. Safe first-aid tools."
        ),
        "dont2": (
            "Never Waste Golden Time on Snake Stones or Faith Healers",
            "ભુવા કે ઝેરમોરા પાછળ કિંમતી સમય ન બગાડવો",
            "Over 70% of snakes are non-venomous; faith healers claim false credit while venomous bites progress to fatal paralysis during delays.",
            "સાપ કરડવા પર ઝાડ-ફૂંક કે પથ્થર ઘસવામાં એક મિનિટ પણ ન બગાડો; સમયસર હોસ્પિટલ પહોંચવાથી દર્દીનો જીવ ૧૦૦% બચે છે.",
            "photos/cphc_emergency_snakebite_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian 108 emergency ambulance arriving outside a village home to transport a snakebite patient swiftly to hospital. High-speed emergency response."
        )
    },
    {
        "tier": 2, "cat": "emergency_trauma_108",
        "title_en": "Road Trauma First Aid & 108 Golden Hour Action",
        "title_gu": "માર્ગ અકસ્માત ટ્રોમા સારવાર અને ૧૦૮ ગોલ્ડન અવર",
        "theme_en": "Direct Pressure on Bleeding | Full-Face Helmets",
        "theme_gu": "ઘા પર સીધું દબાણ આપી લોહી રોકો | ISI હેલ્મેટ પહેરો",
        "do1": (
            "Apply Firm Direct Pressure to Stop Severe Bleeding",
            "વહેતા લોહી પર સ્વચ્છ કપડાથી દબાણ આપો",
            "Press a clean cloth firmly directly over bleeding wounds for at least 10 continuous minutes. Direct pressure stops 90% of lethal hemorrhage.",
            "અકસ્માતમાં વહેતા લોહી પર સ્વચ્છ કપડું મૂકી હથેળીથી ૧૦ મિનિટ સતત દબાવી રાખો; દબાણ આપવાથી લોહી વહેતું અટકી જાય છે.",
            "photos/cphc_emergency_trauma_108_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A trained first aider firmly holding clean sterile folded gauze dressing over a forearm wound, demonstrating life-saving direct pressure. Clear procedural realism."
        ),
        "do2": (
            "Wear ISI Full-Face Helmet & Click Seatbelts",
            "ISI હેલ્મેટ અને સીટબેલ્ટ અવશ્ય પહેરો",
            "Fasten chin-strap on two-wheelers and wear 3-point seatbelts in cars. Golden hour hospital care within 60 minutes saves trauma victims.",
            "બાઈક પર ચિન-સ્ટ્રેપ સાથે ISI હેલ્મેટ પહેરો અને કારમાં સીટબેલ્ટ બાંધો; અકસ્માત થાય તો તરત ૧૦૮ બોલાવો.",
            "photos/cphc_emergency_trauma_108_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A responsible Indian commuter properly clicking the chin-strap of a certified matte black full-face motorcycle helmet before starting journey. Sharp safety awareness."
        ),
        "dont1": (
            "Never Forcibly Remove Helmet of Crash Victims",
            "અકસ્માત પછી હેલ્મેટ ઝટકાથી ન ખેંચવું",
            "Roughly jerking a helmet off an injured rider fractures damaged cervical vertebrae, instantly causing permanent quadriplegia or death.",
            "પટકાયેલા વ્યક્તિનું હેલ્મેટ જોરથી ન ખેંચો; ડોક હલવાથી કરોડરજ્જુ તૂટી કાયમી લકવો થઈ શકે છે. ૧૦૮ ટીમને આવવા દો.",
            "photos/cphc_emergency_trauma_108_card3.png",
            "Editorial realistic photograph, authentic Indian setting. Paramedics carefully securing an injured patient's neck with an adjustable rigid cervical collar on a spine board. Professional trauma spinal stabilization."
        ),
        "dont2": (
            "Never Transport Trauma Victims Without Spine Support",
            "દર્દીને વાંકાચૂંકા ઊંચકીને રિક્ષામાં ન લઈ જવા",
            "Do not bundle trauma victims into autos with bent spines. Keep head, neck, and torso aligned in a straight line on a firm stretcher.",
            "અકસ્માતના દર્દીને વાંકા વળીને ઊંચકવા નહીં; ગરદન અને પીઠ સીધી રહે તે રીતે પાટિયા કે ૧૦૮ ના સ્ટ્રેચર પર જ લઈ જાઓ.",
            "photos/cphc_emergency_trauma_108_card4.png",
            "Editorial realistic photograph, authentic Indian setting. Emergency responders smoothly wheeling a stabilized trauma patient on an ambulance gurney into a trauma care centre. Urgent teamwork documentary."
        )
    },
    {
        "tier": 2, "cat": "ert_less_salt_sugar_oil",
        "title_en": "Eat Right India: Aaj Se Thoda Kam (Salt, Sugar, Oil)",
        "title_gu": "ઈટ રાઈટ ઈન્ડિયા: આજ સે થોડા કમ (મીઠું, ખાંડ, તેલ)",
        "theme_en": "Limit Sodium, Trans-Fats & Refined Sugars Daily",
        "theme_gu": "રોજિંદા આહારમાં મીઠું, તેલ અને ખાંડનું પ્રમાણ ઘટાડો",
        "do1": (
            "Measure Cooking Oil with a Spoon, Not Direct Pouring",
            "તેલ ચમચીથી માપીને વાપરો (મહિને ૫૦૦ મિલી)",
            "Limit household oil consumption to under 500ml per person per month. Measure cooking oil with teaspoons to slash invisible saturated fat.",
            "શાક-વઘારમાં તેલ ડબ્બામાંથી સીધું રેડવાને બદલે ચમચીથી માપીને નાખો; વ્યક્તિ દીઠ મહિને ૫૦૦ મિલીથી વધુ તેલ ન વાપરવું.",
            "photos/cphc_ert_less_salt_sugar_oil_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An Indian homemaker measuring a single teaspoon of clear vegetable oil into a stainless steel cooking pan in a bright domestic kitchen. Mindful culinary discipline."
        ),
        "do2": (
            "Satisfy Sweet Tooth with Fresh Seasonal Fruits",
            "મીઠાઈને બદલે તાજા મોસમી ફળો ખાઓ",
            "Choose whole apples, papayas, oranges, and guavas instead of Indian sweets (mithai). Whole fruits provide protective fiber and antioxidants.",
            "જમ્યા પછી મીઠાઈ ખાવાને બદલે પપૈયું, જામફળ, મોસંબી કે દાડમ જેવા તાજા ફળો ખાવાની ટેવ પાડો.",
            "photos/cphc_ert_less_salt_sugar_oil_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An appetizing assortment of freshly sliced Indian fruits: ripe yellow papaya, green guava, and bright pomegranate arils on an earthenware plate. Vibrant healthy nourishment."
        ),
        "dont1": (
            "Never Reheat Cooking Oil Repeatedly for Frying",
            "તળેલું તેલ વારંવાર ગરમ કરીને ન વાપરવું",
            "Reheating vegetable oils creates dangerous Total Polar Compounds (TPC) and industrial trans fats that trigger coronary blockages.",
            "પૂરી કે ભજીયાં તળ્યા પછી વધેલું તેલ વારંવાર ગરમ ન કરો; કાળું પડેલું તેલ હૃદયની નળીઓ બ્લોક કરે છે અને કેન્સરનું જોખમ વધારે છે.",
            "photos/cphc_ert_less_salt_sugar_oil_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A clean modern kitchen showing freshly baked or air-roasted healthy snacks instead of deep-fried street food. Wholesome nutritional alternative."
        ),
        "dont2": (
            "Avoid Ultra-Processed Packaged Snacks & Colas",
            "પેકેટવાળા નમકીન અને બેકરી આઇટમોથી દૂર રહો",
            "Packaged chips, puffs, biscuits, and sodas contain massive amounts of hidden sodium, palm oil, and high-fructose corn syrup.",
            "બહારના પડીકાં, વેફર્સ, બિસ્કિટ અને સોડા-કોલ્ડડ્રિંક્સ ખાલી કેલરી આપે છે; બાળકોને શેકેલા ચણા, મખાના અને તાજા ફળ આપો.",
            "photos/cphc_ert_less_salt_sugar_oil_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A dining table displaying healthy traditional Indian snacks: roasted foxnuts (makhana), roasted chickpeas, and pumpkin seeds in clean glass jars. Pure healthy snacking focus."
        )
    },
    {
        "tier": 2, "cat": "ert_balanced_thali_millets",
        "title_en": "Eat Right: Desi Balanced Thali & Shree Anna Millets",
        "title_gu": "ઈટ રાઈટ: દેશી સંતુલિત થાળી અને શ્રીઅન્ન (મિલેટ્સ)",
        "theme_en": "Half Plate Greens | One-Quarter Millets | Protein",
        "theme_gu": "અડધી થાળી શાકભાજી-સલાડ | પા ભાગ કઠોળ | બાજરી-જુવાર",
        "do1": (
            "Adopt the Traditional Rainbow Balanced Thali",
            "થાળીમાં ત્રિરંગો સંતુલિત આહાર સામેલ કરો",
            "Fill 50% of your thali with colorful vegetables and raw salads, 25% with whole dals/curd/paneer, and 25% with wholesome grains.",
            "રોજિંદા ભોજનમાં અડધી થાળી લીલા શાકભાજી અને કાચા સલાડની, ચોથો ભાગ કઠોળ-દાળ-દહીં અને ચોથો ભાગ અનાજ રાખો.",
            "photos/cphc_ert_balanced_thali_millets_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A traditional bronze Indian thali arranged with colorful wholesome foods: green spinach sabzi, yellow dal, cucumber-carrot salad, curd, and hot bajra rotla. Balanced dietary excellence."
        ),
        "do2": (
            "Integrate Bajra, Jowar, Ragi & Foxtail Millets",
            "બાજરી, જુવાર અને રાગીનો ઉપયોગ વધારો",
            "Shree Anna millets offer complex fiber, low glycemic index, magnesium, and calcium that protect against diabetes and obesity.",
            "રોટલીમાં બાજરી, જુવાર અને રાગી જેવા પૌષ્ટિક ધાન્ય ઉમેરો; આ જાડા અનાજ સુગર અને કોલેસ્ટ્રોલને કુદરતી રીતે કાબૂમાં રાખે છે.",
            "photos/cphc_ert_balanced_thali_millets_card2.png",
            "Editorial realistic photograph, authentic Indian setting. Hands skillfully patting rustic pearl millet (bajra) rotla dough on a wooden board, raw grains of sorghum and finger millet displayed in earthenware bowls nearby. Authentic rustic kitchen."
        ),
        "dont1": (
            "Never Rely Exclusively on Polished White Rice & Maida",
            "મેંદો અને વધુ પડતા પોલિશ કરેલા ચોખા ન ખાવા",
            "Ultra-refined grains lack bran and germ, causing rapid insulin spikes and accelerating visceral abdominal fat accumulation.",
            "મેંદો, સફેદ બ્રેડ અને વધુ પડતા ભાત ખાવાથી વજન અને સુગર ઝડપથી વધે છે; તેના બદલે આખા અનાજ અને દળેલા લોટનો ઉપયોગ કરો.",
            "photos/cphc_ert_balanced_thali_millets_card3.png",
            "Editorial realistic photograph, authentic Indian setting. Storage containers of whole unpolished grains, unpolished brown rice, and whole wheat grains in a clean pantry. Whole grain health focus."
        ),
        "dont2": (
            "Never Skip Daily Pulses, Dals or Sprouts",
            "રોજના ભોજનમાં દાળ કે કઠોળ ખાવાનું ન ચૂકવું",
            "Vegetarian Indian diets require diverse sprouted pulses (moong, chana) and dals to meet essential amino acid protein requirements.",
            "શાકાહારી ભોજનમાં કઠોળ પ્રોટીનનો મુખ્ય સ્ત્રોત છે; રોજિંદા ભોજનમાં ફણગાવેલા મગ, ચણા કે તુવેર દાળ અવશ્ય સામેલ કરો.",
            "photos/cphc_ert_balanced_thali_millets_card4.png",
            "Editorial realistic photograph, authentic Indian setting. Fresh sprouted green moong beans and bengal gram in an earthenware bowl with coriander and lemon wedge, brightly lit in natural sunlight. Fresh protein nutrition."
        )
    },
    {
        "tier": 2, "cat": "anemia_mukt_bharat",
        "title_en": "Anemia Mukt Bharat Nutrition & Iron Synergy",
        "title_gu": "એનીમિયા મુક્ત ભારત: લોહતત્ત્વયુક્ત પૌષ્ટિક આહાર",
        "theme_en": "Iron-Rich Local Greens Squeezed with Fresh Lemon",
        "theme_gu": "લોહતત્ત્વ વાળા ભાજી-કઠોળ પર લીંબુ નીચોવીને ખાઓ",
        "do1": (
            "Pair Plant Iron with Fresh Citrus Vitamin C",
            "પાલખ-ભાજી સાથે લીંબુ કે આમળા લો",
            "Squeeze fresh lemon over spinach, fenugreek, and sprouted pulses; ascorbic acid converts ferric iron into absorbable ferrous form.",
            "પાલખ, તાંદળજો અને ફણગાવેલા કઠોળ ખાતી વખતે ઉપર લીંબુ નીચોવો; વિટામિન સી લોહતત્ત્વનું શોષણ ૪ ગણું વધારી દે છે.",
            "photos/cphc_anemia_mukt_bharat_card1.png",
            "Editorial realistic photograph, authentic Indian setting. Hands squeezing fresh juice from a ripe yellow lemon half over a colorful bowl of sprouted pulses and pomegranate arils. Fresh droplets, crisp natural lighting."
        ),
        "do2": (
            "Cook in Traditional Cast-Iron Vessels (Kadhai)",
            "લોખંડની કઢાઈમાં રસોઈ બનાવવાની ટેવ પાડો",
            "Cooking vegetables in cast-iron kadhais enriches food with natural dietary iron. Include moringa (saragvo) leaves and jaggery.",
            "શાક બનાવતી વખતે લોખંડની કઢાઈ વાપરો, સરગવાના પાનનું શાક ખાઓ અને ગોળ-તલ લો; તેનાથી શરીરમાં લોહી ઝડપથી બને છે.",
            "photos/cphc_anemia_mukt_bharat_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A traditional seasoned cast-iron skillet cooking fresh green leafy vegetables on a domestic gas stove with wooden spoon. Rustic healthy cooking."
        ),
        "dont1": (
            "Never Drink Tea or Coffee with or Immediately After Meals",
            "જમ્યાની સાથે કે તુરંત પછી ચા-કોફી ન પીવી",
            "Tannins in tea and polyphenols in coffee bind dietary iron in the intestine, blocking up to 60% of iron absorption from food.",
            "જમવાની સાથે કે જમ્યા પછી તરત ચા-કૉફી ન પીવો; ચામાં રહેલું ટેનિન ખોરાકમાંથી લોખંડને ચૂસાવા દેતું નથી.",
            "photos/cphc_anemia_mukt_bharat_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A person enjoying a cup of warm water with lemon after meals instead of strong tea. Mindful digestive routine."
        ),
        "dont2": (
            "Never Dismiss Pallor, Dizziness & Extreme Fatigue",
            "થાક, સુસ્તી કે ફીકાશને નબળાઈ ગણી ન છોડવું",
            "Pale tongue, inner eyelids, breathlessness on climbing stairs, and chronic fatigue signal severe anemia. Get hemoglobin tested at HWC.",
            "હાથની હથેળી કે આંખની પાંપણ સફેદ દેખાય, ચક્કર આવે કે થાક લાગે તો આરોગ્ય કેન્દ્ર પર હિમોગ્લોબિન મપાવો અને આયર્નની સારવાર લો.",
            "photos/cphc_anemia_mukt_bharat_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A female health worker testing hemoglobin with a digital hemoglobinometer for an adult woman in an Ayushman Arogya Mandir. Reassuring clinical diagnostic focus."
        )
    },
    {
        "tier": 2, "cat": "wash_infection_control",
        "title_en": "Water, Sanitation & Hygiene (WASH / NQAS)",
        "title_gu": "સ્વચ્છતા, શૌચાલય અને ચેપ નિયંત્રણ (WASH)",
        "theme_en": "6-Step 20-Sec Soap Handwash | Safe Water Storage",
        "theme_gu": "સાબુથી ૨૦ સેકન્ડ હાથ ધોવા | પીવાના પાણીની શુદ્ધતા",
        "do1": (
            "Practice 6-Step 20-Second Soap Handwashing",
            "સાબુથી ૨૦ સેકન્ડ સુધી હાથ ઘસીને ધોવો",
            "Wash palms, back of hands, between fingers, thumbs, knuckles, and wrists with soap under running water before eating and after toilet.",
            "જમતા પહેલાં અને શૌચ પછી ઓછામાં ઓછી ૨૦ સેકન્ડ સાબુથી હથેળી, આંગળીઓ અને કાંડાં વ્યવસ્થિત ઘસીને પાણીથી ધોવો.",
            "photos/cphc_wash_infection_control_card1.png",
            "Editorial realistic photograph, authentic Indian setting. An adult woman demonstrating proper 20-second hand washing with rich white soap lather under running tap water in a clean washbasin. Clean water droplets, crisp documentary realism."
        ),
        "do2": (
            "Store Drinking Water in Clean Covered Tapped Vessels",
            "પીવાનું પાણી નળવાળા વાસણમાં ઢાંકીને રાખો",
            "Store drinking water in narrow-mouthed vessels fitted with a tap. Keep covered with lid and clean containers thoroughly every week.",
            "પીવાનું પાણી હંમેશા નળવાળા માટલામાં કે વાસણમાં ઢાંકીને રાખો જેથી હાથ અડવાથી પાણી ગંદુ ન થાય.",
            "photos/cphc_wash_infection_control_card2.png",
            "Editorial realistic photograph, authentic Indian setting. A clean traditional earthen water pot fitted with a brass tap, resting on a clean wooden stand with a stainless steel lid. Traditional hygienic Indian home."
        ),
        "dont1": (
            "Never Dip Unwashed Hands Directly into Water Pots",
            "પીવાના પાણીના માટલામાં સીધો ગ્લાસ ન બોળવો",
            "Dipping unwashed cups or hands into domestic storage pots spreads gastroenteritis, cholera, and hepatitis A through the entire family.",
            "માટલામાંથી પાણી લેવા હાથ બોળશો નહીં; લાંબા હાથાવાળો ડોયો વાપરો અથવા નળ વાળા વાસણમાંથી જ પાણી લો.",
            "photos/cphc_wash_infection_control_card3.png",
            "Editorial realistic photograph, authentic Indian setting. Using a clean long-handled stainless steel ladle to pour water cleanly from a pitcher into a glass without touching water. Safe hygiene demonstration."
        ),
        "dont2": (
            "Never Defecate in Open Fields Near Water Bodies",
            "ખુલ્લામાં શૌચ ન જવું, શૌચાલયનો જ ઉપયોગ કરવો",
            "Open defecation contaminates groundwater and soil with parasitic roundworms and hookworms. Always use clean domestic toilets.",
            "ખુલ્લામાં શૌચ જવાનું સદંતર બંધ કરો; શૌચાલયનો જ ઉપયોગ કરવાથી કરમિયા, ટાઇફોઇડ અને કમળા જેવા રોગોથી ગામ સુરક્ષિત રહે છે.",
            "photos/cphc_wash_infection_control_card4.png",
            "Editorial realistic photograph, authentic Indian setting. A clean, well-constructed rural individual household latrine unit in a swept village courtyard, demonstrating Swachh Bharat sanitation dignity. Sunny morning light."
        )
    },
    {
        "tier": 2, "cat": "antibiotic_stewardship",
        "title_en": "Rational Drug Use & Antibiotic Stewardship",
        "title_gu": "દવાનો સાચો ઉપયોગ અને એન્ટિબાયોટિક સુરક્ષા",
        "theme_en": "Never Buy Red-Line Drugs OTC | Complete Full Course",
        "theme_gu": "લાલ લીટી વાળી દવા જાતે ન ખરીદો | પૂરો કોર્સ કરો",
        "do1": (
            "Take Antibiotics Only with Qualified Medical Prescription",
            "એન્ટિબાયોટિક્સ ફક્ત ડોક્ટરની સલાહથી જ લો",
            "Antibiotics are precious life-saving drugs that treat bacterial infections only. Take them strictly under registered medical advice.",
            "એન્ટિબાયોટિક દવાઓ માત્ર લાયકાત ધરાવતા ડોક્ટર લખે ત્યારે જ લો; સાચી બીમારીમાં સાચી દવાથી જ રોગ નાશ પામે છે.",
            "photos/cphc_antibiotic_stewardship_card1.png",
            "Editorial realistic photograph, authentic Indian setting. A licensed physician in a consultation office explaining a medication prescription calmly to a patient, emphasizing rational drug use. Professional clinical lighting."
        ),
        "do2": (
            "Always Complete the Entire 5-to-7-Day Antibiotic Course",
            "સારું લાગે તો પણ એન્ટિબાયોટિકનો પૂરો કોર્સ કરો",
            "Stopping antibiotics early because fever subsided allows surviving mutated bacteria to become incurable drug-resistant superbugs.",
            "બે દિવસમાં તાવ ઊતરી જાય તો પણ ડોક્ટરે લખેલા ૫ કે ૭ દિવસનો પૂરો કોર્સ કરો; અધૂરી દવાથી બચેલા જીવાણુ વધુ ઘાતક બને છે.",
            "photos/cphc_antibiotic_stewardship_card2.png",
            "Editorial realistic photograph, authentic Indian setting. An adult carefully organizing a standard prescription blister strip on a bedside table, ensuring every scheduled dose is accounted for. Thoughtful, disciplined routine."
        ),
        "dont1": (
            "Never Demand Antibiotics for Common Viral Cold & Cough",
            "સામાન્ય શરદી-ખાંસીમાં એન્ટિબાયોટિક્સ ન માગો",
            "Antibiotics do not kill common cold, influenza, or viral dengue viruses. Demanding antibiotics for viral illness produces zero cure.",
            "સામાન્ય શરદી, ઉધરસ કે વાયરલ તાવમાં એન્ટિબાયોટિક્સ કોઈ કામ કરતી નથી; ગરમ પાણી, આરામ અને પેરાસિટામોલ જ પૂરતા છે.",
            "photos/cphc_antibiotic_stewardship_card3.png",
            "Editorial realistic photograph, authentic Indian setting. A principled pharmacist behind a dispensary counter politely returning an old paper slip, explaining the need for fresh evaluation. Ethical pharmacy practice."
        ),
        "dont2": (
            "Never Share Leftover Antibiotics with Family Members",
            "પોતાની જૂની દવાઓ પરિવારમાં બીજાને ન આપવી",
            "Every infection requires a specific drug class, precise dosing, and duration. Sharing leftover pills causes toxic kidney/liver harm.",
            "ઘરમાં પડેલી જૂની દવાઓ પરિવારના અન્ય સભ્યોને ન આપો; ખોટી દવા લેવાથી એલર્જી અને કિડનીને ગંભીર નુકસાન થઈ શકે છે.",
            "photos/cphc_antibiotic_stewardship_card4.png",
            "Editorial realistic photograph, authentic Indian setting. An adult checking expiry dates on a medicine strip under a reading lamp before discarding expired pills into a waste container. Responsible household safety."
        )
    }
]
