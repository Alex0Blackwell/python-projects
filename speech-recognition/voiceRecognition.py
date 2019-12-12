# Voice recognition project

import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import wavio


fs = 44100  # Set the sample rate
duration = 5  # Time in seconds
r = sr.Recognizer()  # Make an instance of Recognizer

print("...and start talking:")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until the recording is finished
print("...and stop.")
# Save a file of what the mic captured (note, will overwrite last 'input.wav')
wavio.write('input.wav', myrecording, fs, sampwidth=2)

micInput = sr.AudioFile('input.wav')

with micInput as source:
    # Get the data from the file (not parsing any words yet)
    r.adjust_for_ambient_noise(source)  # Uses first second
    audio = r.record(source)

words = r.recognize_google(audio)
print(words)
