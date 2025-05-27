from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from typing import Annotated


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True    

class PostCreate(PostBase):
    pass

class Post(PostBase):
   created_at: datetime
   id: int
   owner_id: int
   owner: UserOut

   class Config:
        orm_mode = True
        # This allows us to convert SQLAlchemy models to Pydantic models

class PostOut(BaseModel):
    Post: Post
    votes: int        

class UserCreate(BaseModel):
    email: EmailStr
    password: str     



class UserLogin(BaseModel):
    email: EmailStr
    password: str     

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None            

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, conint(le=1)]