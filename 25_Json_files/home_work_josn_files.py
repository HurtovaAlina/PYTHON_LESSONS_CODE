# Завдання 1
# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями


import random
from typing import Dict
import json


DATA_FILE: str = "game_stats.txt"


def generate_secret_number() -> int:
    """
    Генерує випадкове число від 1 до 100.
    :return: int - загадане комп'ютером число
    """
    return random.randint(1, 100)


def play_game(secret_number: int, max_attempts: int = 5) -> bool:
    """
    Запускає один раунд гри "Вгадай число".

    Користувач вводить числа, а програма підказує
    "більше" або "менше".

    :param secret_number: int - число, яке потрібно вгадати
    :param max_attempts: int - максимальна кількість спроб
    :return: bool - True, якщо користувач переміг, False якщо програв
    """

    print("Guess the number")
    attempt = 0

    while max_attempts > attempt:
        number = int(input("Enter number from 1 to 100 "))
        if number == secret_number:
            print("You've  guessed!!!!")
            return True
        else:
            if number > secret_number:
                print("Your number is greater than secret")
            else:
                print("Your number is less than secret")
            attempt+=1
            if attempt < max_attempts:
                print("Try one more time")
    print("Your attempts ran out")
    return False


def start_new_game(wins: int, losses: int) -> Dict[str, int]:
    """
    Починає нову гру та оновлює статистику.

    :param wins: int - поточна кількість перемог
    :param losses: int - поточна кількість програшів
    :return: Dict[str, int] - оновлені перемоги та програші
    """

    game_results = {}
    games_qty = int(input("How many games do you want to play? "))
    for _ in range (1, games_qty+1):
        secret_number = generate_secret_number()
        # print(f"cheat :) {secret_number}")
        if play_game(secret_number):
            wins +=1
        else:
            losses+=1
    game_results["wins"]= wins
    game_results["losses"]= losses
    # print(f"Results: {game_results}")
    return game_results


def save_data(game_results: Dict[str, int], filename: str = DATA_FILE) -> None:
    """
    Зберігає статистику у файл.

    :param game_results: Dict[str, int] - словник зі збереженими результатами
    :param filename: str - ім'я файлу для збереження
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(game_results, file,  indent=2)


def load_data(filename: str = DATA_FILE) -> Dict[str, int]:
    """
    Завантажує статистику з файлу.

    :param filename: str - ім'я файлу
    :return: Dict[str, int] - перемоги та програші
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            results = json.load(file)
            return results
    except FileNotFoundError:
        print("File not found")
        return {"wins": 0, "losses": 0}


def main_menu() -> None:
    """
    Головне меню програми.
    """

    print("Starting game")
    generate_secret_number()
    results = start_new_game(0, 0)
    save_data(results)
    print(f"Your results: {load_data()}")


if __name__ == "__main__":
    main_menu()
