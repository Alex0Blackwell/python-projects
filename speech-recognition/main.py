# Voice recognition project

import sounddevice as sd
import speech_recognition as sr
import wavio


fs = 44100  # Set the sample rate
r = sr.Recognizer()  # Make an instance of Recognizer

myrecording = sd.rec(int(5 * fs), samplerate=fs, channels=2)  # Record from mic
# Save a file of what the mic captured, this will overwrite the previous file
# called 'input.wav'
wavio.write('input.wav', myrecording, fs, sampwidth=2)

micInput = sr.AudioFile('input.wav')
with micInput as source:
    # Get the data from the file (not parsing any words yet)
    audio = r.record(source)

words = r.recognize_google(audio)
print(words)
