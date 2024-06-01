from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings class for application configuration.

    Environment Variables:
    - EXA_API_KEY: API key for Exa service
    - OPENAI_API_KEY: API key for OpenAI service
    """
    exa_api_key: str = "Please_set_EXA_API_KEY_environment_variable"
    openai_api_key: str = "Please_set_OPENAI_API_KEY_environment_variable"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

    @staticmethod
    def describe_fields():
        return {
            'exa_api_key': 'API key for Exa service',
            'openai_api_key': 'API key for OpenAI service'
        }

settings = Settings()
