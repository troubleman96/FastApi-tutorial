from jose import JWTError, jwt
from .schemas import TokenData
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import database, schemas, models
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login") #this is the url that will be used to get the token

#SECRECTKEY #Algorithm #expirationTime

SECRET_KEY = "09U26Y8D289QWJCXJZJCKKMCZNXHYDI9W872382JWDNSACZXCXZNDNCHDBSCZNXC"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 

def create_access_token(data: dict):
    to_encode = data.copy() ## so as to not manipulate the data payload

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  ##making sure the token expires

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token:str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = TokenData(id=id)    
    except JWTError:
        raise credentials_exception

    return token_data

# this function will be used to get the current user from the token
def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(database.get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = f"could not validate credentials ", headers = {"WWW-AUTHENTICATE": "bearer"})
    
    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user