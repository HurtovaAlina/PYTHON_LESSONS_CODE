# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»
import math


class Student:

    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def get_student_info(self):
        print(f"Ім'я: {self.name}, вік: {self.age}")

students = []
student_1 = Student("John", 25)
student_2 = Student("Alice", 22)
student_3 = Student("Bob", 23)

students.append(student_1)
students.append(student_2)
students.append(student_3)

for student in students:
    student.get_student_info()


# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.

new_students = []
students_qty = 3
for i in range (students_qty):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    new_students.append(Student(name, age))

for student in new_students:
    student.get_student_info()

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return self.radius**2*math.pi

circle_1 = Circle(3)
print(circle_1.circle_area())

# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

class BancAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -= amount
        else:
            print("Can not withdraw")


    def get_account_info(self):
        print(f"Account info: owner {self.owner} current balance {self.balance}")


account = BancAccount("Alina", 1000)
account.get_account_info()
deposit = float(input("Add money to account "))
account.deposit(deposit)
account.get_account_info()

withdraw = float(input("Add amount to withdraw "))
account.withdraw(withdraw)
account.get_account_info()


# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.

class Car:

    def __init__(self, brand, year, is_ready = False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready

    def start_engine(self):
        if not self.is_ready:
            self.is_ready = True

    def move(self):
        if self.is_ready:
            print(f"Car {self.brand} is moving")
        else:
            print(f"Car {self.brand} not ready to move")


car_1 = Car("opel", 2020)
car_2 = Car ("nissan", 2024)

car_1.start_engine()
car_1.move()
car_2.move()
