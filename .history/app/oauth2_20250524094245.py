from jose import JWTError, jwt
from datetime import datetime, timedelta


#SECRECTKEY #Algorithm #expirationTime

SECRET_KEY = "09U26Y8D289QWJCXJZJCKKMCZNXHYDI9W872382JWDNSACZXCXZNDNCHDBSCZNXC"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

def create_access_token(data: dict):
    to_encode = data.copy() ## so as to not manipulate the data payload

    expire = datetime.noew + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    