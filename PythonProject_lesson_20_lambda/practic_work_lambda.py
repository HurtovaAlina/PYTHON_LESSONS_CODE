import time

# 1
# Напишіть lambda-функції, які:
#  Підносить число до квадрату

sqr_func = lambda num: num**2
n = 6
print(f"Квадрат числа {n} =  {sqr_func(n)}")

#  Отримує довжини трикутника і повертає периметр
triang_perimetr = lambda a, b, c: a + b + c
print(f"периметр трикутника = {triang_perimetr(3,4,5)}")

#  Отримує прізвище та ім’я і повертає рядок у форматі
# «Прізвище, ім’я»

surname_name = lambda surname, name: surname + ", " + name
print(f"Прізвище, ім’я = {surname_name('Hurtova', 'Alina')}")

#  Перевіряє чи є число парним

is_even_num = lambda num: num % 2 == 0
num = int(input("Enter num "))
print(f"Number {num} is even: {is_even_num(num)}")

# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел та повертає список з лише
# додатніми числами
nums = [1, -4, 6, -9, -3, 5, 3, 2, 0, -5]
positive_nums = filter(lambda num: num > 0, nums)
print(list(positive_nums))


#  Отримує список слів та повертає список слів, в яких
# більше ніж 3 літери
words = ["sdf", "wert", "er", "fghhj", "errtyuyuu", "e", "qww"]
longer_words = filter(lambda word: len(word) > 2, words)
print(list(longer_words))

#  Отримує список слів та літеру і повертає список тих
# слів, які починаються на цю літеру(регістр
# неважливий)


def words_start_with_letter(words, letter):
    return filter(lambda word: word[0] == letter.lower(), words)


words = ["dfghh", "asddf", "ert", "asdfg", "eryuu"]
print(list(words_start_with_letter(words, "A")))

# 3
# Напишіть функцію, яка отримує іншу функцію та
# параметри. Поверніть час роботи функції у секундах


def sum_func(number):
    sum_of_numbers = 0
    for i in range(number):
        sum_of_numbers += i
    return sum_of_numbers


def my_func(sum_func):
    start = time.time()
    print(f"Calculation {sum_func.__name__}")
    res = sum_func(10000)
    end = time.time()
    duration = end - start
    print(f"Function work duration = {duration:.4f}")
    return res


print(my_func(sum_func))


# 4
# Напишіть функції, які:
#  Сортує список слів за останньою літерою
def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1])


words = ["apple", "banana", "ananas", "peach"]
print(sort_by_last_letter(words))


#  Сортує список чисел за кількістю цифр
def sort_by_qty_numbers(numbers):
    return sorted(numbers, key=lambda number: len(str(number)))


numbers = [23, 1, 15, 4567, 567]
print(sort_by_qty_numbers(numbers))


#  Знаходить число зі списку, яке найближче до
# заданого(передається як параметр)
def find_closed_number(numbers, number):
    return min(numbers, key=lambda num: abs(num - number))


numbers = [23, 1, 15, 4567, 567]
number = 17
print(
    f"Find closed number for {number} ", "- it is ", find_closed_number(numbers, number)
)

#  Знаходить слово у списку з найменшою довжиною


def shorter_word(words):
    return min(words, key=lambda word: len(word))


words = ["dfghh", "asddf", "ert", "asdfg", "eryuu"]
print("Shorter word ", shorter_word(words))


#  Сортує список чисел за кількістю цифр, якщо кількість
# цифр однакова, то сортує за значенням числа
def sort_by_qty_numbers(numbers):
    return sorted(numbers, key=lambda number: len(str(number)))


def sort_by_numbers(numbers):
    return sorted(numbers, key=lambda number: int(number))


numbers = [23, 1, 15, 4567, 567]
sort_by_qty_numbers = sort_by_qty_numbers(numbers)

print(sort_by_numbers(sort_by_qty_numbers))
