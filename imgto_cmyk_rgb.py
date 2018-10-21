from reportlab.graphics import renderPM
from PIL import Image
from svglib.svglib import svg2rlg
import img2pdf
import os

####This program converts in 3 module
# (1) SVG will convert in image file
# (2) image will convert into RGB & CMYK color form
# (3) output image will convert into PDF


####Here svg will convert into an Image
file_name = 'app'  ###type only file name(which you want to convert in PDF) without extension
svg = file_name + ".svg"
new_image_file_name = file_name + '.jpg'
drawing = svg2rlg(svg)  ##Input file
renderPM.drawToFile(drawing, new_image_file_name)

####For open image
image = Image.open(new_image_file_name)

####For convert any color type image into RGB & CMYK image

try:
    ###if image already in RGB form than it will automatically convert into PDF
    if image.mode == 'RGB':
        with open("RGB.pdf", "wb") as f:  ##RGB.pdf is new PDF name
            f.write(img2pdf.convert(image))
        print("Your image is already in RGB mode so i converted it in PDF")

    if image.mode == "CMYK":
        picture = image.convert('RGB').save('RGB.jpg')
        print("Your image is in CMYK color mode i converted it to RGB image successfully")

    if image.mode == "1":
        picture = image.convert('RGB').save('RGB.jpg')
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

    ###new image file in RGB
    with open("RGB.pdf", "wb") as f:
        f.write(img2pdf.convert('RGB.jpg'))
    print("PDF created successfully")

except:
    print(" ")

##CMYK

try:
    ###if image in CMYK color mode than it will automatically convert in PDF
    if image.mode == 'CMYK':
        im = Image.open(image)
        with open("CMYK.pdf", "wb") as f:  ####CMYK.pdf is new PDF name
            f.write(img2pdf.convert(image))
            print("Your image in already in CMYK format so i convert it to PDF")

    if image.mode == "RGB":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in RGB color mode i converted it to CMYK image successfully")

    if image.mode == "1":
        picture = image.convert('CMYK').save('CMYK.jpg')
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
        print(
            "Your image is in YCbCr(3x8-bit pixels, colour video format) color mode i converted it to CMYK image successfully")

    if image.mode == "I":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in I(32-bit signed integer pixels) color mode i converted it to CMYK image successfully")

    if image.mode == "F":
        picture = image.convert('CMYK').save('CMYK.jpg')
        print("Your image is in F(32-bit floating point pixels) color mode i converted it to CMYK image successfully")

    ##new iimage file in CMYK color form
    with open("CMYK.pdf", "wb") as f:
        f.write(img2pdf.convert('CMYK.jpg'))
    print("PDF created successfully")


except:
    print(" ")

####For removing unnecessary files(JPGs)
os.remove('RGB.jpg')
os.remove('CMYK.jpg')

