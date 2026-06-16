# Робота зі списками рядків
# 71. Довгі слова
# Маючи список слів, виведіть лише ті, довжина яких перевищує 5 символів.
# Підказка: Умова фільтрації: len(word) > 5.

def word_len(words: list, l:int = 5)-> list:
    return [word for word in words if len(word) > l]

words = ["hello", "world", "python", "list", "string", "tuple", "set", "dict"]
print(word_len(words))


# 72. Найдовше слово
# Знайдіть і виведіть найдовше слово зі списку без використання max().
# Підказка: Ітеруйте і порівнюйте len(word) з довжиною поточного максимуму.

def find_max_length(words: list) -> list:
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return [word for word in words if len(word) == max_length]

words = ["hello", "world", "python", "list", "string", "tuple", "set", "dict"]
print(find_max_length(words))

# 73. Найкоротше слово
# Знайдіть і виведіть найкоротше слово зі списку без використання min().
# Підказка: Аналогічно до пошуку найдовшого, але порівнюйте на менше.

def find_min_length(words: list) -> list:
    min_length = len(words[0])
    for word in words:
        if len(word) < min_length:
            min_length = len(word)
    return [word for word in words if len(word) == min_length]

words = ["hello", "world", "python", "list", "string", "tuple", "set", "dict"]
print(find_min_length(words))

# 74. Слова з великої літери
# Виведіть лише ті слова зі списку, що починаються з великої літери.
# Підказка: Метод word[0].isupper() або word.istitle().

def word_starts_with_uppercase(words:list)-> list:
    new_list = []
    for word in words:
        if word.istitle():
            new_list.append(word)
    return new_list

words = ["hello", "World", "Python", "list", "string", "tuple", "set", "Dict"]
print(word_starts_with_uppercase(words))

# 75. Слова з літерою а
# Виведіть слова зі списку, що містять літеру "а" (в будь-якому регістрі).
# Підказка: Умова: "а" in word.lower().

def word_with_letter(words:list, letter:str) -> list:
    return [word for word in words if letter in word.lower()]

print(word_with_letter(words, letter="e"))

# 76. Слова на -ія
# Виведіть слова зі списку, що закінчуються на "ія".
# Підказка: Метод word.endswith("ія").




# 77. Сортування за алфавітом
# Відсортуйте список слів за алфавітом і виведіть результат.
# Підказка: Використайте sorted(lst) або lst.sort().

words = ["hello", "world", "python", "list", "string", "tuple", "set", "dict"]
print(sorted(words))


# 78. Сортування за довжиною
# Відсортуйте список слів за зростанням їхньої довжини і виведіть.
# Підказка: sorted(lst, key=len) або lst.sort(key=len).


# 79. Кількість слів
# Порахуйте та виведіть кількість слів у списку.
# Підказка: Просто len(lst).


# 80. Верхній регістр
# Створіть новий список, де всі слова записані у верхньому регістрі.
# Підказка: List comprehension: [w.upper() for w in lst].
