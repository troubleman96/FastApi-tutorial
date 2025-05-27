from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    


settings = Settings()    
