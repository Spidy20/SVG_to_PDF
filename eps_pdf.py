# import img2pdf
#
# with open("RGB.pdf", "wb") as f:
#     f.write(img2pdf.convert('RGB.svg'))
# print("PDF created successfully")
from PIL import Image
import ghostscript
image = Image.open('photo.eps')

file = ('thes.svg')
im = Image.open(file)
new_file = 'thes.pdf'
print("PDF created successfully")
im.save(new_file, resolution=300)
