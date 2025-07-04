from datetime import datetime
from pydantic import BaseModel, EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
    pass

class Post(PostBase):
   created_at: datetime
   id: int

   class Config:
        orm_mode = True
        # This allows us to convert SQLAlchemy models to Pydantic models

class UserCreate(BaseModel):
    email: EmailStr
    password: str     

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str     

class Token(Basemodel):
            
