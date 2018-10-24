
from PIL import Image
import numpy as np
import matplotlib.image as mpimg

image = mpimg.imread('html.png' ,format='PNG') #reading image file into matplotlib.image
print(image.shape)                 #image has shape (height,width,3)
W = np.array([...])                #arbitrary 3x3 matrix of weights
x = np.rollaxis(image,2,1)         #moving the RGB axis to 2nd position
print(x.shape)                     #x has shape (height,3,width)
wx = np.dot(W,x)                   #matrix multiplication
print(wx.shape)                    #Wx has shape (3,height,width)
y = np.rollaxis(wx,0,3)            #moving RGB axis back to 3rd position to have image shape
print(y.shape)