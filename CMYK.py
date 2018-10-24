from PIL import Image
import ghostscript
image = Image.open('photo.eps')
import img2pdf

try:
    if image.mode == 'CMYK':

        print("Your image is already in CMYK mode")

    if image.mode=="RGB":
        picture=image.convert('CMYK').save('CMYK.eps')
        print("Your image is in RGB color mode i converted it to CMYK image successfully")

    if image.mode=="1":
        picture=image.convert('CMYK').save('CMYK.eps')
        print("Your image is in 1(1-bit pixels, black and white) color mode i converted it to CMYK image  successfully")

    if image.mode == "L":
        picture = image.convert('CMYK').save('CMYK.eps')
        print("Your image is in L(8-bit pixels, black and white) color mode i converted it to CMYK image successfully")

    if image.mode == "P":
        picture = image.convert('CMYK').save('CMYK.eps')
        print("Your image is in P(8-bit pixels, mapped to any other mode using a colour palette) color mode i converted it to CMYK image successfully")

    if image.mode == "RGBA":
        picture = image.convert('CMYK').save('CMYK.eps')
        print("Your image is in RGBA(4x8-bit pixels, true colour with transparency mask) color mode i converted it to CMYK image successfully")

    if image.mode == "YCbCr":
        picture = image.convert('CMYK').save('CMYK.eps')
        print("Your image is in YCbCr(3x8-bit pixels, colour video format) color mode i converted it to CMYK image successfully")

    if image.mode == "I":
        picture = image.convert('CMYK').save('CMYK.eps')
        print("Your image is in I(32-bit signed integer pixels) color mode i converted it to CMYK image successfully")

    if image.mode == "F":
        picture = image.convert('CMYK').save('CMYK.eps')
        print("Your image is in F(32-bit floating point pixels) color mode i converted it to CMYK image successfully")


    with open("RGB.pdf", "wb") as f:
        f.write(img2pdf.convert('RGB.eps'))
        print("PDF created successfully")

except:
    print("failure")


file = 'CMYK.eps'
im = Image.open(file)
new_file = 'CMYK.pdf'
print("PDF created successfully")
im.save(new_file, resolution=10.0,vectorize='true')
