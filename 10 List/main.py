# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно порахувати, скільки у списку парних
# і непарних чисел. Результати вивести на екран.

# n = int(input("Enter length of list "))
# ls = [int(input("Enter number ")) for _ in range(0, n)]
# print(ls)
# sum_even =0
# sum_odd = 0
# for x in ls:
#     if x % 2 == 0:
#         sum_even +=1
#     if x % 2 != 0:
#         sum_odd +=1
# print("Sum of even numbers: ", sum_even, "\n" "Sum of odd numbers: ", sum_odd)
#
#
# # Завдання 2
# # Користувач із клавіатури вводить список цілих чисел. Необхідно визначити максимальне і мінімальне значення
# # у списку. Результати вивести на екран.
#
# n = int(input("Enter length of list "))
# ls = [int(input("Enter number ")) for _ in range(0, n)]
# print(ls)
# print("Max number: ", max(ls), "\n" "Min number: ", min(ls))
#
#
# # Завдання 3
# # У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний елемент і максимальний,
# # від'ємний елемент, порахувати кількість від'ємних елементів, порахувати кількість додатних елементів, порахувати
# # кількість нулів. Результати вивести на екран.
#
# n = int(input("Enter length of list "))
# ls = [random.randint(-10, 10) for _ in range(0, n)]
# print(ls)
# list_positive = []
# list_negative = []
# count_zero = 0
#
# for i in ls:
#     if i == 0:
#         count_zero+=1
#     elif i > 0:
#         list_positive.append(i)
#     elif i < 0:
#         list_negative.append(i)
#
# print("Positive ", list_positive)
# print("Negative",  list_negative)
#
# print("Min positive ", min(list_positive), "\n" "Count positive ", len(list_positive))
# print("Max negative ", max(list_negative), "\n" "Count negative ", len(list_negative))
# print("Count zero ", count_zero)
#
# #
# # Завдання 4
# # Користувач із клавіатури вводить список цілих чисел і деяке число. Необхідно видалити зі списку всі елементи,
# # які менші за задане число. Результат вивести на екран.
#
# n = int(input("Enter length of list "))
# ls = [int(input("Enter number ")) for _ in range(0, n)]
# print(ls)
# number = int(input("Enter any  number "))
# new_list = ls.copy()
#
# for i in ls:
#     if i < number:
#         new_list.remove(i)
# print(new_list)
#
# #
# # Завдання 5
# # Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12.
# # Необхідно вивести на екран результат виразу. У нашому прикладі це 35. Арифметичний вираз може складатися тільки
# # з трьох частин: число, операція, число. Можливі операції: +, -, *, /.
#
# s = input("Enter math expression like a + b: ")
# res = re.sub(r"\s+", "", s)
# number_1 = ""
# number_2 = ""
# operation = ""
# is_operation = False
# result = 0
#
# for i in res:
#     if i.isdigit() and is_operation == False:
#         number_1 +=i
#     elif i.isdigit() and is_operation == True:
#         number_2 +=i
#     else:
#         is_operation = True
#         operation = i
#
# if operation not in "+-*/":
#     print("Wrong operator")
#     exit()
# else:
#     if operation == "+":
#         result = int(number_1) + int(number_2)
#     if operation == "-":
#         result = int(number_1) - int(number_2)
#     if operation == "*":
#         result = int(number_1)*int(number_2)
#     if operation == "/":
#         result = int(number_1) / int(number_2)
# print(f"Result: {number_1}{operation}{number_2} = {result}")
#
# # Завдання 6
# # Користувач із клавіатури вводить список цілих чисел. Необхідно відсортувати цей список так,
# # щоб від'ємні числа залишилися на своїх місцях, а решта елементів були відсортовані за зростанням.
# # Результат вивести на екран.
#
# n = int(input("Enter length of list "))
# ls = [int(input("Enter number ")) for _ in range(0, n)]
# print(ls)
# positive_list = []
# ind = 0
# new = []
# # create new list with positive numbers and sort it
# for i in ls:
#     if i>=0:
#         positive_list.append(i)
# print(positive_list)
# sorted_positive_list = sorted(positive_list)
# print(sorted_positive_list)
#
# for i in ls:
#     if i < 0:
#         new.append(i)
#     else:
#         new.append(sorted_positive_list[ind])
#         ind+=1
# print(new)
