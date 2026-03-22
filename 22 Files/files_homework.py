import re
# Завдання 1
# Є текстовий файл. Запишіть в інший файл таку
# статистику:
#  Кількість символів
#  Кількість рядків
#  Кількість цифр
#  Кількість голосних літер(aeuio)

def count_of_chars(text):
    return len(text.replace("\n", ""))

def count_of_lines(text):
    return text.count("\n") + 1

def count_of_digits(text):
    return sum(1 for char in text if char.isdigit())

def count_of_vowels(text):
    vowels_list = ["a","e","u","i","o"]
    return sum(1 for char in text if char in vowels_list)


with open("text_1.txt", "r") as file:
    text = file.read().lower()

with open("text_staistic.txt", "w") as file:
    file.write(f"Кількість символів: {count_of_chars(text)}\n")
    file.write(f"Кількість рядків: {count_of_lines(text)}\n")
    file.write(f"Кількість цифр: {count_of_digits(text)}\n")
    file.write(f"Кількість голосних літер: {count_of_vowels(text)}\n")


# Завдання 2
# Користувач вводить слово та назву файлу. Виведіть
# кількість цього слова у файлі.

word = input("Enter word ").lower()
file_name = input("Enter file name ")

def text_to_list(text):
    text = text.lower().replace("\n", " ")
    clean_text = re.sub(r"[^\w\s]", "", text)
    return clean_text.split(" ")

def count_of_word(text, word):
    return sum(1 for w in text if w == word)

with open(file_name+".txt", "r") as file:
    text = file.read()
text = text_to_list(text)

print(f"Count of word \"{word}\" = {count_of_word(text, word)}")


# Завдання 3
# Є текстовий файл. Видаліть з нього останній рядок.

with open("text_3.txt", "r") as file:
    text = file.readlines()
text = "".join(text[:-1])

with open("text_3.txt", "w") as file:
    file.write(text)