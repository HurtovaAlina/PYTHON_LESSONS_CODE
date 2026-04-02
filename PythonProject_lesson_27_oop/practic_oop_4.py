# Завдання 1
# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи.
import math


class Rectangle:

    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def get_perimetr(self) -> float:
        return  self._width * self._height

    def display_info(self):
        print(f"Rectangle width = {self._width}, Rectangle height = {self._height}")
        print(f"Perimetr = {self.get_perimetr()}")


class Circle:

    def __init__(self, radius: float):
        self._radius = radius

    def get_perimetr(self) -> float:
        return 2* math.pi * self._radius

    def display_info(self):
        print(f"Circle radius = {self._radius}")
        print(f"Perimetr = {self.get_perimetr()}")


class Triangle:

    def __init__(self,a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def get_perimetr(self) -> float:
        return self._a + self._b + self._c

    def display_info(self):
        print(f"Triangle = a : {self._a}, b : {self._b}, c : {self._c}")
        print(f"Perimetr = {self.get_perimetr()}")

def create_figure() -> Rectangle | Circle | Triangle | None:
    type_of_figure = input("Enter type of figure: Rectangle, Circle, Triangle ").strip(" ")

    if type_of_figure == "Rectangle":
        width = float(input("Enter width "))
        height = float(input("Enter height "))
        return Rectangle(width, height)

    elif type_of_figure == "Circle":
        radius = float(input("Enter radius "))
        return Circle(radius)

    elif type_of_figure == "Triangle":
        a = float(input("Enter side a "))
        b = float(input("Enter side b "))
        c = float(input("Enter side c "))
        return Triangle(a,b,c)

    else:
        print("Invalid figure")
        return None

figures = []
for i in range(1,4):
    figure = create_figure()
    if figure:
        figures.append(figure)

for figure in figures:
    figure.display_info()
