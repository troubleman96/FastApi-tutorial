from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    title: str
    content: str
    published: bool
    created_at: datetime

    class Config:
        orm_mode = True
        # This allows us to convert SQLAlchemy models to Pydantic models