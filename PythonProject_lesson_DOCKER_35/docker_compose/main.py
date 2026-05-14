import time
import random
from settings import settings

# print random number in a 1 sec

while True:
    time.sleep(1)

    rand_num = random.randint(
        settings.start_range,
        settings.end_range
    )
    print(f"Random number {rand_num}")
    print(f"Password {settings.password}")
    print(f"Login {settings.login}")
