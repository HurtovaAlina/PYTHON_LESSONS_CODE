# # функція як об'єкт
# age = 15
# text = 'Hello world'
#
#
# def greeting():
#     num = 10
#
#     print("hello")
#
#     return None
#
#
# result = age
# print(result)
#
#
# greeting2 = greeting
# greeting2()
#
# my_print = print
# my_print('hello, world', end='!\n')
#
#
# # print = 'text'
# # print()
#
#
# nums = [1, 2, 3]
# nums.append(1)
#
# name = my_print.__name__
# print(name)
#
#
# # список функцій
#
# nums = [1, 2, 3]
#
# def average(num1, num2):
#     return (num1 + num2) / 2
#
# funcs = [min, max, average]
#
# for func in funcs:
#     result = func(10, 20)
#     print(func.__name__, result)


# функція як аргумент(параметр) іншої функція
# функція яка застосовує іншу функцію до 10, 20

# def apply_func(func):
#     print(f"Використовую {func.__name__}")
#
#     result = func(10, 20)
#     print(result)


# # apply_func(min)
# # apply_func(max)
#
#
# # отримати найкоротше слово зі списку слово
#
# words = ['apple', 'banana', 'cat', 'zone']
#
#
# res = min(words)  # за замовчуванням перше слово за "алфітом"
# print(res)
#
# res = min(words, key=len)  # знайде таке слово word що key(word) найменше
# print(res)
#
#
# # знайти слово в якому найбільше літер a
# def count_a(word):
#     return word.lower().count('a')
#
# res = max(words, key=count_a)
# print(res)


# # lambda функція або анонімна функція
# # def func(param1, param2, ...):
# #      return [result]
#
# # func = lambda param1, param2, ...: [result]
#
# def count_a(word):
#     return word.lower().count('a')
#
# count_a2 = lambda word: word.lower().count('a')
#
# res = max(words, key=lambda word: word.lower().count('a'))
# print(res)
#
#
# func = lambda num: num + 10
# print(func(2))
#
# func = lambda num: num > 10
# print(func(2))
#
# func = lambda num1, num2: (num1 + num2) / 2
# print(func(2, 5))
#
# # фільтрування
# # дістати лише додатні числа зі списку
# #
# nums = [-1, 1, 4, 2, -2, 5, 6, -3, -5]
#
# # filter(функція, послідовність)
#
# positive_nums = filter(lambda num: num > 0, nums)
# positive_nums = list(positive_nums)
# print(positive_nums)


# функція як результат іншої функції


# def get_func(name: str):
#     if name.lower() == 'min':
#         return min
#
#     elif name.lower() == 'max':
#         return max
#
#     return None
#
#
# func = get_func('max')
#
# if func:
#     res = func([12, 123, 4, 8, 45])
#     print(res)


# декоратор
# надає вашій функції певні властовості

# @[декоратор]
# def func(param1, ...):
#   ....

# формально пайтон робить таке
# func = [декоратор](func)


# # надати функції яка отримує одне число властивіть: тепер вона отримує
# # список чисел і застосовується до кожного числа зі списку
#
# def decorator(func):
#     # нова функція з новими властовостями
#     def new_func(nums):  # функція яка працює зі списком
#         new_nums = []
#
#         for num in nums:
#             res = func(num)  # застосовуємо оригінальну фугкцію
#             new_nums.append(res)
#         return new_nums
#
#     return new_func
#
#
#
# @decorator
# def mult2(num):
#     if num < 0:
#         return None
#
#     return num*2
#
# # mult2 = decorator(mult2)
#
#
# @decorator
# def count_a(word):
#     return word.lower().count('a')
#
# # count_a = decorator(count_a)
#
# # res = mult2(10)
# # print(res)
#
# nums = [1, 3, 4, 6, -2, 3]
# res = mult2(nums)  # [2, 6, 8, 12, -4, 6]
# print(res)
#
# words = ['apple', 'banana', 'kiwi', 'pear']
# res = count_a(words)
# print(res)
