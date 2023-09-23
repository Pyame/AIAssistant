import speech_recognition as sr
import pyttsx3


# Speach engine init
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[12].id) # 12 - is for male english


# Set activation word
activationWord = "Alex" # It should be one word


# Speach Regonition process
recognizer = sr.Recognizer()


# Define speak function
def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


with sr.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

    
try:
    query = recognizer.recognize_whisper(audio, language= "english")
    print("You said: " + query)
    speak(query)
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Whisper")
    