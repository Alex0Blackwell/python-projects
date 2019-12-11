# Voice recognition project

import speech_recognition as sr

r = sr.Recognizer()  # Make on instance of Recognizer
harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    # Get the data from the file (not parsing any words yet)
    audio = r.record(source)


words = r.recognize_google(audio)
print(words)
