from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import sqlite3
import time
   
app = FastAPI()

class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    
try:
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    print("Database Connection was sucessful")
    #break
except Exception as error:
    print("Connection to DB failed")
    print("Error: ", error)
    time.sleep(2)    


@app.get("/")
def root():
    return {"message": "Wagwaan"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/createposts", status_code=status.HTTP_201_CREATED)
def     
    
    


