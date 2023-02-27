import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    # base
    ENV: str = os.getenv('ENV', 'dev')

    # auth
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')

    # database
    DB: str = os.getenv('DB', 'postgresql')
    DB_USER: str = os.getenv('POSTGRES_USER')
    DB_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    DB_HOST: str = os.getenv('POSTGRES_HOST')
    DB_PORT: str = os.getenv('POSTGRES_PORT')
    DB_DATABASE: str = os.getenv('POSTGRES_DB', 'dev-debit-control')

    DATABASE_URL: str = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    )


settings = Settings()
