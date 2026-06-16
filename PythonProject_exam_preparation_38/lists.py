# Списки
# 61. Список із 10 чисел
# Попросіть користувача ввести 10 чисел і збережіть їх у список. Виведіть список.
# Підказка: Використайте цикл і метод .append() або list comprehension.

# numbers = []
# for i in range(10):
#     numbers.append(int(input(f"Enter number {i+1}: ")))
#
# print(numbers)


# 62. Сума елементів списку
# Маючи список чисел, обчисліть і виведіть суму всіх його елементів без використання
# sum().
# Підказка: Ітеруйте по списку і накопичуйте суму у змінній total.

numbers = [2,4,5,6,7,9]
summ = 0

for num in numbers:
    summ+=num

print(f"Sum of numbers = {summ}")

# 63. Найбільший елемент
# Знайдіть і виведіть найбільший елемент списку без використання max().
# Підказка: Ініціалізуйте maximum = lst[0], порівнюйте з кожним наступним елементом.

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Max = {maximum}")

# 64. Найменший елемент
# Знайдіть і виведіть найменший елемент списку без використання min().
# Підказка: Аналогічно до пошуку максимуму, але з умовою el < minimum.

minimum = numbers[0]

for num in numbers:
    if num <  minimum:
        minimum = num

print(f"Min = {minimum}")

# 65. Середнє значення
# Обчисліть і виведіть середнє арифметичне елементів списку.
# Підказка: Середнє = сума елементів / кількість елементів. Кількість — len(lst).

def avg_nmubers(numbers:list) -> int:
    return sum(numbers)/len(numbers)

print(f"Average = {avg_nmubers(numbers)}")


# 66. Список квадратів
# Створіть список квадратів чисел від 1 до 10: [1, 4, 9, ..., 100].
# Підказка: Використайте list comprehension: [i**2 for i in range(1, 11)].

print([i**2 for i in range(1, 11)])

# 67. Лише парні числа
# Маючи список чисел, створіть новий список, що містить лише парні елементи
# вихідного.
# Підказка: Використайте list comprehension: [x for x in lst if x % 2 == 0].

print([num for num in numbers if num % 2 ==0])

# 68. Видалення від'ємних
# Маючи список чисел, видаліть із нього всі від'ємні значення. Виведіть очищений
# список.
# Підказка: Створіть новий список: [x for x in lst if x >= 0], або видаляйте елементи через
# remove().8

list_of_numbers = [-1, 6, 7, 8, -9, 0, -12]

print([num for num in list_of_numbers if num>0])

# 69. Кількість додатних
# Порахуйте, скільки елементів у списку є додатними (більшими за нуль).
# Підказка: Використайте лічильник або sum(1 for x in lst if x > 0).
print(sum(1 for num in list_of_numbers if num > 0))

# 70. Перший і останній
# Поміняйте місцями перший і останній елементи списку. Виведіть результат.
# Підказка: lst[0], lst[-1] = lst[-1], lst[0] — Python дозволяє таке присвоєння.

list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]

print(list_of_numbers)
