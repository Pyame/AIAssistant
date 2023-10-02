import openai
import angel.chatter as chatter
import speech_recognition as sr


recognizer = sr.Recognizer()
  

def use_chat_gpt():
    chat = chatter.Chatter()
        
        
def command():
    with sr.Microphone(device_index= 0) as source:
        print("Say something!")
        audio = recognizer.listen(source)
    
    try:
        query = recognizer.recognize_whisper(audio, language= "english")
        print("You said: " + query)
        return query
    except sr.UnknownValueError:
            print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")