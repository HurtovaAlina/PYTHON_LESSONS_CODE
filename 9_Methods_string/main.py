# Завдання 1
# Користувач вводить текст і набір символів. Видаліть з тексту всі
# слова, що містять хоча б один з цих символів, і виведіть результат.

# text = input("Enter text: ").lower()
# chars = input("Enter some chars to delete separated by spaces: ").lower()
# l = list()
# new_list = list()
# word = ""
# chars_to_delete = chars.replace(" ", "")
#
# for i in text:
#     if i not in " .,:;:!-—":
#         word += i
#     else:
#         if word != "":
#             l.append(word)
#             word = ""
# print(l)
# for element in l:
#     to_delete = False
#     for i in element:
#         if i in chars_to_delete:
#             to_delete = True
#             break
#     if not to_delete:
#         new_list.append(element)
# print(new_list)
# print(" ".join(new_list))


# Завдання 2
# Створіть програму, яка із введеного тексту створює "зворотний текст"
# (перевертає текст на рівні слів, а не символів). Наприклад, "я люблю Python"
# перетворюється на "Python люблю я"

# text = input("Enter text: ").lower().split()
# print(" ".join(text[::-1]).capitalize())

# Завдання 3
# Напиши програму, яка читає з консолі 1 рядок і визначає, чи є він валідним ідентифікатором змінної,
# валідний ідентифікатор має правила:
#
# Перший символ це латинська літера A-Z або a-z або символ підкреслення _
# Далі можуть бути латинські літери, цифри або _
# Довжина від 1 до 20 символів включно
#
# Треба вивести:
# OK якщо рядок валідний
# NO якщо невалідний
#
# Приклади
# Валідні:
# name
# _temp
# user1
# A
# var_20
# Невалідні:
# 1user (починається з цифри)
# my-name (дефіс не дозволений)
# hello world (пробіл)
# `` (порожній рядок)
# this_identifier_is_too_long (довше 20)

# rule = r"^[A-Za-z_]\w{0,19}$"
# s = input("Enter string ")
# is_correct = re.fullmatch(rule, s)
# if is_correct:
#      print("OK")
# else:
#     print("No")
