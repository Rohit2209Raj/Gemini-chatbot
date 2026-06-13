from fastapi import FastAPI,HTTPException
from chat import chatting
from dotenv import load_dotenv
import os


app=FastAPI()
load_dotenv()


@app.get('/')
def homepage():
    return {'message':'Welcome to my AI Gemini Chatbot'}


@app.post('/chat')
def chat_with_gemini(api_key:str,question:str)->str:
    # if api_key != os.getenv('API_KEY'):
    #     raise HTTPException(
    #         status_code=401,
    #         detail='Invalid api_key'
    #     )

    answer = chatting(question)
    return (answer)


