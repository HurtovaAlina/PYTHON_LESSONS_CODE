print("Hello World", "Python", 2 + 2)
print("Hello World", "Python", 2 + 2, sep="-")
print("Hello World", "Python", 2 + 2, end="&")
print("Hello Students!", end="@")
print("Hello Students!")

# escape
# \n  new line
print("Hello \nWorld")
# \t  tab
print("Hello \t\t\tWorld")
# \'
# \"
print('"Hello World"')
# \\
print("Hello \\World\\")
# \r carriage return
print("Hello \rWorld")
# \b backspace
print("Hell\bo World\b")

print("\n   Hello")
print(
    """
    /   g
     /
X
"""
)

# string methods -> literals
23.4
2
print(23.4 + 2)
print(0.3 + 0.3 + 0.3)

print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
# ділення без остачі - відкидає дробну частину  14//5 = 2
print(14 // 5)
# ступінь
print(2**4)
# повертає остачу від ділення 7%2 = 1
print(7 % 2)
print(1372 % 56)
# 1372/56
# 24.5
# 1372-1344
# 28
##########
# 3%5 -> 3 ліва сторона
print(3 % 5)
# відʼємне значення по модулю береться -> знайти формулу
# Порахуємо:
# Обчислюємо floor(-13 / 7)
# -13 / 7 ≈ -1.857
# floor → -2
# Підставляємо:
# -13 - 7 * (-2)
# = -13 + 14
# = 1

print(-13 % 7)
# 0%5 -> 0 завжди

print(0.5)

# +,  -
# унарний
print(-2)
# **
# *,/, %, //
# +, -
# бінарний
print(2 - 1)

name = "Sam"
age = 25
print("Name: ", name, "Age: ", age)
# format
print(f"Name: {name}\nAge: {age}")

n1 = 5
n2 = 10
print("n1+n2 =", n1 + n2)
print(f"{n1} + {n2} = {n1 + n2}")

n3 = n1 + n2
print(n3)

# n1 = n1 + n2 -> the same  for -=, *=, /=, %=, **=
n1 += n2
print(n1)

# строка підтримує додавання з строкою - конкатенація,  і множення на число - дублює строку
n1 = "10"
n2 = 10
print(n1 + n1)
print(n1 * n2)

# типи даних
n1 = 10  # Integer int
n2 = "Hello"  # String str
n3 = 4.5  # Float float
n4 = True  # Boolean bool

# int -> str
# input() введення даних
# name = input("Enter your name: ")
# print(name)
# print(input("Enter your age: "))

# Task 1
# User inputs 2 numbers, output sum of these numbers // all data is string by default

n1 = input("Enter number 1: ")
n2 = input("Enter number 2: ")
print(f"{n1} + {n2} = {n1 + n2}")  # result STRING
print(int("7") + 7)  # конвертація
# любе число в bool -> True, 0 -> False. Строка, якщо не порожня - завжди True. Все, де є якась інформація буде True
print(7, int(2.56), int(False), int(True), int("7"))
print(str(7), str(2.56), str(False), str(True), "7" + "7")
print(float("13") + 7, 2.56, float(False), float(True), float("7"))
print(bool("13") + 7, bool(2.56), False, True, bool("7"))
print(bool("") + 7, bool(0.0), False, True, bool(""))

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
print(f"{n1} + {n2} = {n1 + n2}")
