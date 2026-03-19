# nums = [-3, -1, 0, 2, 5, 6, 7, 8]
# # Потрібно:
# # залишити невід’ємні (>= 0)
# # залишити тільки кратні 2
# # помножити кожне число на 10
#
# def not_negative(i):
#     return i >= 0
#
# def evens(i):
#     return i % 2 == 0
#
# def multiplier(i):
#     return i*10
#
# steps = [("filter", not_negative),("filter", evens),("map", multiplier)]
#
# def pipeline(nums, steps):
#     numbers = nums
#     summary = []
#     for step_type, func in steps:
#         if step_type == "filter":
#             numbers = list(filter(func, numbers))
#             summary.append(numbers)
#         if step_type == "map":
#             numbers = list(map(func, numbers))
#             summary.append(numbers)
#     return summary
#
# not_negatives, only_evens, mult = pipeline(nums, steps)
# print("Not negatives ", not_negatives)
# print("Only evens ", only_evens)
# print("Multiplied ", mult)



# Вимоги:
#
# Залишити тільки додатні числа (> 0)
# Залишити тільки ті, що кратні 3
# Піднести кожне число до куба

# Потрібно:
#
# створити функції-трансформації
# створити apply_pipeline(data, steps)
# steps — список кортежів ("filter", func) / ("map", func)
# пайплайн має бути:
# positive → divisible by 3 → cube
# повернути проміжні результати
# після позитивних: [5, 9, 12, 8, 3, 15]
# після кратних 3:  [9, 12, 3, 15]
# після куба:      [729, 1728, 27, 3375]

# nums = [0, -4, 5, 9, 12, -7, 8, 3, 15]
#
# def positive_numbers(i):
#     return  i > 0
#
# def div_by_3(i):
#     return i % 3 ==0
#
# def cube(i):
#     return pow(i,3)
#
# steps = [("filter", positive_numbers),("filter", div_by_3),("map", cube)]
#
# def apply_pipeline(nums, steps):
#     numbers = nums
#     summary = []
#     for step_type, func in steps:
#         if step_type == "filter":
#             numbers = list(filter(func, numbers))
#             summary.append(numbers)
#         elif step_type == "map":
#             numbers = list(map(func, numbers))
#             summary.append(numbers)
#     return summary
#
# positives, divided_3, cubes = apply_pipeline(nums,steps)
# print("Positives ", positives)
# print("Divided by 3 ", divided_3)
# print("Cubes ", cubes)

# Кроки:
#
# залишити тільки числа > 0
# залишити тільки непарні
# помножити кожне число на 2

# nums = [-10, -3, 0, 4, 7, 8, 15]
#
# def positives(i):
#     return i > 0
#
# def odds(i):
#     return i % 2 !=0
#
# def mult(i):
#     return i * 2
#
# def more_than(i, a):
#     return i > a
#
# steps = [("filter", positives),("filter", odds),("map", mult), ("filter", lambda x: more_than(x, 20))]
#
# def actions(nums, steps):
#     result = nums
#     summary = []
#     for step_type, func in steps:
#         if step_type == "filter":
#             result = list(filter(func, result))
#             summary.append(result)
#         if step_type == "map":
#             result = list(map(func, result))
#             summary.append(result)
#     return summary
#
# positive, odd, multiple, more = actions(nums, steps)
# print("Positives ", positive)
# print("Odds ", odd)
# print("Mult ", multiple)
# print("More than 20", more)

