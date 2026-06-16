# 1. Клас Student — інформація про студента
# Атрибути: ім'я (str), вік (int), середній бал (float).
# Метод display(): виводить усі дані про студента у зручному форматі.
# Метод update_grade(new_grade): приймає нове значення балу і оновлює атрибут.
# Перевіряйте, що бал у межах 0–100.
# 2. Клас Book — книга
# Атрибути: назва (str), автор (str), кількість сторінок (int).
# Метод display(): виводить назву, автора та кількість сторінок.
# Метод update_pages(n): оновлює кількість сторінок. Перевіряйте, що n > 0.

# 3. Клас Dog — собака
# Атрибути: кличка (str), порода (str), вік у роках (int).
# Метод display(): виводить усі дані про собаку.
# Метод birthday(): збільшує вік на 1 рік і виводить привітання.

class Dog:

    def __init__(self, name: str, breed: str, age:int):
        if age <= 0:
            raise ValueError("Age must be greater than 0")

        self.name =  name
        self.breed = breed
        self.age = age

    def display(self):
        print(f"Dog: \n"
              f"Name: {self.name}\n"
              f"Breed: {self.breed}\n"
              f"Age: {self.age}")

    def birthday(self):
        self.age+=1
        print(f"Happy birthday! You are {self.age} years old!")

dog = Dog("Lucky", "jack-rassel", 3)
dog.display()
dog.birthday()


# 4. Клас Product — товар
# Атрибути: назва (str), ціна (float), кількість на складі (int).
# Метод display(): виводить повну інформацію про товар.
# Метод set_price(new_price): оновлює ціну. Ціна не може бути від'ємною.
# Метод restock(amount): додає кількість одиниць на склад.
# 5. Клас Movie — фільм
# Атрибути: назва (str), жанр (str), рейтинг (float, від 0 до 10).
# Метод display(): виводить усі дані про фільм.
# Метод update_rating(r): оновлює рейтинг. Перевіряйте діапазон 0–10.
