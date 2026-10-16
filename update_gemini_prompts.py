"""
Updates all 365 days in data/health_365.json and js/calendar-data.js
to adhere strictly to the Gemini Imagen 3 Prompt Formula:
"Ultra-photorealistic 4:3 close-up photograph of [SUBJECT / ACTION]. Warm natural lighting, authentic Indian domestic or clinical setting, clean clinical hygiene, cinematic depth of field, 8k resolution, editorial medical magazine quality. No text, no logos, no distorted hands."
"""

import json
import os
import re

DATA_PATH = os.path.join("data", "health_365.json")
JS_PATH = os.path.join("js", "calendar-data.js")

# Exact handcrafted clinical editorial subjects for October 15 to October 21
OCTOBER_WEEK_SUBJECTS = {
    # 10-15: Global Handwashing Day & World White Cane Day
    ("10-15", 1): "Indian healthcare worker demonstrating proper 20-second hand washing technique with rich soap lather under a clean chrome tap",
    ("10-15", 2): "Indian individual with a white cane with red safety band walking carefully and with dignity along bright yellow tactile paving",
    ("10-15", 3): "Indian mother washing fresh organic vegetables thoroughly under clean running tap water before cooking a domestic meal",
    ("10-15", 4): "Indian ophthalmologist gently administering sterile prescribed eye drops to an Indian patient in a modern clinical room",

    # 10-16: World Food Day & World Spine Day
    ("10-16", 1): "balanced traditional Indian bronze thali with steel katoris of yellow dal, steamed sabzi, fresh curd, sprouted pulses, and warm multigrain roti",
    ("10-16", 2): "Indian IT professional working at an ergonomic desk with upright spine posture, lumbar cushion support, and natural window lighting",
    ("10-16", 3): "colorful assortment of fresh whole Indian fruits like papaya, pomegranate, guava and tender coconut water on a wooden table",
    ("10-16", 4): "Indian physiotherapist demonstrating safe weight-lifting technique with bent knees and a straight spine in a clinical studio",

    # 10-17: World Trauma Day (Road Safety & Golden Hour)
    ("10-17", 1): "responsible Indian two-wheeler commuter securely fastening an ISI certified full-face safety helmet before riding",
    ("10-17", 2): "Indian 108 emergency ambulance response team with modern paramedic equipment responding during the critical golden hour",
    ("10-17", 3): "disciplined Indian riders waiting calmly at a pedestrian zebra crossing wearing safety helmets in orderly city traffic",
    ("10-17", 4): "trained Indian first aid volunteer demonstrating gentle airway and recovery positioning with a sterile emergency first-aid kit",

    # 10-18: World Menopause Day
    ("10-18", 1): "middle-aged Indian woman enjoying mild morning sunlight in a veranda garden with a nutritious bowl of roasted sesame and almonds",
    ("10-18", 2): "healthy Indian woman practicing serene Anulom-Vilom pranayama breathing outdoors surrounded by green plants in morning sunlight",
    ("10-18", 3): "female Indian doctor explaining a bone density DXA scan chart to an Indian woman in a modern consultation clinic",
    ("10-18", 4): "warm and supportive healthcare consultation between an Indian woman and an experienced female gynecologist in a clinic",

    # 10-19: Preventive Health: Ear & Hearing Care + Oral Hygiene
    ("10-19", 1): "Indian person holding a soft-bristle toothbrush with herbal toothpaste in a clean modern domestic bathroom",
    ("10-19", 2): "Indian ENT specialist gently examining an adult patient's ear with a modern diagnostic otoscope in an examination room",
    ("10-19", 3): "gentle ear hygiene visual showing a clean soft cotton towel drying outer ear gently after bathing",
    ("10-19", 4): "healthy smiling Indian adult with clean bright teeth and gums holding a crisp fresh green apple, representing tobacco-free life",

    # 10-20: World Osteoporosis Day
    ("10-20", 1): "elderly Indian senior safely using a sturdy stainless steel bathroom grab bar with clean dry non-slip tiled flooring",
    ("10-20", 2): "active elderly Indian couple walking briskly in a sunlit morning park wearing comfortable supportive walking shoes",
    ("10-20", 3): "senior Indian citizen performing gentle standing balance exercises under physiotherapist guidance in a bright living room",
    ("10-20", 4): "brightly lit Indian home hallway with safe non-skid floor runners and completely clear walkways for fall prevention",

    # 10-21: World Iodine Deficiency Disorders Prevention Day
    ("10-21", 1): "traditional Indian kitchen counter with fine iodized salt being scooped from a clean airtight ceramic jar",
    ("10-21", 2): "Indian home cook gently adding a measured pinch of iodized salt towards the end of preparing a fresh vegetable curry",
    ("10-21", 3): "tightly sealed glass kitchen container with iodized salt stored in a cool dry pantry cupboard away from heat and moisture",
    ("10-21", 4): "vibrant array of micronutrient-rich Indian staples including homemade curd, green leafy vegetables, lentils and whole grains"
}

def clean_subject(title_en, desc_en, day_title):
    # Strip prefixes like "Message #1", "DO", "DON'T", etc.
    cleaned_title = re.sub(r'^(DO|DON\'T|Avoid|Never|Ensure|Practice|Always)\s*[:\-]?\s*', '', title_en, flags=re.I).strip()
    cleaned_desc = re.sub(r'^(DO|DON\'T|Avoid|Never|Ensure|Practice|Always)\s*[:\-]?\s*', '', desc_en, flags=re.I).strip()
    
    # Synthesize subject action
    return f"Indian health context demonstrating {cleaned_title.lower()} ({cleaned_desc.lower().rstrip('.')})"

def build_gemini_prompt(subject_action):
    # Strict prompt formula
    return (
        f"Ultra-photorealistic 4:3 close-up photograph of {subject_action}. "
        "Warm natural lighting, authentic Indian domestic or clinical setting, clean clinical hygiene, "
        "cinematic depth of field, 8k resolution, editorial medical magazine quality. "
        "No text, no logos, no distorted hands."
    )

def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    updated_count = 0
    for day in data:
        day_id = day.get("id")
        day_title = day.get("title_en", "")
        cards = day.get("cards", [])
        
        for idx, card in enumerate(cards, start=1):
            key = (day_id, idx)
            if key in OCTOBER_WEEK_SUBJECTS:
                subject_action = OCTOBER_WEEK_SUBJECTS[key]
            else:
                # Use card's current prompt or synthesize
                current_prompt = card.get("ai_prompt", "")
                # Check if current prompt already has a descriptive body
                m = re.search(r'(?:visual of|representing|depicting|showing|depicting the danger of|photo of|photograph of)\s+([^,]+)', current_prompt, re.I)
                if m:
                    extracted = m.group(1).strip()
                    subject_action = f"Indian health context depicting {extracted.lower()}"
                else:
                    subject_action = clean_subject(card.get("title_en", ""), card.get("desc_en", ""), day_title)
                    
            new_prompt = build_gemini_prompt(subject_action)
            card["ai_prompt"] = new_prompt
            updated_count += 1
            
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    with open(JS_PATH, "w", encoding="utf-8") as f:
        f.write("// 365-Day Indian Health Calendar Data (Preloaded)\n")
        f.write("window.HEALTH_CALENDAR_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
        
    print(f"Successfully upgraded {updated_count} cards across all 365 days to the Gemini Imagen 3 prompt formula!")

if __name__ == "__main__":
    main()
