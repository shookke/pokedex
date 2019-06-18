import inkyphat
import time
from PIL import Image, ImageFont, ImageDraw

inkyphat.set_colour("black")

img = Image.open("resources/pokemon_logo.png")
inkyphat.set_image(img)
inkyphat.show()

time.sleep(10)

from font_fredoka_one import FredokaOne
img = Image.new("P", (214, 104))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 22)

message = 'Hello, Emma!'
w, h = font.getsize(message)
x = (214 / 2) - (w / 2)
y = (104 / 2) - (h / 2)

draw.text((x, y), message, inkyphat.BLACK, font)
inkyphat.set_image(img)
inkyphat.show()
