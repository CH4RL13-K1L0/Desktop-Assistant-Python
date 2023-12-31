from gpt4all import GPT4All
import logging
import llamacpp
import os
import time
import playsound
from gtts import gTTS
import wikipedia
import uuid 

model = GPT4All(r"FILEPATH HERE") <------- ENTER MODEL FILEPATH

logging.basicConfig(level=logging.WARNING)

os.system('cls' if os.name == 'nt' else 'clear')

def assistant():
    print("Desktop Assistant")
    
    while True:
        try:
         
         print("Assistant: How can I help?")
         user_input = input("You: ").strip()
         user_command = user_input
         print('\n')
         
         try:
             if "tell me about" in user_input.lower():
                parts = user_input.lower().split("tell me about", 1)
                wikipedia_query = parts[1].strip()
            
                result = wikipedia.summary(wikipedia_query)
                print("Assistant: ", result)
                
                break
                
         except Exception as e:
                print(f"An error occurred: {e}")
                break
                
         if user_input.lower() in ["exit", "quit", "bye", "stop"]:
                         print("Assistant: Goodbye!")
                         exit()
 
         output = model.generate(user_command, max_tokens= SPECIFY) <------ SPECIFY MAX TOKENS FOR USE

         print("Assistant:", output)
         print('\n')

        except Exception as e:
            print(f"An error occurred: {e}")
            
if __name__ == "__main__":
    while True:
        print('\n')
        assistant()
          
         
   

