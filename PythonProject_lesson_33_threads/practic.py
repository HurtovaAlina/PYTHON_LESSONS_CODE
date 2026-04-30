# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import threading

numbers = []
count = int(input("Enter count of numbers: "))
for _ in range(count):
    number = int(input("Enter number: "))
    numbers.append(number)

def find_max(numbers: list[int], res_max:dict[str, int]):
    res_max["max"] = max(numbers)

def find_min(numbers: list[int], res_min:dict[str, int]):
    res_min["min"] = min(numbers)


res_max: dict[str, int] = {}
res_min: dict[str, int] = {}

thread_max = threading.Thread(
    target = find_max,
    args = (numbers, res_max),
)

thread_min = threading.Thread(
    target = find_min,
    args = (numbers, res_min),
)

thread_max.start()
thread_max.join()
print(f"Max = {res_max}")

thread_min.start()
thread_min.join()
print(f"Min = {res_min}")

# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

numbers = list(map(int,input("Enter numbers via ',' ").split(",")))
print(numbers)

def sum_of_numbers(numbers, res):
    res
