import openai

class Chatter():
    def __init__(self) -> None:
        try: 
            file = open('./api_key.txt', 'r')
            openAI_api_key = file.read()
            file.close()
            openai.api_key = openAI_api_key
        except:
            print("No key file or wrong directory!")
        
    def call_chat(self, query):
        completion = openai.ChatCompletion.create(model= "gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
        print(completion.choices[0].message.content)