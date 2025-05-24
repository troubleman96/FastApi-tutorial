from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #default hashing algorithm , the algorith used

def hash(password: str):
    return pwd_context.hash(password)
