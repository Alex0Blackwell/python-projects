# Heads up but worse and on the computer

import time as t
import random as r


def main():
    prompts = ['pants', 'kitten', 'ants']

    maxTime = 15
    t0 = t.time()
    timeTot = 0

    correct = 0
    while(timeTot < maxTime):
        # loop this until 15 secs
        prompt = r.choice(prompts)
        print("Your word:", prompt)
        usrAns = input("Enter if correct, \"p + enter\" to pass\n")
        timeTot = t.time() - t0  # Time final - initial

        if(timeTot > maxTime):
            print(f"Sorry, you didn't guess \"{prompt}\" in time, you were",
                  f"{round(timeTot-maxTime, 2)} seconds too late.")
        elif(usrAns == ''):
            correct += 1

    print(f"Finish! you got a final score of {correct} right answers in",
          f"{maxTime} seconds.")


main()
