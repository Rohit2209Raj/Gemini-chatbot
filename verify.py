from dotenv import load_dotenv
import os

load_dotenv()

def check_api_key(api_key:str)->bool:
    if api_key != os.getenv("USER_API_KEY"):
        return False
    return True