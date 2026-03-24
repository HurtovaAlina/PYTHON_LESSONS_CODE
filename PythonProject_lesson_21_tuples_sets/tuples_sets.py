# кортеж
# функція map

# # набір чисел, користувач вводить числа через кому
#
# user_data = input("Введіть числа через кому: ")
# nums = user_data.split(', ')
#
# # new_nums = []
# # for num in nums:
# #     num = int(num)
# #     new_nums.append(num)
# #
#
# # те саме через функцію map
# # map(func, [послідовність])
# # застосовує функцію func до кожного елемента послідовності
#
# new_nums = map(int, nums)
# new_nums = list(new_nums)
# print(new_nums)
#
# # усе разом в одному рядку(так не робити)
# nums = list(map(int, input("Введіть числа через кому: ").split(', ')))
#
# nums = list(
#     map(
#         int,
#         input("Введіть числа через кому: ").split(', ')
#     )
# )


# кортежі(tuple)
text = "hello"  # послідовність символів
nums = [1, 2, 3, 4]  # послідовність будь-чого

nums = (1, 2, 3, 4)  # кортеж чисел
words = ("apple", "banana")  # кортеж слів

# списки -- змінний тип даних
# кортеж -- незмінний тип даних


def get_statistic():
    count = 5
    average = 10.5

    return count, average  # тут повертається кортеж з двома елементами


my_count, my_average = get_statistic()

result = get_statistic()


data = ("Ukraine", "Kyiv", 32)

# розпаковка кортежа по змінних
# country, capital, size = data
#
# print(f"{country = }")
# print(f"{capital = }")
# print(f"{size = }")


# data = [
#     ("Ukraine", "Kyiv", 32),
#     ("France", "Paris", 52),
#     ("Spain", "Madrid", 40)
# ]
#
# print(len(data[0]))
#
# for country, capital, size in data:
#     print(f"{country = }")
#     print(f"{capital = }")
#     print(f"{size = }")
#
#     print()


# enumerate
# вивести елементи списку разом з індексами

# words = ['apple', 'banana', 'pear', 'cherry', 'orange']
#
# # for i in range(len(words)):
# #     word = words[i]
# #
# #     print(i, word)
#
# for i, word in enumerate(words, start=1):  # вказати що індекси починаються з 1
#     print(i, word)


items = ["хліб", "молоко", "сир"]
prices = [30, 70, 150]
quantities = [1, 1, 0.5]  # кількості товарів


# вивести пари товар-ціна

# for item, price, quantity in zip(items, prices, quantities):
#     print(item, price, quantity)


data = [("Ukraine", "Kyiv", 32), ("France", "Paris", 52), ("Spain", "Madrid", 40)]

# # порахувати загальне насерення
#
# total = 0
# for _, _, size in data:
#     total += size
#
# print(total)

# індекси

words = ("apple", "banana", "pear", "cherry", "orange")

# останій
print(words[-1])

# pear
print(words[2])

# перші 3 слова
print(words[0:3])
print(words[:3])

# останні 3
# print(words[:-3])
print(words[-3:])

# задом наперед
print(words[::-1])
