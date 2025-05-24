from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #default hashing algorithm , the algorith used

hashed_password = pwd_context.hash(user.password)
user.password = hashed_password