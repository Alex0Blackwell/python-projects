# Alex

from PIL import Image, ImageDraw


def horLines(maxWidth, maxHeight, draw):
    xStart = 0
    xFin = maxWidth
    y = 0

    while(y < maxHeight):
        horLine = ((xStart, y), (xFin, y))
        draw.line(horLine, fill=128)
        y += 10


def main():
    height = 300
    width = 300
    image = Image.new(mode='L', size=(height, width), color=255)
    draw = ImageDraw.Draw(image)
    horLines(width, height, draw)
    image.show()


main()
# if __name__ == '__main__':
#
#     horLine = ((xStart, yStart), (xFin, yFin))
#     draw.line(horLine, fill=128)
#     # del draw
#
#     image.show()
