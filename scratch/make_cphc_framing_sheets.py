import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'review/cphc_framing_2026-10-27'
records = json.loads((OUT/'profiles.json').read_text())['records']
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 14)
for start in range(0,len(records),10):
    sheet=Image.new('RGB',(1080,1980),'#0b1726')
    draw=ImageDraw.Draw(sheet)
    for x,label in [(0,'SOURCE FRAME'),(230,'PREVIOUS SQUARE'),(535,'CORRECTED SQUARE'),(845,'CORRECTED VERTICAL')]:
        draw.text((x+3,3),label,font=font,fill='#8bd7ff')
    for row,record in enumerate(records[start:start+10]):
        name=Path(record['image']).name
        y=25+row*195
        paths=[ROOT/record['image'],OUT/'before'/name.replace('.png','_square.png'),OUT/'after'/name.replace('.png','_square.png'),OUT/'after'/name.replace('.png','_vertical.png')]
        for target,(x,w) in zip(paths,[(0,225),(230,300),(535,300),(845,230)]):
            with Image.open(target) as source:
                thumb=ImageOps.contain(source.convert('RGB'),(w,165))
                sheet.paste(thumb,(x+(w-thumb.width)//2,y))
        draw.text((3,y+169),name+'   '+str(record['profile']),font=font,fill='white')
    sheet.save(OUT/f'comparison_{start//10+1:02d}.jpg',quality=93)
print('14 comparison sheets written')
