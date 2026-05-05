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

import pickle
import json
from typing import Dict

music_groups: Dict[str, list] = {}

def add_group(music_groups: Dict[str, list], group: str) :
    if group not in music_groups:
        music_groups[group] = []
    else:
        raise KeyError(f"{group} already exists")


def add_album(music_groups: Dict[str, list], group: str, album: str) :
    if group not in music_groups:
        raise KeyError(f"{group} not found")

    if album in music_groups[group]:
        raise ValueError(f"{album} already exists")

    music_groups[group].append(album)


def save_to_json(file_name: str, music_groups: Dict[str, list]):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(music_groups, file, indent=2)
    print("Saved to json")


def save_to_pickle(file_name: str, music_groups: Dict[str, list]):
    with open(file_name, "wb") as file:
        pickle.dump(music_groups,file)
    print("Saved to pickle")


def load_from_json(file_name: str) -> Dict[str, list]:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            music_groups = json.load(file)
        return music_groups if music_groups is not None else {}
    except FileNotFoundError:
        return {}

def load_from_pickle(file_name: str) -> Dict[str, list]:
    try:
        with open(file_name, "rb") as file:
            music_groups = pickle.load(file)
        return music_groups if music_groups is not None else {}
    except FileNotFoundError:
        return {}


for _ in range(3):
    group = input("Enter group name ")

    try:
        add_group(music_groups, group)
    except KeyError as error:
        print(error)
        continue

    qty_of_albums = int(input(f"Enter qty of albums you want to add to the {group} "))
    for _ in range(qty_of_albums):
        album = input("Enter album ")
        try:
            add_album(music_groups, group, album)
        except ValueError as error:
            print(error)



save_to_json("music_groups.json", music_groups)
save_to_pickle("music_groups.pickle", music_groups)

print("Loading from json...")
music_groups_json = load_from_json("music_groups.json")
print(music_groups_json)

print("Loading from pickle...")
music_groups_pickle = load_from_pickle("music_groups.pickle")
print(music_groups_pickle)
