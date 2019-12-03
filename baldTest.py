# Test if you are bald, but it turns out we can't actually test for that and
# we just collect data

import time as t


def stall(phrase):
    # Text animation: unecessary but kind of cool
    for x in range(0, 4):
        print(phrase+'.'*x, end='\r')
        t.sleep(.3)
    print(phrase+'.'*x)


def textAnim(sentence):
    c = 0
    while(c < 2):
        for i in range(len(sentence)):
            begStr = sentence[:i]
            endStr = sentence[i+1:]

            print(begStr + sentence[i].upper() + endStr, end='\r')
            t.sleep(0.1)
        c += 1
    print(sentence)


def getInfo(prompt, key):
    # Continuously prompts the user until the user inputs what is specified in
    # the key. If the key is multiple (y or n) input the key as "yn"
    usrIn = ''
    while(usrIn == '' or usrIn not in key):  # '' in any string. Use lazy eval
        usrIn = input(prompt)
    return usrIn


def baldFamily(bald):
    # Returns True if a family member is bald and False otherwise
    res = False
    if(bald == 'y'):
        res = True
    return res


def main():
    name = input("What is your name?:\n")
    stall(f"Oh, hello {name}, today we are going to test for baldness")
    stall("Can you")
    print("Can you hold your head closer to the screen?")
    t.sleep(0.2)
    stall("I can't see")
    stall("You're not doing it are you")

    hered = getInfo("Ok, well. Is anyone in your family bald? (y/n): ", "yn")
    rage = input("Out of ten, how many rage points would you give yourself?:\n")

    textAnim("Calculating")

    print("Ok we have the results.")
    t.sleep(0.5)
    print("there is a 88.55% chance you will go bald")
    t.sleep(3)  # Really stress them out
    print("I'm kidding")
    t.sleep(0.2)
    stall("We actually can't determine if you are going to go bald")

    plural = ''
    if(int(rage) != 1):  # Adds an s if the number is not 0, proper grammar...
        plural = 's'
    stall(f"But remember when you gave yourself {rage} rage point{plural}!")
    print("That was wild.")
    t.sleep(0.7)

    if(baldFamily(hered)):  # Check if there is a bald family member
        print("Also you have a bald family member.")


main()
