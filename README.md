# AIAssistant
AI computer assistant. 
Let's call it Angel for now (later will think about name).

##  Business requirements 
AI Assistant should have:
 * [x] Speach recognition
 * [x] Text to speach
 * [x] Basic understanding of commands
 * [x] Answering query (speach and text)
 * [ ] Genereating code
 * [ ] Communicate with other programms
 * [ ] Friendly UI (maybe?)
 * [ ] Default commands

## speech recognition

For now Angel can only repeat after speaker and type text according to what he/she said.
Language is configurable.

## Text to speech
Angel can read text and change text to speech. 
### To do
It should be able to talk in many languages, now it's only english.
### To fix
**It can only use male voice!!!**

## Understanding and Speech
In order to speak it has google tts engine applied. Additionally it can understand commands and do conversation thanks to connection with openAI chatGPT. 

# Ideas for future
> Create database to let Angel remember every conversation. DB will also contain basic informations (Ur Name, its Name etc.) for Angel.

> Create default commands, something that will not necessary use openAI chatGPT API. 

> Create new NN for Chat that will learn through process of creation.
