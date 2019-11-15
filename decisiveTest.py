# Decisive test

import time as t


def length(time):
    res = ''
    if(time < 1):
        res = f"{time} seconds is extremely fast."
    elif(time < 3):
        res = f"{time} seconds is pretty fast."
    elif(time < 5):
        res = f"{time} seconds is kind of fast."
    elif(time < 10):
        res = f"{time} seconds is pretty slow."
    else:
        res = f"{time} seconds is really slow."
    return res


def main():
    InvalidInput = True
    while InvalidInput:
        t0 = t.time()
        yORn = input("Are you decisive?\n(y / n)\n(e to exit)\n")
        yOrnClean = yORn.lower()
        t1 = t.time()

        totalTime = round(t1 - t0, 2)

        if(yOrnClean == 'y' or yOrnClean == 'n'):
            message = length(totalTime)
            if(yOrnClean == 'y'):
                if(totalTime < 5):
                    print(f"Maybe, {message}")
                else:
                    print(f"I don't know, {message}")
            else:
                if(totalTime < 5):
                    print(f"I don't know, {message}")
                else:
                    print(f"Maybe, {message}")
            InvalidInput = False

        else:
            if(yOrnClean == 'e'):
                print('Goodbye!')
                InvalidInput = False
            else:
                print("Try inputting Y or N. Idiot.\n")


main()
