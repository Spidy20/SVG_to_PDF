import cairosvg
import cairocffi as cairo

png=cairosvg.svg2png(url="simple.svg", write_to="test.png")
print(png)
