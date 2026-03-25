# Завдання 1
# Користувач вводить з клавіатури три числа. Залежно від вибору користувача програма виводить на екран суму трьох чисел
# або добуток трьох чисел.

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
action = input("Enter action: SUM or MULT: ")

if action == "SUM":
    print("Sum : ", n1 + n2 + n3)
elif action == "MULT":
    print("Mult : ", n1 * n2 * n3)
else:
    print("Wrong action!")

# Завдання 2
# Користувач вводить з клавіатури три числа. Залежно від вибору користувача програма виводить на екран максимум із
# трьох, мінімум із трьох або середньоарифметичне трьох чисел.

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
action = input("Enter action: MAX or MIN or AVRG: ")

max_num = n1
min_num = n1
if n2 > max_num:
    max_num = n2
if n2 < min_num:
    min_num = n2
if n3 > max_num:
    max_num = n3
if n3 < min_num:
    min_num = n3

if action == "MAX":
    print("MAX : ", max_num)
elif action == "MIN":
    print("MIN : ", min_num)
elif action == "AVRG":
    print("AVRG : ", (n1 + n2 + n3) / 3)
else:
    print("Wrong action!")

# Завдання 3
# Користувач вводить число, що представляє оцінку за шкалою від 1 до 5. Програма повинна вивести текстову інтерпретацію
# оцінки:
# Дуже погано.
# Погано.
# Задовільно.
# Добре.
# Відмінно.

rate = int(input("Enter rate "))
if rate == 1:
    print("Very bad")
elif rate == 2:
    print("Bad")
elif rate == 3:
    print("Satisfactorily")
elif rate == 4:
    print("Good")
elif rate == 5:
    print("Perfect")
else:
    print("Wrong rate!")

# Завдання 4
# Користувач вводить з клавіатури кількість метрів. Програма має запропонувати кілька варіантів перекладу і,
# залежно від вибору користувача, перевести метри в одну або кілька одиниць виміру. Можливі варіанти:
# Перевести в одну з одиниць на вибір: милі, дюйми або ярди.
# Перевести одразу в усі три одиниці (милі, дюйми та ярди) і вивести результати для кожної.
# Перевести в кілометри та сантиметри, якщо користувач обирає цей варіант.

metr = float(input("Enter meters: "))
option = input("Enter one of option: MILES, INCHES, YARDS, ALL, KM & SM ")

miles = 1609.34
inches = 39.37
yards = 1.09

result_mile = float(metr / miles)
result_inch = float(metr * inches)
result_yard = float(metr * yards)

if option == "MILES":
    print("METERS -> MILES : ", round(result_mile, 2))
elif option == "INCHES":
    print("METERS -> INCHES : ", round(result_inch, 2))
elif option == "YARDS":
    print("METERS -> YARDS : ", round(result_yard), 2)
elif option == "ALL":
    print(f"MILES : {result_mile}, INCHES : {result_inch}, YARD : {result_yard}")
elif option == "KM & SM":
    metr_km = metr / 1000
    metr_sm = metr * 100
    print(f"KM : {round(metr_km, 2)}; SM : {round(metr_sm, 2)}")
else:
    print("Wrong option!")

# Завдання 5
# Користувач вводить два числа і вибирає операцію (додавання, віднімання, множення, ділення, знаходження залишку,
# піднесення до степеня). Програма повинна виконати вибрану операцію і вивести результат.

number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))

action = input("Enter one of action: ADD, SUB, MULT, DIV, REM, POW  ")

if action == "ADD":
    print("Result of ADD: ", round(number_1 + number_2, 2))
elif action == "SUB":
    print("Result of SUB: ", round(number_1 - number_2, 2))
elif action == "MULT":
    print("Result of MULT: ", round(number_1 * number_2, 2))
elif action == "DIV":
    print("Result of DIV: ", round(number_1 / number_2, 2))
elif action == "REM":
    print("Result of REM: ", round(number_1 % number_2, 2))
elif action == "POW":
    print("Result of POW: ", round(number_1**number_2, 2))
else:
    print("Wrong action!")


# Завдання 6
# Користувач вводить тризначне число. Програма повинна визначити, чи всі цифри числа однакові.
# Якщо всі цифри однакові, вивести «Всі цифри однакові», інакше — «Цифри різні».

number = int(input("Enter 3-digit number: "))

n_3 = number % 10
n_2 = (number // 10) % 10
n_1 = number // 100

if n_3 == n_2 == n_1:
    print("All numbers are equal")
else:
    print("Numbers are different")
