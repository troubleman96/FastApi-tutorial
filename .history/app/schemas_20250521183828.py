import datetime
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
   created_at: datetime.datetime

   class Config:
        orm_mode = True
        # This allows us to convert SQLAlchemy models to Pydantic models