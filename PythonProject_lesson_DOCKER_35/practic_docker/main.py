import time
import pydantic
import sys
import datetime

start_time = datetime.datetime.now()

while True:
    time.sleep(2)
    print(f"Version {sys.version}")
    print(f"Pydantic version: {pydantic.__version__}")
    print(f"Program started: {start_time}")
    print("Hello")
