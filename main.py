import speech_recognition as sr
from gtts import gTTS
import playsound
import openai

# speech engin configuration
lang = 'en'
accent = "com.au"
slow = False 

# Set activation word
activationWord = "Alex" # It should be one word


# speech Regonition process
recognizer = sr.Recognizer()

# OpenAI configuration
try: 
    file = open('api_key.txt', 'r')
    openAI_api_key = file.read()
    file.close()
    openai.api_key = openAI_api_key
except:
    print("No key file or wrong directory!")
    

# Define speak function
def speak(text, rate = 120):
    speech = gTTS(text = text, lang= lang, slow= slow, tld= accent)
    speech.save("speech.mp3")
    playsound.playsound("speech.mp3")

with sr.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

    
try:
    query = recognizer.recognize_whisper(audio, language= "english")
    print("You said: " + query)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': "user", "content": query}]
        )
    response = response.choices[0].message.content
    speak(response)
    print(response)
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Whisper")
    