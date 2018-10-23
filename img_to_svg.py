import os
import base64

startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
 <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
 <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 256.001 256.001" style="enable-background:new 0 0 512.001 512.001;" xml:space="preserve">
"""

endSvgTag = """</svg>"""

files='seo.png'
pngFile = open(files, 'rb')
base64data = base64.b64encode(pngFile.read()).replace(b'\n',b'')
base64String = '<image xlink:href="data:image/png;base64,{0}" width="240" height="240" x="0" y="0" />'.format(base64data.decode('utf-8'))
f = open(os.path.splitext(files)[0] + ".svg", 'w')
f.write(startSvgTag + base64String + endSvgTag)
print('Converted ', files, ' to ', os.path.splitext(files)[0], ".svg")