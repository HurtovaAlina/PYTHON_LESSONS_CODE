# Самостійна робота

# Рівень 1
# Завдання 1
# Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. Межі діапазону передаються як параметри.
# Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.

# x = int(input("Enter x "))
# y = int(input("Enter y "))
#
# def multiplier(x, y):
#     mult = 1
#     if x > y:
#         x,y = y,x
#     for i in range(x, y+1):
#         mult *=i
#     return mult
#
# print(multiplier(x,y))


# Завдання 2
# Напишіть функцію для знаходження максимуму в списку цілих. Список передається як параметр.
#
# numbers = input("Enter numbers ")
# list_of_numbers = numbers.split(',')
# print(list_of_numbers)
#
# def find_max(numbers):
#     max = int(numbers[0])
#     for i in numbers:
#         i = int(i)
#         if i > max:
#             max = i
#     return max
#
# print(find_max(list_of_numbers))


# Завдання 3
# Напишіть функцію, що обчислює суму елементів списку цілих. Список передається як параметр.

# numbers = input("Enter numbers ")
# list_of_numbers = numbers.split(',')
# print(list_of_numbers)
#
# def find_sum(numbers):
#     sum_elements = 0
#     for i in numbers:
#         i = int(i)
#         sum_elements += i
#     return sum_elements
#
# print(find_sum(list_of_numbers))


# Завдання 4
# Напишіть функцію, що визначає кількість парних, непарних, додатних, від'ємних елементів списку цілих.
# Список передається як параметр.

# numbers = input("Enter numbers ")
# list_of_numbers = numbers.split(',')
# print(list_of_numbers)
#
# def find_ev_odd_pos_neg_elements(numbers):
#     count_evens = 0
#     count_odds = 0
#     count_positive = 0
#     count_negative = 0
#     for i in numbers:
#         if int(i) > 0:
#             count_positive+=1
#         else:
#             count_negative+=1
#         if int(i) % 2 == 0:
#             count_evens += 1
#         else:
#             count_odds += 1
#     return (print("Evens =", count_evens, "Odds =", count_odds, "Positives =", count_positive,
#             "Negatives =", count_negative))
#
# find_ev_odd_pos_neg_elements(list_of_numbers)

# Завдання 5
# Напишіть функцію, що перевертає вміст списку цілих.

# numbers = input("Enter numbers ")
# list_of_numbers = numbers.split(',')
# print(list_of_numbers)
#
# def reverse_numbers(numbers):
#     new_list = []
#     for i in range(len(numbers)-1, -1, -1):
#         new_list.append(numbers[i])
#     return new_list
#
# print(reverse_numbers(list_of_numbers))


# Завдання 6
# Напишіть функцію, що вираховує факторіал кожного елемента списку цілих. Функція повертає новий список,
# що містить отримані факторіали.

# numbers = input("Enter numbers ")
# list_of_numbers = numbers.split(',')
# print(list_of_numbers)
#
# def fact_elements(numbers):
#     new_list = []
#     fact = 1
#     for i in numbers:
#         for j in range(1, int(i)+1):
#             fact *=int(j)
#         new_list.append(fact)
#         fact = 1
#     return new_list
#
# print(fact_elements(list_of_numbers))

# Завдання 7
# Напишіть функцію, яка шукає всі числа Фібоначчі у списку цілих.

# input_list = input("Enter numbers ").split(',')
# list_of_numbers = [int(i) for i in input_list]
# print(list_of_numbers)
#
#
# n = int(input("Enter quantity of Fibonacci series "))
#
# def create_fibonacci(n):
#     fibonacci_list = [0,1]
#     for i in range (2,n):
#         fibonacci_number = fibonacci_list[i-1]+fibonacci_list[i-2]
#         fibonacci_list.append(fibonacci_number)
#     return fibonacci_list
#
# print("Fibonacci series: ", create_fibonacci(n))
#
#
# def fibonacci_numbers(list_of_numbers, fibonacci_list):
#     new_list = []
#     for i in sorted(list_of_numbers):
#             if int(i) in fibonacci_list:
#                 new_list.append(i)
#     return new_list
#
# print("Fibonacci numbers in the entered list: ", fibonacci_numbers(list_of_numbers,
#                                                                    fibonacci_list= create_fibonacci(n)))
