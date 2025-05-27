from pydantic import BaseSettings

class Settings(BaseSettings):
    path: int
    database_username: str = "postgres"
    secret_key: str = ""
    database_password: str = "darkknight"
