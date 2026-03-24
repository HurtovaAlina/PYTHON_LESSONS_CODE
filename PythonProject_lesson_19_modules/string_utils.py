"""
модуль для роботи зі строками

"""

import re


def punctuation_delete(text: str) -> str:
    """Видаляє пунктуацію з строки

    :param text: строка
    :return: строка без пунктуації
    """
    punctuation_pattern = "[,.?!;:—]"
    return re.sub(punctuation_pattern, "", text)


def vowels_check(text: str) -> int:
    """Рахує голосні літери в строкі

    :param text: строка
    :return: кількість голосних літер
    """
    vowels_list = ["а", "е", "и", "о", "у", "я", "ю", "є", "ї", "і"]
    count = 0
    for i in text:
        if i in vowels_list:
            count += 1
    return count


def is_palindrom(text: str) -> bool:
    """
    Перевіряє чи є текст палендромом

    :param text:
    :return: true (якщо паліндром) або false (якщо не паліндром)
    """
    reversed_text = text[::-1]
    return text.lower() == reversed_text.lower()


"""
    перевірка роботи функцій
"""

if __name__ == "__main__":
    print("Перевірка роботи модуля")
    text = input("Введіть текст: ")
    function = input(
        "Введіть назву функції: punctuation_delete | vowels_check | is_palindrom "
    )

    if function == "punctuation_delete":
        new_text = punctuation_delete(text)
        print("Текст без знаків пунктуації: ", new_text)

    elif function == "vowels_check":
        vowels_count = vowels_check(text)
        print("Кількість голосних: ", vowels_count)

    elif function == "is_palindrom":
        text_is_palindrom = is_palindrom(text)
        print("Текст паліндром: ", text_is_palindrom)

    else:
        print("Невірна назва функції")
