# Завдання 1
# Є список з товарами. Користувач вводить індекс товару,
# який треба вивести. Обробіть виняток

products = ["banana", "apple", "peach", "milk", "bread"]

try:
    index = int(input(f"Enter index "))
    print(products[index])

except IndexError:
    print("Index doesnt exist")
    print(f"Index must be to ")

except ValueError:
    print(f"Not a digit {len(products)-1} ")


# Завдання 2
# Напишіть функцію, яка запитує користувача вік та
# повертає його. Якщо вік неправильний(<0 або >130)
# викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.

def ask_age():
    age  = int(input("Enter your age "))

    if age < 0 :
        raise ValueError("Age < 0 is not allowed")

    if age > 130:
        raise ValueError("Age > 130 is not allowed")

    return age

try:
    age = ask_age()
    print(f"Your age is {age}")

except ValueError as error:
    print(f"Error {error}")


# Завдання 3
# Напишіть функцію, яка запитує користувача номер
# телефону та повертає його. Якщо номер не вірний, тобто не
# починається з +038 або в ньому не 11 символів то викликати
# виняток ValueError.
# Написати код try … except який використовує дану
# функцію.
# Практичне завдання

def ask_number():
    number = input("Enter number ")
    print(number)

    if number[:4] != "+380":
        raise ValueError("Not ukrainian number")

    if number == "":
        raise ValueError("Numbers can not be empty")

    if len(number) != 10:
        raise ValueError("Number is not valid")

    return number

try:
    number = ask_number()
    print(f"Your phone number is {number}")

except ValueError as error:
    print(f"Error {error}")



# Завдання 4
# Організуйте фільтр товарів в онлайн магазині. Усі товари
# діляться на певні категорії, причому один і той самий товар
# може відноситись до різних категорій. Є словник, де ключі –
# назви категорій, а значення – множини з товарами цієї
# категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які
# відносяться одночасно до цих двох категорій.
# Обробіть виняток коли категорії немає в словнику.
# Додатково: змініть код якщо користувач вводить декілька
# категорій.

categories = {
    "Одяг": {"футболка", "штани", "куртка"},
    "Взуття": {"кросівки", "черевики"},
    "Спорт": {"футболка", "кросівки", "шорти"},
    "Знижки": {"футболка", "черевики"}
}

# category_1 = input("Enter category 1 ")
# category_2 = input("Enter category 2 ")

asked_categories = input("Enter categories ").split(", ")
print(asked_categories)

try:
    common_items = categories[asked_categories[0]]
    for category in asked_categories:
        common_items = common_items & categories[category]

    print(common_items)

except KeyError as e:
    print(f"Error {e}")



# Завдання 5
# Організуйте базу даних «Співробітники». Усі дані мають
# зберігатись у словнику де ключ – ім’я людини, значення –
# зарплата. Реалізуйте такий функціонал(через функції):
#  Вивести дані на екран
#  Добавити співробітника
#  Видалити співробітника
#  Показати зарплату співробітника
#  Змінити зарплату співробітнику
# У випадку некоректних даних функції повинні викликати
# винятки з описом помилки


employees = {
    "Андрій": 15000,
    "Марина": 18000,
    "Ігор": 22000
}

def output_employees(employees):
    for employee, salary in employees.items():
        print(f"Employee name: {employee}, salary: {employees[employee]}")

def add_employee(employees):
    employee_name = input("Enter employee name ")

    if employee_name == "":
        raise ValueError("Name can not be empty ")

    if not employee_name.isalpha():
        raise ValueError("Name must contain only letters")

    employee_salary = int(input("Enter employee salary "))

    if employee_salary < 0:
        raise ValueError("Salary can not be < 0")

    employees[employee_name] = employee_salary
    return employees

def remove_employee(employees):

    employee_name = input("Enter employee name to remove ")

    if employee_name not in employees:
        raise KeyError

    employees.pop(employee_name)
    return employees

def show_salary(employees):

    employee_name = input("Enter employee name to show salary ")

    if employee_name not in employees:
        raise KeyError

    print(f" Employee name: {employee_name}, Salary: {employees[employee_name]}")

def update_employee(employees):

    employee_name = input("Enter employee name to update salary ")

    if employee_name not in employees:
        raise KeyError

    new_salary = int(input("Enter employee new salary "))

    if new_salary < 0:
        raise ValueError("Salary can not be < 0")

    employees[employee_name] = new_salary
    return employees


output_employees(employees)

try:
    print("New employee")
    add_employee(employees)
    print("Updated employees ")
    output_employees(employees)

    print("Remove employee ")
    remove_employee(employees)
    output_employees(employees)

    print("Show salary")
    show_salary(employees)

    print("Update salary")
    output_employees(update_employee(employees))


except ValueError as error:
    print(f"Error: {error}")

except KeyError as error:
    print(f"Key Error: {error}")


