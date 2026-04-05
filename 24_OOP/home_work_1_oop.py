# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

class Cart:

    def __init__(self, client):
        self.client = client.capitalize()
        self.items = []

    def add_item(self, item):
        self.items.append(item.lower())

    def remove_item(self, item):
        item = item.lower()
        try:
            self.items.remove(item)
            print(f"Item {item} was removed from the Cart")
        except ValueError:
            print(f"Item {item} is not in the Cart")

    def print_cart(self):
        print(f"{self.client} has items {self.items} in the Cart")

client_name = input("Enter client name ")
client_1 = Cart(client_name)
qty_items = int(input("Enter quantity of items "))

for i in range(1, qty_items+1):
    item_name  = input("Enter item ")
    client_1.add_item(item_name)

print("Items were added to the Cart")
client_1.print_cart()

item_to_remove = input("Enter item to remove ")
client_1.remove_item(item_to_remove)
client_1.print_cart()


# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон

class Phone:

    def __init__(self, number, battery_level):
        self.number = number
        self.battery_level = battery_level

    def decrease_battery_level(self, value):
        if self.battery_level - value >=20:
            self.battery_level -=value
            print(f"Battery level was decreased by {value}")
            print(f"New battery level {self.battery_level}%")
        else:
            print("Low battery!")

    def phone_info(self):
        print(f"Your phone with number: {self.number} has battery level {self.battery_level}%")

phone_1 = Phone("+380661234567", 100)
try:
    battery_level = int(input("Enter value to decrease battery level "))
    phone_1.decrease_battery_level(battery_level)
except ValueError:
    print("You must enter a digits!")

phone_1.phone_info()
