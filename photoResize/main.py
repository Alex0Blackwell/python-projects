# image resizer

from PIL import Image
import os


def resize(name):
    basewidth = 1000
    img = Image.open(f"photos/{name}")
    print(img.size)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f"resized/{name}")


def main():
    photoNames = os.listdir('photos/')
    photoNum = len(photoNames)
    print(photoNames)
    for i in range(photoNum):
        resize(photoNames[i])


main()
