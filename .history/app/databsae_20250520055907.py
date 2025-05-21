from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declaratuive_base 
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:darkknight@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)