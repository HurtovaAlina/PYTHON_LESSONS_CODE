# Завдання 1
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

import pickle
import json
from typing import List, Dict


# def add_item(items: List[str]) -> None:
#     item = input("Enter item ")
#     items.append(item)
#     print(f"Item {item} was added")
#
#
# def items_output(items: List[str]):
#     print("Items list:")
#     for item in items:
#         print(item)
#
# def save_to_json(items:List[str]) -> None:
#     with open("items.json", "w", encoding="utf-8") as file:
#         json.dump(items, file)
#         print("Saved to items.json")
#
#
# def read_from_json() -> List[str] | None:
#     try:
#         with open("items.json", "r", encoding="utf-8") as file:
#             data = json.load(file)
#             return data if data is not None else []
#     except FileNotFoundError:
#         return []
#
#
#
# def save_to_picle(items:List[str]) -> None:
#     with open("items.pickle", "wb") as file:
#         pickle.dump(items, file)
#         print("Saved to items.pickle")
#
#
# def read_from_pickle() -> List[str] | None:
#     try:
#         with open("items.pickle", "rb") as file:
#             data = pickle.load(file)
#             return data if data is not None else []
#     except FileNotFoundError:
#         return []
#
#
#
# if __name__ == "__main__":
#
#     items = []
#     for i in range(1,4):
#         add_item(items)
#
#     items_output(items)
#
#     save_to_json(items)
#     items_in_cart = read_from_json()
#     print(f"Items from json {items_in_cart}")
#
#     save_to_picle(items)
#     items_in_order = read_from_pickle()
#     print(f"Items from pickle {items_in_cart}")

# Завдання 2
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Практичне завдання
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.

class Student:

    def __init__(self, name: str, specialization: str, grades: List[int] ):
        self._name = name
        self._specialization = specialization

        if grades is None:
            self._grades = []
        else:
            self._grades = grades


    def add_grade(self, grade: int):
        self._grades.append(grade)


    def avg_grade(self):
        if len(self._grades) == 0:
            return None
        return sum(self._grades) / len(self._grades)

    def show_info(self):
        print(f"Name: {self._name}")
        print(f"Specialization: {self._specialization}")
        print(f"Average grade: {self.avg_grade()}")

    def save_to_json(self, filename: str = "students.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self._get_state_dict(), file, indent= 4)
            print("Saved to items.json")


    def _get_state_dict(self):
        return {
            'name': self._name,
            'specialization': self._specialization,
            'grades': self._grades
        }

    def _set_state_dict(self, students):
            self._name = students['name']
            self._specialization = students['specialization']
            self._grades = students['grades']

    def load_json(self, filename: str = "students.json"):
        with open(filename, "r") as file:
            students = json.load(file)

        self._set_state_dict(students)


    def save_to_pickle(self, filename: str = "students.pickle"):
        with open(filename, "wb") as file:
            pickle.dump(self._get_state_dict(), file)
        print("Saved to students.pickle")


    def read_pickle(self, filename: str = "students.pickle"):
        with open(filename, "rb") as file:
            students = pickle.load(file)

        self._set_state_dict(students)


student_1 = Student("Alina", "IT", [10, 11, 12, 9])
student_2 = Student("Danilo", "KB", [10, 12,12,12])
student_3 = Student("Alisa", "Management", [9,10,10])

student_3.add_grade(12)
student_1.show_info()
student_2.show_info()
student_3.show_info()

student_1.save_to_json("student_1.json")
student_2.save_to_json("student_2.json")
student_3.save_to_json("student_3.json")

student_1.load_json("student_1.json")
student_2.load_json("student_2.json")
student_3.load_json("student_3.json")

student_1.save_to_pickle("student_1.pickle")
student_2.save_to_pickle("student_2.pickle")
student_3.save_to_pickle("student_3.pickle")

student_1.read_pickle("student_1.pickle")
student_2.read_pickle("student_2.pickle")
student_3.read_pickle("student_3.pickle")

#Add friend

def add_friends(friends: Dict[str, List[str]]):

    friend_1 = input("Enter friend_1 ")
    friend_2 = input("Enter friend_2 ")


    if friend_1 not in friends:
        friends[friend_1] = []

    if friend_2 not in friends:
        friends[friend_2] = []

    friends[friend_2].append(friend_1)
    friends[friend_1].append(friend_2)


def save_to_json(friends: Dict[str, List[str]], filename: str = "friends.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(friends, file, indent=4, ensure_ascii=False)


def load_json(filename:str = "friends.json") -> Dict[str, List[str]]:
    with open(filename, "r", encoding = "utf-8") as file:
        return json.load(file)


def save_to_pickle(friends: Dict[str, List[str]], filename: str = "friends.pickle"):
    with open(filename, "wb") as file:
        pickle.dump(friends, file)


def load_pickle(filename:str = "friends.pickle") -> Dict[str, List[str]]:
    with open(filename, "rb") as file:
        return pickle.load(file)


friends = {}
add_friends(friends)

save_to_json(friends)
loaded_from_json = load_json()
print(f"Loaded from json: {loaded_from_json}")

save_to_pickle(friends)
loaded_from_pickle = load_pickle()
print(f"Loaded from pickle: {loaded_from_pickle}")


# Завдання 1
# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle
