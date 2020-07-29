import playsound
from gtts import gTTS 
import os


def speak(text):
	tts=gTTS(text=text,lang='en')
	filename='voice.mp3'
	tts.save()
	playsound.playsound(filename)

speak("hello vivek")