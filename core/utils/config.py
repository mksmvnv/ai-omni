from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TG_TOKEN: str
    TG_IDS: str
    AI_TOKEN: str
    AI_BASE_URL: str
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = ".env"


settings = Settings()
