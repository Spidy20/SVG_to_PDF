from PIL import Image
from reportlab.graphics import renderPM
from PIL import Image
from svglib.svglib import svg2rlg

drawing = svg2rlg("testing.svg")
renderPM.drawToFile(drawing, "testing.jpg")
image = Image.open('testing.jpg')


try:
    if image.mode == 'RGB':

        print("Your image is already in RGB mode so i converted it in PDF")

        im = Image.open(image)
        new_file = 'RGB.pdf'

        im.save(new_file, resolution=300.0)

    if image.mode=="CMYK":
        picture=image.convert('RGB').save('RGB.jpg')
        print("Your image is in CMYK color mode i converted it to RGB image successfully")

    if image.mode=="1":
        picture=image.convert('RGB').save('RGB.jpg')
        print("Your image is in 1(1-bit pixels, black and white) color mode i converted it to RGB image  successfully")

    if image.mode == "L":
        picture = image.convert('RGB').save('RGB.jpg')
        print("Your image is in L(8-bit pixels, black and white) color mode i converted it to RGB image successfully")

    if image.mode == "P":
        picture = image.convert('RGB').save('RGB.jpg')
        print("Your image is in P(8-bit pixels, mapped to any other mode using a colour palette) color mode i converted it to RGB image successfully")

    if image.mode == "RGBA":
        picture = image.convert('RGB').save('RGB.jpg')
        print("Your image is in RGBA(4x8-bit pixels, true colour with transparency mask) color mode i converted it to RGB image successfully")

    if image.mode == "YCbCr":
        picture = image.convert('RGB').save('RGB.jpg')
        print("Your image is in YCbCr(3x8-bit pixels, colour video format) color mode i converted it to RGB image successfully")

    if image.mode == "I":
        picture = image.convert('RGB').save('RGB.jpg')
        print("Your image is in I(32-bit signed integer pixels) color mode i converted it to RGB image successfully")

    if image.mode == "F":
        picture = image.convert('RGB').save('RGB.jpg')
        print("Your image is in F(32-bit floating point pixels) color mode i converted it to RGB image successfully")

    file = 'RGB.jpg'
    im = Image.open(file)
    new_file = 'RGB.pdf'
    print("PDF created successfully")
    im.save(new_file, resolution=300.0)
except:
    print(" ")


##CMYK

try:
    if image.mode == 'CMYK':



        im = Image.open(image)
        new_file = 'CMYK.pdf'
        print("Your image in already in CMYK format so i convert it to PDF")
        im.save(new_file, resolution=300.0)

    if image.mode=="RGB":
        picture=image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in RGB color mode i converted it to CMYK image successfully")

    if image.mode=="1":
        picture=image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in 1(1-bit pixels, black and white) color mode i converted it to CMYK image  successfully")

    if image.mode == "L":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in L(8-bit pixels, black and white) color mode i converted it to CMYK image successfully")

    if image.mode == "P":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in P(8-bit pixels, mapped to any other mode using a colour palette) color mode i converted it to CMYK image successfully")

    if image.mode == "RGBA":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in RGBA(4x8-bit pixels, true colour with transparency mask) color mode i converted it to CMYK image successfully")

    if image.mode == "YCbCr":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in YCbCr(3x8-bit pixels, colour video format) color mode i converted it to CMYK image successfully")

    if image.mode == "I":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in I(32-bit signed integer pixels) color mode i converted it to CMYK image successfully")

    if image.mode == "F":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in F(32-bit floating point pixels) color mode i converted it to CMYK image successfully")

    file = 'CMYK.jpg'
    im = Image.open(file)
    new_file = 'CMYK.pdf'
    print("PDF created successfully")
    im.save(new_file, resolution=300.0)


except:
    print("failure")


