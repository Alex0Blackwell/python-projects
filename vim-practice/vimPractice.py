# Vim movement practice

import time as t
import random as r


def keytest(key, direc):
    # Give down, up, left, right and the function will check if it matched and
    # how long it took
    res = False
    t0 = t.time()
    usrIn = input(direc)
    t1 = t.time()
    tTotal = t1 - t0

    if(usrIn == key):
        res = True
    return (res, tTotal)


def main():
    direcLst = [('k', 'up: '), ('j', 'down: '), ('h', 'left: '),
                ('l', 'right: ')]
    totalTimes = []

    print("Up: k, Down: j, Left: h, Right: l")
    correct = (True, '', 0)
    c = 0
    while(correct[0]):
        choseDir = r.choice(direcLst)
        correct = keytest(choseDir[0], choseDir[1])
        totalTimes += [correct[1]]  # Get the amount of time on key took
        c += 1

    avgT = 0
    for el in totalTimes:
        avgT += el
    avgT /= len(totalTimes)
    print("You had a streak of", c)
    print("And an average speed of", round(avgT, 2), "seconds.")


main()
