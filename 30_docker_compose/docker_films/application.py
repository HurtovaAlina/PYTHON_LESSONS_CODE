from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel
import json
from settings import settings

app = FastAPI()



class Films(BaseModel):
    id : int
    title : str
    director : str
    year : int

@app.get("/movies")
def get_all_films()-> List[Films]:
    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)
        return films

@app.get("/movies/{movie_id}")
def get_film(movie_id: int):
    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)
    for film in films:
        if film["id"] == movie_id:
            return film

@app.post("/movies")
def add_film(film: Films) -> Dict[str, str]:
    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)
    if len(films) <= settings.max_films:
        films.append(film.model_dump())
    else:
        return {"message": "Max films limit reached"}

    with open(settings.data_file_path, "w") as file:
        json.dump(films, file, indent=4)

    return {"message": "Film was added"}

@app.delete("/movies/{movie_id}")
def delete_film(movie_id: int):
    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)

    for film in films:
        if film["id"] == movie_id:
            films.remove(film)
            break

    with open(settings.data_file_path, "w", encoding="utf-8") as file:
        json.dump(films, file, indent=4)

    return {"message": "Film was deleted"}
