from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import sqlite3
import time
import psycopg2
from psycopg2.extras import RealDictCursor

   
app = FastAPI()

class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    
try:
    conn = psycopg2.connect(host="localhost", database="posts", user="postgres", password="darkknight", cursor_factory=RealDictCursor)
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


@app.get("/posts" tags=["Posts"])
def get_posts():
    posts = cur.execute
    return {"data": my_posts}


@app.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}    
    
    


