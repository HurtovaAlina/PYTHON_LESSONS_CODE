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

#
# def load_users(filename: str = "users.json") -> dict[str, str]:
#     with open(filename, "r", encoding="utf-8") as file:
#         my_users = json.load(file)
#     return my_users
#
#
# def save_users(users: dict[str, str], filename: str = "users.json"):
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(users, file, indent=2, ensure_ascii= False)
#
#
# def add_user(users: dict[str,str]):
#     user = input("Enter login ")
#     if user in users:
#         print("User already exists")
#         return
#
#     password = input("Enter password ")
#
#     users[user] = password
#
#
# def delete_user(users: dict[str,str], user_to_delete: str):
#     if user_to_delete in users:
#         users.pop(user_to_delete)
#     else:
#         print(f"User {user_to_delete} was not found")
#
# def change_password(users: dict[str,str], user: str,  new_password: str):
#     if user in users:
#         users[user] = new_password
#         print("Password was changed")
#
#     else:
#         print(f"User {user} was not found")
#
# def enter_to_system(users: dict[str,str], user: str, password: str):
#     if user in users:
#         if users[user] == password:
#             print("You successfully logged in")
#
#         else:
#             print(f"User was not found")


# if __name__ == "__main__":
    # users = load_users()
    #
    # while True:
    #     command = int(input("enter command: "))
    #
    #     if command == 1:
    #         add_user(users)
    #
    #     elif command == 2:
    #         save_users(users)
    #
    #     elif command == 3:
    #         user_to_delete = input("Enter user to delete ")
    #         delete_user(users, user_to_delete)
    #         save_users(users)
    #
    #     elif command == 4:
    #         user = input("Enter user you want to change password ")
    #         new_password = input("Enter new password ")
    #         change_password(users, user, new_password)
    #         save_users(users)
    #
    #     elif command == 5:
    #         user = input("Enter user you want to enter to system ")
    #         password = input("Enter password ")
    #         enter_to_system(users, user, password)
    #
    #
    #     elif command == 0:
    #         print("Finish")
    #         break


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

class Cart:

    def __init__(self, user: str):
        self._user = user
        self._items: list[str] = []
        self._total: float = 0

    def add_item(self, item: str, price: float):
        if item in self._items:
            print(f"Item {item} already exists")
        else:
            self._items.append(item)
            self._total += price

    def delete_item(self, item: str, price: float):
        if item in self._items:
            self._items.remove(item)
            self._total -= price

        else:
            print(f"Item {item} was not found")

    def info(self):
        print(f"User: {self._user} total: {self._total}")
        print(f"items in the Cart: {self._items}")

    def save_cart(self, filename: str = "cart.json"):
        cart = {
            "user": self._user,
            "total": self._total,
            "items": self._items

                }
        with open(filename, "w") as file:
            json.dump(cart, file, indent=2)

    def load_cart(self, filename: str = "cart.json"):
        with open(filename, "r") as file:
            cart = json.load(file)

        self._user = cart["user"]
        self._total = cart["total"]
        self._items = cart["items"]

cart = Cart("Alina")
for i in range(1,4):
    item = input("Enter item ")
    price = float(input("Enter price "))
    cart.add_item(item, price)

cart.info()
cart.save_cart()
cart.load_cart()


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
