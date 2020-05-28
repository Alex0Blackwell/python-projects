import math
import time as t

class Animate():
    # set how many columns the game will use
    def __init__(self, numColumns, speed, repeats):
        self.cols = numColumns
        self.timeDelay = 1 / speed - 0.18
        self.repeats = repeats

    # default look with no '-'
    def gen(self):
        self.arr = ['#'] * (self.cols + 2)
        self.arr[0] = '|'
        self.arr[self.cols+1] = '|'

    # animate given speed, the number of repeats, and the number of columns
    def animate(self):
        for i in range(self.repeats * 2):
            # *2 because we go there and back for one cycle
            if(i % 2 != 0):
                backwards = True
            else:
                backwards = False
            for j in range(self.cols + 2):
                if(backwards):
                    j = self.cols + 1 - j
                if(j == 0):
                    self.arr[j] = '<'
                    self.arr[j+1] = '#'
                elif(j == self.cols+1):
                    self.arr[j] = '>'
                    self.arr[j-1] = '#'
                else:
                    self.arr[j] = '-'
                    self.arr[j-1] = '#'
                    self.arr[j+1] = '#'
                    self.arr[0] = '|'
                    self.arr[self.cols+1] = '|'

                print(''.join(self.arr), end='\r')
                t.sleep(self.timeDelay)
        self.gen()
        print(''.join(self.arr), end='\r')




if __name__ == "__main__":
    userCols = userSpeed = userRepeats = ''
    while(not(userCols.isdigit() and int(userCols) >= 1)):
        userCols = input("How many columns should the animation have?: ")
    while(not(userSpeed.isdigit() and 1 <= int(userSpeed) <= 5)):
        userSpeed = input("What level of speed do you want to try? (1-5, where 5 is the fastest): ")
    while(not(userRepeats.isdigit() and int(userRepeats) >= 1)):
        userRepeats = input("How many repeats?: ")

    anim = Animate(int(userCols), int(userSpeed), int(userRepeats))
    anim.gen()
    anim.animate()
