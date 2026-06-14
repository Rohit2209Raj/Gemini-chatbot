from fastapi import FastAPI,HTTPException
from chat import chatting
from dotenv import load_dotenv
from verify import check_api_key
from fastapi.responses import RedirectResponse
import os


app=FastAPI()
load_dotenv()

logged_in=False

@app.get('/')
def homepage():
    return {'message':'Welcome to my AI Gemini Chatbot'}

@app.post('http://127.0.0.1:8000/login')
def check_client(api_key:str):
    global logged_in
    if check_api_key(api_key) == True:
        logged_in=True
        # RedirectResponse(
        #     url="/chat",
        #     status_code=200
        # )
        return {'message':'Login successful'}
    else:
        raise HTTPException(
            status_code=401,
            detail='Invalid API_KEY'
        )
        


@app.post('/chat')
def chat_with_gemini(question:str)->str:
    if not logged_in:
        raise HTTPException(
            status_code=403,
            detail="Login required"
        )
    else:
        answer = chatting(question)
        return (answer)


