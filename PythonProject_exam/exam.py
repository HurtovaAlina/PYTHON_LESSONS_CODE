from datetime import datetime
import random
from typing import List, Dict


# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.
#
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
start = min(num1, num2)
end = max(num1, num2)

s = 0

for i in range(start+1, end): # range between start and end doesn't include start and end nums
    s += i

print(f"Summ of range between {start} and {end} = {s}")



# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

s = 0

for i in range(2, 101,2):
    if i % 2 ==0:
        s+=i

print(f"Sum of evens  = {s}")


# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

text = input("Enter string ")

for letter in text:
    print(letter)

# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

list_of_numbers = [random.randint(1, 100) for n in range(20)]
print(f"List of random  numbers {list_of_numbers}")
new_list = []

for number in list_of_numbers:
    if number % 2 ==0:
        new_list.append(number)

print(f"List with evens = {new_list}")

# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

line = input("Enter strings separated by comma: ").split(",")

def find_uppers(list: list)-> list:
    list_of_uppers = []

    for word in list:
        if word[0].isupper():
            list_of_uppers.append(word)
    return list_of_uppers

print(f"List of titles {find_uppers(line)}")


# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

line = input("Enter strings separated by comma: ").split(",")

def find_word(line:list, word:str) -> list:
    return [w for w in line if word in w]

print(find_word(line, "Python"))


# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.

def create_dict() -> Dict[str, str]:
    return {}

def show_dict(dict: Dict[str, str]):
    print("\nYour dictionary:")
    for key, value in dict.items():
        print(f"{key}: {value}")


def add_to_dict(dict:Dict[str, str], key:str, value:str)-> Dict[str, str]:
    dict[key] = value
    return dict

def remove_dict(dict:Dict[str, str], key:str)-> Dict[str, str]:
    if key in dictionary:
        dict.pop(key)
        print(f"{key} removed")
    else:
        print(f"{key} not found")
    return dict

def find_dict(dict:Dict[str, str], key_to_find:str)-> Dict[str, str]:
    if key_to_find in dict:
        return dict[key_to_find]
    else:
        return "Word not found"

dictionary = create_dict()
qty_of_records = int(input("Enter qty of records do you want to create "))

for i in range(qty_of_records):
    key = input("Enter key: ")
    value = input("Enter value: ")
    add_to_dict(dictionary, key, value)

show_dict(dictionary)

find_dict(dictionary, "key1")
remove_dict(dictionary, "key2")

show_dict(dictionary)

# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1,
# 3), (3, 2), (2, 1)]).
#
numbers = [(1, 3), (3, 2), (2, 1)]

result = sorted(numbers, key=lambda x: x[1])

print(result)

# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з певною назвою та URL.
# Додайте можливість створювати нові сторінки для сайту, вводячи заголовок та вміст.
# Реалізуйте  функцію для видалення сторінок з сайту.
# Включіть функцію для відображення всієї інформації про сайт, включаючи  список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
# Додаткові можливості (за бажанням на кристалики):
# Реалізуйте систему логіну/реєстрації для керування
# сайтом. Додайте можливість редагування існуючих сторінок.
# Створіть функціонал для пошуку сторінок за ключовими
# словами у заголовку або вмісті.

class WebPage:

    def __init__(self, title: str, content: str, date: str):
        self.title = title
        self.content = content
        self.date = date

    def show_page(self):
        print(f"Page name: {self.title}\n"
              f"Content: {self.content}\n"
              f"Date: {self.date}"
              )


class WebSite:

    def __init__(self, name:str, url:str):
        self.name = name
        self.url = url
        self.pages:List[WebPage] = []

    def add_page(self, page:WebPage):
        for p in self.pages:
            if p.title == page.title:
                print("Page is already on the WebSite")
                return
        self.pages.append(page)
        print("New page was added")


    def remove_page(self, title: str):
        for i in range(len(self.pages)):
            if self.pages[i].title == title:
                removed_page = self.pages.pop(i)
                print(f"Page {removed_page.title} was removed")
                return

        print("Page was not found")

    def edit_page(self, title:str, updated_content:str):
        for page in self.pages:
            if page.title == title:
                page.content = updated_content
                print("Page was updated")
                return

        print("Page was not found")

    def find_page(self, key_word:str) -> WebPage | None:
        key_word = key_word.lower()
        for page in self.pages:
            if key_word in page.title.lower() or key_word in page.content.lower():
                return page

        print("Page was not found")
        return None

    def _show_pages(self):
        for page in self.pages:
            print(f"Title: {page.title}\n"
                  f"Content: {page.content}\n"
                  f"Date: {page.date}")


    def show_website_info(self):
        print("Website info")
        print(f"Web site: {self.name}\n"
              f"URL: {self.url}\n"
              f"Pages: ")
        self._show_pages()

def main() -> None:
    web_site = None

    while True:
        action = input("Enter action "
            "\n1 - Create site\n"
            "2 - Add page\n"
            "3 - Remove page\n"
            "4 - Show all info about website\n"
            "5 - Edit page content\n"
            "6 - Find page\n"
            "0 - Exit\n")

        if action == "1":
            site_name = input("Enter site name ").lower()
            url = input("Enter site url ").lower()
            web_site = WebSite(site_name, url)

        elif action == "2":
            if web_site:
                title = input("Enter title ")
                content = input("Enter content ")
                date = datetime.now().strftime("%d.%m.%Y %H:%M")

                page = WebPage(title, content, date)
                web_site.add_page(page)

            else:
                print("You need to create site, before creating pages")

        elif action == "3":
            if  web_site:
                title_to_remove = input("Enter title of the page to remove ")
                web_site.remove_page(title_to_remove)

            else:
                print("You need to create site with pages, before removing pages")


        elif action == "4":
            if web_site:
                web_site.show_website_info()
            else:
                print("Website was not created")

        elif action == "5":
            if web_site:
                title = input("Enter title of the page you want to update ")
                content_to_update = input("Enter new content")
                web_site.edit_page(title, content_to_update)

            else:
                print("Website was not created")

        elif action == "6":
            if web_site:
                key_word = input("Enter key word to find page ")
                page = web_site.find_page(key_word)

                if page:
                    page.show_page()

            else:
                print("Website was not created")

        elif action == "0":
            print("Program is finished")
            break
        else:
            print("Action is not allowed")

main()
