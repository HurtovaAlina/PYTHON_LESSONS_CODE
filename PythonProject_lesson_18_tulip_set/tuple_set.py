# s = (1,2,3,4)
# print(s[2])

# s = ()
# t = 5,
# t = (5,)
# t = 1,2,3,4,5
# ls = []
# print(t[::2])
# t.
# t = (9,) *3
# print(t)
# t = (1,2,[1,2,3])
# t[2][0] = 5
# del t[2]
# print(t)
# print(len(t))
# print(2 in t)

# a = (1,2)
# b = (3,4)
#
# print(a+b)
# print(a, b)
# print(a*3)


# def foo():
#     name = "ALex"
#     age = 20
#     return name, age
#
#
# user = foo()
# print(user)
# name, age = foo()
#
# print(name, age)

# db = ("User1", "User2", "User3", "User4")
# ls_db = list(db)
# db_t = tuple(ls_db)
# print(db_t)
# db.
# userTypes = ('admin', 'student', 'teacher', 'moderator')
# for i in range(len(userTypes)):
#     print(userTypes[i])

# {('1',):5}
# {1,2,3,(1,2,3)}
# users = {1}
# ls= ["Hello1", "Hello2", "Hello3", "Hello4", "Hello5", "Hello6", "Hello7"]
# users = set(ls)
# print(users)
# print(len(users))
#
# print("Hello1" in users)

# users = {"Den", "Alex", "John", "Alice", "Bob"}
# for i in users:
#     print(i)

# user = users.pop()
# print(user)

# users2 = users.copy()
# print(users2, users, )
# print(id(users), id(users2), )

# users.remove("Den")
# print(users)

# users.add("Den")
# print(users)

# users.update({"Tom", "Poll"})
# print(users)
#
# users.intersection()
# intersection (перетин) — це операція, яка знаходить спільні елементи між двома або більше наборами (множинами).
# Простіше кажучи:
# 👉 повертає ті значення, які є одночасно в усіх наборах.
#
# a = {1, 2, 3}
# b = {3, 4, 5}

#
# res = a.intersection(b)
#
# print(res)
#
# a.intersection_update(b)
# intersection_update() у Python оновлює множину, залишаючи в ній тільки ті елементи, які є спільними з іншою множиною.
# 👉 Тобто це як intersection(), але
# змінює початкову множину, а не створює нову.
#
# print(a)
# print(a & b)

# res1 = a.difference(b)
# res2 = b.difference(a)
# print(res1,res2)
# difference() повертає елементи, які є в множині a, але відсутні в множині b.
# 👉 Тобто це різниця множин.

# a.difference_update(b)
# print(a)
# difference_update() видаляє з множини a всі елементи, які є в множині b.
# 👉 На відміну від difference(),
# ця операція змінює саму множину a, а не створює нову.

# print(a - b, b - a)


# res = a.union(b)
# print(res, a | b)
# union() повертає об’єднання множин — тобто всі унікальні елементи з a і b.
# 👉 Беруться всі значення з обох множин без повторів.

# res = a.symmetric_difference(b)
# print(a ^ b)
# print(res)
# symmetric_difference() повертає елементи, які є в a або в b, але НЕ в обох одночасно.
# 👉 Тобто це елементи без спільних.
# c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# print(a.issubset(c))
# issubset() перевіряє, чи є множина a підмножиною множини c.
# 👉 Тобто чи всі елементи a входять у c.

# print(c.issubset(a))
#
# print(a.issuperset(c))
# print(c.issuperset(a))

# issuperset() перевіряє, чи є множина a надмножиною множини c.
# 👉 Тобто чи всі елементи c входять у a.

# a.remove()
# Видаляє елемент x з множини a. Якщо елемента немає, буде помилка:

# a.discard()
# Теж видаляє елемент x,
# але без помилки, якщо його немає.

# a.isdisjoint()
# Перевіряє, чи множини не мають спільних елементів.
# 👉 Повертає True, якщо спільних елементів немає.

# print(a.isdisjoint(b))

# fs = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 0})
# print(len(fs), 5 in fs, 5 not in fs)
# print(set(map(lambda x: x.lower(), ["User", "user"])))
# ls = [...]
# list(set(ls))
