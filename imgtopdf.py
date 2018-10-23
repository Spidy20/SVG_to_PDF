from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

svg='seo.svg'
pdf='kk.pdf'
drawing = svg2rlg(svg) ##Input file
renderPDF.drawToFile(drawing, pdf)


