from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    tg_token: str
    tg_ids: str
    ai_token: str
    ai_base_url: str
    pg_url: str
    pg_user: str
    pg_password: str
    pg_db_name: str

    class Config:
        env_file = ".env"


settings = Settings()
