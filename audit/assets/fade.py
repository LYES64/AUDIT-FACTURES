from PIL import Image
import numpy as np
im=Image.open("douche.jpg").convert("RGB")
W,H=im.size
# crop on the walk-in shower (glass + grab bar + seat + column + drain)
box=(int(0.31*W),int(0.14*H),int(0.80*W),int(0.94*H))  # left,top,right,bottom
im=im.crop(box)
# resize to output (retina)
OW,OH=680,760
im=im.resize((OW,OH),Image.LANCZOS)
arr=np.asarray(im).astype(np.float32)

xs=np.linspace(0,1,OW)[None,:]
ys=np.linspace(0,1,OH)[:,None]
def smooth(t):
    t=np.clip(t,0,1); return t*t*(3-2*t)
# left strong fade (0->0.34), right gentle (0.93->1), top/bottom feather
left = smooth(xs/0.34)
right= smooth((1-xs)/0.10)
top  = smooth(ys/0.09)
bot  = smooth((1-ys)/0.09)
mask=(left*right*top*bot)
mask=np.clip(mask,0,1)
alpha=(mask*255).astype(np.uint8)
rgba=np.dstack([arr.astype(np.uint8),alpha])
out=Image.fromarray(rgba,"RGBA")
out.save("douche_fade.png")
print("saved douche_fade.png",out.size)
