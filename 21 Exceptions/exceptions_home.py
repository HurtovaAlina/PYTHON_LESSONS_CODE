# Завдання 1
# Напишіть функцію, яка запитує користувача пароль та
# повертає його. Якщо пароль поганий, тобто менше 8 символів
# чи містить однакові символи то викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.


def check_password():
    password = input("Enter password ")
    password_without_repeated_chars = set(password)

    if password == "":
        raise ValueError("Password can not be empty")

    if len(password) < 8:
        raise ValueError("Password must be no less 8 chars length")

    if len(password) != len(password_without_repeated_chars):
        raise ValueError("Password can not have repeated chars")

    return password


try:
    print(check_password())

except ValueError as error:
    print("Value error:", error)


# Завдання 2
# Є словник де ключ – логін, а значення – пароль. Напишіть
# функцію, яка запитує користувача логін та пароль. Якщо
# логіна немає в словнику, або невірний пароль, то викликати
# ValueError.
# Написати код try … except який використовує дану
# функцію.


def ask_login_password(credentials):
    login = input("Enter login ")

    if login == "":
        raise ValueError("Login can not be empty")

    if login not in credentials:
        raise ValueError("Login was not found")

    password = input("Enter password ")

    if password == "":
        raise ValueError("Password can not be empty")

    if credentials[login] != password:
        raise ValueError("Wrong password")

    return login, password


credentials = {"admin": "1234QWERTY", "user": "QAZ12345", "support": "poiu345"}

try:
    login, password = ask_login_password(credentials)
    print(f"Credentials: login = {login}, password = {password}")

except ValueError as error:
    print("Value Error ", error)
