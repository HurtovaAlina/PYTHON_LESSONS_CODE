# h = int(input("Введіть висоту: "))
# ch = input("Введіть символ: ").strip()
#
# BLUE = "\033[34m"  # синій
# GRAY = "\033[90m"  # сірий
# RESET = "\033[0m"  # скидання кольору
#
# mid = h // 2
#
# for r in range(h):
#     dist = abs(mid - r)
#     i = mid - dist
#     leading_spaces = dist
#     width = 2 * i + 1
#
#     if width == 1:
#         # верх або низ ромба (одна точка)
#         print(" " * leading_spaces + BLUE + ch + RESET)
#     else:
#         inside_spaces = width - 2
#         # ліва грань синя права грdань сіра
#         print(
#             " " * leading_spaces
#             + BLUE + ch + RESET
#             + " " * inside_spaces
#             + GRAY + ch + RESET
#         )
import random
# module string
import string
#
# "".isascii()
# "" in string.ascii_letters #vбуква входить в набір латинського алфавіту

# print(string.whitespace)
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.printable)
# print(string.punctuation)
# print(string.digits)

# alphabet = string.ascii_letters+string.digits+string.punctuation # ramdom password
#
# print("".join(random.choice(alphabet) for _ in range(10))) #генератор набір елементів (списків)

# шаблон строки - темплейт
# t1 = string.Template("Hello! $name! Your order №$code.")
# print(t1.substitute(name = "John", code="132456"))

# f = string.Formatter()
# f.format()
# "Name: {name}".format("Den")

# f-string форматована строка f"asd {name}"
# t-string темплейт стрінг літерал t"asd {name}" з 3.14.2 версії  буде повертатися шаблон (темплейт)

# name = "Den"
# line_f = f"asd {name}"
# line_t = t"asd {name}"
# print(line_f)
# print(line_t)

# print(string.capwords("alina hurtova"))

# name = "Мир"
# t_val = t
# "Привет, {name}!"
#
# # 1. Если просто напечатать, мы увидим структуру объекта:
# print(t_val)
# # Template(strings=('Привет, ', '!'), ...)
#
# # 2. Чтобы получить текст, используем стандартный обработчик:
# from string import render
#
# result = render(t_val)
# print(result)  # Выведет: Привет, Мир!

# regex
#1. Базова модель
# літерали - букви звичайні символи cat
#конкатенація - склеювання (cat)
#альтернація - або буква або інша буква c|a|t
#групування (ab|cd)

# 2. Екранування як шукати
# . ^ $ * + ? ( ) [ ] { } | \
# . любий доступний символ в строці  c.t
# . любий доступний символ в строці  c\.t - буде крапка

#3. Метасимволи і  Квантифікатори, групи
# Метасимволи спеціальні символи (слово з повторенням cat, catcat )

# 1) Базова
# модель;
#
# ^;
#
# 1.
# Літерали(звичайні
# символи)
#
# 2.
# Конкатенація(cat)
#
# 3.
# Альтернація(a | b)
#
# 4
# групування(ab | cd)
#
# 2) Екранування
#
#    . ^ $ *+ ? ( )[]
# {} | \
#  \
# 3) Метасимволи, Квантифікавтори, групи
#
# aaa
#
# Hello is me
# H
#
# aaabbbbababab
#
# Метасимволи:
#
# aaab
#
# aabbb
#
# d
#
# c
#
# x
#
# z
#
# s
#
# d
#
# f
#
# g
#
# HelloHelloHello
#
# Hellooo
#
# oooooooo
#
# oooooo
#
# H
#
# admin -
#
# admin - a
#
# d
#
# admin - Den
#
# admin - Bob
#
# admin - 123
#
# admin - Bob2
#
# Hello! Is
# me.How
# are
# u?
#
# a.
#
# {2, 5
#
# .Завдання(представлення) одного довільного символу(крім символу нового рядка)
#
# ^ Ознака
# початку
# послідовності
#
# $ Ознака
# закінчення
# послідовності
#
# * Позначає
# будь - яку
# кількість
# повторень
# одного
# символу(0
# або
# більше), що
# передує
# символу « * »
#
# + Позначає
# будь - яку
# кількість
# повторень
# одного
# символу(1
# або
# більше), попереднього
# до
# символу «+»
#
# ? Позначає
# нуль
# або
# одне
# повторення
# одного
# символу, попереднього
# до
# символу «?»
#
# {n}
# Позначає
# задане
# число(n)
# повторень
# одного
# символу, попереднього
# до
# символу «{»
#
# []
# Використовується
# для
# задання
# будь - якого
# символу
# з
# перелічених
# всередині[]
#
# \ Використовується
# для
# екранування
# метасимволів
#
# | Відповідає
# логічному
# АБО(значення
# до
# або
# після
# символу « | »)
#
# ()
# Для
# створення
# групи
# символів(вираз
# усередині) розглядається
# як
# один
# елемент)
