from google import genai

config = genai.Client(api_key='AIzaSyCR6Q7XY_HLq57xFBO2RlCSEVrbSuSIKVY')

context=""
while True:
    question = input("Enter your question: ")
    context+=question

    if question == 'Exit' or question=='exit'  :
        break

    response=config.models.generate_content(
        model='gemini-3.5-flash',
        contents=context
    )
    print(response.text)
