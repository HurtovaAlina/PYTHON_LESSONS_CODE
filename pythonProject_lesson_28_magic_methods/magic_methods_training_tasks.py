# Створи клас Book:
# атрибути: title, author
# Реалізуй __str__
from typing import List


class Book:

    def __init__(self, title, author):
        self._title = title
        self._author = author

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}"


book = Book("Гаррі Поттер", "Дж Роулінг")
print(book)

# Створи клас Cart:
# атрибут: список товарів
# Реалізуй __len__

class Cart:

    def __init__(self, items: List[str]):
        self.items = items

    def __len__(self):
        return len(self.items)

cart = Cart(["banana", "apple", "ananas"])
print(f"Items qty: {len(cart)}")

# Створи клас Box:
# атрибут: items_count
# Реалізуй додавання коробок

class Box:

    def __init__(self, items_count: int):
        self.items_count = items_count

    def __add__(self, other):
        if not isinstance(other, Box):
            raise TypeError("Can only add Box to Box")
        return Box(self.items_count + other.items_count)

    def __str__(self):
        return f"Box: {self.items_count} items"

box_1 = Box(3)
box_2 = Box(5)
box_3 = box_1+box_2
print(box_3)

# Клас Student:
# атрибут: grade (оцінка)
# True, якщо оцінки однакові

class Student:

    def __init__(self, grade: int):
        self.grade = grade

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.grade == other.grade

student_1 = Student(4)
student_2 = Student(5)
student_3 = Student(4)

print(student_1==student_2)
print(student_1==student_3)

# Клас Player:
# атрибути: name, level
# True, якщо рівень більший
# Додай перевірку:
# якщо порівнюють не з Player → кинути TypeError

class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __gt__(self, other):
        if not isinstance(other, Player):
            raise TypeError("Cannot compare Player with non-Player")
        else:
            return self.level > other.level

player_1 = Player("Dan", 4)
player_2 = Player("Anna", 3)
print(f"Comparing player_1 > player_2: {player_1 > player_2}")
try:
    print(player_1 >3)
except:
    print("TypeError - you try to compare not obj type")


# Клас Playlist:
# список пісень
# Реалізуй:
# __len__ → кількість пісень
# __add__ → об’єднання двох плейлистів
# __str__ → гарний вивід списку пісень

class Playlist:

    def __init__(self, songs: List[str]):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __add__(self, other):
        return Playlist(self.songs + other.songs)

    def __str__(self):
        return f"Playlist: {self.songs}"

playlist_1 = Playlist(["song_1", "song_2", "song_3"])
playlist_2 = Playlist(["song_4", "song_5", "song_6"])

playlist_3 = playlist_1+playlist_2
print(playlist_3)

# Клас Money:
# amount
# Реалізуй:
# __add__
# __sub__
# __eq__
# __str__
# 👉 щоб можна було:
# m1 + m2
# m1 - m2
# print(m1)
# m1 == m2

class Money:

    def __init__(self, amount: float):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount+other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount

    def __str__(self):
        return f"Money: {self.amount}"

money_1 = Money(300)
money_2 = Money(100)

money_3 = money_1 + money_2
print(money_3)

money_4  = money_1 - money_2
print(money_4)

print(f"Money_1 are equal money_2?  {money_1 == money_2}")
