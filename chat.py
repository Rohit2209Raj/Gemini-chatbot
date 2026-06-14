from google import genai
from dotenv import load_dotenv

import os
load_dotenv()
config = genai.Client(api_key=os.getenv("API_KEY"))
print(os.getenv("API_KEY"))

def chatting(default_question:str)->str:
    response=config.models.generate_content(
        model='gemini-2.5-flash',
        contents=default_question
        )
    return response
