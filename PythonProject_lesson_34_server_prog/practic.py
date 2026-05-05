# Завдання 1
# Напишіть сервер:
# ● шлях – /hello
# ● метод – POST
# Функція має повертати JSON об’єкт
# {"message": "Привіт з сервера!"}
# Запустіть сервер:
# ● host – localhost
# ● port – 8000
# uvicorn main:app --port 8000 –host localhost --reload
# Напишіть клієнта який робить запит на сервер
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# class HelloResponse(BaseModel):
#     message: str
#
#
# @app.post("/hello")
# def hello() -> HelloResponse:
#     return HelloResponse(
#         message = "Привіт з сервера!",
#     )


# Завдання 2
# Напишіть сервер1:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8000
# Напишіть сервер2:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8001
# Запустіть обида сервери на localhost
# Напишіть клієнта який робить запита на обидва
# сервери

# class HelloResponse(BaseModel):
#     message: str
#
#
# @app.get("/greeting")
# def hello() -> HelloResponse:
#     return HelloResponse(message = "Привіт з сервера1")


# Завдання 4
# Напишіть сервер для симуляції роботи бібліотеки.
# Дані про книги знаходяться у файлі books.json
# Напишіть модель на pydentic для книги з такими
# даними:
# ● id
# ● title
# ● author
# ● year
# ● pages
# Функціонал:
# 1. Отримання всіх книг
# ○ шлях – books
# ○ метод – GET
# 2. Отримання даних за ID книги
# ○ шлях – books/{book_id}
# ○ метод – GET
# 3. Додавання нової книги
# ○ шлях – books
# ○ метод – POST
# 4. Видалення книги за ID
# ○ шлях – books/{book_id}
# ○ метод – DELETE

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int

class BookResponse(BaseModel):
    book_id: int
    book_title: str
    book_author: str
    book_year: int
    book_pages: int

@app.get("/books")
def get_all_books() -> List[Book]:
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)
        return books

@app.get("/books/{book_id}")
def get_book_by_id(id: int):
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)
    for book in books:

        if book["id"]== id:
            return book

@app.post("/books/")
def add_book(book: Book) -> dict[str, str]:
    with open("books.json", "r") as file:
        books = json.load(file)
    books.append(book.model_dump()) # переведе обʼєкт в словник

    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)
    return {"message": "book was added"}
