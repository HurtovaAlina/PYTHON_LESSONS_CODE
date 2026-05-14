from settings import settings
import time
import random

while True:
    time.sleep(settings.delay)

    print(f"{settings.symbol * random.randint(settings.min_len, settings.max_len)}")
