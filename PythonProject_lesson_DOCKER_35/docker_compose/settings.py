from pydantic_settings import BaseSettings, SettingsConfigDict
#SettingsConfigDict reads from .env

class Settings(BaseSettings):
    start_range: int = 0
    end_range: int = 10

# secret info
    password : str = ""
    login : str = ""

    # read from .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
