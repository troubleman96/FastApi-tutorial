from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import sqlite3
import time
import psycopg2
   
app = FastAPI()

class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    
try:
    conn = psycopg2.connect("postgresql+psycopg2://postgres:darkknight@localhost/posts")
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
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}    
    
    


