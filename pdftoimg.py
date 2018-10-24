# import PythonMagick
#
#
# img = PythonMagick.Image()
# img.density("300")
# img.read("thes.pdf") # read in at 300 dpi
# img.write("thes.png")

import PythonMagick
img = PythonMagick.Image("thes.pdf")
img.density("300") # too late, already read as 72 dpi when image instantiated
img.write("thes.svg")