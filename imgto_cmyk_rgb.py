from reportlab.graphics import renderPM
from PIL import Image
from svglib.svglib import svg2rlg

####This program converts in 3 module
#(1) SVG will convert in image file
#(2) image will convert into RGB & CMYK color form
#(3) output image will convert into PDF


####Here svg will convert into an Image
drawing = svg2rlg("simple.svg")
new_file_name='simple.jpg'
renderPM.drawToFile(drawing, new_file_name)
####For open image
image = Image.open(new_file_name)

####For convert any color type image into RGB & CMYK image

try:
    ###if image already in RGB form than it will automatically convert into PDF
    if image.mode == 'RGB':
        print("Your image is already in RGB mode so i converted it in PDF")
        im = Image.open(image)
        new_file = 'RGB.pdf'
        im.save(new_file, resolution=200.0)

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

    file = 'RGB.jpg' ###new image file in RGB
    im = Image.open(file)
    new_file = 'RGB.pdf' ###PDF file
    print("PDF created successfully")
    im.save(new_file, resolution=200.0)
except:
    print(" ")


##CMYK

try:
    ###if image in CMYK color mode than it will automatically convert in PDF
    if image.mode == 'CMYK':
        im = Image.open(image)
        new_file = 'CMYK.pdf'
        print("Your image in already in CMYK format so i convert it to PDF")
        im.save(new_file, resolution=200.0)

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

    file = 'CMYK.jpg'##new iimage file in CMYK color form
    im = Image.open(file)
    new_file = 'CMYK.pdf' ####new pdf file
    print("PDF created successfully")
    im.save(new_file, resolution=200.0)
except:
    print(" ")
