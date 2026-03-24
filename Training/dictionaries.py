# 1️⃣ Телефонна книга
# Створи словник, де:
# ключ — ім’я людини
# значення — номер телефону
# Завдання:
# додати новий контакт
# знайти номер за ім’ям

#
# phone_book = {
#     "Alina": "+380661844701",
#     "Yurii": "+380504807178",
#     "Danilo": "+380997782210",
#     "Alisa": "+380993599313"
# }
#
# def add_contact(phone_book):
#     new_name = input("Enter name ")
#     new_number = input("Enter number ")
#
#     if new_name not in phone_book:
#         phone_book[new_name] = new_number
#
#     return phone_book
#
# def find_phone_number(phone_book):
#     number_to_find = input("Enter number ")
#     for name, number in phone_book.items():
#         if number == number_to_find:
#             return name
#     print("Phone number was not found")
#
#
# print(add_contact(phone_book))
# print(find_phone_number(phone_book))

# 2️⃣ Кількість літер у слові
# Напиши програму, яка:
# отримує слово від користувача
# рахує скільки разів кожна літера зустрічається

# word = input("Enter word ")
# count_letters = dict()
# for w in word:
#     count_letters[w] = word.count(w)
#
# print(count_letters)

# 3️⃣ Студенти і оцінки
# Створи словник:
# {"Іван": 85, "Марія": 92, "Олег": 74}
# Напиши програму яка:
# знаходить студента з найбільшою оцінкою
# знаходить середній бал

# students = {
#     "Іван": 85,
#     "Марія": 92,
#     "Олег": 74
# }
#
# def best_mark(students):
#     return max(students.values())
#
# def avg_mark(students):
#     return round(sum(students.values())/len(students), 2)
#
# print("Best mark: ", best_mark(students))
# print("Average mark: ", avg_mark(students))


# 4️⃣ Магазин
# Створи словник товарів:
# {"apple": 20, "banana": 15, "milk": 40}
# Завдання:
# користувач вводить товар
# програма показує його ціну
# якщо товару немає → повідомлення
#
# goods = {
#     "apple": 20,
#     "banana": 15,
#     "milk": 40
# }
#
# selected_good = input("Enter good ")
# if selected_good in goods:
#     print(f"You have chosen {selected_good}, with price {goods[selected_good]}")
# else:
#     print("Good was not found")

# 5️⃣ Словник перекладу
# Створи словник перекладу:
# {"cat": "кіт", "dog": "собака", "sun": "сонце"}
# Програма повинна:
# запитати слово англійською
# показати переклад
# якщо слова немає → запропонувати додати

# translations = {
#     "cat": "кіт",
#     "dog": "собака",
#     "sun": "сонце"
# }
#
# word_to_translate = input("Enter word to translate ")
# if word_to_translate in translations:
#     print(f"{word_to_translate}, {translations[word_to_translate]}")
# else:
#     action = input(f"Do you want to add the word {word_to_translate} to translations? Y/N ")
#     if action == "Y" :
#         translation = input(f"Enter translation for {word_to_translate} ")
#         translations[word_to_translate] = translation
#         print(translations)
#     else:
#         print("Finish program")

# 6️⃣ Видалення елементів
# Є словник банку:
# {"Іван": 1500, "Марія": 200, "Олег": 50, "Анна": 3000}
# Завдання:
# видалити клієнтів, у яких менше 500 грн

# bank_accounts = {
#     "Іван": 1500,
#     "Марія": 200,
#     "Олег": 50,
#     "Анна": 3000
# }
# # list(bank_accounts.items()) створює копію елементів, тому можна безпечно змінювати словник.
# for name, amount in list(bank_accounts.items()):
#     if amount < 500:
#         del bank_accounts[name]
#
# print(bank_accounts)


# Порахувати кількість входжень слів.
# Умова:
# Є текст:
# "apple banana apple orange banana apple"
# Потрібно створити словник:
# {
#  "apple": 3,
#  "banana": 2,
#  "orange": 1
# }

# text = "apple banana apple orange banana apple"
# text_to_list = text.split(" ")
# print(text_to_list)
# words_dict = {}
# for word in text_to_list:
#     count = text_to_list.count(word)
#     words_dict[word] = count
#
# print(words_dict)

# Сортування словника
# Умова:
# Є словник:
#
# students = {
#     "Anna": 85,
#     "Ivan": 92,
#     "Oleg": 78
# }
#
# Вивести студентів від більшого бала до меншого.
# Очікуваний результат:
# Ivan 92
# Anna 85
# Oleg 78

# students = {
#     "Anna": 85,
#     "Ivan": 92,
#     "Oleg": 78
# }
#
# sorted_students = dict(sorted(students.items(), key = lambda item: item[1], reverse = True))
# print(sorted_students)

# Завдання рівня Junior (дуже корисне)
#
# Умова:
# Користувач вводить товари і ціну.
# Наприклад:
# apple 10
# banana 15
# milk 20
# stop
#
# Створи словник:
# {
#  "apple": 10,
#  "banana": 15,
#  "milk": 20
# }
# Після введення stop:
# виведи суму всіх товарів
#
# items_dictionary = {
#     "apple": 10,
#     "banana": 15,
#     "milk": 20
# }
#
# while True:
#     item = input("Enter item ").lower()
#
#     if item == "stop":
#         break
#     else:
#         price = float(input("Enter price "))
#         items_dictionary[item] = price
#
# print(items_dictionary)
# print(sum(items_dictionary.values()))
