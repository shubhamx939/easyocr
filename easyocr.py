

import easyocr
reader = easyocr.Reader(['en'])

import PIL
from PIL import ImageDraw
img = PIL.Image.open("111111.png")
img

bounds = reader.readtext("111111.png")
bounds

def draw_boxes(image, bounds, color="blue", width=2):
  draw = ImageDraw.Draw(image)
  for bound in bounds:
    p0, p1, p2, p3 = bound[0]
    draw.line([*p0, *p1, *p2, *p3, *p0], fill = color, width = width)
  return image

draw_boxes(img, bounds)

bounds = reader.readtext("111111.png", contrast_ths=0.05, adjust_contrast=0.7, add_margin=0.45, width_ths=0.7, decoder="beamsearch")
bounds

