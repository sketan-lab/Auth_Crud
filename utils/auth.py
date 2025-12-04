from datetime import datetime,timedelta
from jose import JWTError,jwt
# from typing import dict
import os
# from dotenv import load_dotenv

# load_dotenv



def Create_Access_Token(data:dict):
    to_encode=data.copy()
    expire=datetime.now() + timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRES_MINUTES')))
    to_encode.update({"exp":expire})

    return jwt.encode(to_encode,os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))

