import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///./sql_app.db'

    # auth
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')

    class Config:
        env_file = '.env'


settings = Settings()
