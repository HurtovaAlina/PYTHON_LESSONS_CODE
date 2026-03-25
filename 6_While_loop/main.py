# Завдання 1
# Користувач вводить із клавіатури два числа (початок і кінець діапазону). Потрібно проаналізувати всі числа в цьому
# діапазоні за таким правилом: якщо число кратне 7, його треба виводити на екран.

start = int(input("Enter start = "))
end = int(input("Enter end = "))

if start > end:
    start, end = end, start

while start <= end:
    if start % 7 == 0:
        print(f"{start}")
    start += 1
print("End of loop")

# Завдання 2
# Користувач вводить із клавіатури два числа (початок і кінець діапазону). Потрібно проаналізувати всі числа в
# цьому діапазоні. Потрібно вивести на екран:
# Усі числа діапазону.
# Усі числа діапазону в спадному порядку.
# Усі числа, кратні 7.
# Кількість чисел, кратних 5.

start = int(input("Enter start = "))
end = int(input("Enter end = "))

if start > end:
    start, end = end, start
print("\nPrint all numbers")
i = start
while i <= end:
    print(i, end="\t")
    i += 1
print("\nPrint all numbers in opposite order")
j = start
while j < i:
    i -= 1
    print(i, end="\t")
count = 0
print("\nPrint numbers multiple of 7")
while start <= end:
    if start % 7 == 0:
        print(f"{start}", end="\t")
    if start % 5 == 0:
        count += 1
    start += 1
print("\nAmount of numbers multiple of 5 = ", count)

# Завдання 3
# Користувач вводить із клавіатури два числа (початок і кінець діапазону). Потрібно проаналізувати всі числа
# в цьому діапазоні. Виведення на екран має відбуватися за правилами, зазначеними нижче.
# Якщо число кратне 3 (ділиться на 3 без залишку) потрібно вивести слово "Fizz". Якщо число кратне 5 потрібно
# вивести слово "Buzz". Якщо число кратне 3 і 5 потрібно вивести "Fizz Buzz". Якщо число не кратне не 3 і 5
# потрібно вивести саме число.

start = int(input("Enter start = "))
end = int(input("Enter end = "))

if start > end:
    start, end = end, start

while start <= end:
    if start % 3 == 0 and start % 5 != 0:
        print("Fizz,", end="\t")
    if start % 5 == 0 and start % 3 != 0:
        print("Buzz,", end="\t")
    if start % 3 == 0 and start % 5 == 0:
        print("Fizz Buzz,", end="\t")
    if start % 5 != 0 and start % 3 != 0:
        print(f"{start},", end="\t")
    start += 1
print("\nEnd of loop")


# Завдання 4
# Користувач вводить два числа і крок (інтервал), з яким потрібно проходити по діапазону. Програма має показати числа
# від початку діапазону до кінця, збільшуючи кожне число на вказаний крок. Також програма повинна надавати вибір
# порядку виведення: у прямому або зворотному порядку.

start = int(input("Enter start = "))
end = int(input("Enter end = "))
step = int(input("Enter step = "))
output_result = input("Enter output direct OR reverse order ")

if start > end:
    start, end = end, start

if output_result == "direct":
    while start <= end:
        print(start, end="\t")
        start += step
    print(end)
elif output_result == "reverse":
    while end > start:
        print(end, end="\t")
        end -= step
    print(start)
else:
    print("Incorrect value of output")

# Завдання 5
# Користувач вводить два числа, що представляють діапазон. Програма повинна пройти по діапазону і вивести
# добуток усіх чисел, які діляться на 4, але не діляться на 6. Якщо таких чисел немає, вивести відповідне
# повідомлення. Діапазон має автоматично нормалізуватися, якщо початок більший за кінець.

start = int(input("Enter start = "))
end = int(input("Enter end = "))
mult = 1

if start > end:
    start, end = end, start

while start <= end:
    if start % 4 == 0 and start % 6 != 0:
        mult *= start
    start += 1
if mult == 1:
    print("There are no any numbers multiples of 4 and not multiple of 6")
else:
    print("Multiplication of numbers multiples of 4 = ", mult)

# Завдання 6
# Користувач вводить два числа: число A і ступінь N, у який потрібно піднести число. Програма повинна обчислити A
# у степені N за допомогою циклу (без використання вбудованих функцій піднесення до степеня).

A = int(input("Enter number "))
N = int(input("Enter power "))
i = 1
power = 1
if N > 0:
    while i <= N:
        power = power * A
        i += 1
    print(power)
if N == 0:
    print("Power of the number A = ", power)
