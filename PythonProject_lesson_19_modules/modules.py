# modules
# import [module name]


# для встановлення нової бібліотеки  in Terminal
# pip install [name]

# отримати функцію з модуля
# [назва модуля].[назва функції]
#
# res = random.randint(0, 100) # рандомное число от 0 до 99
# print(res)

# отримати одразу функцію
# from [назва модуля] import [назва функції], [назва функції]

# from random import randint
# res1 = randint(0, 100)
# print(res1)

# імпорт власного модуля - знаходить в venv або папці де зараз працюємо
import geometry  # формально запускається весь код всередині модуля geometry

print("Lesson module")
area = geometry.get_circle_area(10)
print(area)

# Hello from geometry
# Enter radius: 2
# Circle perimetr
# Perimeter: 12.56
# Lesson module
# Circle area
# 314.0
