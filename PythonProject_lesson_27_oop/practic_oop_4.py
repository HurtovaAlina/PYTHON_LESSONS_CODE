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


# class Rectangle:
#
#     def __init__(self, width: float, height: float):
#         self._width = width
#         self._height = height
#
#     def get_perimetr(self) -> float:
#         return  self._width * self._height
#
#     def display_info(self):
#         print(f"Rectangle width = {self._width}, Rectangle height = {self._height}")
#         print(f"Perimetr = {self.get_perimetr()}")
#
#
# class Circle:
#
#     def __init__(self, radius: float):
#         self._radius = radius
#
#     def get_perimetr(self) -> float:
#         return 2* math.pi * self._radius
#
#     def display_info(self):
#         print(f"Circle radius = {self._radius}")
#         print(f"Perimetr = {self.get_perimetr()}")
#
#
# class Triangle:
#
#     def __init__(self,a: float, b: float, c: float):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     def get_perimetr(self) -> float:
#         return self._a + self._b + self._c
#
#     def display_info(self):
#         print(f"Triangle = a : {self._a}, b : {self._b}, c : {self._c}")
#         print(f"Perimetr = {self.get_perimetr()}")
#
# def create_figure() -> Rectangle | Circle | Triangle | None:
#     type_of_figure = input("Enter type of figure: Rectangle, Circle, Triangle ").strip(" ")
#
#     if type_of_figure == "Rectangle":
#         width = float(input("Enter width "))
#         height = float(input("Enter height "))
#         return Rectangle(width, height)
#
#     elif type_of_figure == "Circle":
#         radius = float(input("Enter radius "))
#         return Circle(radius)
#
#     elif type_of_figure == "Triangle":
#         a = float(input("Enter side a "))
#         b = float(input("Enter side b "))
#         c = float(input("Enter side c "))
#         return Triangle(a,b,c)
#
#     else:
#         print("Invalid figure")
#         return None
#
# figures = []
# for _ in range(3):
#     figure = create_figure()
#     if figure:
#         figures.append(figure)
#
# for figure in figures:
#     figure.display_info()

# Завдання 2
# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька співробітників, добавте їх у список та для
# кожного викличте відповідні методи.

class Manager:

    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return self._base_salary


class Developer:

    def __init__(self, name: str, base_salary: float, work_experience: int):
        self._name = name
        self._base_salary = base_salary
        self._work_experience = work_experience

    def get_salary(self) -> float:
        if self._work_experience > 4:
            return self._base_salary * 1.2
        else:
            return self._base_salary



class Intern:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return self._base_salary * 0.5



def create_worker()-> Manager | Developer | Intern | None:
    type_of_worker = input("Enter type of worker: Manager/ Developer/ Intern ")

    if type_of_worker == "Manager":
        name = input("Enter name ")
        base_salary = float(input("Enter salary "))
        return Manager(name, base_salary)

    elif type_of_worker == "Developer":
        name = input("Enter name ")
        base_salary = float(input("Enter salary "))
        work_experience = int(input("Enter work experience "))
        return Developer(name, base_salary, work_experience)

    elif type_of_worker == "Intern":
        name = input("Enter name ")
        base_salary = float(input("Enter salary "))
        return Intern(name, base_salary)

    else:
        print("Invalid worker")
        return None

workers = []

for _ in range(3):
    worker = create_worker()
    if worker:
        workers.append(worker)

for worker in workers:
    print(worker.get_salary())
