# Завдання 1
# Напишіть сервер для збереження даних про фільми.
# Дані знаходяться у файлі films.json
# Напишіть модель на pydentic з такими даними:
# ● id
# ● title
# ● director
# ● year
# Функціонал:
# 1. Отримання даних за ID фільму
# ○ шлях – movies/{movie_id}
# ○ метод – GET
# 2. Додавання нового фільму
# ○ шлях – movies
# ○ метод – POST
# 3. Видалення фільму за ID
# ○ шлях – movies/{movie_id}
# ○ метод – DELETE
# Запустіть сервер
# Напишіть клієнта з таким фуннкціоналом для
# користувача:
# ● отримати дані про фільм
# ● додати новий фільм
# ● видалити фільм
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()



class Films(BaseModel):
    id : int
    title : str
    director : str
    year : int

@app.get("/movies")
def get_all_films()-> List[Films]:
    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)
        return films

@app.get("/movies/{movie_id}")
def get_film(movie_id: int):
    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)
    for film in films:
        if film["id"] == movie_id:
            return film

@app.post("/movies")
def add_film(film: Films) -> Dict[str, str]:
    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)

    films.append(film.model_dump())

    with open("films.json", "w") as file:
        json.dump(films, file, indent=4)

    return {"message": "Film was added"}

@app.delete("/movies/{movie_id}")
def delete_film(movie_id: int):
    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)

    for film in films:
        if film["id"] == movie_id:
            films.remove(film)
            break

    with open("films.json", "w", encoding="utf-8") as file:
        json.dump(films, file, indent=4)

    return {"message": "Film was deleted"}
