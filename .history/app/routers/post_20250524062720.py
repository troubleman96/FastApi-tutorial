from typing import List
from .. import models, schemas
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix = "/posts"
)


@router.get("/", tags=["Posts"], response_model=List[schemas.Post]) #since they can back many, list will handle
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts



@router.post("/posts", status_code=status.HTTP_201_CREATED, tags=["Posts"], response_model=schemas.Post)
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
    

@router.get("/posts/{id}", tags = ["Posts"], response_model = schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):  
    #cur.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    #post = cur.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
   
    return post 


@router.delete("/posts/{id}", tags = ["Posts"])
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
    

@router.put("/posts/{id}", tags = ["Posts"], response_model = schemas.Post)
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