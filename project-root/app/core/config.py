# config.py: Configuration settings for the application. This file contains the Settings class, which is used to define the configuration settings for the application. The settings are loaded from environment variables using the pydantic_settings library. The describe_fields method is used to provide a description of the configuration settings.
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings class for application configuration.

    System OS Secrets:
    - EXA_API_KEY: API key for Exa service
    - OPENAI_API_KEY: API key for OpenAI service
    """
    exa_api_key: str = os.getenv("EXA_API_KEY", "Please_set_EXA_API_KEY_system_OS_secret")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "Please_set_OPENAI_API_KEY_system_OS_secret")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

    @staticmethod
    def describe_fields():
        return {
            'exa_api_key': 'API key for Exa service retrieved from system OS secrets',
            'openai_api_key': 'API key for OpenAI service retrieved from system OS secrets'
        }

settings = Settings()