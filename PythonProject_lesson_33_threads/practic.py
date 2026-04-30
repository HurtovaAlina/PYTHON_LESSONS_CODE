# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import threading
import time
from typing import List

numbers = []
count = int(input("Enter count of numbers: "))
for _ in range(count):
    number = int(input("Enter number: "))
    numbers.append(number)

def find_max(numbers: list[int], res:dict[str, int]):
    res["max"] = max(numbers)

def find_min(numbers: list[int], res:dict[str, int]):
    res["min"] = min(numbers)


res: dict[str, int] = {}

thread_max = threading.Thread(
    target = find_max,
    args = (numbers, res),
)

thread_min = threading.Thread(
    target = find_min,
    args = (numbers, res),
)

thread_max.start()
thread_max.join()
print(f"Result = {res}")

thread_min.start()
thread_min.join()
print(f"Result = {res}")

# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

numbers = list(map(int,input("Enter numbers via ',' ").split(",")))
print(numbers)

def sum_of_numbers(numbers, res:dict[str, int]):
    time.sleep(1)
    res["sum"] = sum(numbers)

def average(numbers, res:dict[str, int]):
    time.sleep(2)
    res["average"] = sum(numbers)/len(numbers)

res: dict[str, int] = {}

thread_sum = threading.Thread(
    target = sum_of_numbers,
    args = (numbers, res),
)

thread_avg = threading.Thread(
    target = average,
    args = (numbers, res),
)

thread_sum.start()
thread_sum.join()
print(f"Result = {res}")

thread_avg.start()
thread_avg.join()
print(f"Result = {res}")


# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.


# /Users/ahurt/Documents/DOCUMENTS/AI COURSE/PHYTON_LESSONS_CODE/PythonProject_lesson_33_threads/numbers.txt
path_to_file = input("Enter path ")

with open(path_to_file, "r") as file:
    numbers = list(map(int, file.read().split(",")))

def new_file_with_evens(numbers:List[int], res:dict[str, int]):
    evens = list(filter(lambda n: n % 2 == 0, numbers))
    res["evens"] = len(evens)
    evens = str(evens)

    with open("evens.txt", "w") as file:
        file.write(evens)


def new_file_with_odds(numbers:List[int], res:dict[str, int]):
    odds = list(filter(lambda n: n % 2 != 0, numbers))
    res["odds"] = len(odds)
    odds = str(odds)

    with open("odds.txt", "w") as file:
        file.write(odds)


res: dict[str, int] = {}

thread_evens = threading.Thread(
    target = new_file_with_evens,
    args = (numbers, res),
)

thread_odds = threading.Thread(
    target = new_file_with_odds,
    args = (numbers, res),
)

thread_evens.start()
thread_evens.join()
print(f"Result = {res}")

thread_odds.start()
thread_odds.join()
print(f"Result = {res}")
