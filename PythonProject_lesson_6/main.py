# Diskriminant

# ax^2+bx+c=0
# a = 5
# b = 1
# c = 6

# D > 0 (2 different x)
# D = 0 (have only x)
# D < 0 (doesnt have)

# print("ax^2+bx+c=0")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# D = b * b - 4 * a * c
#
# if D > 0:
#     x_1 = (-b - sqrt(D))/(2*a)
#     x_2 = (-b + sqrt(D))/(2*a)
#     print(f"Є два дійсних коренів \nx1 = {x_1}, \nx2 = {x_2}")
# elif D == 0:
#     x = -b / (2 * a)
#     print(f"Є один дійсний корень \nx = {x}")
# elif D < 0:
#     print("немає дійсних коренів")


# Користувач вводить зп і стаж
# salary = float(input("Enter salary: "))
# years = float(input("Experience (years) : "))
#
# if years < 1:
#     print("No award")
# elif years < 3:
#     bonus = salary * 0.05
#     print("Award : ", bonus)
# elif years < 5:
#     bonus = salary * 0.1
#     print("Award : ", bonus)
# else:
#     bonus = salary * 0.15
#     print("Award : ", bonus)

# match

# match <varible>:
# ....case <variable_value1>:
# ........code for case
# ....case <variable_value2>:
# ........code for case

# x = 5
# match x:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case 5:
#         print("Five")
#     case _:
#         print("Another")

# x = 12
# match x:
#     case 0:
#         print("Zero")
#     case 1 | 2 | 3:
#         print("Small number")
#     case 4 | 5 | 6:
#         print("Middle number")
#     case _:
#         print("Another")

# x = None
# x = str(x) # "None"
# match x:
#     case "True":
#         print("its True")
#     case "False":
#         print("its False")
#     case "None":
#         print("its None")
#     case _:
#         print("Another text")


# x = 10
# match x:
#     case 1:
#         print("its One")
#     case value:
#         if value % 2 == 0:
#             print("its even number")
#         print("Another ", value)

# guard if after case -> additional check to have case worked

# Користувач вводить зп і стаж
# salary = float(input("Enter salary: "))
# years = float(input("Experience (years) : "))
#
# match years:
#     case y if y <1:
#         print("No award", y)
#     case y if 1<= y < 3:
#         print("Award : ", salary * 0.05)
#     case y if 3<= y < 5:
#         print("Award : ", salary * 0.1)
#     case y if y > 5:
#         print("Award : ", salary * 0.15)

# isinstance() -> повертає чи є типу даних
x = "Hello"
print(isinstance(x, int), type(x))
