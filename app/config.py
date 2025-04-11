from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # Explicitly load the .env file


class Settings(BaseSettings):
    POSTGRES_HOSTNAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_PORT: int
    API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
