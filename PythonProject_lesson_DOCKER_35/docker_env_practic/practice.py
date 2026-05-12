import time

from settings import settings
#settings = Settings() - variable

# раз в секунду вивести налаштування

while True:
    time.sleep(1)

    print(f"app_name = {settings.app_name}")
    print(f"filename = {settings.filename}")
    print(f"login = {settings.login}")
    print(f"password = {settings.password}")
