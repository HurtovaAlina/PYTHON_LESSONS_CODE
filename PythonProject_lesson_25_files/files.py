# файли
# # вказуєте шлях до файлу
# filename = "test.txt"  # шукає в тій самій папці
# filename = "tmp/test2.txt"  # шлях до файлу в папці/папках
# # абсолютний шлях до файлу
# filename = "/home/anton-halysh/Programs/Python+AI54/tmp/test2.txt"
#
# # відкрити файл
# file = open("test.txt")
#
# # отримати ввесь вміст
# text = file.read()
#
# print(repr(text))
# print(text)
#
# # закрити файл
# file.close()


# для уникнення проблем з пошкодженням файлу
# рекомендують робити ось так

# except ValuerError as err

# with open(..) as file:
#    [code]

# with open("test.txt") as file:  # file = open("test.txt")
#     text = file.read()
#
# # # ось тут файл безпечно закриється
# # print(text)
#
# # прочитати файл як рядки
#
# with open("test.txt") as file:
#     lines = file.readlines()
#
# # lines -- list[str]
# print(lines)


# записати дані у файл
# mode файла -- для чого відкривати файл
# w -- для запису
# r -- для читання(за замовчуванням)
# a -- для додавання

# про mode w
# якщо файла немає -- тоді він створюється
# якщо файл існує -- тоді попередня інформаціє зникне
# with open("new_file.txt", "w") as file:
#     file.write("hello, world")


# # якщо треба довати новий вміст не видаляючи старий
# with open("new_file1.txt", "a") as file:
#     file.write("\n")  # перехід на новий рядок
#     file.write("some text")


# # видалити перший рядок з файлу
# with open("test.txt", "r") as file:
#     lines = file.readlines()
#
# lines.pop(0)  # видаляєте рядок з індексом 0
# print(lines)
#
# with open("test.txt", "w") as file:
#     file.writelines(lines)


# # user = "Anton"
# # # записувати інформацію у файл через print
# # with open("print_file.txt", "w") as f:
# #     print(f"Hello1 {user}", file=f)
# #     print(f"Hello2 {user}", file=f)
# #     print(f"Hello3 {user}", file=f)
#
# user = "Anton"
# # проблема з українською
# # рекомендується вказувати кодування UTF-8
# with open("ua_file.txt", "w", encoding="UTF-8") as f:
#     print(f"Привіт {user}", file=f)
#
#
# with open("ua_file.txt", "r", encoding="UTF-8") as f:
#     text = f.read()
# print(text)


# користувач вводить назву файлу. Вивести такі дані
# кількість символів
# кількість рядків
# кількість букв h
# збережіть статистику у новий файл

# print_file.txt

# # користувач вводить назву файлу
# filename = input("Введіть назву файлу: ")
#
# # читаємо вміст файлу
# with open(filename, "r") as file:
#     # читаємо як рядки
#     lines = file.readlines()
#
# # кількість символів
# total_len = 0
# for line in lines:
#     # кількість символів у конкретному рядку
#     total_len += len(line)
#
# # кількість рядків
# line_count = len(lines)
#
# # кількість букв h
# count_h = 0
# for line in lines:
#     # кількість символів h у конкретному рядку
#     count_h += line.lower().count('h')


# зберегти статистику у файлі
# назва файлу
# name.txt -> name_statistic.txt
# filename = name.txt

# print_file.txt
# print_file_statistic.txt

# output_filename = filename[:-4] + "_statistic.txt"
#
# with open(output_filename, "w", encoding="UTF-8") as file:
#     print(f"кількість символів {total_len = }", file=file)
#     print(f"{line_count = }", file=file)
#     print(f"{count_h = }", file=file)


# все те саме через read()

filename = "print_file.txt"
with open(filename) as file:
    # читаємо як суцільний текст
    text = file.read()

print(repr(text))

# кількість символів
total_len = len(text)
print(total_len)

# кількість рядків
count_lines = text.count("\n")
print(count_lines)

# кількість букв h
count_h = text.lower().count("h")
print(count_h)
