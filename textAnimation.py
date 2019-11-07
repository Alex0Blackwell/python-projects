# Console Text Animation
import time as t


def textAnim(sentence):

    c = 0
    while(c < 3):
        for i in range(len(sentence)):
            begStr = sentence[:i]
            endStr = sentence[i+1:]

            print(begStr + sentence[i].upper() + endStr, end='\r')
            t.sleep(0.1)
        c += 1
    print(sentence)


textAnim("some sample text to animate")
