# Завдання 1
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є у всіх кортежах.

tuple_1 = (1, 2, 3, 4, 5, 6)
tuple_2 = (7, 8, 9, 5, 6, 0, 11)
tuple_3 = (5, 6, 3, 7, 8, 9, 11)

set_1 = set(tuple_1)
set_2 = set(tuple_2)
set_3 = set(tuple_3)

res = set_1.intersection(set_2, set_3)
print(res)

# Завдання 2
# Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку.

tuple_1 = (1, 2, 3, 4, 5, 6)
tuple_2 = (7, 8, 9, 5, 6, 0, 11)
tuple_3 = (5, 6, 3, 7, 8, 9, 11, 22)

set_1, set_2, set_3 = set(tuple_1), set(tuple_2), set(tuple_3)

only_in_set_1 = set_1.difference(set_2).difference(set_3)
only_in_set_2 = set_2.difference(set_1).difference(set_3)
only_in_set_3 = set_3.difference(set_1).difference(set_2)

res = only_in_set_1.union(only_in_set_2, only_in_set_3)

print(res)

# Завдання 3
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є в кожному з кортежів і знаходяться в кожному
# з них на тій самій позиції.

tuple_1 = (1, 2, 3, 4, 6, 7)
tuple_2 = (7, 8, 3, 5, 6, 0)
tuple_3 = (5, 6, 3, 7, 6, 9)

res = list(
    zip(tuple_1, tuple_2, tuple_3, strict=False)
)  # list(zip()) - список, де кожен елемент — це кортеж з елементів
# на однакових позиціях.
print(res)  # [(1, 7, 5), (2, 8, 6), (3, 3, 3), (4, 5, 7), (6, 6, 6), (7, 0, 9)]
list_of_elements = []
for x, y, z in res:
    if x == y == z:
        list_of_elements.append(x)
print(tuple(list_of_elements))
