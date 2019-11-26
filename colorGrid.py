import random as r
from PIL import Image, ImageDraw


def squares(xMax, yMax, draw):
    step = 25
    for a in range(0, xMax, step):
        for b in range(0, yMax, step):
            d = r.randint(0, 100)
            dark = (d, d, d)
            light = (r.randint(120, 150), r.randint(175, 230), r.randint(240, 255))
            if(r.random() > 0.5):
                draw.rectangle((a, b, a+step, b+step), fill=light)
            else:
                draw.rectangle((a, b, a+step, b+step), fill=dark)


def main():
    height = 500
    width = 500
    image = Image.new('RGB', (height, width))
    draw = ImageDraw.Draw(image)
    squares(width, height, draw)
    image.show()


main()
