# множини
nums = ["apple", "banana", "kiwi"]
nums.append("pear")


# множини
# як добавити новий елемент
# елемент - вираховуєте "номер" використовуючи функцію hash
# добавляєте в комірку з цим номером

# item = 'banana'
# number = hash(item)
#
# print(number)

# перевірка чи є елемент у множині
# вираховуєте "номер" використовуючи функцію hash
# перевіряєте комірку з відповідним номер
# цвидкість перевірки НЕ залежить від кількості елементів в множині


# # # перевірка чи є елемент
# import time
#
#
# N = 10**7
# list1 = list(range(N))
# set1 = set(range(N))
#
# item = 10000
#
# start = time.time()
# if item in list1:
#     pass
# end = time.time()
#
# print(f"Витрачено часу з list: {end - start:.8f}")
#
# start = time.time()
# if item in set1:
#     pass
# end = time.time()
#
# print(f"Витрачено часу з set: {end - start:.8f}")

# # створення
# fruits = {"apple", 'banana', "kiwi"}
#
# nums = [1, 2, 3, 4, 5]
# nums = set(nums)
#
# print(fruits)
# print(nums)
#
# # порожня множина
# empty = {}  # це не множина
# print(type(empty))
#
# empty = set()  # оце порожня множина
# print(type(empty))

# # Ціна швидкість
# # 1. Множина немає порядку
# fruits = {"apple", 'banana', "kiwi"}
# print(fruits)
#
# # fruits[0] # помилка
#
# # 2. Не можна зберігати дублікати
# fruits = {"apple", "apple", "apple", "apple", 'banana', "kiwi"}
# print(fruits)
#
# # видалити дублікати зі списку
# fruits = ["apple", "apple", "apple", "apple", 'banana', "kiwi"]
# print(fruits)
#
# fruits = list(set(fruits))
# print(fruits)
#
# # 3. Не можна добавляти елементи що змінюються
# # Нехешовані типи даних --- незмінні типи даних
# # int float bool str tuple
# # set1 = {"apple", 'kiwi', [1, 2]}


# методи
# fruits = {"apple", 'banana', "kiwi"}
#
# # добавити елемент
# fruits.add("orange")
#
# print(fruits)
#
# fruits.add("banana")  # вже є в мнодині, нічого не станеться
#
# print(fruits)
#
# # видалення
# fruits.discard('apple')
# fruits.remove('banana')
# print(fruits)
#
# # видалення елемента якого немає
# fruits.discard('melon')  # нічого не станеться
# fruits.remove('melon')   # Error
# print(fruits)


# операції з множинами

workers = ["Анна", "Олег", "Ігор", "Олег", "Анна", "Марія", "Сергій", "Олег"]
special_workers = ["Анна", "Ігор", "Вікторія"]  # працівники з особливим доступом

# перевести дані в множини
workers = set(workers)
special_workers = set(special_workers)


# вивести усіх працівників
# об'єднання множин

# all_workers = workers.union(special_workers)
# print(all_workers)
#
# # по іншому
# all_workers = special_workers | workers
# print(all_workers)


# вивести працівників які не мають спеціального доступу
# різниця множин


# no_special_workers = workers.difference(special_workers)
# print(no_special_workers)
#
# # по іншому
# no_special_workers = workers - special_workers
# print(no_special_workers)
#
# # порядок множин важливий
# no_special_workers = special_workers - workers
# print(no_special_workers)


# перетин множин
# елементи які є в обох одночасно
both = workers.intersection(special_workers)
print(both)

both = special_workers & workers
print(both)
