from reportlab.graphics import renderPDF,renderPM
from svglib.svglib import svg2rlg

svg='photo.svg'
eps='photo.eps'
drawing = svg2rlg(svg) ##Input file
renderPM.drawToFile(drawing, eps)
