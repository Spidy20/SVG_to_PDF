from PIL import Image
import ghostscript
image = Image.open('photo.eps')

try:
    if image.mode == 'RGB':

        print("Your image is already in RGB mode")

    if image.mode=="CMYK":
        picture=image.convert('RGB').save('RGB.eps')
        print("Your image is in CMYK color mode i converted it to RGB image successfully")

    if image.mode=="1":
        picture=image.convert('RGB').save('RGB.svg')
        print("Your image is in 1(1-bit pixels, black and white) color mode i converted it to RGB image  successfully")

    if image.mode == "L":
        picture = image.convert('RGB').save('RGB.svg')
        print("Your image is in L(8-bit pixels, black and white) color mode i converted it to RGB image successfully")

    if image.mode == "P":
        picture = image.convert('RGB').save('RGB.svg')
        print("Your image is in P(8-bit pixels, mapped to any other mode using a colour palette) color mode i converted it to RGB image successfully")

    if image.mode == "RGBA":
        picture = image.convert('RGB').save('RGB.svg')
        print("Your image is in RGBA(4x8-bit pixels, true colour with transparency mask) color mode i converted it to RGB image successfully")

    if image.mode == "YCbCr":
        picture = image.convert('RGB').save('RGB.svg')
        print("Your image is in YCbCr(3x8-bit pixels, colour video format) color mode i converted it to RGB image successfully")

    if image.mode == "I":
        picture = image.convert('RGB').save('RGB.eps')
        print("Your image is in I(32-bit signed integer pixels) color mode i converted it to RGB image successfully")

    if image.mode == "F":
        picture = image.convert('RGB').save('RGB.svg')
        print("Your image is in F(32-bit floating point pixels) color mode i converted it to RGB image successfully")


except:
    print("failure")


file = ('RGB.svg')
im = Image.open(file)
new_file = 'RGB.pdf'
print("PDF created successfully")
im.save(new_file, resolution=300)

