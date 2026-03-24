# name = "Den"
#
# def foo():
#     name = "John"
#     print(globals(), "\n", locals())
#     print("Call from foo")
#     print(": ", name)
#
#
# foo()
#
#
# print(name)
#
# print(globals(),"\n", locals())

# x1 = "x1"
# def outer():
#     x2 = "x2"
#     print("Start outer")
#     def inner():
#         x3 = "x3"
#         print("Start inner")
#         print(x2)
#         print("End inner")
#     inner()
#     print("End outer")
#
#
# outer()
# counter = 0
#
# def foo():
#     global counter
#     counter += 1
#
#
# foo()
# foo()
# foo()
# print(counter)


# def outer():
#     counter = 0
#
#     def inner():
#         nonlocal counter
#         counter += 1
#
#     inner()
#
#     inner()
#     inner()
#
#     print(counter)
#
# outer()

# def action1(a, b):
#     return a + b
#
#
# def action2(a, b):
#     return a - b

#
# def action3(a, b):
#     return a * b
#
#
# def action4(a, b):
#     if b == 0:
#         return 0
#     return a / b
#
#
# ls = [action1, action2, action3, action4]
#
# choice = input("Enter action(1/2/3/4): ")
# if choice in ["1", "2", "3", "4"]:
#     print(ls[int(choice) - 1](int(input("Enter a: ")), int(input("Enter b: "))))  # action1

# def x(a,b, poww):
#     return (a+b)

# def action1(a, b):
#     return a + b
#
#
# def action2(a, b):
#     return a - b
# def do_action(a,b, op):
#     return op(a,b)
#
#
# print(do_action(1,2, action1))
# print(do_action(1,2, action2))

# foo()
# ! return
# if !

# def foo():
#     print("Hello")
#     foo()
#
#
# foo()


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#     # return 1 if n ==1 else n * fact(n-1)
#
# print(fact(5))


# ls = [1, [1, 2], [[3], 5], [1], [[[[5], 6]]]]
# def deep_sum(items):
#     total = 0
#
#     for item in items:
#         if isinstance(item, list):
#             total += deep_sum(item)
#         elif isinstance(item, int):
#             total += item
#
#     return total
#
# print(deep_sum(ls))

# ["a",["b","c",["d"]], "e"]
# a
# [
#     b
#     c
#     [
#         d
#     ]
# ]
# e
# print(ls)

# def print_nested(items, level=0):
#     indent = "\t" * level
#     # print(indent + "" + str(level + 1))
#     for item in items:
#         if isinstance(item, list):
#             print(indent + "[")
#             print_nested(item, level + 1)
#             print(indent + "]")
#         else:
#             print(indent + str(item))
#
# print_nested(ls)
# print(ls)

# line = "hello"

# print(line[::-1])


# def pow_n(m, n):
#     if n == 1:
#         return m
#     else:
#         return m * pow_n(m,n-1)
#
#
# print(pow_n(2, 3))
