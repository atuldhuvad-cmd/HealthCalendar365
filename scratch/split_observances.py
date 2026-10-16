import json
import re

with open("D:/HealthCalendar365/data/health_365.json", "r", encoding="utf-8") as f:
    cal = json.load(f)

print("Total calendar items:", len(cal))
multis = []
for item in cal:
    title = item.get("title_en", "")
    # Check for & or and connecting distinct health days
    if (" & " in title or " + " in title or " and " in title.lower()) and ("Day" in title or "Care" in title):
        multis.append((item["id"], title))

print(f"Found {len(multis)} items with combined titles:")
for m in multis:
    print(m)
