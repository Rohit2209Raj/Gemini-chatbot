from fastapi import FastAPI,HTTPException
from chat import chatting

app=FastAPI()

@app.get('/')
def homepage():
    return {'message':'Welcome to my AI Gemini Chatbot'}


@app.post('/api_key')
def chat_with_gemini(question:str)->str:
    # if api_key != 'AIzaSyCR6Q7XY_HLq57xFBO2RlCSEVrbSuSIKVY':
    #     raise HTTPException(
    #         status_code=200,
    #         detail='Invalid api_key'
    #     )

    answer = chatting(question)
    print(answer)
    return (answer)


