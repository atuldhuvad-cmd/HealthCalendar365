"""
[DEPRECATED SCRIPT] extract_clean_photos.py
-----------------------------------------------------------------------------
This script has been PERMANENTLY RETIRED.
HealthCalendar365 uses independent high-resolution 4:3 photographs stored
directly in photos/. Blind monolithic PNG pixel cropping is obsolete.

For AI photographic asset generation, use the official Gemini Image Pipeline:
  python generate_with_gemini.py --day 10-15
-----------------------------------------------------------------------------
"""

import sys

def main():
    print("[DEPRECATED] extract_clean_photos.py has been retired.")
    print("HealthCalendar365 uses independent 4:3 photo assets stored in photos/.")
    print("For Gemini image asset generation, run: python generate_with_gemini.py")
    sys.exit(0)

if __name__ == "__main__":
    main()
