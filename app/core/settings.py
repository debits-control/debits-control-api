from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///./sql_app.db'

    # auth
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    SECRET_KEY: str = 'a622568486010900860c3ecda40f3ded0f2a092840482cb41d735027ecd8695a'


settings = Settings()
