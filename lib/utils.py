from pydantic_settings import BaseSettings

class BotConfig(BaseSettings):
    bot_token: str

    class Config:
        env_prefix = 'TG_'
