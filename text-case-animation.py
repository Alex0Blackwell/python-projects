# Console Text Animation
# This animation looks like the metasploit framework animation for booting

import time as t


def textAnim(sentence, cycles):
    # Give a sentence and how many times to repeat the animation
    c = 0  # Initialize a counter
    while(c < cycles):  # Will go as many times as defined in the given argument
        for i in range(len(sentence)):
            begStr = sentence[:i]
            endStr = sentence[i+1:]
            print(begStr + sentence[i].upper() + endStr, end='\r')
            t.sleep(0.1)
        c += 1
    print(sentence)  # To make sure--if everything goes wrong--that the content is still printed


textAnim("some sample text to animate", 2)
