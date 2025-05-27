from pydantic import BaseSettings

class Settings(BaseSettings):
    path: int
    database_username: str = "postgres"
    se
