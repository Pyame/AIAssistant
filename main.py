import speech_recognition as sr
from angel.angel import Angel

# speech engin configuration
angel = Angel(name= "Angel")


# speech Regonition process
recognizer = sr.Recognizer()

# OpenAI configuration
# 

if __name__ == "__main__":
    while True:
        with sr.Microphone(device_index= 0) as source:
            print("Say something!")
            audio = recognizer.listen(source)

            
        try:
            query = recognizer.recognize_whisper(audio, language= "english")
            print("You said: " + query)
            if angel.name in query:
                angel.speak(text= "Hello, I'm here to help!")
                angel.use_command(query)
                # print(angel.possibilities)
                # while
            
        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Whisper")
        