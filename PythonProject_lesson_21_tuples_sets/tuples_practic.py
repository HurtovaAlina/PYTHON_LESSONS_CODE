# Завдання 1
# Користувач вводить числа через кому. Збережіть їх у
# кортеж. Виведіть на екран:
#  Суму чисел
#  Найбільше та найменше число
#  Перші та останні 3 числа
#  Кількість чисел 7
#  Пари індекс – число
# Додатково, якщо користувач введе порожній рядок, то
# створіть власний кортеж з випадковими числами(12 шт).
import random

numbers = input("Enter numbers separated with comma ")

if numbers.strip() =='':
    new_numbers = tuple(random.randint(1, 100) for _ in range(12))
    print(new_numbers)
else:
    numbers = numbers.split(',')
    new_numbers = tuple(map(int, numbers))

sum_of_numbers = sum(new_numbers)
print("Sum of numbers = ", sum_of_numbers)

min_number = min(new_numbers)
max_number = max(new_numbers)
print(f"Min number = {min_number}, max number = {max_number}")

first_three_numbers = new_numbers[:3]
last_three_numbers = new_numbers[-3:]
print(f"First three numbers = {first_three_numbers}, last three numbers = {last_three_numbers}")

count_of_sevens = lambda num: new_numbers.count(7)
print("Count of sevens = ", count_of_sevens(new_numbers))

for i, num in enumerate(new_numbers):
    print(i, num)

# Завдання 2
# Напишіть наступну програму: є кортеж з іменами
# зареєстрованих студентів. Користувач вводить ім’я студента
# після чого отримує повідомлення, чи студент зареєстрований.
# Програма закінчує роботу коли користувач введе порожній
# рядок

registered_students = ("Anna", "Den", "John", "Bob", "Paul", "Laura")
while True:
    name = input("Enter student's name ")
    if name in registered_students:
        print(f"Student {name} is registered")
    elif name == "":
        print("Finish")
        break
    else:
        print("Student is not registered")

# Завдання 3
# Напишіть наступну програму: є кортеж з назвами фільмів.
# Користувач вводить назву фільму.
# Практичне завдання
#  Якщо фільм знаходиться в першій половині кортежу,
# треба вивести ретро-фільм
#  Якщо в другій половині – сучасний фільм
#  Якщо один з останніх п'яти – новий фільм

movies = (
    "The Godfather",
    "Casablanca",
    "Psycho",
    "Gone with the Wind",
    "Roman Holiday",
    "Inception",
    "Interstellar",
    "Parasite",
    "Joker",
    "Dune",
    "Infinity",
    "12 Angry Men",
    "Some Like It Hot"
)

film_name = input("Enter the film ")
half_of_tuple = int(round((len(movies)+1)/2, 0))

if film_name in movies:
    if film_name in movies[:half_of_tuple]:
        print("Retro film")
    elif film_name in movies[half_of_tuple:len(movies)] and film_name in movies[-5:]:
        print("New film")
    elif film_name in movies[half_of_tuple:len(movies)]:
        print("Modern film")

else:
    print("film is not in the Movies list")

# Завдання 4
# Напишіть функцію, яка отримує кортеж з назвами фруктів
# та слово. Потрібно повернути скільки разів дане слово
# зустрічається в кортежі(регістр неважливий). Складні назви
# теж враховуються. Приклад:
# ("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко")
# Яблуко зустрічається 3 рази

fruits = (
    "apple",
    "banana",
    "red apple",
    "peach",
    "plum",
    "golden apple"
)

def count_of_word(fruits, word)-> int:
    """
    returns how many times word met in fruits
    :param fruits: tuple of fruits
    :param word: wird in tuple
    :return: count of times the word was met
    """
    word = word.lower()
    return sum(fruit.count(word) for fruit in fruits)

word = "apple"
print(f"Word {word} meets in fruits {count_of_word(fruits, word)} times")

# Завдання 5
# Напишіть функцію, яка отримує кортеж з числами та
# виводить на екран статистику по кількості чисел з різною
# кількістю цифр. Приклад:
# одноцифрових – 3 шт
# двоцифрових – 5 шт
# трицифрових – 2 шт
#
numbers = (
    2,
    -33,
    56,
    5,
    -789,
    0,
    45,
    245,
    34,
    6789
)


def digits_count(numbers):
    max_digits = 0
    for num in numbers:
        length = len(str(abs(num)))
        if length > max_digits:
            max_digits = length

    count_of_digits = [0]*max_digits
    for num in numbers:
        length = len(str(abs(num)))
        count_of_digits[length - 1] += 1
    return count_of_digits


count_of_digits = digits_count(numbers)
for i in count_of_digits:
    print(f"{count_of_digits.index(i)+1}-digits – {i}")




# Завдання 6
# Користувач вводить назви товарів через кому. Потрібно
# сформувати кортеж. Також вводяться ціни товарів, які теж
# треба зберегти у кортеж. Виведіть на екран пари товар – ціна.
# Також виведіть назви найдорожчого та найдешевшого товарів.

items = input("Enter items, separated by comma ")
items_tuple = tuple(items.lower().split(', '))

prices = input("Enter price for each item ")
prices_tuple = tuple(map(float, prices.split(', ')))

agregated_data = []

for item, price in zip(items_tuple, prices_tuple):
    result = (item, price)
    agregated_data.append(tuple(result))
    print(item, price)

item_with_max_price = max(agregated_data, key=lambda x: x[1])
item_with_min_price = min(agregated_data, key=lambda x: x[1])

print("Item with max price", item_with_max_price)
print("Item with min price", item_with_min_price)







