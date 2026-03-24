# Завдання 1
# Напишіть функцію, яка отримує 2 словника та об’єднує їх
# в один. Якщо ключі співпадають то потрібно додати
# відповідні їм значення.
import re


def total_working_hours(working_hours, working_hours_overtime):
    total_hours = working_hours.copy()

    for name in working_hours_overtime:
        if name in total_hours:
            total_hours[name] += working_hours_overtime[name]
        else:
            total_hours[name] = working_hours_overtime[name]

    return total_hours


working_hours = {"John": 10, "Mary": 20, "Den": 30}

working_hours_overtime = {"John": 2, "Anna": 5, "Den": 4}

total = total_working_hours(working_hours, working_hours_overtime)
print(total)


# Завдання 2
# Напишіть функцію, яка отримує словник та інвертує його,
# тобто повертає новий словник, де ключі та значення змінені
# місцями.
#
def reverse_dist(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict


dictionary = {"John": 10, "Mary": 20, "Den": 30}

print(reverse_dist(dictionary))


# Завдання 3
# Користувач вводить назви товарів та їх ціни поки не введе
# порожній рядок. Збережіть дані у словник. Якщо користувач
# вводить товар повторно та треба додати стару та нову ціни.
# В кінці виведіть таблицею товар – ціна. Також виведіть
# загальну ціну.

items = {}
total_price = 0

while True:
    key = input("Enter item name ")

    if key != "":
        value = float(input("Enter price "))
        if key in items:
            items[key] += value
            total_price += value
        else:
            items[key] = value
            total_price += value
    else:
        break

print(items)
for key, value in items.items():
    print(key, "-", value)
print(total_price)

# Завдання 4
# Напишіть функцію, яка отримує текст та повертає
# словник, де ключі – це слова, а значення – їхня кількість в
# тексті.
# Добавте параметр за замовчуванням який визначає, чи
# значення в словнику будуть кількостями слів, чи
# частотою(відсотком від загальної кількості).


def text_to_dictionary(text, qty=True):
    deleted_punctuation = re.sub(r"[^\w\s]", "", text)
    text = deleted_punctuation.split()

    total_letters = 0
    for word in text:
        total_letters += len(word)

    new_dictionary = {}
    for word in text:
        if qty:
            new_dictionary[word] = len(word)
        else:
            new_dictionary[word] = round((len(word) / total_letters) * 100, 2)
    return new_dictionary


print(text_to_dictionary("Fflgjfh ghjj - ghfghdgh, ryththy.", False))

###############################################################################


def text_to_dictionary(text, qty):
    deleted_punctuation = re.sub(r"[^\w\s]", "", text)
    text = deleted_punctuation.split()

    total_words = len(text)
    print(total_words)
    new_dictionary = {}

    for word in text:
        if word in new_dictionary:
            new_dictionary[word] += 1
        else:
            new_dictionary[word] = 1

    if not qty:
        for word in new_dictionary:
            new_dictionary[word] = round((new_dictionary[word] / total_words) * 100, 2)

    return new_dictionary


print(text_to_dictionary("Fflgjfh ghfghdgh ghjj - ghfghdgh, ghjj ryththy ghjj.", False))

# Завдання 5
# Створіть словник, де ключі – це назви груп, а значення –
# списки студентів, що належать до цих груп.
# Реалізуйте 3 функції для додавання та видалення студентів
# з груп, а також для виведення даних на екран

groups = {
    "Group A": ["John", "Mary", "Den"],
    "Group B": ["Anna", "Kate", "Tom"],
    "Group C": ["Mike", "Sara"],
}


def add_student(group, student):
    if group in groups:
        groups[group].append(student)
    else:
        groups[group] = [student]
    print(f"Added student {student} to {group}")


def delete_student(student):
    for group, students in groups.items():
        if student in students:
            students.remove(student)
    print(f"Deleted student {student} from {group}")


def print_groups_of_students():
    for group, students in groups.items():
        print(f"{group} - {students}")


add_student("Group C", "Alina")
print_groups_of_students()
delete_student("Alina")
print_groups_of_students()


# Завдання 6
# Напишіть функцію, яка запитує в користувача ім’я, вік,
# посаду та повертає ці дані у вигляді словника.
# Створіть іншу функцію, яка добавляє 5 людей у словник,
# де ключ ім’я, а значення – словник з попередньої функції.
# Після чого виведіть середній вік.


def name_age_position():
    users_info = {}

    users_info["name"] = input("Enter name: ")
    users_info["age"] = int(input("Enter age: "))
    users_info["position"] = input("Enter position: ")

    return users_info


def add_users(user_num):
    new_users_info = {}
    for i in range(user_num):
        user_info = name_age_position()
        new_users_info[user_info["name"]] = user_info

    return new_users_info


def avg_age(new_users_info):
    total_age = sum(user["age"] for user in new_users_info.values())
    return round(total_age / len(new_users_info), 2)


new_users = add_users(3)
print(new_users)
print(avg_age(new_users))
