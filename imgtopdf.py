from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


drawing = svg2rlg("man.svg")
renderPDF.drawToFile(drawing, "man.pdf")