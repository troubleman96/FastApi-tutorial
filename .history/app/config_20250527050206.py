from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    


settings = Settings()    
