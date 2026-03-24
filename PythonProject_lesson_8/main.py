# while - поки умова true  виконувати тіло поки не стане false
# for in задача перебрати колекцію поелементно. Коли все перебере - зупиниться

# for  <variable> in <container>:
#  ... code
# .... code
# <variable> мітить копію елемента, який ми беремо з контейнера
# повторення певних дій кілька разів
# може використовувати break, continue, else

# line = "У разі вибору пунтку 4 програма завершує роботу."
#
# for i in line:
#     print(i)

# функція range(1, 2, 5) - повертає обʼєкт діапазон і цикл перебирає діапазон
# range(start, stop)
# range(1,5) -> 1,2,3,4
# range(5) -> 0, 1, 2, 3, 4
# range(start, stop, step)
# range(2,10,2) -> 2, 4, 6, 8
# range(10, 2, -2) -> 10, 8, 6, 4
# r = range(1,5,2)
# print(r)

# for i in range(10, 2, -2):
#     print(i)
#
# for i in range(5):
#     print(i)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end = "\t")
#     print()

# Завдання 2
# Користувач вводить із клавіатури число. Потрібно порахувати факторіал числа. Наприклад, якщо введено 3, факторіал
# числа 1*2*3 = 6.
# Формула для розрахунку факторіалу: n! = 1*2*3...*n, де n — число для розрахунку факторіалу.

# n = int(input("n ")) #1*2*3*4*5... n
# f = 1
# for i in range(1, n+1):
#     f *= i
# print(f)


# Завдання 3
# Користувач вводить із клавіатури довжину лінії. Потрібно відобразити на екрані горизонтальну лінію з *,
# вказаної довжини.
# Наприклад, якщо було введено 7, тоді виведення на екран буде таким:
# *******

# l = int(input("length "))
# for i in range(1, l+1):
#     print("*", end = "")

# print("*"*int(input("length ")))

# line = ""
# l = int(input("length "))
#
# for i in range(1, l+1): # якщо змінну і не використовую всередині циклу - замінити на _
# # for _ in range(1, l+1):
#     line += "*"
#
# print(line)

# Завдання 4
# Користувач вводить з клавіатури довжину лінії та символ для заповнення лінії. Потрібно відобразити на екрані
# горизонтальну лінію із введеного символу, зазначеної довжини.
# Наприклад, якщо було введено 5 і &, тоді виведення на екран буде таким:
# &&&&&

# width = 10
# ch = "&"
#
# i = 0
# line = ""
# while i < width:
#     line += ch
#     i += 1
# print(line)


# Завдання 5
# Створіть програму, яка відображає меню з опціями для вибору: 1 — знайти мінімум двох чисел, 2 — знайти максимум двох
# чисел, 3 — вихід. Програма має запитувати в користувача номер опції і, якщо вибрано пункт 1 або 2, запитувати введення
# двох чисел, після чого знаходити і виводити або мінімум (якщо вибрано 1), або максимум (якщо вибрано 2) із введених
# чисел. При введенні пункту 3 програма завершує роботу, виводячи повідомлення про вихід. Якщо введено некоректну опцію,
# програма має повідомити про помилку і знову показати меню. Програма має працювати в циклі, повторюючи виведення меню
# і виконання дій доти, доки не буде обрано вихід.

# use while infinity
# while True:
#     print("\nМеню: ")
#     print("1. MIN")
#     print("2. MAX")
#     print("3. EXIT")
#
#     choice = input("Select option 1/2/3: ")
#
#     if choice == "1":
#         a = float(input("Enter a: "))
#         b = float(input("Enter b: "))
#         # min_n = a
#         # if a> b:
#         #     min_n = b
#         # print("MIN: ", min_n)
#         # A if <cond> else B
#         print("MIN: ", a if a < b else b)
#
#     elif choice == "2":
#         a = float(input("Enter a: "))
#         b = float(input("Enter b: "))
#         print("MAX: ", a if a > b else b)
#
#     elif choice == "3":
#         print("Exit")
#         break
#     else :
#         print("error")


# Завдання 1
# Створіть програму, яка відображає меню з опціями для вибору: 1 — додавання двох чисел, 2 — віднімання двох чисел,
# 3 — ділення двох чисел, 4 — вихід. Програма має запитувати в користувача номер опції і, якщо обрано пункт 1, 2
# або 3, запитувати введення двох чисел, після чого виконувати обрану операцію: додавати (якщо обрано 1), віднімати
# (якщо обрано 2) або ділити (якщо обрано 3) введені числа. Результат операції має бути виведено на екран. У разі
# вибору пункту 4 програма завершує роботу, виводячи повідомлення про вихід. Якщо введено некоректну опцію, програма
# має повідомити про помилку і знову показати меню. Програма має працювати в циклі, повторюючи виведення меню і
# виконання дій доти, доки не буде обрано вихід.

