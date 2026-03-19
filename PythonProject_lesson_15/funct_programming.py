# fcf
# hof
# def action1(a, b):
#     return a + b
#
#
# def action2(a, b):
#     return a - b
#
# def do_action(a,b, op):
#     return op(a,b)
#
#
# print(do_action(1,2, action1))
# print(do_action(1,2, action2))

#hof  - high order function

#side effects -> function changes outside
# мінімізувати зміни в глобальній області

# Наприклад, завдання знаходження успішних студентів у групі (з середнім балом понад 60) зручно розбити на такі кроки (окремі підзадачі):
# введення даних про оцінки студентів групи;
# підрахунок середнього балу кожного студента з усіх предметів;
# знаходження студентів із середнім балом понад 60 та формування списку успішних студентів;
# виведення списку успішних студентів з їх середнім балом.

# Кожне з цих завдань легко реалізувати та просто тестувати у вигляді окремої функції.

# Функційний стиль:
# def input_students():
#     n = int(input("Кількість студентів: "))
#     students = []
#     for i in range(n):
#         name = input(f"Імя студента #{i + 1} : ")
#         m = int(input("Скільки оцінок(предметів)?: "))
#
#         while True:
#             parts = input(f"Введіть {m} оцінок через пробіл: ").strip().split()
#             if len(parts) != m:
#                 print("Кількість оцінок не співпадає..")
#                 continue
#
#             grades = list(map(int, parts))
#
#             students.append([name, grades])
#             break
#
#     return students
#
#
# def avg(grades):
#     return sum(grades) / len(grades) if grades else 0
#
#
# def add_average(students):
#     return list(map(lambda s: [*s, avg(s[1])], students))
#
#
# def successful_students(students_with_avg, limit):
#     return list(filter(lambda s: s[2] >= limit, students_with_avg))
#
#
# def print_successful(successful):
#     successful_sorted = sorted(successful, key=lambda s: s[2], reverse=True)
#     print("Список успішних студентів: ")
#     for s in successful_sorted:
#         print(f"- {s[0]}: {s[2]:.2f}")
#
# def main():
#     students = [['den', [100]*6],['den2', [80]*6],['den3', [61]*6], ['john', [1, 2, 3]]]  # input_students()
#     students_with_avg = add_average(students)
#     successful = successful_students(students_with_avg, limit=60)
#     print_successful(successful)

# Імперативний
# def main():
#     n = int(input("Кількість студентів: "))
#     students = []
#     for i in range(n):
#         name = input(f"Імя студента #{i + 1} : ")
#         m = int(input("Скільки оцінок(предметів)?: "))
#
#         while True:
#             parts = input(f"Введіть {m} оцінок через пробіл: ").strip().split()
#             if len(parts) != m:
#                 print("Кількість оцінок не співпадає..")
#                 continue
#
#             grades = [int(x) for x in parts]
#
#             break
#
#         avg_score = sum(grades) / len(grades) if grades else 0
#
#         if avg_score > 60:
#             students.append([name, avg_score])
#
#     successful_sorted = sorted(students, key=lambda s: s[1], reverse=True)
#     print("Список успішних студентів: ")
#     for s in successful_sorted:
#         print(f"- {s[0]}: {s[1]:.2f}")
#
# if __name__ == '__main__':
#     main()


# def main():
#     print('main logic')
#
# print("global scope in main")
# print(__name__)
# if __name__ == '__main__':
#     main()
#
# def foo():
#     pass

# lambda аргументи: вираз
# def doo(ls, op):
#     temp = []
#     for i in ls:
#         temp.append(op(i))
#     return temp
#
#
# ls = [1, 2, 3, 4, 5]
#
# new_ls = doo(ls, lambda n: n*3)
# print(new_ls)


# map, filter, zip, sorted
# ls = [1, 2, 3, 4, 5]

# ls = ["  Alex ", "!@John ", "__Den"]
# res = list(map(lambda n: n.strip(" !@_"), ls))
#
# print(res)
# def foo(i):
#     if isinstance(i, int):
#         return i
#
#     return i % 2 == 0
# ls = [1, 2, [3, 4], 5]
# res = list(filter(foo, ls))
#
# print(res)

# def foo(i):
#     if isinstance(i, int):
#         return i
#
#     return i % 2 == 0
#
#
# ls = [[1, 2], [3, 4], [5, 0]]
# res = list(map(lambda sub_ls: sub_ls[0]+sub_ls[1], ls))
#
# print(res)


# ls1 = [1, 2, 3, 4, 5]
# ls2 = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x1, x2: x1 + x2, ls1, ls2))
#
# print(res)
#
# name = 5
# def x(asd):
#     return asd
# ls1 = ["Den", "John", "Bob"]
# ls2 = ["den@g.com", "jonh@g.com", "bob@g.com"]
# ls3 = ["+380xx", "+380yy", "+380zz", "+380aa"]
# res = list(zip(ls1, ls2, ls3))
# print(res)


import functools


# def foo(acc, x):
#     print(acc, x)
#     if isinstance(x, int):
#         return acc + x
#     return acc
#
#
# ls = ["1", 2, print, 3, 4]
# res = functools.reduce(foo, ls, 0)
# print(res)
#
# def power(base, exp=4):
#     return base ** exp
#
# power_exp4 = functools.partial(power, exp=4)
# power_exp9 = functools.partial(power, exp=9)
#
# print(power_exp4(2))
# print(power_exp4(5))
#
#
# power(2, 4)
# power(2, 4)
# power(2, 4)
#
# power(2, 9)
# power(2, 9)
# power(2, 9)
# power(2, 9)
# power(2, 9)
#
# power_exp9(2)
# power_exp9(2)
# power_exp9(2)