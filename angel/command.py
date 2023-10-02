import openai
import angel.chatter as chatter
import speech_recognition as sr


recognizer = sr.Recognizer()
          
# Create command that angel should listen to        
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
        
# calling chatGPT        
def use_chat_gpt(query):
    chat = chatter.Chatter()
    chat.call_chat(query)
