# 11. Клас Library — бібліотека
# Клас Book: атрибути — назва (str), автор (str).
# Клас Library: атрибут — список книг (list, за замовчуванням порожній).
# Метод add_book(book): додає об'єкт Book до списку.
# Метод remove_book(title): видаляє книгу за назвою. Виводьте повідомлення, якщо
# книгу не знайдено.
# Метод find_book(title): шукає і повертає книгу за назвою (часткове співпадіння).
# Метод show_all(): виводить список усіх книг.
from typing import List

class Book:

    def __init__(self, title:str, author: str):
        self.title = title.lower()
        self.author = author.lower()



class Library:
    def __init__(self):
        self.books: List[Book] = []


    def add_book(self, book:Book):
        for b in self.books:
            if b.title == book.title:
                print("This book is already added")
                return

        self.books.append(book)
        print(f"Book {book.title} of author {book.author} was added")



    def remove_book(self, title):
        for i in range(len(self.books)):
            if title == self.books[i].title:
                removed_book = self.books.pop(i)
                print(f"Book {removed_book.title} was removed")
                return
        print(f"Book {title} was not found")


    def find_book(self, title):
        for book in self.books:
            if title in  book.title:
                print(f"Book {book.title} is found")
                return book

        print(f"Book {title} was not found")
        return None


    def show_all(self):
        if not self.books:
            print("Library is empty")
            return

        for book in self.books:
            print(f" Book {book.title}\n"
                  f"Author {book.author}")


books = Library()

qty_books = int(input("Enter qty of books you want to add "))

for i in range(qty_books):
    title = input("Enter title of book ")
    author = input("Enter author of book ")
    books.add_book(Book(title, author))

books.show_all()
book_to_remove = input("Enter book to remove ").lower()
books.remove_book(book_to_remove)
book_to_find = input("Enter book to fond ").lower()
books.find_book(book_to_find)
books.show_all()


# 12. Клас Team — спортивна команда
# Клас Player: атрибути — ім'я (str), номер (int), позиція (str).
# Клас Team: атрибути — назва команди (str), список гравців (list).
# Методи Team: add_player(player), remove_player(name), find_player(name), show_roster()
# — аналогічно до Library.
# 13. Клас Classroom — клас учнів
# Клас Student: атрибути — ім'я (str), оцінка (float).
# Клас Classroom: список учнів.
# Методи: add_student(), remove_student(name), find_student(name), show_all().
# Метод average_grade(): обчислює і повертає середню оцінку по всьому класу.
