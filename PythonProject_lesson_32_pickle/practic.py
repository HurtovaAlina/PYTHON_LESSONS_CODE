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
from typing import List


def add_item(items: List[str]) -> None:
    item = input("Enter item ")
    items.append(item)
    print(f"Item {item} was added")


def items_output(items: List[str]):
    print("Items list:")
    for item in items:
        print(item)

def save_to_json(items:List[str]) -> None:
    with open("items.json", "w", encoding="utf-8") as file:
        json.dump(items, file)
        print("Saved to items.json")


def read_from_json() -> List[str] | None:
    with open("items.json", "r", encoding="utf-8") as file:
        return json.load(file)



def save_to_picle(items:List[str]) -> None:
    with open("items.pickle", "wb") as file:
        pickle.dump(items, file)
        print("Saved to items.pickle")


def read_from_pickle() -> List[str] | None:
    with open("items.pickle", "rb") as file:
        return pickle.load(file)



if __name__ == "__main__":

    items = []
    for i in range(1,4):
        add_item(items)

    items_output(items)

    save_to_json(items)
    items_in_cart = read_from_json()
    print(f"Items from json {items_in_cart}")

    save_to_picle(items)
    items_in_order = read_from_pickle()
    print(f"Items from pickle {items_in_cart}")
