from PIL import Image
import numpy as np
im = Image.open("RGB.eps")
im2=im.convert()
colors = im2.getcolors()
colorsandcount = list(zip(*colors))[1]
print("palette: [" + str(len(colorsandcount)) + "] " + str(colorsandcount) )
p = np.array(im)
print(p.reshape(-1, p.shape[2]))
im2.save('ss.png')