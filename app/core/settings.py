from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///./sql_app.db'


settings = Settings()
