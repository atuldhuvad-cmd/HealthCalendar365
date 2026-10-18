import json
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

candidates = [
    {
        "slot": "10-19-oral_card2",
        "day_id": "10-19-oral",
        "card_idx": 2,
        "current_title_en": "Rinse Mouth Vigorously After Meals",
        "current_title_gu": "કંઈપણ ખાધા પછી સ્વચ્છ પાણીના કોગળા કરો",
        "current_desc_en": "Rinsing removes trapped carbohydrate debris, neutralizes plaque acids, and prevents enamel erosion.",
        "current_desc_gu": "જમ્યા પછી કે નાસ્તો કર્યા પછી મોંમાં સ્વચ્છ પાણી ભરીને જોરથી કોગળા કરો; દાંતમાં સડો થતો અટકે છે.",
        "rejected_image": "photos/oct19_oral_card2.png",
        "rejection_reason": "Visual Concordance FAIL: Displayed plastic interdental flossing picks instead of vigorous water mouth rinsing after meals.",
        "clinical_intent": "Vigorous post-prandial water swishing/rinsing to dislodge sticky carbohydrates and neutralize plaque acid without invasive equipment.",
        "clinical_safety_rules": [
            "Must depict plain clean water mouth rinsing at washbasin.",
            "Strictly NO dental floss, plastic floss picks, or toothpicks.",
            "Positive clinical hygiene polarity."
        ],
        "required_visual_elements": [
            "Indian adult at a modern, clean domestic washbasin",
            "Swishing clear water with puffed cheeks, preparing to spit into sink",
            "A clean drinking glass or water tumbler nearby",
            "Natural bright morning lighting, realistic dental hygiene setting"
        ],
        "prohibited_elements": [
            "Dental floss thread or plastic flosser sticks",
            "Commercial toothpaste branding or chemical mouthwash bottles",
            "Distorted teeth or unnatural facial expressions"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_19_oral_card2_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian individual actively rinsing mouth with water at a clean, modern ceramic washbasin after a meal. The person has water in mouth with puffed cheeks during a vigorous swish, leaning slightly forward over the sink. A simple clear glass water tumbler rests on the counter. Natural indoor morning lighting, authentic Indian domestic bathroom or wash area setting, clean clinical hygiene, cinematic depth of field, 8k resolution, editorial medical quality. Strictly NO dental floss, NO flosser picks, NO toothpicks, NO logos, NO text."
        }
    },
    {
        "slot": "10-20_card1",
        "day_id": "10-20",
        "card_idx": 1,
        "current_title_en": "Bright Lighting & Bathroom Grab Bars",
        "current_title_gu": "ઘરમાં પૂરતો પ્રકાશ અને બાથરૂમમાં ગ્રેબ-બાર",
        "current_desc_en": "Install sturdy stainless steel grab bars beside toilets, keep night lights on, and remove throw rugs.",
        "current_desc_gu": "વડીલો માટે બાથરૂમમાં મજબૂત ગ્રેબ-બાર લગાવો, રાત્રે અજવાળું રાખો અને લપસી જાય તેવી સાદડીઓ હટાવો.",
        "rejected_image": "photos/oct20_do1.png",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Legacy western stock senior in unauthentic setting lacking sturdy stainless steel bathroom grab bars.",
        "clinical_intent": "Environmental fall prevention for osteoporotic elders: secure architectural support in high-risk wet zones.",
        "clinical_safety_rules": [
            "Depict an authentic Indian senior in domestic environment.",
            "Grab bar must be sturdy, wall-anchored stainless steel, positioned ergonomically.",
            "Bathroom floor must be visibly dry with non-slip tiles."
        ],
        "required_visual_elements": [
            "Indian senior citizen (65+ years) safely and confidently gripping a wall-mounted stainless steel grab bar",
            "Well-lit Indian domestic bathroom or assisted living space",
            "Dry, matte non-skid floor tiles",
            "Warm supportive lighting"
        ],
        "prohibited_elements": [
            "Western hospital ward stock look",
            "Wet or slippery glossy marble floors",
            "Distorted hands or impossible gripping angles"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card1_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an elderly Indian senior citizen (65+ years) safely gripping a sturdy, wall-mounted brushed stainless steel bathroom grab bar in a brightly lit Indian home bathroom. The bathroom has clean, dry, matte non-slip floor tiles and warm morning lighting. Dignified posture, authentic Indian domestic setting, clean clinical fall-prevention environment, cinematic depth of field, 8k resolution, editorial medical journal quality. No text, no logos, no distorted limbs, no slippery wet puddles."
        }
    },
    {
        "slot": "10-20_card2",
        "day_id": "10-20",
        "card_idx": 2,
        "current_title_en": "Weight-Bearing Walks & Ragi / Sesame Nutrition",
        "current_title_gu": "રોજિંદી ચાલવાની કસરત અને રાગી-તલનો આહાર",
        "current_desc_en": "Daily walking stimulates osteoblasts to build bone. Include calcium-rich ragi, sesame, paneer and curd.",
        "current_desc_gu": "દરરોજ પગપાળા ચાલવાથી હાડકાં મજબૂત થાય છે. આહારમાં રાગીની રોટલી, સફેદ તલ અને પનીરનો ઉપયોગ વધારો.",
        "rejected_image": "photos/oct20_do2.png",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Stock park walk lacking Indian elders and calcium-rich dietary context.",
        "clinical_intent": "Dual approach to osteopenia/osteoporosis prevention: weight-bearing mechanical bone loading plus traditional Indian calcium-dense dietary staples.",
        "clinical_safety_rules": [
            "Must clearly highlight traditional Indian calcium sources: ragi, white sesame (til), paneer, curd, or active walking elders.",
            "Do NOT recommend unprescribed pharmaceutical mega-dose calcium pills."
        ],
        "required_visual_elements": [
            "Elderly Indian couple walking actively in a sunlit park in morning light wearing supportive walking shoes OR an authentic Indian kitchen counter displaying roasted ragi flour, white sesame seeds in a brass bowl, fresh artisanal paneer cubes, and set curd",
            "Natural morning sunlight (vital for cutaneous Vitamin D3 synthesis)",
            "Warm authentic Indian setting"
        ],
        "prohibited_elements": [
            "Non-Indian stock models",
            "Synthetic pills or pharmaceutical bottles",
            "Sedentary or frail postures"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card2_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph of active elderly Indian couple walking briskly along a paved walking path in a sunlit Indian garden park during golden morning hours, wearing comfortable walking shoes and cotton attire. Soft natural morning sunlight illuminating them. A tasteful inset or subtle foreground display of traditional Indian calcium foods: ragi grains, small bowl of white sesame seeds, and fresh paneer. Warm authentic Indian lifestyle, healthy bone aging, cinematic depth of field, 8k resolution, editorial medical quality. No text, no logos, no pills."
        }
    },
    {
        "slot": "10-20_card3",
        "day_id": "10-20",
        "card_idx": 3,
        "current_title_en": "Eliminate Slip, Trip & Fall Hazards at Home",
        "current_title_gu": "ઘરમાં લપસી પડવાના અને ઠોકર ખાવાના જોખમો દૂર કરો",
        "current_desc_en": "Slippery wet floors and loose cords are a leading avoidable cause of falls and hip fractures in elders.",
        "current_desc_gu": "ભીનો ફ્લોર અને છૂટા વાયરો વડીલોમાં થાપાના ફ્રેક્ચરનું એક મુખ્ય ટાળી શકાય તેવું કારણ છે.",
        "rejected_image": "photos/oct20_dont1.png",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Generic slip-and-fall graphic lacking authentic Indian elder domestic setting; clinical title/desc mismatch.",
        "clinical_intent": "Elderly fall hazard mitigation: resolving domestic clutter, wet surfaces, and trip hazards that cause osteoporotic hip fractures.",
        "clinical_safety_rules": [
            "Depict hazard resolution (safe environment) or gentle balance exercise.",
            "Avoid fear-mongering graphic depictions of catastrophic injury.",
            "Resolve title/desc conflict by staging title to 'Eliminate Slip, Trip & Fall Hazards at Home'."
        ],
        "required_visual_elements": [
            "Senior Indian home living area with clear, unobstructed walkways",
            "Electrical cables neatly bundled and routed along baseboards away from footpaths",
            "Dry clean floor with firmly anchored non-skid mat",
            "Gentle balance maintenance: Indian elder performing gentle standing balance support"
        ],
        "prohibited_elements": [
            "Gruesome depiction of fallen injured senior",
            "Messy western apartment stock",
            "Cartoon slip warning signs"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card3_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph of an Indian elder living room demonstrating fall hazard prevention: completely clear, uncluttered walkways with electrical cords safely bound and secured along the wall baseboard. A senior Indian grandfather is standing steadily and upright near a firm armchair, wearing non-slip footwear. Warm natural indoor daylight, dry matte tiled flooring, authentic Indian domestic setting, clinical fall-prevention safety, cinematic depth of field, 8k resolution, editorial medical standard. No text, no warning icons, no injured bodies."
        }
    },
    {
        "slot": "10-20_card4",
        "day_id": "10-20",
        "card_idx": 4,
        "current_title_en": "Limit Excessive Salt Intake & Choose Wholesome Hydration",
        "current_title_gu": "વધુ પડતું મીઠું ટાળો અને પૂરતું પાણી-છાશ પીઓ",
        "current_desc_en": "Excessive dietary salt increases urinary calcium loss. For adults, keep total salt from all foods below 5 g/day (equivalent to less than 2 g/day sodium). Choose water or traditional unsalted buttermilk.",
        "current_desc_gu": "વધારે પડતું મીઠું ખાવાથી પેશાબ વાટે કેલ્શિયમ નીકળી જાય છે; પુખ્ત વયના લોકો માટે દિવસભરના બધા ખોરાકમાંથી મળતું કુલ મીઠું ૫ ગ્રામથી ઓછું રાખો (આશરે ૨ ગ્રામથી ઓછું સોડિયમ). પાણી અથવા મીઠું ઉમેર્યા વગરની છાશ પસંદ કરો.",
        "rejected_image": "photos/oct20_dont2.png",
        "rejection_reason": "Visual Concordance FAIL: Generic salt and soda graphic lacking Indian dietary and bone health context; title/desc mismatch.",
        "clinical_intent": "Dietary calcium conservation: educating that excessive dietary sodium (>5g/day) and phosphoric acid in dark sodas accelerate urinary calcium excretion.",
        "clinical_safety_rules": [
            "Depict avoidance of raw salt sprinkling and dark aerated sodas.",
            "Promote hydration with traditional unsalted chaas (buttermilk) or water.",
            "Resolve title/desc conflict by staging title to 'Limit Excessive Salt Intake & Choose Wholesome Hydration'."
        ],
        "required_visual_elements": [
            "Indian dining table setting showing freshly cooked food",
            "A shaker of raw salt set aside with a clear 'moderation' visual cue",
            "A glass of plain refreshing water or homemade thin buttermilk alongside dark carbonated soda pushed away",
            "Authentic Indian home culinary context"
        ],
        "prohibited_elements": [
            "Commercial brand soda logos",
            "Piles of chemical white powder",
            "Unrelated western fast food"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_20_card4_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian dining table setting demonstrating healthy bone nutrition: a glass of fresh homemade buttermilk (chaas) and clean water in focus, with a dark aerated soda bottle and an open salt shaker pushed away to the background. Wholesome Indian meal setting with brass or stainless steel plate, warm natural daylight, editorial clinical nutrition focus, cinematic depth of field, 8k resolution, medical journal quality. Strictly NO brand logos, NO text labels, NO artificial graphic overlays."
        }
    },
    {
        "slot": "10-21_card1",
        "day_id": "10-21",
        "card_idx": 1,
        "current_title_en": "Store Iodized Salt in Airtight Jars",
        "current_title_gu": "આયોડાઇઝ્ડ મીઠું હવાચુસ્ત બરણીમાં ઢાંકીને રાખો",
        "current_desc_en": "Always buy sealed packets with the smiling sun iodized logo. Store in airtight ceramic or glass jars.",
        "current_desc_gu": "હંમેશા પેક કરેલું આયોડાઇઝ્ડ મીઠું ખરીદો અને તેને કાચ કે ચિનાઈ માટીની હવાચુસ્ત બરણીમાં ઢાંકીને રાખો.",
        "rejected_image": "photos/oct21_do1.png",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Refrigerator storage plastic containers lacking Indian kitchen setting with traditional airtight ceramic/glass salt jars.",
        "clinical_intent": "Universal Salt Iodization (USI) compliance: airtight storage of potassium iodate fortified salt to prevent volatile sublimation.",
        "clinical_safety_rules": [
            "Show fine iodized salt stored in airtight ceramic (barni) or glass container.",
            "Must indicate sealed packaged salt with smiling sun icon concept.",
            "Do NOT recommend storing salt in the refrigerator (moisture risk)."
        ],
        "required_visual_elements": [
            "Authentic Indian kitchen counter with a traditional glazed ceramic jar (barni) or heavy glass airtight jar",
            "Scooping clean fine iodized white salt with a dry wooden or stainless steel spoon",
            "A sealed foil/plastic packet of iodized salt nearby with generic smiling sun iodized symbol",
            "Clean, dry, warm domestic kitchen atmosphere"
        ],
        "prohibited_elements": [
            "Plastic refrigerator crisper bins",
            "Damp or open dripping surfaces",
            "Commercial brand names"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card1_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an authentic Indian kitchen counter featuring a traditional ceramic barni (glazed white and brown porcelain jar) with an airtight lid, and a clear glass jar containing fine white iodized salt. A small wooden spoon is resting beside the open jar showing clean dry powdered salt. In the background sits a sealed salt packet with a generic smiling sun iodized logo. Warm natural kitchen lighting, clean hygiene, authentic Indian domestic setting, cinematic depth of field, 8k resolution, editorial quality. No commercial brand logos, no text."
        }
    },
    {
        "slot": "10-21_card2",
        "day_id": "10-21",
        "card_idx": 2,
        "current_title_en": "Add Iodized Salt Towards the End of Cooking",
        "current_title_gu": "રાંધતી વખતે મીઠું છેલ્લે ઉમેરવાની ટેવ પાડો",
        "current_desc_en": "Prolonged high-heat boiling can degrade and leach fortified iodine compounds. Adding iodized salt towards the end of cooking helps retain full micronutrient value.",
        "current_desc_gu": "લાંબા સમય સુધી વધુ ગરમીમાં ઉકાળવાથી આયોડિનનું પ્રમાણ ઘટી શકે છે; રસોઈ પૂરી થવાના સમયે મીઠું ઉમેરવાથી આયોડિનનું મૂલ્ય જળવાય છે.",
        "rejected_image": "photos/oct21_do2.png",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Unrelated salad shield graphic lacking Indian cooking setting and salt addition timing context.",
        "clinical_intent": "Thermostability preservation: potassium iodate in salt is heat-sensitive; adding salt towards the final stage of Indian cooking retains maximal micronutrient potency.",
        "clinical_safety_rules": [
            "Show measured addition of salt (do NOT depict heavy pouring).",
            "Must be an authentic Indian cooking vessel (kadai, handi, or steel pot).",
            "Maintain moderate daily sodium message (<5g/day total)."
        ],
        "required_visual_elements": [
            "Indian home cook gently adding a small, measured pinch/spoon of fine iodized salt into a freshly prepared vegetable curry (sabzi)",
            "Stainless steel kadai or pot on a clean gas burner near the end of cooking",
            "Steam gently rising from the colorful nutritious dish",
            "Authentic warm Indian domestic culinary context"
        ],
        "prohibited_elements": [
            "Western raw salad bowls",
            "Vigorous violent boiling with large salt pours",
            "Brand packaging over the pot"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card2_v1.png",
            "prompt": "Ultra-photorealistic 4:3 close-up photograph of an Indian home cook's hand gently sprinkling a measured small pinch of fine iodized salt into a traditional stainless steel kadai containing freshly cooked vegetable curry (sabzi) near the end of cooking. Gentle soft steam rising, authentic Indian home kitchen with clean countertop, natural warm kitchen lighting, cinematic depth of field, 8k resolution, editorial culinary medicine standard. Strictly no raw salad, no commercial logos, no oversized salt pouring."
        }
    },
    {
        "slot": "10-21_card3",
        "day_id": "10-21",
        "card_idx": 3,
        "current_title_en": "Avoid Unbranded Loose Coarse Salt",
        "current_title_gu": "ખુલ્લું અને બિન-આયોડાઇઝ્ડ મીઠું વાપરવાનું ટાળો",
        "current_desc_en": "Unbranded loose coarse salt lacks iodine; iodine deficiency in pregnant mothers leads to child mental retardation.",
        "current_desc_gu": "ખુલ્લું બિન-આયોડાઇઝ્ડ મીઠું વાપરશો નહીં; આયોડિનની કમીથી બાળકોમાં માનસિક મંદતા અને ગલગંડ (ગોઇટર) થાય છે.",
        "rejected_image": "photos/oct21_dont1.png",
        "rejection_reason": "Visual Concordance & Cultural Authenticity FAIL: Generic rock salt visual without authentic Indian market/kitchen context; title/desc conflict.",
        "clinical_intent": "Rejection of unfortified non-iodized loose salt: preventing preventable intellectual disability and endemic goiter in mothers and children.",
        "clinical_safety_rules": [
            "Do NOT imply that rock salt (sendha namak) or black salt is naturally iodized.",
            "Do NOT recommend eating more salt; recommend switching exclusively to iodized salt.",
            "Resolve title/desc conflict by staging title to 'Avoid Unbranded Loose Coarse Salt'."
        ],
        "required_visual_elements": [
            "Visual contrast: A packet of certified iodized salt chosen in favor of open, unbranded coarse raw crystal salt in a rustic burlap sack",
            "Indian grocery (kirana) or pantry setting",
            "Clear educational focus on packaged iodized protection"
        ],
        "prohibited_elements": [
            "Implying rock salt is healthy for thyroid without iodine",
            "Graphic medical photos of giant disfiguring goiters (keep dignified/educational)",
            "Brand trademarks"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card3_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph of an educational comparison in an authentic Indian grocery or kitchen: in clear focus, a clean sealed packet of fine iodized salt with a sun logo, placed beside an open unbranded rustic gunny sack of coarse grey crystal rock salt with a subtle push-away composition. Clean lighting, authentic Indian grocery context, focus on maternal and child thyroid health protection, cinematic depth of field, 8k resolution, editorial public health quality. No text slogans, no brand trademarks, no disfiguring medical anomalies."
        }
    },
    {
        "slot": "10-21_card4",
        "day_id": "10-21",
        "card_idx": 4,
        "current_title_en": "Balanced Micronutrient Diet",
        "current_title_gu": "પૂરતાં પોષક તત્ત્વોવાળો આહાર",
        "current_desc_en": "Store iodized salt in a tightly closed container in a cool, dry place away from moisture.",
        "current_desc_gu": "આયોડાઇઝ્ડ મીઠું હવાચુસ્ત બરણીમાં, ઠંડી અને સૂકી જગ્યાએ ભેજથી દૂર રાખો.",
        "rejected_image": "photos/oct21_dont2.png",
        "rejection_reason": "Visual Concordance FAIL: Unrelated food panel lacking dry, covered iodized-salt storage context.",
        "clinical_intent": "Keep iodized salt tightly covered and protected from moisture in a cool, dry storage area.",
        "clinical_safety_rules": [
            "Show iodized salt in a tightly closed container on a clean, cool, dry pantry shelf."
        ],
        "required_visual_elements": [
            "Indian kitchen pantry cupboard shelf, cool and dry, with a tightly closed salt jar",
            "Clear protection from moisture",
            "Clean, organized, authentic Indian kitchen"
        ],
        "prohibited_elements": [
            "Open or damp salt container",
            "Unrelated western food panels",
            "Brand logos"
        ],
        "candidate_spec": {
            "aspect_ratio": "4:3",
            "minimum_dimensions": "720x540",
            "target_filename": "photos/staging/candidate_10_21_card4_v1.png",
            "prompt": "Ultra-photorealistic 4:3 photograph showing proper iodized-salt storage in an Indian kitchen: a tightly closed ceramic or glass salt container placed on a clean, cool, dry pantry shelf protected from moisture. Authentic Indian home setting, warm natural lighting, 8k editorial quality. No logos or text."
        }
    }
]

out_path = os.path.join(PROJECT_DIR, 'review', 'candidate_specifications_9_rejected.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({
        "total_rejected_candidates": len(candidates),
        "production_hold_notice": "PRODUCTION HOLD ACTIVE: These specifications and prompts are staged for human review. Do NOT invoke image APIs or spend credits until formal authorization.",
        "candidate_specifications": candidates
    }, f, indent=2, ensure_ascii=False)

print(f"Generated {out_path} with {len(candidates)} candidate specifications.")
