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
print(f"Max = {res}")

thread_min.start()
thread_min.join()
print(f"Min = {res}")

# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

# numbers = list(map(int,input("Enter numbers via ',' ").split(",")))
# print(numbers)
#
# def sum_of_numbers(numbers, res_sum:dict[str, int]):
#     res_sum["sum"] = sum(numbers)
#
# def average(numbers, res_avg:dict[str, int]):
#     res_avg["average"] = sum(numbers)/len(numbers)
#
# res_sum: dict[str, int] = {}
# res_avg: dict[str, int] = {}
#
# thread_sum = threading.Thread(
#     target = sum_of_numbers,
#     args = (numbers, res_sum),
# )
#
# thread_avg = threading.Thread(
#     target = average,
#     args = (numbers, res_avg),
# )
#
# thread_sum.start()
# thread_sum.join()
# print(f"Sum = {res_sum}")
#
# thread_avg.start()
# thread_avg.join()
# print(f"Average = {res_avg}")


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

# def
