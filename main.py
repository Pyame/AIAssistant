import speech_recognition as sr


recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    query = recognizer.listen(source)
    
try:
    print("You said: " + recognizer.recognize_whisper(query, language= "polish"))
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Whisper")
    