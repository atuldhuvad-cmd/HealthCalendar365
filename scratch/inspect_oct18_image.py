from PIL import Image
import hashlib
from pathlib import Path

ROOT = Path(r"D:\HealthCalendar365")
p = ROOT / "photos" / "oct18_dont2.png"

with Image.open(p) as im:
    print("Format:", im.format)
    print("Size:", im.size)
    print("Mode:", im.mode)
    extrema = im.getextrema()
    print("Extrema:", extrema)
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print("SHA256:", h)
