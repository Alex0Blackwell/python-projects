# image resizer

from PIL import Image
import os


def resize(name, width):
    basewidth = width
    img = Image.open(f"photos/{name}")
    origImgS = img.size
    if(img.size[0] > basewidth):
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        print(f"{origImgS} => {basewidth, hsize}")
        img.save(f"resized/{name}")
    else:
        print(f"image \"{name}\" was already small enough.")


def main():
    chosenWidth = eval(input("What would you like the width to be (in px):\n"))
    photoNames = os.listdir('photos/')
    photoNum = len(photoNames)
    print(photoNames)
    for i in range(photoNum):
        print(f"\nResizing \"{photoNames[i]}\"...")
        resize(photoNames[i], chosenWidth)
    print(f"\nDone resizing all {photoNum} photos.")


main()
