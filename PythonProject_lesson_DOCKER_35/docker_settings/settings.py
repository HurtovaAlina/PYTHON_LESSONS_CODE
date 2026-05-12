from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
# використовуються сеттінги для програми, паролі і сікрети, які не мають бачити на гіті і в git ignor .env зберігаються змінні середовища

class Settings(BaseSettings):

    secret_text: str = "hello"
    password: str | None = None

    min_num: int =10
    max_num: int = 100

# читання налаштувань з  .env

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        )

# створити обʼєкт классу

settings = Settings()

print(settings.password)
print(settings.secret_text)
