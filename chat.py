from google import genai
from dotenv import load_dotenv

import os
load_dotenv()
config = genai.Client(api_key=os.getenv("API_KEY"))

def chatting(default_question:str)->str:
        context=default_question
        question=""
        while True:
            if(default_question == ""):
                question = input("Enter your question: ")
                context+=question

            if question != "" and question.strip().lower() == 'exit'  :
                break
            response=config.models.generate_content(
                model='gemini-2.5-flash',
                contents=context
            )
            default_question=""
            return response.text
