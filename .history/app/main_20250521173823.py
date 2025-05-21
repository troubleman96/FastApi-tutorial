from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from sqlalchemy.orm import Session
import time
from .database import engine, get_db
from fastapi import Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from app import models

   
models.Base.metadata.create_all(bind=engine)  

app = FastAPI()

   

class Post(BaseModel):
    title: str
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
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}



@app.post("/posts", status_code=status.HTTP_201_CREATED, tags=["Posts"])
def create_posts(post: Post, db: Session = Depends(get_db)):
#     cur.execute(
#     "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
#     (post.tittle, post.content, post.published)
# )
#     new_post = cur.fetchone()
#     conn.commit() 

#**post.dict() - used to replace the values from models

      new_post = models.Post(**post.dict())  
      db.add(new_post)
      db.commit()
      db.refresh(new_post)
      return {"data": new_post}    
    

@app.get("/posts/{id}", tags = ["Posts"])
def get_post(id: int, db: Session = Depends(get_db)):  
    #cur.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    #post = cur.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
   
    return {"post_detail": post}  


@app.delete("/posts/{id}", tags = ["Posts"])
def delete_post(id: int, db: Session = Depends(get_db)):
    #cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    #deleted_post = cur.fetchone()
    #conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}", tags = ["Posts"])
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):
    #cur.execute("UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *",
                #(post.tittle, post.content, post.published, str(id)))
    #updated_post = cur.fetchone()
    #conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id: {id} does not exist")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return {"data": post_query.first()}
