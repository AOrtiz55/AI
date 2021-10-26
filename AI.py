
import pyttsx3
import math
import pyaudio

import datetime
import os
import time
import playsound
import speech_recognition as sr
from  gtts import gTTS
from google.cloud import texttospeech
import subprocess
engine = pyttsx3.init()
#engine.say(text)
#engine.runAndWait()
#engine.say("Hello anakaren, My name is holo. My creator aaron made me for single people who will die alone")
#engine.runAndWait()
converter = pyttsx3.init()
 #tts = gTTS(text=text, lang="en")
    #filename= "voice.mp3"
    #tts.save(filename)
    #playsound.playsound(filename)

#rate
rate = engine.getProperty('rate') #getting details of current speaking rate
#print (rate) #printing current voice rate
engine.setProperty('rate', 192) #setting up new voice rate

#volume
#volume= engine.getProperty('volume')
#print ('volume')
##engine.setProperty('volume', 1.0)

#voice
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)

#voice change?
converter.setProperty('rate', 192) 

# Set volume 0-1 
converter.setProperty('volume', 0.7) 

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
rate = engine.getProperty('rate') #getting details of current speaking rate
#print (rate) #printing current voice rate
engine.setProperty('rate', 192) #setting up new voice rate


def get_audio():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said= ""
 
        try: 
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said      
    
#speak("Hello, how can i help you aaron")



text = get_audio()
if "hello" in text:
    speak(" Hi Aaron, How can I help you?")

if "Halo" in text:
    speak("what can i do for you Aaron?")
#converter.runAndWait()


def note(text):
    
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "=note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
    
NOTE_STRS = ["write this down"]
for phrase in NOTE_STRS:
    if phrase in text:
        speak("what would you like me to write down Sir")
        note_text = get_audio()
        speak("you have told me to write down" + note_text)
        note(note_text)
        speak("I have noted that for you.")
        speak("is there anything else i can assist you with?")

converter.runAndWait()


    


#engine.say("hi wife")
#engine.say('my current speaking rate is' + str(rate))
#engine.runAndWait()
#engine.stop