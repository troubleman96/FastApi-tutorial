from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from random import randrange
from sqlalchemy.orm import Session
import time
from .database import engine, get_db
from fastapi import Depends
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
from app import models, schemas



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


@app.get("/posts", tags=["Posts"], response_model=list[schemas.Post]) #since they can back many, list will handle
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts



@app.post("/posts", status_code=status.HTTP_201_CREATED, tags=["Posts"], response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
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
      return new_post    
    

@app.get("/posts/{id}", tags = ["Posts"], response_model = schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):  
    #cur.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    #post = cur.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
   
    return post 


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
    

@app.put("/posts/{id}", tags = ["Posts"], response_model = schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
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

    return post_query.first()


@app.post("/users", tags=["Users"], status_code=status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user