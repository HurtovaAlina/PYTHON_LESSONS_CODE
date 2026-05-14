from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
# ip address
    host: str = "0.0.0.0"
#port
    port: int = 8080

    text: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
