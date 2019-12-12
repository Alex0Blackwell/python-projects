# Voice recognition project

import sounddevice as sd
from scipy.io.wavfile import write
# import speech_recognition as sr


audioArray = []
fs = 44100  # Because of the sample rate
# r = sr.Recognizer()  # Make on instance of Recognizer
# harvard = sr.AudioFile('harvard.wav')

# with harvard as source:
#     # Get the data from the file (not parsing any words yet)
#     audio = r.record(source)

myrecording = sd.rec(int(5 * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until the recording is finished
# print(myrecording)
write('input.wav', fs, myrecording)
# words = r.recognize_google(audio)
# print(words)
