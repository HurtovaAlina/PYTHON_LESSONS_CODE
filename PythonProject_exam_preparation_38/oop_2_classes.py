# 14. Інтернет-магазин
# Клас Product: атрибути — назва (str), ціна (float).
# Клас Cart (кошик): список товарів.
# Метод add_item(product): додає товар до кошика.
# Метод remove_item(name): видаляє товар за назвою.
# Метод total(): обчислює і повертає загальну суму всіх товарів у кошику.
# Метод display(): виводить вміст кошика і загальну суму.
from typing import List


class Product:

    def __init__(self, name: str, price:float):
        self.name = name.lower()
        self.price = price


class Cart:

    def __init__(self):
        self.products: List[Product] = []


    def add_item(self, product: Product):
        for p in self.products:
            if p.name == product.name:
                print("Product already in the Cart")
                return

        self.products.append(product)
        print(f"Product {product.name} was added")


    def remove_item(self, name):
        for i in range(len(self.products)):
            if self.products[i].name == name:
                removed_item = self.products.pop(i)
                print(f"Product {removed_item.name} was removed")
                return

        print("Product was not found")


    def total(self)-> float:
        total = 0
        for product in self.products:
            total+=product.price
        return total #return sum(product.price for product in self.products)

    def display_cart(self):
        print("Products in Cart")
        for product in self.products:
            print(f"Name: {product.name}, "
                  f"Price: {product.price:.2f}"
                  )
        print(f"Total = {self.total()}")


products = Cart()
qty_products = int(input("Enter qty of products do you want to add "))
for i in range(qty_products):
    name = input("Enter product name ").lower()
    price = float(input("Enter product price "))
    products.add_item(Product(name, price))

products.display_cart()
product_to_remove = input("Enter product do you want to remove ").lower()
products.remove_item(product_to_remove)
products.display_cart()






# 15. Телефонна книга
# Клас Contact: атрибути — ім'я (str), номер телефону (str).
# Клас PhoneBook: список контактів.
# Методи: add_contact(contact), remove_contact(name), find_contact(name) — пошук за
# частиною імені, show_all() — всі контакти за алфавітом.


# 16. Плейлист
# Клас Song: атрибути — назва (str), виконавець (str).
# Клас Playlist: назва плейлиста (str), список пісень.
# Методи: add_song(song), remove_song(title), find_song(title), show() — виводить усі пісні
# з нумерацією.
