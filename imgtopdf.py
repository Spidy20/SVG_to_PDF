# from PIL import Image
# import os
# file='First_Page.jpg'
# im=Image.open(file)
# new_file='First_Page.pdf'
# im.save(new_file,resolution=100.0)

import img2pdf

with open("new.pdf","wb") as f:
    f.write(img2pdf.convert('CMYK.jpg'))

