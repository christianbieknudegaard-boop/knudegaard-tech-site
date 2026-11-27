# Lager assets/og.png (1200x630) til forhåndsvisning ved deling
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
W, H, S = 1200, 630, 2           # tegnes i dobbel størrelse og skaleres ned for skarphet
w, h = W*S, H*S
bg = Image.new('RGB', (w, h), (7, 28, 49))
glow = Image.new('RGB', (w, h), (7, 28, 49))
d = ImageDraw.Draw(glow)
for (x, y, r, c) in [(-100, -200, 700, (10, 116, 168)), (w-300, 250, 650, (18, 184, 154)), (w//2-200, h+50, 520, (44, 239, 176))]:
    d.ellipse((x-r, y-r, x+r, y+r), fill=c)
bg = Image.blend(bg, glow.filter(ImageFilter.GaussianBlur(220)), .55)

def rounded(im, size, radius):
    im = im.convert('RGBA').resize((size, size), Image.LANCZOS)
    m = Image.new('L', (size, size), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, size-1, size-1), radius, fill=255)
    im.putalpha(m)
    return im

def shadow(base, box, radius, blur=40, alpha=110, dy=24):
    sh = Image.new('RGBA', base.size, (0, 0, 0, 0))
    x0, y0, x1, y1 = box
    ImageDraw.Draw(sh).rounded_rectangle((x0, y0+dy, x1, y1+dy), radius, fill=(0, 0, 0, alpha))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))

for out, l1, l2 in [('og.png','Apper uten reklame for iPhone, iPad og Android','Laget i Lillesand · knudegaard.no'),
                    ('og-en.png','Ad-free apps for iPhone, iPad and Android','Made in Lillesand, Norway · knudegaard.no')]:
  base = bg.convert('RGBA')
  logo = Image.open('brand/logo-horisontal-hvit.png')
  lw = 560*S; logo = logo.resize((lw, round(logo.height*lw/logo.width)), Image.LANCZOS)
  base.alpha_composite(logo, (90*S, 105*S))

  font = ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', 34*S, index=0)
  d = ImageDraw.Draw(base)
  d.text((92*S, 290*S), l1, font=font, fill=(255, 255, 255, 200))
  d.text((92*S, 338*S), l2, font=font, fill=(159, 233, 214, 230))

  sz, rad, gap = 128*S, 29*S, 22*S
  x = 90*S; y = 418*S
  for n in ['skanlio', 'lumtidy', 'wordarc', 'offthehook']:
      shadow(base, (x, y, x+sz, y+sz), rad, blur=18*S, alpha=120, dy=10*S)
      base.alpha_composite(rounded(Image.open(f'assets/{n}.png'), sz, rad), (x, y))
      x += sz + gap
  base = base.convert('RGB').resize((W, H), Image.LANCZOS)
  base.save('assets/'+out, optimize=True)
  print(out, os.path.getsize('assets/'+out)//1024, 'KB')
