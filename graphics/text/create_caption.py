#!/usr/bin/env python
# coding=utf-8
from PIL import Image, ImageFont, ImageDraw
import sys
import os

#create_caption.py <background_image> <title?> <phase?> <outfile>

#try:
#    font = ImageFont.truetype("DejaVuSansCondensed-Bold.ttf", 11)
#except IOError:
font = ImageFont.load_default()


txt1= u"© 2001-2017"
txt2= os.environ['VERSION']
background_image = Image.open(sys.argv[1])
background_image.load()
background_image = background_image.convert("RGBA")
image = Image.new("RGBA", background_image.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(image)
txt1_size = draw.textsize(txt1, font=font)
txt2_size = draw.textsize(txt2, font=font)
draw.text((5, int(image.height - txt1_size[1] - 5)), txt1, font=font, fill=(255,165,0,255))
draw.text((int(image.width - txt2_size[0] - 10), int(image.height - txt2_size[1] - 5)), txt2, font=font, fill=(255,165,0,255))

if len(sys.argv) > 3:
    #paste the other stuff onto the thing.
    logo = Image.open(sys.argv[2])
    logo.load()
    phase = Image.open(sys.argv[3])
    phase.load
    image.paste(logo, ((int(image.width/2) - int(logo.width/2), 18)))
    image.paste(phase, ((int(image.width/2) - int(phase.width/2)), int(image.height - phase.height - 30)))
    outfile_name = sys.argv[4]
else:
    outfile_name = sys.argv[2]

image = Image.alpha_composite(background_image, image)
image.save(outfile_name)
