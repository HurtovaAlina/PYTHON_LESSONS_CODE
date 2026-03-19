# Завдання 1
# Напишіть функцію, яка відображає на екран форматований текст, зазначений нижче:
# "Don't compare yourself with anyone in this world…
#     if you do so, you are insulting yourself."
#         Bill Gates

def format_text():
    print("\"Don't compare yourself with anyone in this world…\n \t if you do so, you are insulting yourself.\" "
          "\n \t\t Bill Gates")

format_text()

# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

x = int(input("Enter x "))
y = int(input("Enter y "))

def evens(x, y):
    if x > y:
        x,y = y,x
    new_list = []
    for i in range(x, y+1):
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print("Even numbers = ", evens(x,y))

# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу.
# Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.

length = int(input("Enter length "))
char = input("Enter char ")
filled = input("Enter True / False ").strip().lower()
filled_bool = True if filled == "true" else False

def square_drawing(length, char, filled_bool):
    if filled_bool:
        for i in range(1, length+1):
            for j in range(1, length+1):
                print(char, end = "\t")
            print()
    elif not filled_bool:
        for i in range(1, length + 1):
            for j in range(1, length + 1):
                if i==1 or i == length:
                    print(char, end = "\t")
                elif j == 1 or j == length:
                    print(char, end = "\t")
                else:
                    print("", end = "\t")
            print()

square_drawing(length, char, filled)


# Завдання 4
# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри

numbers = input("Enter numbers ")
list_of_numbers = numbers.split(',')
print(list_of_numbers)


def min_from_numbers(list_of_numbers):
    min = int(list_of_numbers[0])
    for i in list_of_numbers:
        if int(i) < min:
            min = int(i)
    return min

print("Min = ", min_from_numbers(list_of_numbers))


# Завдання 5
# Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр.
# З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.

number = input("Enter number ").strip()

def digits_qty(number):
    return len(number)

print("Digits qty ", digits_qty(number))

# Завдання 6
# Напишіть функцію, яка перевіряє чи є число паліндромом. Число передається як параметр. Якщо число паліндром,
# потрібно повернути з функції true, інакше false.
# "Паліндром" — це число, у якого перша частина цифр дорівнює другій перевернутій частині цифр.
# Наприклад, 123321 — паліндром (перша частина 123, друга 321, яка після перевороту стає 123), 546645 —
# паліндром, а 421987 — не паліндром.

number = input("Enter number ").strip()

def is_palindrom(number):
    return "is palindrom" if number == number[::-1] else "is not a palindrom"

print(is_palindrom(number))

# Самостійна робота

# Рівень 1
# Завдання 1
# Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. Межі діапазону передаються як параметри.
# Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.

x = int(input("Enter x "))
y = int(input("Enter y "))

def multiplier(x, y):
    mult = 1
    if x > y:
        x,y = y,x
    for i in range(x, y+1):
        mult *=i
    return mult

print(multiplier(x,y))


# Завдання 2
# Напишіть функцію для знаходження максимуму в списку цілих. Список передається як параметр.
#
numbers = input("Enter numbers ")
list_of_numbers = numbers.split(',')
print(list_of_numbers)

def find_max(numbers):
    max = int(numbers[0])
    for i in numbers:
        i = int(i)
        if i > max:
            max = i
    return max

print(find_max(list_of_numbers))


# Завдання 3
# Напишіть функцію, що обчислює суму елементів списку цілих. Список передається як параметр.

numbers = input("Enter numbers ")
list_of_numbers = numbers.split(',')
print(list_of_numbers)

def find_sum(numbers):
    sum_elements = 0
    for i in numbers:
        i = int(i)
        sum_elements += i
    return sum_elements

print(find_sum(list_of_numbers))



# Завдання 4
# Напишіть функцію, що визначає кількість парних, непарних, додатних, від'ємних елементів списку цілих.
# Список передається як параметр.

numbers = input("Enter numbers ")
list_of_numbers = numbers.split(',')
print(list_of_numbers)

def find_ev_odd_pos_neg_elements(numbers):
    count_evens = 0
    count_odds = 0
    count_positive = 0
    count_negative = 0
    for i in numbers:
        if int(i) > 0:
            count_positive+=1
        else:
            count_negative+=1
        if int(i) % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    return (print("Evens =", count_evens, "Odds =", count_odds, "Positives =", count_positive,
            "Negatives =", count_negative))

find_ev_odd_pos_neg_elements(list_of_numbers)

# Завдання 5
# Напишіть функцію, що перевертає вміст списку цілих.

numbers = input("Enter numbers ")
list_of_numbers = numbers.split(',')
print(list_of_numbers)

def reverse_numbers(numbers):
    new_list = []
    for i in range(len(numbers)-1, -1, -1):
        new_list.append(numbers[i])
    return new_list

print(reverse_numbers(list_of_numbers))


# Завдання 6
# Напишіть функцію, що вираховує факторіал кожного елемента списку цілих. Функція повертає новий список,
# що містить отримані факторіали.

numbers = input("Enter numbers ")
list_of_numbers = numbers.split(',')
print(list_of_numbers)

def fact_elements(numbers):
    new_list = []
    fact = 1
    for i in numbers:
        for j in range(1, int(i)+1):
            fact *=int(j)
        new_list.append(fact)
        fact = 1
    return new_list

print(fact_elements(list_of_numbers))

# Завдання 7
# Напишіть функцію, яка шукає всі числа Фібоначчі у списку цілих.

input_list = input("Enter numbers ").split(',')
list_of_numbers = [int(i) for i in input_list]
print(list_of_numbers)


n = int(input("Enter quantity of Fibonacci series "))

def create_fibonacci(n):
    fibonacci_list = [0,1]
    for i in range (2,n):
        fibonacci_number = fibonacci_list[i-1]+fibonacci_list[i-2]
        fibonacci_list.append(fibonacci_number)
    return fibonacci_list

print("Fibonacci series: ", create_fibonacci(n))


def fibonacci_numbers(list_of_numbers, fibonacci_list):
    new_list = []
    for i in sorted(list_of_numbers):
            if int(i) in fibonacci_list:
                new_list.append(i)
    return new_list

print("Fibonacci numbers in the entered list: ", fibonacci_numbers(list_of_numbers,
                                                                   fibonacci_list= create_fibonacci(n)))

