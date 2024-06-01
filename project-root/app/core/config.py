from pydantic import BaseSettings

class Settings(BaseSettings):
    exa_api_key: str
    openai_api_key: str

settings = Settings()
