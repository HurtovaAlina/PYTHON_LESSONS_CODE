# def foo():
#     print("Hello from foo!")
#
#
# foo()
# foo()
# foo()
# def x():
#     print("is x!")
#
# def foo():
#     def inner_foo():
#         print("Hello from inner function1")
#
#     inner_foo()
#     x()
#     print("Hello from foo!")
#
# def inner_foo():
#     print("Hello from inner function2")
#
#
# inner_foo()
#
# foo()

# def validate_n(n: str):
#     if not (n.isdigit() and 30 <= int(n) <= 50):
#         exit(-1)

# def validate_ls(ls: list):
#     for i in ls:
#         if not (i.isdigit() and 30 <= int(i) <= 50):
#             print(i, " is not a valid number.")
#             exit(0)
#     print("The end function")

# n1 = "12"
# validate_n(n1)
# n2 = "47"
# validate_n(n2)
# n3 = "45"
# validate_n(n3)
# n4 = "50"
# validate_n(n4)
# n5 = "46"
# validate_n(n5)
# print("The end")
#
# ls = [n1, n2, n3, n4, n5]
# validate_ls(ls)
# print("The end")


# def foo(n1, n2):
#     print(n1 + n2)

# foo(5, 10)
# foo(3, 2)
# foo(1, 1)
# foo(5)


# def pow_m(base=1, exponent=1):
#     print(base ** exponent)
#
# pow_m(2,3)
# pow_m(8)
# pow_m(2)
# pow_m(3)
# pow_m()
#
# def foo(*n1, n2=1, x=0):
#     print(x)
#     print(n1,n2)
#     print(sum(x))
# ls = [1, 2, 3]
# a, *x = ls
# foo()
# foo(1, 2, 3,2,3,3,2,1, n2=10, x=5)
# foo(1, 2)
# foo(1, 2, 3, 4, 5, 6, 7, 8)
# foo(4, 3, 5, 6)

# def foo(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# foo(1,2,3,4,5, n1=1,n2=2,n3=3,n4=4,n5=5,n6=6)

# def action1():
#     pass
#
# def action2():
#     pass
#
# def action3():
#     pass
#
# action2()

# def foo(n1: int, n2: int) -> int:
#     print("Start")
#     if n1 > 0 and n2 > 0:
#         return n1 + n2
#     print("Stop")
#     return 0
#
#
# res = foo(-6, 2)
# print(res)
