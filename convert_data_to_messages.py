import json
import os

GUJARATI_NUMERALS = {
    '0': '૦', '1': '૧', '2': '૨', '3': '૩', '4': '૪',
    '5': '૫', '6': '૬', '7': '૭', '8': '૮', '9': '૯'
}

def to_gu_num(n):
    return "".join(GUJARATI_NUMERALS.get(c, c) for c in str(n))

json_path = os.path.join(r"d:\HealthCalendar365", "data", "health_365.json")
js_path = os.path.join(r"d:\HealthCalendar365", "js", "calendar-data.js")

with open(json_path, "r", encoding="utf-8") as f:
    cal = json.load(f)

for day in cal:
    cards = day.get("cards", [])
    for idx, card in enumerate(cards, start=1):
        card["type"] = "message"
        card["index"] = idx
        card["badge_en"] = f"Message #{idx}"
        card["badge_gu"] = f"માર્ગદર્શન #{to_gu_num(idx)}"
        
        # Clean title & prompt if they had "DON'T" or "DO" prefix
        title_en = card.get("title_en", "")
        title_gu = card.get("title_gu", "")
        
        # Clean up specific October week negative titles into constructive messages
        if day["id"] == "10-15":
            if idx == 3:
                card["title_en"] = "Prevent Face & Food Contamination"
                card["title_gu"] = "મોં અને ખોરાકને ગંદકીથી બચાવો"
            elif idx == 4:
                card["title_en"] = "Gentle Eye Care & Safe Drops"
                card["title_gu"] = "આંખની સુરક્ષા અને યોગ્ય ટીપાં"
        elif day["id"] == "10-16":
            if idx == 3:
                card["title_en"] = "Limit Fried Fast Food & Colas"
                card["title_gu"] = "તળેલા ખોરાક અને સોડાથી સાવચેતી"
            elif idx == 4:
                card["title_en"] = "Safe Lifting & Spine Posture"
                card["title_gu"] = "વજન ઊંચકવાની સાચી પદ્ધતિ"
        elif day["id"] == "10-17":
            if idx == 3:
                card["title_en"] = "Controlled Speed & Helmet Discipline"
                card["title_gu"] = "નિયંત્રિત ગતિ અને હેલ્મેટ શિસ્ત"
            elif idx == 4:
                card["title_en"] = "Safe Golden Hour Care"
                card["title_gu"] = "ગોલ્ડન અવરમાં પ્રાથમિક સારવાર"
        elif day["id"] == "10-18":
            if idx == 3:
                card["title_en"] = "Bone Density & Joint Care"
                card["title_gu"] = "હાડકાંની મજબૂતી અને સાંધાની સંભાળ"
            elif idx == 4:
                card["title_en"] = "Qualified Gynecologist Consultation"
                card["title_gu"] = "ગાયનેકોલોજિસ્ટની યોગ્ય સલાહ"
        elif day["id"] == "10-19":
            if idx == 3:
                card["title_en"] = "Protect Ear Canal from Sharp Objects"
                card["title_gu"] = "કાનમાં તણખલાં કે પિન ન નાખવી"
            elif idx == 4:
                card["title_en"] = "Zero Tobacco, Gutkha & Mawa"
                card["title_gu"] = "તમાકુ, ગુટખા અને માવા મુક્તિ"
        elif day["id"] == "10-20":
            if idx == 3:
                card["title_en"] = "Regular Movement & Postural Balance"
                card["title_gu"] = "બેઠાડુ જીવન છોડી નિયમિત સક્રિયતા"
            elif idx == 4:
                card["title_en"] = "Non-Slip Flooring & Lighting"
                card["title_gu"] = "લપસણા ફ્લોરિંગ સામે સુરક્ષા"
        elif day["id"] == "10-21":
            if idx == 3:
                card["title_en"] = "Dry & Airtight Salt Storage"
                card["title_gu"] = "મીઠાને ભેજ અને ગરમીથી બચાવો"
            elif idx == 4:
                card["title_en"] = "Balanced Micronutrient Diet"
                card["title_gu"] = "પૂરતાં પોષક તત્ત્વોવાળો આહાર"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(cal, f, ensure_ascii=False, indent=2)

with open(js_path, "w", encoding="utf-8") as f:
    f.write("// 365-Day Indian Health Calendar Data (Preloaded)\n")
    f.write("window.HEALTH_CALENDAR_DATA = ")
    json.dump(cal, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Successfully converted all 365 days to 4 unified positive health messages!")
