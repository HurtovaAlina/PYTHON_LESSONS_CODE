# Завдання 1
# Є словник з логінами(ключ) та паролями(значення)
# користувачів. Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна паролю
#  вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.

import json
#
# users = {
#     "alina": "qwerty123",
#     "ivan": "password",
#     "admin": "admin123"
# }


def load_users(filename: str = "users.json") -> dict[str, str]:
    with open(filename, "r", encoding="utf-8") as file:
        my_users = json.load(file)
    return my_users


def save_users(users: dict[str, str], filename: str = "users.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii= False)


def add_user(users: dict[str,str]):
    user = input("Enter login ")
    if user in users:
        print("User already exists")
        return

    password = input("Enter password ")

    users[user] = password


def delete_user(users: dict[str,str], user_to_delete: str):
    if user_to_delete in users:
        users.pop(user_to_delete)
    else:
        print(f"User {user_to_delete} was not found")


if __name__ == "__main__":

    users = load_users()

    while True:
        command = int(input("enter command: "))

        if command == 1:
            add_user(users)

        elif command == 2:
            save_users(users)

        elif command == 3:
            user_to_delete = input("Enter user to delete ")
            delete_user(users, user_to_delete)
            save_users(users)

        elif command == 0:
            print("Finish")
            break


# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# save(fiename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за
# замовчуванням cart.json)
# Завдання 3
# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу
# Напишіть код, де завантажується налаштування і
# створюються відповідні змінні size, background_color, …
