from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    tg_token: str
    tg_ids: str
    ai_token: str
    ai_base_url: str
    postgres_url: str


settings = Settings()
