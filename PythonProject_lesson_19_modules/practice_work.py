#1
import string_utils
print("Імпортований модуль")
text = input("Введіть текст: ")

text_without_punctuation = string_utils.punctuation_delete(text)
print('Текст без знаків пунктуації: ', text_without_punctuation)

count_vowels = string_utils.vowels_check(text)
print('Кількість голосних літер: ', count_vowels)

palindrom = string_utils.is_palindrom(text_without_punctuation)
print('Текст паліндром: ', palindrom)


#2
import math


def triangle_area(a: float, b: float, c: float) -> float:
    """

    :param a: сторона трикутника а
    :param b: сторона трикутника в
    :param c: кут між ними в градусах
    :return: площа трикутника
    """
    """
    переведення кута в градусах в радіани
    """
    rad = math.radians(c)
    return 0.5 * a * b * math.sin(rad)

area = triangle_area(3,4,90)
print(round(area,2))

#3
import time

def sum_of_numbers(n:int) -> int:
    total = 0
    for i in range (1, n+1):
        total+=i
    return total

start_time = time.time()
result = sum_of_numbers(10000000)
end_time = time.time()
print("Сума: ", result)
print(f"Час виконання: {end_time- start_time:.4f} секунд")

#4
import datetime

def age_calculation(date_of_birth: str) -> int:
    """

    :param date_of_birth:
    :return: вік
    """

    """
    Метод fromisoformat() використовується для створення об’єкта date з рядка у форматі ISO 8601:
    """
    date = datetime.date.fromisoformat(date_of_birth)
    current = datetime.date.today()
    delta = current-date
    """
    current-date повертає timedelta
    .days повертає кількість днів (тип int)
    """
    return delta.days

date_of_birth = input("Введіть дату народження в форматі YYYY-MM-DD ")
age_in_days = age_calculation(date_of_birth)
print(f"Ваш вік {age_in_days} днів")