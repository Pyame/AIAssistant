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
        pass