

from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from settings import settings

app = FastAPI()


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
    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        books = json.load(file)
        return books

@app.get("/books/{book_id}")
def get_book_by_id(id: int):
    with open( settings.data_file_path, "r", encoding="utf-8") as file:
        books = json.load(file)
    for book in books:

        if book["id"]== id:
            return book

@app.post("/books/")
def add_book(book: Book) -> dict[str, str]:
    with open(settings.data_file_path, "r") as file:
        books = json.load(file)
        books_qty = len(books)
    if settings.max_books is not None and settings.max_books < books_qty:
        books.append(book.model_dump()) # переведе обʼєкт в словник
    else:
        raise HTTPException(
            status_code=409,
            detail=f"Maximum number of books is {settings.max_books}")

    with open(settings.data_file_path, "w") as file:
        json.dump(books, file, indent=4)
    return {"message": "book was added"}

@app.get("/select/{author}")
def get_book_by_author(author: str):
    with open( settings.data_file_path, "r", encoding="utf-8") as file:
        books = json.load(file)
    for book in books:
        if book["author"]== author:
            return book
