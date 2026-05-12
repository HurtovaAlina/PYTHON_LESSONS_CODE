import time

from settings import settings
#settings = Settings() - variable

# раз в секунду вивести налаштування

while True:
    time.sleep(1)

    print(settings.secret_text)
    print(settings.password)
    print(settings.min_num)
    print(settings.max_num)
