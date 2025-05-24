from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from random import randrange
from sqlalchemy.orm import Session
import time
from .database import engine, get_db
from fastapi import Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from app import models, schemas, utilis


models.Base.metadata.create_all(bind=engine)  

app = FastAPI()

   
    
# try:
#     conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="darkknight", cursor_factory=RealDictCursor)
#     cur = conn.cursor()
#     print("Database Connection was sucessful")
#     #break
# except Exception as error:
#     print("Connection to DB failed")
#     print("Error: ", error)
#     time.sleep(2)    


@app.get("/")
def root():
    return {"message": "Wagwaan"}





 