# Завдання 1
# Користувач вводить імена людей, поки не введе порожній
# рядок. Збережіть усі імена в множині. Якщо ім’я вводиться
# повторно, то вивести повідомлення про це.
# Виведіть кількість людей

#
# all_people = set()
# while True:
#     name = input("Enter name ")
#
#     if name == "":
#         print("Program is finished")
#         break
#
#     if name in all_people:
#         print("Person is already in the list")
#
#     else:
#         all_people.add(name)
#
# print(set(all_people))


# Завдання 2
# Студентів розбили на 2 групи, кожна з яких навчається у
# свій день. Перевірте чи не виникло помилки, а саме
#  Чи немає студентів які є в двох групах одночасно(якщо
# є, то вивести їх імена)
#  Чи немає студентів, про яких забули(якщо є, то вивести
# імена)
# Напишіть відповідну функцію, яка отримує два списки з
# іменами студентів кожної групи, та список усіх студентів.
# Додатково: змініть код, якщо груп 3

# def check_students_in_groups(students, group_1, group_2):
#
#     """
#      Чи немає студентів які є в двох групах одночасно(якщо
#     є, то вивести їх імена)
#
#     Чи немає студентів, про яких забули(якщо є, то вивести
#     імена)
#     """
#     students = set(students)
#     group_1 = set(group_1)
#     group_2 = set(group_2)
#
#     students_in_groups = group_1.union(group_2)
#     forgotten_students = students.difference(students_in_groups)
#     print(f"Forgotten students {forgotten_students}")
#
#     students_in_both_groups = group_1.intersection(group_2)
#     print(f"Students in both groups {students_in_both_groups}")
#
#
# students = ["Anna", "Ivan", "Oleg", "Maria", "Dmytro", "Sofia"]
#
# group_1 = ["Ivan", "Oleg", "Maria"]
# group_2 = ["Maria", "Dmytro", "Sofia"]
#
# check_students_in_groups(students, group_1, group_2)


# Завдання 3
# Є словник з цінами продуктів, де ключ – назва продукту, а
# значення – ціна за кг. Організуйте просту роботу магазину:
# користувач вводить назву продукту та вагу, потрібно вивести
# загальну ціну.
# Практичне завдання

# products = {
#     "apple": 3.5,
#     "banana": 2.8,
#     "orange": 4.2,
#     "potato": 1.5,
#     "tomato": 3.9
# }
#
# product_name = input("Enter product ")
#
# if product_name in products:
#     weight = float(input("Enter weight "))
#     total_price = round(products[product_name]*weight, 2)
#     print(f"Total price for {product_name} with weight {weight} is {total_price}")
# else:
#     print("Product doesn't exist")


#
# Завдання 4
# Є словник з інформацією про вміст вітаміну С в різних
# продуктах, де ключ – назва продукту, значення – вміст
# вітаміну С у мг. Користувач вводить свій раціон: список з
# назвами продуктів
# Обчисліть вміст вітаміну С в раціоні(якщо у словнику
# немає якогось продукту, вважайте вміст вітаміну рівним 0 мг).
# Виведіть продукт з найбільшим вмістом вітаміну С.
#
# products_vitamin_c = {
#     "orange": 53,
#     "lemon": 53,
#     "kiwi": 92,
#     "strawberry": 59,
#     "broccoli": 89,
#     "pepper": 128
# }
#
# diet = input("Enter your diet (products separated by comma) ").split(", ")
# print(diet)
#
# vitamin_c_total = 0
# diet_with_vitamin_c = {}
#
# for product in diet:
#     if product in products_vitamin_c:
#         vitamin_c_total += products_vitamin_c[product]
#         diet_with_vitamin_c[product] = products_vitamin_c[product]
#
# if diet_with_vitamin_c:
#     max_product = max(diet_with_vitamin_c, key=diet_with_vitamin_c.get)
#     print(f"Product in your diet with max vitamin C: {max_product}")
# else:
#     print("No products with vitamin C found")
#
# print(f"Total vitamin C {vitamin_c_total}")
#


# Завдання 5
# Склад футбольної команди розподіляється між такими
# позиціями:
#  воротар – 1
#  захисник – 4
#  півзахисник – 4
#  нападник – 2
# Користувач поступово вводить імена гравців та їх позиції.
# Потрібно зберегти ці дані у словник, де ключ – назва позиції,
# значення – список з іменами гравців на цю позицію. Перевірте
# чи склад команди правильний.
# Також виведіть імена всіх гравців.


def free_position(team, limits):
    free_positions = {}
    for position, players in team.items():
        if len(players) < limits[position]:
            free_positions[position] = limits[position] - len(players)
    return free_positions


team = {"воротар": [], "захисник": [], "півзахисник": [], "нападник": []}

limits = {"воротар": 1, "захисник": 4, "півзахисник": 4, "нападник": 2}

while True:
    if free_position(team, limits):
        player = input("Enter player ")
        position = input("Enter position ")

        if player == "":
            print("Player can not be empty")
            continue

        if player in sum(team.values(), []):
            print(f"Player {player} is already in the team")
            continue

        if position in team:
            if len(team[position]) < limits[position]:
                team[position].append(player)
            else:
                print(f"Position {position} is already full")
                print(f"Free postions {free_position(team, limits)}")
        else:
            print("Position doesn't exist")
            continue
    else:
        print("Team is completed")
        print(team)
        break


# Завдання 6
# Організуйте фільтр товарів в онлайн магазині. Усі товари
# діляться на певні категорії, причому один і той самий товар
# може відноситись до різних категорій. Є словник, де ключі –
# назви категорій, а значення – множини з товарами цієї
# категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які
# відносяться одночасно до цих двох категорій.
# Додатково: змініть код якщо користувач вводить декілька
# категорій.
