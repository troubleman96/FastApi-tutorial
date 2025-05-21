from .database import Base  

class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)