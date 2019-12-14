# Voice recognition project
# This is the voice assistant Grimmels
# Extremely powerfull

import time as t
import random as r
import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
from win10toast import ToastNotifier
import wavio  # Like wario but not as WAAAA


def timer(hour, min, sec):
    toaster = ToastNotifier()
    cHour = 0
    while(cHour < hour):
        t.sleep(3600)  # Wait an hour
        cHour += 1
    cMin = 0
    while(cMin < min):
        t.sleep(60)  # Wait a minute
        cMin += 1
    cSec = 0
    while(cSec < sec):
        t.sleep(1)  # Wait a second
        cSec += 1
    # Once all the tjmers run down, display the message
    toaster.show_toast("Timer", f"Your {hour} hour, {min} minute {sec} second timer is up")


def respond(usrInput):
    usrL = usrInput.lower()
    unknown = ["My creator doesn't know what he's doing. That's probably you isn't it?",
               "My name is GRIMMELS (I don't understand)",
               "I'm a computer program. I don't know how to respond and I have no fear."]
    greeting = ['hi', 'hello', 'hey grimmels', 'how\'s life', 'how are things',
                'what\'s cracking', 'what\'s good', 'how are you', 'what\'s up',
                'what is up', 'how are ya']
    greetingRes = ["Hello. They call me Grimmels.", "Oh hello!", "Oh Hi!"
                   "Hello, my name is Grimmels but you can call me \"The Grim Reaper\"",
                   "Hello! I love meeting new people! I don't remember any of them..."]

    res = ''
    for i in range(len(greeting)):
        if(greeting[i] in usrL):
            res = r.choice(greetingRes)
            break

    if('minute' in usrL or 'second' in usrL or 'hour' in usrL):
        # Prepare the timer
        usrLst = []
        hour = 0
        min = 0
        sec = 0
        if('-' in usrL):
            # Sometimes it will be in the format of "22-minutes" ect...
            usrL = usrL.replace('-', ' ')
        usrLst = usrL.split()

        if('hour' in usrL):
            numIndex = usrLst.index('hour') - 1  # Get number before "hour"
            if(usrLst[numIndex] == 'one'):  # 'one' is the only case like this
                # All other numbers show numerical form eg) 22
                hour = 1
            else:
                hour = int(usrLst[numIndex])
        if('minute' in usrL):
            numIndex = usrLst.index('minute') - 1
            if(usrLst[numIndex] == 'one'):
                min = 1
            else:
                min = int(usrLst[numIndex])
        if('second' in usrL):
            numIndex = usrLst.index('second') - 1
            if(usrLst[numIndex] == 'one'):
                sec = 1
            else:
                sec = int(usrLst[numIndex])

        hText = ''
        mText = ''
        sText = ''
        if(hour > 0):
            hText = str(hour) + ' hour'
        if(min > 0):
            mText = str(min) + ' minute'
        if(sec > 0):
            sText = str(sec) + ' second'
        print(f"Ok, setting a {hText} {mText} {sText} timer")

        timer(hour, min, sec)
    elif('grimmels' in usrL):
        res += " I Can't believe you know my name! I must be famous!"
    else:
        res = r.choice(unknown)

    return res


def main():
    fs = 44100  # Set the sample rate
    r = sr.Recognizer()  # Make an instance of Recognizer

    # Set defaults for the microphone input
    sd.default.samplerate = fs
    sd.default.channels = 2

    initialTime = t.time()

    res = ''
    for a in range(3, 0, -1):
        # Countdown (total time: 1.5 secs)
        res += f"{a} "
        print(f"Press Enter to start recording in {res}", end='\r')
        t.sleep(0.5)
    print()

    # Don't accept recording longer than 15 seconds
    myrecording = sd.rec(int(15 * fs))

    input("Press enter to stop recording: ")
    finalTime = t.time() - initialTime

    if(finalTime > 15):
        print("That was way too long and I don't understand much. Even if",
              "it's short. But jeez that was actually like", finalTime//1,
              "seconds. JEEZ!")
    else:
        # Save a file of what the mic captured
        # (note, will overwrite last 'input.wav')
        wavio.write('input.wav', myrecording, fs, sampwidth=2)

        micInput = sr.AudioFile('input.wav')

        with micInput as source:
            # Get the data from the file (not parsing any words yet)
            r.adjust_for_ambient_noise(source)  # Uses first second
            # In the offset time, subtract 1 because it is used for ambient
            # noise adjustment. Note this 1 second will always exist because
            # the countdown
            audio = r.record(source, duration=finalTime)
        words = r.recognize_google(audio)
        print("\t\t", words)
        print(respond(words))


main()
