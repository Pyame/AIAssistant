import angel.command as ac
from gtts import gTTS
import playsound

class Angel():
    
    def __init__(self, name, lang = 'en', accent = 'com.au', slow = False) -> None:
        self.name = name
        self.lang = lang
        self.accent = accent
        self.slow = slow
    
    # Angel can listen to commands
    def listen(self, query):
        if self.name in query:
            query.split(' ', 1)[1]
            self.speak(text= "Hello, I'm here to help!")
            self.use_command(query)
    
    
    #Speaking function
    def speak(self, text):
        speech = gTTS(text = text, lang= self.lang, slow= self.slow, tld= self.accent)
        speech.save("speech.mp3")
        playsound.playsound("speech.mp3")
        
    
    # Deciding witch command User want Angel to do
    def use_command(self, query, com=""):
        if "GPT" in query:
            query.split(' ', 1)[1]
            ac.use_chat_gpt(query)
            

    