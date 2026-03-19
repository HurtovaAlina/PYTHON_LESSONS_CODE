# Завдання 1
# Користувач вводить через кому список товарів. Виведіть
# цей список на екран, але без повторень назв товарів

list_to_buy = input("Enter list of goods that you want to buy ").split(", ")

list_without_duplicates = set(list_to_buy)
print(list_without_duplicates)

# Завдання 2
# У магазині є два списки клієнтів: ті хто отримав знижкові
# купони, і ті хто ними скористався.
# Напишіть функцію, яка отримує 2 списки та виводить
# інформацію:
#  Імена тих, хто отримав купон, але не скористався,
# також вивести їх кількість
#  Імена шахраїв, які скористались знижкою, але магазин
# не давав їм купони

received_discount = [
    "Оксана Литвин",
    "Ігор Коваленко",
    "Марина Гончар",
    "Андрій Мазур",
    "Світлана Дяченко",
    "Роман Білан"
]

used_discount = [
    "Оксана Литвин",
    "Марина Гончар",
    "Роман Білан",
    "Тетяна Кравець"
]

def check_discount(received_discount, used_discount):
    received_discount = set(received_discount)
    used_discount = set(used_discount)

    received_not_used = received_discount.difference(used_discount)
    qty_not_used = len(received_not_used)
    print(f"Received but not used discount of {qty_not_used} persons", received_not_used)

    used_by_frauds = used_discount.difference(received_discount)
    print("Used but not received discount ", used_by_frauds)

check_discount(received_discount, used_discount)