# while True:
#     print("\nМеню: ")
#     print("1. SUM")
#     print("2. SUB")
#     print("3. DIV")
#     print("4. EXIT")
#
#     choice = input("Select option 1/2/3/4: ")
#
#     if choice == "1":
#         a = float(input("Enter a: "))
#         b = float(input("Enter b: "))
#         print("SUM: ", a + b)
#
#     elif choice == "2":
#         a = float(input("Enter a: "))
#         b = float(input("Enter b: "))
#         print("SUB", a - b)
#
#     elif choice == "3":
#         a = float(input("Enter a: "))
#         b = float(input("Enter b: "))
#         if b != 0:
#             print("DIV", a / b)
#         else:
#             print("DIVISION ON ZERO!")
#
#     elif choice == "4":
#         print("Exit")
#         break
#     else :
#         print("error")

# 2
# Користувач вводить висоту трикутника і символ для заповнення. Програма повинна відобразити рівносторонній трикутник.
# Приклад введення:
# Введіть висоту трикутника: 4.
# Введіть символ: #.
# Приклад виведення:
#    #
#   ###
#  #####
# #######

# height = int(input("height: "))
# ch = input("char: ")
# for i in range(1, height+1):
#     space = height - i
#     char = 2 * i - 1
#     print(" "* space + ch * char + " "* space)

# height = int(input("height: "))
# ch = input("char: ")
# for i in range(1, height+1):
#     space = i-1
#     char = 2 * height - (2*i-1)
#     print(" "* space + ch * char + " "* space)

# 3
# Написати програму, яка перевіряє користувача на знання таблиці множення.
# Програма виводить на екран два числа, користувач має ввести їхній добуток.
# Розробити кілька рівнів складності (відрізняються складністю та кількістю запитань).
# Наприклад, в рівні буде 10 запитань, необхідно порахувати кількість вірних і не вірних відповідей.
# Вивести користувачеві оцінку його знань. якщо відповів 3 з 10 - оцінка не задовільно,
# 5 з 10 - задовільно, 8 з 10 - добре, 10 з 10 - відмінно
# nikname
# select option 1-3
# diapazon in variable
# якщо легка - змінна в рендж кількість кроків
# порахувати кількість правильних відповідей

# name = input("Enter name: ")
# level = int(input("Enter level: 1-2-3: "))
# score = 0
# total_score = 5
#
# if level == 1:
#     print("You need answer for 5 questions")
#     for i in range(1,6):
#         a = randint(1, 10)
#         b = randint(1, 10)
#         print(f"a = {a} , b = {b}")
#         answer = int(input("Please answer a * b: "))
#         if a*b == answer:
#             score +=1
#             print("Correct!")
#         else:
#             print("Wrong!")
#     print("End of level for gamer: ", name)
#     print("Your score: ", score)
#     print("Wrong answers: ", total_score - score)
#     if score == 5:
#         print("Perfect!")
#     elif 5 > score >= 3:
#         print("Good result!")
#     else:
#         print("Not satisfactorily")
#
# elif level == 2:
#     print("You need answer for 5 questions")
#     for i in range(1, 6):
#         a = randint(1, 100)
#         b = randint(1, 10)
#         print(f"a = {a} , b = {b}")
#         answer = int(input("Please answer a * b: "))
#         if a * b == answer:
#             score += 1
#             print("Correct!")
#         else:
#             print("Wrong!")
#     print("End of level for gamer: ", name)
#     print("Your score: ", score)
#     print("Wrong answers: ", total_score - score)
#     if score == 5:
#         print("Perfect!")
#     elif 5 > score >= 3:
#         print("Good result!")
#     else:
#         print("Not satisfactorily")
#
# elif level == 3:
#     print("You need answer for 5 questions")
#     for i in range(1, 6):
#         a = randint(1, 100)
#         b = randint(1, 100)
#         print(f"a = {a} , b = {b}")
#         answer = int(input("Please answer a * b: "))
#         if a * b == answer:
#             score += 1
#             print("Correct!")
#         else:
#             print("Wrong!")
#     print("End of level for gamer: ", name)
#     print("Your score: ", score)
#     print("Wrong answers: ", total_score - score)
#     if score == 5:
#         print("Perfect!")
#     elif 5 > score >= 3:
#         print("Good result!")
#     else:
#         print("Not satisfactorily")
# else:
#     print("Wrong level")
