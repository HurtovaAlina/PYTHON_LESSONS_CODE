# документація

# функція яка формує привітання для користувача
def get_greeting(name: str, age: int) -> str | None:
    """
    Формує та повертає привітання для користувача

    Warning:
        Якщо параметри неправильні:
         * недодатній вік
         * пусте ім'я
         * ім'я не з великої літери
        То функція виведе попередження та поверне None

    :param name: str ім'я користувача
    :param age: int вік користувача
    :return: str фраза з привітанням
    """ # docstring

    # перевірки
    if age <= 0:
        print("[WARNING] Вік має бути дадатнім")
        return None # кінець функції

    if name == '':
        print("[WARNING] Ім'я не може бути пустим")
        return None

    if not name.istitle():
        print("[WARNING] Перша літера має бути великою")
        return None

    # основний код
    greeting = f"Hello, {name} {age}yrs. Welcome"

    return greeting


# отримати документації
# help(get_greeting)
#
# help(print)


# функція яка вітається з користувачами
def greet_users(users: list):
    """
    Виводить привітання для кожного користувача зі списку

    див. get_greeting
    :param users: list[list] -- список користувачів у форматі [ім'я, вік]
    """

    for user in users:
        name = user[0] # name
        age = user[1] # age

        greeting = get_greeting(name, age)

        # перевірка
        if greeting:  # не None
            print(greeting)


# users = [
#     ["John", 46],
#     ["Sophie", 35],
#     ["Mary", 31],
#     ["Mike", 28],
#     ["jhkhjk", -10]
# ]
#
# greet_users(users)

