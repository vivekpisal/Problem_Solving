import os
import time
import playsound
import speech_recognition as speech_recognition 
from gtts import gTTS 

def speak(text):
	tts=gTTS(text=text,lang="en")
	filename="voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)


speak("hello vivek")