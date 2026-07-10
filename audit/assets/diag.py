from PIL import Image, ImageDraw
im=Image.open("douche.jpg").convert("RGB")
W,H=im.size
# crop on the walk-in shower
im=im.crop((int(0.33*W),int(0.13*H),int(0.82*W),int(0.95*H)))
OW,OH=520,440
im=im.resize((OW,OH),Image.LANCZOS).convert("RGBA")

# diagonal left cut: visible polygon (trapezoid), left edge slanted
Xt, Xb = 165, 20        # top-left x, bottom-left x
poly=[(Xt,0),(OW,0),(OW,OH),(Xb,OH)]
mask=Image.new("L",(OW,OH),0)
ImageDraw.Draw(mask).polygon(poly,fill=255)
im.putalpha(mask)

# accent liseré along the diagonal (orange) + fine teal
ov=Image.new("RGBA",(OW,OH),(0,0,0,0))
d=ImageDraw.Draw(ov)
d.line([(Xt,0),(Xb,OH)], fill=(219,138,56,255), width=9)      # orange
d.line([(Xt-13,0),(Xb-13,OH)], fill=(15,59,69,255), width=5)  # teal, just outside (will be clipped by mask edge)
out=Image.alpha_composite(im, ov)
# re-clip so the teal outside diagonal stays transparent
out.putalpha(mask)
out.save("douche_diag.png")
print("saved douche_diag.png", out.size)
