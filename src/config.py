from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PRODUCTION_URL: str = ""
    LOCAL_URL: str = ""
    RATE_LIMIT: str = "10/minute"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

settings = Settings()
