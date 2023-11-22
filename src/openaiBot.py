from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime, timedelta


#Loads OPENAI_API_KEY to env
load_dotenv()

class OpenAIBot:
    client = OpenAI()
    messages = []

    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def add_system_message(self, messageText):
        self.messages.append({"role": "system", "content": messageText})

    def add_user_message(self, messageText):
        self.messages.append({"role": "user", "content": messageText})

    def add_assistant_message(self, messageText):
        self.messages.append({"role": "assistant", "content": messageText})

    def get_response(self):
        response = self.client.chat.completions.create(
            model=self.model, #gpt-4 or gpt-3.5-turbo
            messages=self.messages, timeout=10)
        
        responseText = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": responseText})
        print(self.messages)
        return responseText
    
    
    def reset_messages(self):
        self.messages = []



# if __name__ == "__main__":
#     bot = OpenAIBot()
#     bot.add_user_message("Hello, how are you?")
#     response = bot.get_response()
#     print(response)