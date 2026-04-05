# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального
import random
from typing import Dict, List



class Car:

    def __init__(self, mark: str, mileage: float, fuel_level : float):

        self.mark = mark
        self.mileage = mileage
        self.fuel_level = fuel_level
        self.fuel_consumption : float = 0.1
        self.is_working = True

    def show_info(self):
        print(f"Марка: {self.mark}")
        print(f"Пробіг: {self.mileage} км")
        print(f"Рівень пального: {self.fuel_level} л")
        print(f"Розхід пального: {self.fuel_consumption} л/км")
        print(f"Стан: {'працює' if self.is_working else 'не працює'}")


    def move(self, distance : float):
        fuel_for_distance = distance * self.fuel_consumption
        if fuel_for_distance <= self.fuel_level:
            if self.is_working:
                self.mileage += distance
                self.fuel_level -= fuel_for_distance
                if round(random.random(), 2) < 0.4:
                    self.is_working = False
                    print("Car needs to be repaired")
            else:
                print("Car is not working")
        else:
            print("Low level of fuel")
            print("Increase fuel level")

    def repair(self):
        self.is_working = True
        print("Car was repaired")

    def refueling(self, fuel_value: float):
        self.fuel_level += fuel_value
        print(f"Fuel level was increased on {fuel_value} l")


car = Car("Nissan", 55000, 30.6)
car.show_info()

distance = 100
print(f"Car is moving the distance {distance} km")
car.move(distance)
car.show_info()

if not car.is_working:
    car.repair()

car.refueling(35.00)
car.show_info()

# Завдання 4
# Створіть клас Студент з атрибутами:
#  ім’я
#  словник з предметами, де ключ – назва предмету,
# значення – список оцінок
# Додайте методи:
#  додати новий предмет
#  видалити предмет
#  вчити предмет(якщо отримана оцінка, то додати про це
# інформацію)
#  отримати середню оцінку за конкретним предметом
#  вивести загальну інформацію: ім’я та список предметів
# з середніми оцінками

class Student:

    def __init__(self, name: str):
        self.name = name
        self.subjects: Dict[str, List[int]] = {}

    def add_subject(self, subject_name):
        if subject_name in self.subjects:
            print(f"Subject with {subject_name} already exists")
        else:
            self.subjects[subject_name] = []

    def remove_subject(self, subject_name):
        if subject_name in self.subjects:
            self.subjects.pop(subject_name)
        else:
            print(f"Subject with {subject_name} not found")

    def learn_subject(self, subject_name, mark = None) -> dict[str, list[int]]:
        if mark is not None:
            self.subjects[subject_name].append(mark)
            print(f"Mark {mark} was given for subject {subject_name}")
            return self.subjects
        else:
            print(f"Subject {subject_name} doesn't have marks yet")
            return self.subjects

    def avg_mark(self, subject_name) -> float | None:
        if subject_name not in self.subjects:
            print(f"Subject '{subject_name}' not found")
            return None
        else:
            marks = self.subjects[subject_name]
            if not marks:
                return 0
            else:
                return sum(marks)/len(marks)

    def show_info(self):
        print(f"Student: {self.name}")
        print("Subjects list with average mark")
        for subj in self.subjects:
            avg = self.avg_mark(subj)
            print(f"{subj}: {avg:.2f}")

student = Student("Alina")
student.add_subject("Math")
student.add_subject("Math")

student.add_subject("English")
student.add_subject("Programming")
student.learn_subject("Math")
student.learn_subject("English", 4)
student.learn_subject("English", 5)
student.learn_subject("English", 3)
student.learn_subject("English", 5)

student.learn_subject("Programming", 5)
student.learn_subject("Programming", 4)
student.learn_subject("Programming", 4)
student.learn_subject("Programming", 4)

student.show_info()
student.remove_subject("Deutsch")
student.remove_subject("Math")



# Завдання 5
# Створіть клас Магазин з атрибутами:
#  назва
#  заробіток
#  словник з товарами, де ключ – назва товару, значення –
# кількість на складі
#  словник з товарами, де ключ – назва товару, значення –
# ціна
# Додайте методи:
#  вивід інформації: назва та список доступних товарів
#  поповнення складу певним товаром(може бути новий)
#  оформлення замовлення, якщо товар у достатній
# кількості доступний

class Shop:

    def __init__(self, name):

        self.name = name
        self.income: float = 0
        self.qty_items: Dict[str, int] = {}
        self.price_items: Dict[str, float] = {}

    def show_items_in_stock(self):
        print(f"Shop : {self.name}")
        for item, qty in self.qty_items.items():
            if qty > 0:
                price = self.price_items[item]
                print(f"{item}: qty {qty}, price {price}")

    def add_item(self, item, qty, price):
        if item not in self.qty_items:
            self.qty_items[item] = qty
            self.price_items[item] = price
        else:
            self.qty_items[item] += qty
            self.price_items[item] = price

    def create_order(self, item, qty):
        if item in self.qty_items:

            if qty <= self.qty_items[item]:
                self.qty_items[item] -= qty
                order_total = self.price_items[item]*qty
                print(f"You purchased {item}, with qty {qty} and paid {order_total}")
            else:
                print(f"This qty = {qty} of the {item} is out of stok, try less value")
        else:
            print(f"Item {item} is not found")


shop = Shop("Varus")

shop.add_item("banana", 340, 35.60)
shop.add_item("chocolate", 20, 90.00)
shop.add_item("juice", 200, 67.80)
shop.add_item("cake", 56, 45.00)
shop.add_item("apple", 230, 29.60)

print("Items in stock")
shop.show_items_in_stock()
shop.create_order("banana", 20)
shop.create_order("cake", 90)
shop.create_order("apple", 15)
