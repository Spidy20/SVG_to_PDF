import os
import base64

startSvgTag = """<?xml version="1.0" encoding="iso-8859-1"?>
<!-- Generator: Adobe Illustrator 19.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="-48 0 280.001 280.001" style="enable-background:new 0 0 512.001 512.001;" xml:space="preserve">"""

endSvgTag = """</svg>"""
files='RGB.eps'
pngFile = open(files, 'rb')
base64data = base64.b64encode(pngFile.read())
base64String = '<image xlink:href="data:image/png;base64,{0}" width="240" height="240" x="0" y="0" />'.format(base64data.decode('utf-8'))
f = open(os.path.splitext(files)[0] + ".svg", 'w')
f.write(startSvgTag + base64String + endSvgTag)
print('Converted ', files, ' to ', os.path.splitext(files)[0], ".svg")