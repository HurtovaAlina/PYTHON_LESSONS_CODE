# Завдання 1. Фільтрація та нормалізація списку покупок
# Є список рядків, де значення можуть бути в різному форматі, з пробілами, у різному регістрі.
# Вхід:
# items = ["  Milk  ", "bread", "BREAD", "", "  eggs", "Eggs ", "   ", "cheese"]
# Вимоги:
# Очистити пробіли по краях (map)
# Викинути порожні рядки після очищення (filter)
# Нормалізувати регістр: зробити все у нижньому регістрі (map)
# Прибрати дублікати, зберігши порядок появи
# Повернути фінальний список
# Очікуваний результат:
# ["milk", "bread", "eggs", "cheese"]

items = ["  Milk  ", "bread", "BREAD", "", "  eggs", "Eggs ", "   ", "cheese"]
items_without_duplicates = []

def remove_empty(i):
    if i !="":
        return i

def remove_duplicates(items):
    res = []
    for i in items:
        if i not in res:
            res.append(i)
    return res

without_spaces = list(map(lambda i: i.strip(), items))
# print(without_spaces)

without_empty = list(filter(remove_empty,without_spaces))
# print(without_empty)

lower_cases = list(map(lambda i: i.lower(), without_empty))
# print(lower_cases)

excluded_duplicates = remove_duplicates(lower_cases)
print(excluded_duplicates)


# Завдання 2. Вищі функції: фабрика фільтрів для студентів
# Є список студентів у вигляді словників.
# Вхід:
# students = [
#     {"name": "Іра", "age": 17, "avg": 91, "has_debt": False},
#     {"name": "Петро", "age": 19, "avg": 73, "has_debt": True},
#     {"name": "Оля", "age": 18, "avg": 88, "has_debt": False},
#     {"name": "Максим", "age": 20, "avg": 60, "has_debt": False},
# ]

# Вимоги:
# Написати вищу функцію make_student_filter(min_avg, max_age, no_debts_only)
# яка повертає функцію-предикат predicate(student) -> bool
# За допомогою filter відібрати студентів, які:
# мають середній бал >= min_avg
# мають вік <= max_age
# якщо no_debts_only=True, то has_debt має бути False
# За допомогою map отримати список імен відібраних студентів
# Додати параметр name_startswith (літера або None), якщо задано,
# фільтрувати ще і за першою літерою імені
# Приклад:
# min_avg=80, max_age=18, no_debts_only=True
# Результат: ["Іра", "Оля"]

students = [
    {"name": "Іра", "age": 17, "avg": 91, "has_debt": False},
    {"name": "Петро", "age": 19, "avg": 73, "has_debt": True},
    {"name": "Оля", "age": 18, "avg": 88, "has_debt": False},
    {"name": "Максим", "age": 20, "avg": 60, "has_debt": False},
]

def make_student_filter(min_avg, max_age, no_debts_only, name_startswith = None):
    def predicate(student):
        if student["avg"] < min_avg:
            return False
        if student["age"] > max_age:
            return False
        if no_debts_only and student["has_debt"]:
            return False
        if name_startswith is not None:
            if not student["name"].startswith(name_startswith):
                return False
        return True
    return predicate

predicate = make_student_filter(80, 18, True)
filtered_students = list(filter(predicate, students))
print(filtered_students)

students_names = list(map(lambda s: s['name'], filtered_students))
print(students_names)


# Завдання 3. Пайплайн обробки даних: застосуйте список трансформацій
# Є список чисел, де треба побудувати обробку як конвеєр з кроків. Кроки задаються як функції.
# Вхід:
# nums = [1, -2, 3, 0, 4, -5, 10, 11, 12]
# Вимоги:
# Створити функції-трансформації:
# only_positive (filter): залишає > 0
# only_even (filter): залишає парні
# square (map): підносить до квадрату
# Створити вищу функцію apply_pipeline(data, steps):
# steps це список кортежів виду ("map", func) або ("filter", func)
# функція проходить по steps і застосовує відповідний map або filter
# Викликати пайплайн:
# positive -> even -> square
# Повернути список результатів
# Очікуваний результат:
# позитивні: [1, 3, 4, 10, 11, 12]
# парні: [4, 10, 12]
# квадрат: [16, 100, 144]

nums = [1, -2, 3, 0, 4, -5, 10, 11, 12]

def only_positive(i):
    if  i>0:
        return i

def only_even(i):
    if i%2==0:
        return i

def square(i):
    return i*i

steps = [("filter", only_positive), ("filter", only_even), ("map", square)]

def apply_pipeline(data, steps):
    result = data
    new_result = []
    for step_type, function in steps:
        if step_type == "filter":
            result = list(filter(function, result))
            new_result.append(result)
        if step_type == "map":
            result = list(map(function, result))
            new_result.append(result)
    return new_result

positive, evens, squares = apply_pipeline(nums,steps)
print("Positive ", positive)
print("Evens ", evens)
print("Square ", squares)




