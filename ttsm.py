import pyttsx3
import nltk


def speak(message):
    
    tts = pyttsx3.init()
    tts.setProperty('rate', 147)     
    tts.say(message)
    tts.runAndWait()