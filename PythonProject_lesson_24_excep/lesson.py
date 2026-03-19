# винятки

# # data = {"Jhon": 22, "Mary": 23}
# # data[0]
#
# #1 + 'John'
# user_input = int('John')
#
# res = 1 / 0

# def get_num():
#     user_input = input("Введіть число: ")
#
#     if user_input.isdigit():  # не пропустить -10  12.14
#         num = float(user_input)
#         return num
#     return None
#
#
# def print_num():
#     num = get_num()
#
#     if num is not None:
#         print(num)
#
#
# def main():
#     print_num()
#
#
# main()


# # try  except
#
#
# try:
#     # код де може відбутись помилка
#     print("Починаємо try")
#     num = float(input("Введіть число: "))
#
#     res = 1 / num
#
#     print(f"Ви ввели {num}")
#     print(res)
#
# except ValueError:
#     print("Ви ввели не число")
#
# except ZeroDivisionError:
#     print("Не можна вводити 0")
#
# except Exception:  # якщо станеться будь-яка помилка
#     print("ПОМИЛКА")
#
#
# print("Кінець програми")



# # функція яка просить у користувача число
#
# def get_num():
#     while True:
#         try:
#             num = float(input("Введіть число: "))
#
#         except ValueError:
#             print("Ви ввели не число")
#             continue
#
#         if num < 0:
#             print("Число не може бути від'ємним")
#             continue
#
#         return num
#
#
#
# number = get_num()
# print(number)



# # Напишіть функцію, яка приймає список чисел і
# # повертає їхнє середнє арифметичне.
# # Обробіть можливий виняток, коли список порожній.
#
# def get_average(nums):
#     """
#     Рахує середнє значення зі списку чисел
#
#     :param nums: list[int|float]
#     :return: float
#     """
#
#     total = sum(nums)
#     count = len(nums)
#
#     return total / count
#
#
# # запускаємо функцію в try
#
# try:
#     nums = [1, 2, 3]
#     average = get_average(nums)
#     print(f"average = {average}")
#
# except ZeroDivisionError:
#     print("Список не повенен бути порожній")
#
# except TypeError:
#     print("Треба передавати список")



# виклик винятків у функціях
# функція що запитує ім'я

def get_name():
    """
    Запитує ім'я в користувача.

    Якщо корустувач введе не літери або користувач введе порожній рядок
    то викличе ValueError

    :return: str
    """

    name = input("Введіть ім'я: ")

    if name == '':
        # виклик помилки
        raise ValueError("користувач ввів порожній рядок")

    if not name.isalpha():
        raise ValueError("користувач ввів не літери")

    return name



# перехоплення помилки

while True:
    try:
        user_name = get_name()
        print(f"Hello {user_name}")

    except ValueError as err:
        # err -- це конкретна помилка з повідомленням
        print(f"ПОМИЛКА: {err}")
