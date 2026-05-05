# Завдання 1
# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран

from typing import List, Dict
import threading

def ask_number(res: Dict[str, List[int]]):
    numbers = []
    while True:
        number = input("Enter number or '' to stop ")

        if number == "":
            break

        try:
            numbers.append(int(number))
        except ValueError:
            print("Not a number!")

    res["numbers"] = numbers

def sum_of_numbers(res: Dict[str, float]):
    numbers = res.get("numbers", [])
    res["sum"] = sum(numbers)

def avg_of_numbers(res: Dict[str, float]):
    numbers = res.get("numbers", [])
    if numbers:
        res["avg"] = sum(numbers)/len(numbers)
    else:
        res["avg"] = 0

res: Dict[str, float] = {}

thread_ask_number = threading.Thread(
    target = ask_number,
    args = (res,),
)

thread_sum = threading.Thread(
    target = sum_of_numbers,
    args = (res,),
)

thread_avg = threading.Thread(
    target = avg_of_numbers,
    args = (res,),
)

thread_ask_number.start()
thread_ask_number.join()

thread_sum.start()
thread_avg.start()
thread_sum.join()
thread_avg.join()

print(f"Result: {res}")
