# # import random
# # from random import randint, randrange, choice
# #
# # print(random.randint(-2,999))
# # print(randint(-2,999))
#
# import math
# # from random import randint as rint, randrange, choice
# # #назва змінній як у функціі
# # randint = 1
# # print(rint(-2,999))
#
# # from const import MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
# #
# # print(MONDAY)
# # print(TUESDAY)
# # print(WEDNESDAY)
# # print(THURSDAY)
# # print(FRIDAY)
# # print(SATURDAY)
# # print(SUNDAY)
#
# #змінні написані капсом - це константи і змінаювати не можна
#
# import random
# #зафіксувати рандом - залежит від поточного часу логіка. Якщо зафіксувати зерно:
# #random.seed(5)
#
# # рандом интеджер: Return random integer in range [a, b], including both end points.
# x= random.randint(-3,56)
# print("Random int: ", x)
# # рандом діапазон: Choose a random item from range(stop) or range(start, stop[, step]). -> 0, 5, 10, 15, 20 бере кожний
# #пятий елемент з діапазону
# x= random.randrange(0, 20, 5)
# print("Random range: ", x)
# #рандом десятичної дроби
# x = random.random()
# x1= x*100
# print("Random float: ", x, "x1 = ", x1)
# #перемішує колекцію
# l = ["a","d","i","d","a","s"]
# random.shuffle(l)
# print("Random shuffle: ", l)
# #вибери рандомно з якось елементу (букву зі строки)
# x= random.choice("hello")
# print("Random choice: ", x)
#
# #math
#
# print(math.ceil(5.45))
# print(math.floor(5.45))
# print(math.pow(2, 4))
# print(math.sqrt(25))
#
# #datetime
# from datetime import time, date, datetime
#
# my_date = date(2020,3,12)
# print(my_date.strftime("%A %d %B %Y"))
#
# today = date.today()
# print(today.strftime("%A %d %B %Y"))
#
# current_time= time(20, 25, 10)
# print(current_time)
# x= datetime(2020, 5,12,20,10,5)
# print(x.strftime("%A %d %B %Y %H:%M:%S"))
#
# print(datetime.now())
#
# #локальний час time
# #різниця між двома тайм стемпами
# import time
#
# start = time.perf_counter()
# input("Enter ... ")
# end = time.perf_counter()
# print(end-start)
import math

# Завдання 1
# Користувач вводить з клавіатури два числа.
# Необхідно знайти суму чисел, різницю чисел, добуток числі.
#  Результат обчислень вивести на екран.
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# print(a+b, a-b, a*b)

# 1234
# 4321
n = 1234
n4 = n % 10
n3 = (n // 10) % 10
n2 = (n // 100) % 10
n1 = n // 1000

print(n4, n3, n2, n1)
x1 = int(f"{n4}{n3}{n2}{n1}")
x2 = n4 * 10**3 + n3 * 10**2 + n2 * 10 + n1
print(x1, x2)

# Завдання 1
# Користувач вводить з клавіатури температуру за шкалою Цельсія.
# Потрібно перевести температуру в градуси за Фаренгейтом і вивести на екран.
temp_C = float(input("Temperature C: "))
temp_F = temp_C * 9 / 5 + 32
print("Temperature F: ", temp_F)

# Завдання 2
# Користувач вводить із клавіатури значення в євро. Напишіть програму,
# яка переводить цю суму в долари, використовуючи курс євро, введений з клавіатури. Результат виводиться на екран.
euro = float(input("Enter euro: "))
euro_to_doll = float(input("Enter euro to dollar: "))  # приклад: євро = 1.17 долл.
print(f"You need to pay {euro*euro_to_doll} dollars for {euro} euro")


# Завдання 3
# Користувач з клавіатури вводить двозначне число.
# Наприклад, 26. Потрібно показати на різних рядках значення першого і другого розряду.
# У нашому випадку це буде виглядати так:
# 2
# 6
number = int(input("Enter two-digit number : "))
n1 = int(number % 10)
n2 = int((number - n1) / 10)
print(n1)
print(n2)

# Завдання 4
# Користувач вводить із клавіатури дві цифри. Необхідно створити число, що містить ці цифри.
# Наприклад, якщо з клавіатури введено 9, 7, тоді потрібно сформувати число 97.
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
res = str(n1) + str(n2)
print(res)

# Завдання 5
# Користувач із клавіатури вводить тризначне число. Наприклад, 891.
# Потрібно показати на різних рядках значення першого, другого і третього розряду.
# Також потрібно показати на окремому рядку суму цих трьох чисел. У нашому випадку це виглядатиме так:
# 8
# 9
# 1
# 18

n = int(input("Enter three-digit number: "))
n1 = n % 10
n2 = (n // 10) % 10
n3 = n // 100

print(n3)
print(n2)
print(n1)
print(n3 + n2 + n1)

# Завдання 6
# Користувач вводить суму вкладу та відсоткову ставку. Напишіть програму, яка:
# Обчислює, скільки користувач отримає через 5 років, якщо щороку сума вкладу збільшується на вказаний відсоток.
# Виводить суму вкладу за кожен рік окремо.
deposit = float(input("Enter deposit: "))
interest_rate = float(input("Enter interest rate % for year: "))
sum = deposit * (1 + interest_rate / 100) ** 5
print(sum)

# Задача - Піцца-паті: скільки піц замовити і скільки лишиться шматків

# Умова
# Введіть з клавіатури:
# people - скільки людей на вечірці
# slices_per_person - скільки шматків зїдає 1 людина
# slices_per_pizza - скільки шматків у 1 піці
# pizza_price - ціна 1 піци (грн)
# delivery_per_pizza - доставка за 1 піцу (грн)

# Потрібно порахувати і вивести:
# - мінімальну кількість піц, щоб усім вистачило шматків
# - скільки шматків залишиться
# - загальну вартість замовлення (піци + доставка)
# - скільки гривень виходить на 1 людину

people = int(input("Enter people count: "))
slices_per_person = int(input("Enter slices eats person: "))
slices_per_pizza = int(input("Enter slices in pizza: "))
pizza_price = float(input("Enter price of 1 pizza"))
delivery_per_pizza = float(input("Enter price of delivery for 1 pizza"))

min_qty_slices = people * slices_per_person
min_pizza_qty = math.ceil(min_qty_slices / slices_per_pizza)
slices_remain = min_pizza_qty * slices_per_pizza - min_qty_slices
total_price = (pizza_price + delivery_per_pizza) * min_pizza_qty
price_per_person = total_price / people

print(min_pizza_qty)
print(slices_remain)
print(total_price)
print(price_per_person)
