from pydantic import BaseSettings

class Settings(BaseSettings):
    path: int
    
