# Voice recognition project
# This is the voice assistant Grimmels
# Extremely powerfull

import time as t
import random as r
import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import wavio  # Like wario but not as WAAAA


def respond(usrInput):
    unknown = ["My creator doesn't know what he's doing. That's probably you isn't it?",
               "My name is GRIMMELS (I don't understand)",
               "I'm a computer program. I don't know how to respond and I have no fear."]
    greeting = ['hi', 'hello', 'hey grimmels', 'how\'s life', 'how are things',
                'what\'s cracking', 'what\'s good', 'how are you', 'what\'s up',
                'what is up', 'how are ya']
    greetingRes = ["Hello. They call me Grimmels.", "Oh hello!", "Oh Hi!"
                   "Hello, my name is Grimmels but you can call me \"The Grim Reaper\"",
                   "Hello! I love meeting new peole! I don't remember any of them..."]

    res = r.choice(unknown)
    for i in range(len(greeting)):
        if(greeting[i] in usrInput.lower()):
            res = r.choice(greetingRes)
            break
    if('grimmels' in usrInput.lower()):
        res += " I Can't believe you know my name! I must be famous!"
    return res


def main():
    fs = 44100  # Set the sample rate
    r = sr.Recognizer()  # Make an instance of Recognizer

    # Set defaults for the microphone input
    sd.default.samplerate = fs
    sd.default.channels = 2

    res = ''
    for a in range(3, 0, -1):
        # Countdown (total time: 1.5 secs)
        res += f"{a} "
        print(f"Press Enter to start recording in {res}", end='\r')
        t.sleep(0.5)
    print()

    initialTime = t.time()
    # Don't accept recording longer than 15 seconds
    myrecording = sd.rec(int(15 * fs))

    # NOTE: I think it might be better to just do the countdown
    input("Press enter to start recording: ")
    offsetTime = t.time() - initialTime
    input("Press enter to stop recording: ")
    finalTime = t.time() - initialTime

    durationTime = finalTime - offsetTime

    if(durationTime > 15):
        print("That was way too long and I don't understand much. Even if",
              "it's short. But jeez that was actually like", durationTime//1,
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
            audio = r.record(source, offset=offsetTime-1, duration=durationTime)
        words = r.recognize_google(audio)
        print("\t\t", words)
        print(respond(words))


main()
