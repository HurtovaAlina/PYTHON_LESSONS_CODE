# Функції
# 81. Квадрат числа
# Напишіть функцію square(n), яка приймає число і повертає його квадрат. Викличте і
# виведіть результат.
# Підказка: return n ** 2

def square(n:int)-> int:
    return n ** 2

number = int(input("Enter number "))
print(f"Square of number {number} = {square(number)}")


# 82. Куб числа
# Напишіть функцію cube(n), яка приймає число і повертає його куб. Викличте і виведіть
# результат.
# Підказка: return n ** 3

def cube(n:int)-> int:
    return n ** 3

number = int(input("Enter number "))
print(f"Cube of number {number} = {cube(number)}")

# 83. Перевірка парності
# Напишіть функцію is_even(n), яка повертає True, якщо число парне, і False — якщо
# непарне.
# Підказка: return n % 2 == 0

def is_even(n: int) -> bool:
    return n % 2 == 0

number = int(input("Enter number "))
print(f"Is {number} even?  {is_even(number)}")

# 84. Максимум з двох
# Напишіть функцію max_two(a, b), яка повертає більше з двох чисел без використання
# max().
# Підказка: return a if a > b else b
# 85. Максимум з трьох
# Напишіть функцію max_three(a, b, c), яка повертає найбільше з трьох чисел.
# Підказка: Порівнюйте попарно або викличте max_two двічі.

# 86. Кількість голосних
# Напишіть функцію count_vowels(text), яка приймає рядок і повертає кількість голосних
# у ньому.
# Підказка: Ітеруйте і перевіряйте ch.lower() in "аеиіоуяюєїaeiou".

def count_vowels(text) -> int:
    count = 0
    for t in text:
        if t.lower():
            count+=1
    return count

text = input("Enter text ")
print(f"Qty of vowels: {count_vowels(text)}")


# 87. Перевірка паліндрома
# Напишіть функцію is_palindrome(text), яка повертає True, якщо рядок є паліндромом.
# Підказка: s = text.lower().replace(" ",""); return s == s[::-1]

def is_palindrome(text: str) -> bool:

    s = text.lower().replace(" ","")
    return s == s[::-1]

text = input("Enter text ")
print(f"Is palindrom: {is_palindrome(text)}")

# 88. Список парних
# Напишіть функцію get_evens(lst), яка приймає список чисел і повертає новий список
# лише з парними.
# Підказка: return [x for x in lst if x % 2 == 0]
# 89. Фільтрація за довжиною
# Напишіть функцію filter_by_length(words, n), яка повертає слова довжиною більше n
# символів.
# Підказка: return [w for w in words if len(w) > n]
# 90. Слова з символом
# Напишіть функцію words_with_char(words, ch), яка повертає список слів, що містять
# заданий символ.
# Підказка: return [w for w in words if ch.lower() in w.lower()]
