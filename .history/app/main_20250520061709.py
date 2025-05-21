from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import time
import psycopg2
from psycopg2.extras import RealDictCursor

   
models.Base.  

app = FastAPI()

class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    
try:
    conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="darkknight", cursor_factory=RealDictCursor)
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


@app.get("/posts", tags=["Posts"])
def get_posts():
    cur.execute("""SELECT * FROM posts""")
    posts = cur.fetchall()
    return {"data": posts}



@app.post("/posts", status_code=status.HTTP_201_CREATED, tags=["Posts"])
def create_posts(post: Post):
    cur.execute(
    "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
    (post.tittle, post.content, post.published)
)
    new_post = cur.fetchone()
    conn.commit() 
    return {"data": new_post}    
    

@app.get("/posts/{id}", tags = ["Posts"])
def get_post(id: int):  
    cur.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    post = cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return {"post_detail": post}  


@app.delete("/posts/{id}", tags = ["Posts"])
def delete_post(id: int):
    cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cur.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}", tags = ["Posts"])
def update_post(id: int, post: Post):
    cur.execute("UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *",
                (post.tittle, post.content, post.published, str(id)))
    updated_post = cur.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id: {id} does not exist")
    return {"data": updated_post}
