# Завдання 1
# Напишіть lambda-функції, які:
#  Множить число на -1

# res_mult = lambda num: num * -1
# num = int(input("Enter num "))
# print(f"Number {num} * -1 = {res_mult(num)}")

#  Перевіряє чи рядок непорожній

# is_empty_str = lambda string: string != ""
# my_string = input("Enter string ")
# print(f"String is not empty: {is_empty_str(my_string)}")


# Завдання 2
# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел, рахує середнє арифметичне та
# повертає список з числами, які більші за середнє

# def numbers_more_avg(numbers) -> list:
#     """
#     Функція отримує список чисел, рахує середнє арифметичне та
#     повертає список з числами, які більші за середнє
#
#     :param numbers: список чисел
#     :return: відфільтрований список чисел, які більше за середнє
#     """
#
#     avg = sum(numbers)/len(numbers)
#     print("average", avg)
#     return list(filter(lambda number: number>avg, numbers))
#
# numbers = [1,6,9,5,3,7,8,4,2]
# print(numbers_more_avg(numbers))

#  Отримує список слів та повертає список слів, в яких
# рівно 4 літери


# def length_of_words(words) -> list:
#     """
#     Функція повертає список слів, в яких ровно 4 літери
#     :param words: список слів
#     """
#     return list(filter(lambda word: len(word)==4, words))
#
# words = ["apple", "pear", "banana", "ananas", "plum", "peach"]
# print(length_of_words(words))

# Завдання 3
# Напишіть функцію, яка отримує літеру та список слів і
# знаходить слово зі списку, в якому найбільша кількість даної
# літери.


def letter_in_word(words, letter) -> list:
    """
    Функція отримує літеру та список слів і знаходить слово зі списку, в якому найбільша кількість даної літери
    :param words: список слів
    """
    # words_with_letter = list(filter(lambda word: letter in word, words))
    word_with_max = max(words, key=lambda word: word.count(letter))
    # max_count = 0
    # word_with_max = words_with_letter[0]
    # for word in  words_with_letter:
    #     count = word.count(letter)
    #     if count > max_count:
    #         max_count = count
    #         word_with_max = word

    return word_with_max


words = ["apple", "pear", "ananas", "plum", "peach", "aaaaa"]
print(letter_in_word(words, "a"))
