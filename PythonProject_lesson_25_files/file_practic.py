# Завдання 1
# Є текстовий файл. Виведіть кількість рядків та кількість
# символів в ньому

with open("text.txt") as file:
    lines = file.readlines()
    print(f"Кількість рядків: {len(lines)}")
total_len = 0
for line in lines:
    # кількість символів у конкретному рядку
    total_len += len(line.strip())
print(f"Кількість символів: {total_len}")


# Завдання 2
# Користувач вводить ім’я та вік. Запишіть їх у файл. Назву
# файлу також вводить користувач(без розширення .txt)

name = input("Enter name ")
age = input("Enter age ")

file_name = input("Enter file name ") + ".txt"

with open(file_name, "w") as f:
    f.write(f"{name}\n")
    f.write(f"{age}\n")

#
# # Завдання 3
# # Є текстовий файл. Запишіть його рядки в інший файл.

with open("text.txt") as file:
    lines = file.readlines()

with open("new_text.txt", "w") as file:
    for line in lines:
        file.write(line)

# Завдання 4
# Користувач вводить літеру та назву файлу. Виведіть усі
# слова з файлу, які починаються на цю літеру.

letter = input("Enter letter ").lower()
file_name = input("Enter file name ").lower() + ".txt"  # "text.txt"

with open(file_name) as file:
    lines = file.readlines()
for line in lines:
    words = line.split()
    for word in words:
        if word.lower().startswith(letter):
            print(word)

# Завдання 5
# Є текстовий файл. Замініть у ньому усі символи * на &, та
# навпаки.

with open("stars.txt") as file:
    text = file.read()
new_text = ""
char_1 = "*"
char_2 = "&"
for char in text:
    if char == char_1:
        new_text += char_2
    elif char == char_2:
        new_text += char_1
    else:
        new_text += char

with open("new_star_file.txt", "w") as file:
    file.write(new_text)


# Завдання 6
# Напишіть функцію, яка отримує назву файлу та список
# чисел як параметри. Потрібно записати всі числа у файл,
# розмістивши кожне число на окремому рядку.
# Напишіть іншу функцію, яка отримує назву файл та читає
# з нього ці числа і повертає як список.


def write_numbers_to_file(file_name, numbers):
    with open(file_name, "w") as file:
        for number in numbers:
            file.write(f"{number}\n")

        return


def print_numbers(file_name):
    with open(file_name) as file:
        numbers = file.readlines()
        numbers_clear = []
        for number in numbers:
            numbers_clear.append(number.strip("\n"))
    return numbers_clear


file_name = input("Enter file name ")
numbers = input("Enter numbers ").split(", ")
write_numbers_to_file(file_name, numbers)
print(print_numbers(file_name))

# Завдання 7
# Є 2 файли, запишіть у третій файл лише ті символи, які є в
# обох файлах одночасно

with open("file_1.txt") as file:
    file_1 = file.read()

with open("file_2.txt") as file:
    file_2 = file.read()

file_1 = "".join(file_1)
file_2 = "".join(file_2)
file_3 = ""
for item in file_1:
    if item.isalpha():
        if item in file_2:
            file_3 += item

with open("file_3.txt", "w") as file:
    file.write(file_3)

# Завдання 8
# Є файл з текстом. Видаліть з нього усі неприйнятні слова.
# Список неприйнятних слів є в іншому файлі.

with open("text_bad_words.txt") as file:
    text = file.read()
    text = text.replace("\n", " ").split()
print(text)

with open("bad_words.txt") as file:
    bad_words = file.read()

bad_words = bad_words.lower().split()
print(bad_words)

with open("text_bad_words.txt", "a") as file:
    for word in text:
        if word.lower() not in bad_words:
            if "." in word:
                word = word + "\n"
            else:
                word = word + " "
            file.write(word)
