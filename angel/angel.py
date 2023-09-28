from angel.command import Command
from gtts import gTTS
import playsound

class Angel():
    
    def __init__(self, name, lang = 'en', accent = 'com.au', slow = False) -> None:
        self.name = name
        self.lang = lang
        self.accent = accent
        self.slow = slow
        pass
    
    #Speaking function

    def speak(self, text):
        speech = gTTS(text = text, lang= self.lang, slow= self.slow, tld= self.accent)
        speech.save("speech.mp3")
        playsound.playsound("speech.mp3")
        print(text)
        
    def use_command(self, text, com=""):
        
        if "GPT" in text:
            Command.use_chat_gpt()