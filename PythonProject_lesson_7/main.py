# i = 1
# while i <= 5:
#     print(f"iteration #{i}")
#     i += 1
# print("The end")
import time

# i = 5
# while i >=1:
#     print(f"iteration #{i}")
#     i -= 1
# print("The End")

# break - stop loop
# continue - skip current step
# else

#  BREAK
# data = ""
# while True:
#     x = input("Enter data: ")
#     if x == "exit":
#         break
#     data += x
#     data += "\n"
# print("Data: ", data)
# print("The End")

# data = ""
# x = None
# while x !="exit":
#     x = input("Enter data: ")
#     data += x
#     data += "\n"
# print("Data: ", data)
# print("The End")

# CONTINUE
# i = 1
# while i <= 5:
#     if i == 2 or i ==3:
#         i += 1
#         continue
#     print(f"iteration #{i}")
#     i += 1
# print("The end")

# i = 1
# while i <= 5:
#     if i  not in (2, 3): # left element is in right element: "h" in "hello"
#         print(f"iteration #{i}")
#     i += 1
# print("The end")

# ELSE коли цикл завершився успішно і не перервався через break - для пошуку в колекціі і якщо елемент не був найдено -
#  else виконається коли завершиться цикл умова True -> False
# i = 1
# while i<=3:
#     print(i)
#     i+=1
# else:
#     print("Loop was finished without break")

# i = 1
# while i<=3:
#     if i == 3:
#         break
#     print(i)
#     i+=1
# else:
#     print("Loop was finished without break")

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i*j, end = "\t")
#         j+=1
#     print()
#     i +=1

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print("*", end = "\t")
#         j+=1
#     print()
#     i +=1

# h =5
# w =5
# i = 1
# while i <= h:
#     j = 1
#     while j <= w:
#         print("*", end = "\t")
#         j+=1
#     print()
#     i +=1

# h =8
# w =10
#
# i = 1
# while i <= h:
#     j = 1
#     while j <= w:
#         if j == 1 or i == 1 or i == h or j == w:
#             print("*", end = "\t")
#         else:
#             print(" ", end = "\t")
#         j+=1
#     print()
#     i +=1

# h =10
# w =10
#
# i = 1
# while i <= h:
#     j = 1
#     while j <= w:
#         if i <= j:
#             print("*", end = "\t")
#         j+=1
#     print()
#     i +=1

# h =10
# w =10
#
# i = 1
# while i <= h:
#     j = 1
#     while j <= w:
#         if i >= j:
#             print("*", end = "\t")
#         else:
#             print(" ", end = "\t")
#         j+=1
#     print()
#     i +=1

# i = 1
# while i <= 500:  #498
#     print(i)
#     i +=1
#
# print("the end1")
# print("the end2")
# print("the end3")
# print("the end4")
# print("the end5")

# command = ""
# while command != "exit":
#     print("Command: login, register, help, exit")
#     command = input("Enter command: ")
#     if command == "login":
#         email = input("Enter email: ")
#         password = input("Enter password: ")
#
#         if email == "" or password == "":
#             print("Error: email or password cannot be empty")
#         elif "@" not in email:
#             print("Error: email must contain @")
#         else:
#             print("Try to connect ...")
#             time.sleep(2)
#             print("Connected")
#             break
#     elif command == "register":
#         pass
#     elif command == "exit":
#         print("Exiting ....")


# Завдання 1
# Користувач вводить із клавіатури два числа. Потрібно порахувати суму чисел у вказаному діапазоні, а також
# середньоарифметичне.

# a =1
# b =5
#
# start = a
# end = b
#
# if start >  end:
#     start, end = end, start
#
# s = 0
# count = 0
#
# i = start
# while i <= end:
#     s +=i
#     count +=1
#     i += 1
#
# avg = s / count
#
# print(f"Summ {s}")
# print(f"Avg {avg}")


# Завдання 2
# Користувач вводить із клавіатури число. Потрібно порахувати факторіал числа. Наприклад, якщо введено 3, факторіал
# числа 1*2*3 = 6.
# Формула для розрахунку факторіалу: n! = 1*2*3...*n, де n — число для розрахунку факторіалу.



# Завдання 3
# Користувач вводить із клавіатури довжину лінії. Потрібно відобразити на екрані горизонтальну лінію з *,
# вказаної довжини.
# Наприклад, якщо було введено 7, тоді виведення на екран буде таким:
# *******

# Завдання 4
# Користувач вводить з клавіатури довжину лінії та символ для заповнення лінії. Потрібно відобразити на екрані
# горизонтальну лінію із введеного символу, зазначеної довжини.
# Наприклад, якщо було введено 5 і &, тоді виведення на екран буде таким:

# Завдання 5
# Створіть програму, яка відображає меню з опціями для вибору: 1 — знайти мінімум двох чисел, 2 — знайти максимум двох
# чисел, 3 — вихід. Програма має запитувати в користувача номер опції і, якщо вибрано пункт 1 або 2, запитувати введення
# двох чисел, після чого знаходити і виводити або мінімум (якщо вибрано 1), або максимум (якщо вибрано 2) із введених
# чисел. При введенні пункту 3 програма завершує роботу, виводячи повідомлення про вихід. Якщо введено некоректну опцію,
# програма має повідомити про помилку і знову показати меню. Програма має працювати в циклі, повторюючи виведення меню
# і виконання дій доти, доки не буде обрано вихід.

# Завдання 6
# Створіть програму, яка відображає меню з опціями для вибору: 1 — додавання двох чисел, 2 — віднімання двох чисел,
# 3 — ділення двох чисел, 4 — вихід. Програма має запитувати в користувача номер опції і, якщо обрано пункт 1, 2
# або 3, запитувати введення двох чисел, після чого виконувати обрану операцію: додавати (якщо обрано 1), віднімати
# (якщо обрано 2) або ділити (якщо обрано 3) введені числа. Результат операції має бути виведено на екран. У разі
# вибору пункту 4 програма завершує роботу, виводячи повідомлення про вихід. Якщо введено некоректну опцію, програма
# має повідомити про помилку і знову показати меню. Програма має працювати в циклі, повторюючи виведення меню і
# виконання дій доти, доки не буде обрано вихід.