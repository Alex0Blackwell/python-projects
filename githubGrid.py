import random as r
from PIL import Image, ImageDraw


def squares(xMax, yMax, draw):
    for a in range(0, xMax, 10):
        for b in range(0, yMax, 10):
            inside = (r.randint(70, 255), r.randint(200, 255), r.randint(125, 200))
            draw.rectangle((a, b, a+10, b+10), fill=inside, outline=('#828282'))


def main():
    height = 500
    width = 500
    image = Image.new('RGB', (height, width))
    draw = ImageDraw.Draw(image)
    squares(width, height, draw)
    image.show()


main()
