# Завдання 1
# Є кортеж з назвами міст. Виведіть ті міста, які
# зустрічаються в кортежі більше одного разу.
import random

cities = (
    "Kyiv",
    "Dnipro",
    "Uzhgorod",
    "Lviv",
    "Dnipro",
    "Lutsk",
    "Ternopil",
    "Kharkiv",
    "Lviv",
)
popular_cities = []
for city in cities:
    if cities.count(city) > 1:
        popular_cities.append(city)

print(set(popular_cities))


# Завдання 2
# Є два кортежі з випадковими числами. Виведіть на екран
# ті числа, які є в першому кортежі, але немає в другому.

numbers_1 = tuple(random.randint(1, 100) for _ in range(12))
print(numbers_1)
numbers_2 = tuple(random.randint(1, 100) for _ in range(12))
print(numbers_2)

for number in numbers_1:
    if number not in numbers_2:
        print(number)

# Завдання 3
# Напишіть функцію, яка отримує 2 кортежі. Поверніть
# список з елементами, які є в обох кортежах і мають однакові
# індекси. Підказка: використайте zip()


def same_elements(elements_1, elements_2):
    """
    :param elements_1: tuple of elements
    :param elements_2: tuple of elements
    :return: list of elements from elements_1 and elements_2 that are equal and have the same index
    """

    list_of_same_elements = []
    for element_1, element_2 in zip(elements_1, elements_2, strict=False):
        if element_1 == element_2:
            list_of_same_elements.append(element_1)
    return list_of_same_elements


elements_1 = ("Kyiv", "Dnipro", "Lviv", "Lutsk", "Ternopil", "Kharkiv")

elements_2 = ("Kyiv", "Lviv", "Dnipro", "Lutsk", "Ternopil", "Kyiv")
print(same_elements(elements_1, elements_2))
