# Завдання 1
# Користувач вводить числа через кому. Збережіть їх у
# множину. Також створіть власну множину з випадковими
# числами(12 шт). Виведіть наступну інформацію:

import random

numbers = input("Enter numbers ").split(",")
numbers = set(map(int, numbers))
print("User's numbers: ", numbers)

random_numbers = set(random.randint(1, 100) for _ in range(12))
print("Random numbers: ", random_numbers)


#  Максимальне та мінімальне число, введене
# користувачем, а також кількість чисел
print("Max number = ", max(numbers))
print("Min number = ", min(numbers))
print("Qty of numbers = ", len(numbers))

#  Унікальні числа, введені користувачем, яких немає
# серед випадкових
# різниця множин
no_in_random = numbers.difference(random_numbers)
print("Difference: ", no_in_random)

#  Спільні числа, введені користувачем, які є серед
# випадкових
# перетин
both = numbers.intersection(random_numbers)
print("Intersection: ", both)

#  Усі числа, які є або в одній або в іншій множині
# обʼєднання
all_numbers = numbers.union(random_numbers)
print("Union: ", all_numbers)

# Завдання 2
# Напишіть функцію, яка отримує список гостей(гості
# можуть повторюватись) та назву події. Потрібно вивести
# запрошення для кожного гостя і лише один раз.


def welcome_gests(guests, ivent):
    guests = set(guests)
    for guest in guests:
        print(f"Dear Guest {guest}, welcome to the {ivent}")


geusts = [
    "Олена Іваненко",
    "Петро Петренко",
    "Олена Іваненко",
    "Марія Коваль",
    "Ігор Сидоренко",
    "Марія Коваль",
    "Анна Шевченко",
]
ivent = "Dance competition"
welcome_gests(geusts, ivent)


# Завдання 3
# Напишіть функцію, яка отримує два списки з назвами
# товарів для покупок двох знайомих людей. Виведіть наступне
# повідомлення:


#  Товари, які можна купити разом
def goods_for_both(person_1, person_2):
    person_1 = set(person_1)
    person_2 = set(person_2)
    both = person_1.intersection(person_2)
    print("Goods to buy both persons: ", both)


#  Товари, які потрібні лише першій людині
#  Товари, які потрібні лише другій людині
def goods_for_one_person(person_1, person_2):
    person_1 = set(person_1)
    person_2 = set(person_2)
    for_one = person_1.difference(person_2)
    return for_one


person1 = ["хліб", "молоко", "яйця", "сир", "яблука"]
person2 = ["молоко", "банани", "сир", "курка", "рис"]

goods_for_both(person1, person2)
print(f"Goods for first person: {goods_for_one_person(person1, person2)}")
print(f"Goods for second person: {goods_for_one_person(person2, person1)}")


# Завдання 4
# Організатор конференції створив 3 списки учасників:
# зареєстровані, ті хто оплатив участь і ті хто підтвердив свою
# присутність

# Список зареєстрованих учасників
registered = [
    "Іван Петренко",
    "Олена Коваль",
    "Андрій Шевченко",
    "Марія Бондар",
    "Наталія Мельник",
    "Дмитро Савченко",
    "Ірина Ткаченко",
]

# Список тих, хто оплатив участь
paid = ["Іван Петренко", "Олена Коваль", "Марія Бондар", "Дмитро Савченко"]

# Список тих, хто підтвердив свою присутність
confirmed = ["Іван Петренко", "Марія Бондар", "Наталія Мельник", "Марія Іванова"]


# Напишіть функцію, яка отримує ці 3 списки та виводить
# наступну інформацію:
def information_about_participants(registered, paid, confirmed):
    registered = set(registered)
    paid = set(paid)
    confirmed = set(confirmed)
    #  Імена тих, хто зареєструвався, але не оплатив участь
    print(f"Registered but not paid: {registered.difference(paid)}")
    #  Імена тих, хто підтвердив присутність, але не
    # зареєстрований
    print(f"Confirmed but not registered: {confirmed.difference(registered)}")
    #  Імена тих, хто оплатив участь, але не підтвердив
    # присутність
    print(f"Paid but not confirmed: {paid.difference(confirmed)}")
    #  Імена тих, хто зареєструвався і оплатив участь
    print(f"Registered and paid: {registered.intersection(paid)}")
    #  Імена тих хто пройшов усі 3 етапи
    print(f"Confirmed Paid Registered: {confirmed.intersection(registered, paid)}")


information_about_participants(registered, paid, confirmed)


# Завдання 5
# Менеджер організовує навчання для своїх співробітників,
# для чого розділив їх на 3 групи, кожна з яких буде навчатись у
# свій день.
# Напишіть функцію, яка отримує 3 списки з іменами та
# список усіх співробітників. Потрібно перевірити чи не
# помилився менеджер, а саме
#  Чи не забули включити якогось співробітника(якщо так
# то вивести імена всіх, про кого забули)
#  Чи випадково немає співробітників, які опинились у
# двох групах(якщо так то теж вивести повідомлення)

# Всі співробітники
all_workers = [
    "Олександр Іваненко",
    "Марина Кравчук",
    "Артем Бойко",
    "Ірина Сидоренко",
    "Владислав Мельник",
    "Олена Ткаченко",
    "Дмитро Шевчук",
    "Марія Коваль",
    "Андрій Бондар",
    "Наталія Петренко",
    "Світлана Савченко",
    "Ігор Романюк",
    "Дмитро Забутий",
]


# Група розробників (IT-відділ)
developers = [
    "Олександр Іваненко",
    "Марина Кравчук",
    "Артем Бойко",
    "Ірина Сидоренко",
    "Владислав Мельник",
]

# Група маркетологів
marketing = ["Олена Ткаченко", "Дмитро Шевчук", "Марія Коваль", "Андрій Бондар"]

# Група бухгалтерії
accounting = ["Наталія Петренко", "Олена Ткаченко", "Світлана Савченко", "Ігор Романюк"]


def check_groups(all_workers, developers, marketing, accounting):
    all_workers = set(all_workers)
    developers = set(developers)
    marketing = set(marketing)
    accounting = set(accounting)
    assigned = developers.union(marketing, accounting)
    forgotten_workers = all_workers.difference(assigned)
    print(f"Forgotten workers : {forgotten_workers}")
    duplicated_workers = (
        developers.intersection(marketing),
        developers.intersection(accounting),
        marketing.intersection(accounting),
    )
    if duplicated_workers:
        print("There are duplicated workers:", duplicated_workers)
    else:
        print("There are no duplicates")


check_groups(all_workers, developers, marketing, accounting)
