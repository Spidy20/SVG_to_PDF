from reportlab.graphics import renderPM
from PIL import Image
import numpy as np
from svglib.svglib import svg2rlg
import img2pdf
import os
import base64

####This program converts in 4 module
#(1) SVG will convert in esp file(for higher resolution)
#(2) esp  will convert into RGB & CMYK esp form
#(3) RGB & CMYK esp file will vectorize & convert into png
#(3) png will image convert into convert into PDF


####Here svg will convert into an EPS
file_name='micro'  ###type only file name(which you want to convert in PDF) without extension
svg=file_name+".svg"
new_image_file_name=file_name+'.eps'
drawing = svg2rlg(svg) ##Input file
renderPM.drawToFile(drawing, new_image_file_name)

####For open image
image = Image.open(new_image_file_name)

####For convert any color type image into RGB & CMYK image

try:

    if image.mode == 'RGB':

        print("Your image is already in RGB mode so i converted it in PDF")
        ###Vectorize
        im = Image.open(new_image_file_name)
        im2 = im.convert()
        colors = im2.getcolors()
        colorsandcount = list(zip(*colors))[1]
        p = np.array(im)
        p.reshape(-1, p.shape[2])
        im2.save('RGB.png')
        ###saving in pdf
        with open("RGB.pdf", "wb") as f:
            f.write(img2pdf.convert('RGB.png'))
            print("PDF created successfully")

    if image.mode=="CMYK":
        picture=image.convert('RGB').save('RGB.eps')
        print("Your image is in CMYK color mode i converted it to RGB image successfully")

    if image.mode=="1":
        picture=image.convert('RGB').save('RGB.eps')
        print("Your image is in 1(1-bit pixels, black and white) color mode i converted it to RGB image  successfully")

    if image.mode == "L":
        picture = image.convert('RGB').save('RGB.eps')
        print("Your image is in L(8-bit pixels, black and white) color mode i converted it to RGB image successfully")

    if image.mode == "P":
        picture = image.convert('RGB').save('RGB.eps')
        print("Your image is in P(8-bit pixels, mapped to any other mode using a colour palette) color mode i converted it to RGB image successfully")

    if image.mode == "RGBA":
        picture = image.convert('RGB').save('RGB.eps')
        print("Your image is in RGBA(4x8-bit pixels, true colour with transparency mask) color mode i converted it to RGB image successfully")

    if image.mode == "YCbCr":
        picture = image.convert('RGB').save('RGB.eps')
        print("Your image is in YCbCr(3x8-bit pixels, colour video format) color mode i converted it to RGB image successfully")

    if image.mode == "I":
        picture = image.convert('RGB').save('RGB.eps')
        print("Your image is in I(32-bit signed integer pixels) color mode i converted it to RGB image successfully")

    if image.mode == "F":
        picture = image.convert('RGB').save('RGB.eps')
        print("Your image is in F(32-bit floating point pixels) color mode i converted it to RGB image successfully")

    im = Image.open('RGB.eps')
    im2 = im.convert()
    colors = im2.getcolors()
    colorsandcount = list(zip(*colors))[1]
    p = np.array(im)
    p.reshape(-1, p.shape[2])
    im2.save('RGB.png')

    with open("RGB.pdf", "wb") as f:
        f.write(img2pdf.convert('RGB.png'))
        print("PDF created successfully")

except:
    print("failure ")


##CMYK

try:
    ###if image in CMYK color mode than it will automatically convert in PDF
    if image.mode == 'CMYK':
        print("Your image is already in CMYK mode so i converted it in PDF")
        im = Image.open(new_image_file_name)
        im2 = im.convert()
        colors = im2.getcolors()
        colorsandcount = list(zip(*colors))[1]
        p = np.array(im)
        p.reshape(-1, p.shape[2])
        im2.save('CMYK.png')

        with open("CMYK.pdf", "wb") as f:
            f.write(img2pdf.convert('CMYK.png'))
            print("PDF created successfully")

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

    im = Image.open('CMYK.eps')
    im2 = im.convert()
    colors = im2.getcolors()
    colorsandcount = list(zip(*colors))[1]
    p = np.array(im)
    p.reshape(-1, p.shape[2])
    im2.save('CMYK.png')

    with open("CMYK.pdf", "wb") as f:
        f.write(img2pdf.convert('CMYK.png'))
        print("PDF created successfully")


except:
    print(" something")

finally:
    ####For removing unnecessary files(JPGs)
    image.close()
    del image
    im.close()
    del im
    os.remove('RGB.eps')
    os.remove('RGB.png')
    os.remove('CMYK.eps')
    os.remove('CMYK.png')
    os.remove(file_name + '.eps')