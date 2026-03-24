def new(x, y):
    return x + y


import math

print(math.sqrt(16))
print(new(3, 4))

def print_text(text_1):

    print(text_1)

print(print_text("Hello world"))

def new_xy(x, y):
    return x * y

print(new_xy(3, 4))


with open("new-text.txt", "r") as file:
    print(file.read())

def add_xy(x, y):
    return x + y

print(add_xy(3, 4))
def read_file(filename):
    with open(filename, "r") as file:
        print(file.read())

print(read_file("new-text.txt"))

print_text()
