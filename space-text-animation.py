# Text animation where a space goes through the string

import time as t


def spaceAnim(phrase):
    # Runs in time O(n)
    phrase += ' '  # Need an extra iteration to not print the last letter twice
    L = len(phrase)
    c = 0
    while(c < 2):  # Do animation 2 times
        for i in range(L):
            if(i == L-1 or phrase[i] != ' '):
                beg = phrase[:i]
                end = phrase[i:]
                print(beg + ' ' + end, end='\r')
                t.sleep(0.1)
        c += 1


spaceAnim("Some sample sentence")
