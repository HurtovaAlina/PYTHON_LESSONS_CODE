# # дз
# nums1 = [1, 2, 3]
# nums2 = [1, 2, 3]
#
# print(nums1 == nums2)  # чи однакові значення
# print(nums1 is nums2)  # чи це один і той самий об'єкт
#
# nums1.append(10)
#
# print(nums1)
# print(nums2)
#
# nums1 = nums2
#
# print(nums1 == nums2)
# print(nums1 is nums2)


# словники

# # є список товарів та їхні ціни. треба по назві товару отримати ціну
#
# items = ['хліб', 'яблуко']
# prices = [30, 65]
#
# user_item = 'яблуко'
#
# # є список клієнтів банку та їхні рахунки. Потрібно поповнити баланс клієнту
#
# clients = ['Mary', "John"]
# balances = [1000, 800]
#
# client = "John"
# add = 300
#
#
# # в словниках можна зберігати дані парами(без індекси)
# # ключ: значення
#
# # словник для банку
# # клієнт: баланс на рахунку
#
# data = {
#     'Mary': 1000,
#     "John": 800,
# }
#
# # бананс у Mary
# client = "Mary"
#
# # отримати значення маючи ключ
# # словник[ключ]
#
# balance = data[client]
#
# print(balance)
#
# data["John"] += 300
#
# print(data["Mary"])
# print(data["John"])

# # ключ: значення
# # значення може бути будь-що
#
# data = {
#     "key1": 10,
#     "key2": "text",
#     "key3": [1, 2, 3, 4],
#     "key4": {}
# }
#
# # ключі зберігаються в "множини",
# # наслідок1, неможе бути дублікатів
#
# data = {
#     "John": 10,
#     "Mary": 20,
#     "John": 30
# }
#
# print(data)
#
# # наслідок2, немає порядку*
# # в деяких версія пайтон наче порядок є(але це не точно)
#
#
# # наслідок3, ключі хешуються, не можна використовувати
# # змінні типи даних
# # list, set, dict
#
# # data = {
# #     [1, 2]: "text"
# # }
#
# data = {
#     "text": [1, 2]
# }
#
# print(data)


data = {"хліб": 30, "яблуко": 65}

# # отримати занчення за ключем
# print(data['хліб'])
# # print(data['молоко'])  # error

# # змінити значення за ключем
# print(data)
#
# data['хліб'] = 35
# print(data)
#
# data['яблуко'] -= 10
# print(data)
#
# data['яблуко'] *= 1.1
# print(data)

# # добавити нову пару
# data['молоко'] = 80
#
# print(data)
#
# # видалити пару
# data.pop('хліб')
# print(data)

# # в циклі for пройтись по ключах словника
#
# data = {
#     'хліб': 30,
#     'яблуко': 65
# }
#
# for key in data:
#     price = data[key]
#     print(key)
#
#
# # отримати лише занчення
# for price in data.values():
#     print(price)
#
# # отримати пару ключ значення
# counter = 0
# for item, price in data.items():
#     print(item, price)
#     counter += 1
#
#     if counter == 5:
#         break


# # перевірка чи ключ є в словнику
# if 'молоко' in data:
#     print(f"yes")
# else:
#     print("no")


# напишуть функцію яка створює словник з інформацією про працівника
# (ім'я, зарплата, досвід)
# напишуть функцію яка створює список з інформацією про співробітників
# напишіть функцію яка збільшить зарплату працівникам які працюють більше 2 років


def create_worker_info():
    worker_info = {}  # порожній словник

    worker_info["name"] = input("Введіть ім'я: ")
    worker_info["salary"] = int(input("Введіть зарплату: "))
    worker_info["exp"] = int(input("Введіть досвід роботу: "))

    return worker_info


def create_workers(worker_num=3):
    workers = []

    for i in range(worker_num):
        worker = create_worker_info()
        workers.append(worker)

    return workers


def increase_salary(workers, bonus, min_exp=2):
    for worker in workers:
        # перевірити чи достатньо досвіду
        if worker["exp"] > min_exp:
            worker["salary"] += bonus


workers = create_workers(worker_num=3)
increase_salary(workers, bonus=250)

# для красивого print
import json

print(workers)
print(json.dumps(workers, indent=2))
