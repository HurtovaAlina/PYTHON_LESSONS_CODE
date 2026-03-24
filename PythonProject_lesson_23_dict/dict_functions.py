# Є словник, де ключ — ім’я учня, а значення — множина гуртків,
# які він відвідує.
# Реалізуйте функціонал:
# 1 -- додати нового учня
# 2 -- додати новий гурток для учня
# 3 -- видалити гурток для учня
# 4 -- показати учнів які відвідують певний гурток(и)
# 5 -- для двох учнів показати гуртки які вони відвідують разом
# 6 -- вивести всю інформацію.
# 7 -- вивести усі згадані гуртки


StudentsDict = dict[str, set[str]]  # тип для зручності


def get_student_name() -> str:
    """
    Запитує в користувач ім'я студента поки не буде
    введено правильно

    :return: str ім'я студента
    """
    while True:
        student = input("Введіть ім'я студента: ")
        student = student.strip()
        student = student.capitalize()  # зробити першу літеру великою

        # перевірки на неправильність
        if student == "":
            print("Ви нічого не ввели")
            continue

        if not student.isalpha():
            print("Має місти лише літери")
            continue

        return student


def is_student_registered(students: StudentsDict, student: str) -> bool:
    """
    Перевіряє чи студент зареєстрований

    :param students: словник зі студентами та їхніми гуртками
    :param student:  ім'я студента
    :return: bool
    """
    # if student in students:
    #     return True
    # return False

    return student in students


def add_student(students: StudentsDict, student: str) -> None:
    """
    Додає нового учня до словника.

    :param students: dict - Словник, де ключ — ім'я учня, значення — множина гуртків
    :param student: str - Ім'я нового учня
    :return: None
    """

    # перевіряє чи цей студент вже є в словнику
    if is_student_registered(students, student):
        print("Студент вже зареєстрований")
        return  # функція закінчила роботу

    # return не спрацював -> студент не зареєстрований
    students[student] = set()  # {} -- порожній словник


def add_club_for_student(students: StudentsDict, student: str, new_club: str) -> None:
    """
    Додає новий гурток для вказаного учня.
    Якщо студент не зареєстрований -- реєструє його

    :param students: dict - Словник учнів та їх гуртків
    :param student: str - Ім'я учня
    :param new_club: str - Назва гуртка, який потрібно додати
    :return: None
    """

    # чи немає студента в словнику
    if not is_student_registered(students, student):
        print(f"Студент {student} не зареєстрований")
        add_student(students, student)
        print(f"Студент {student} був зареєстрований")

    if new_club in students[student]:
        print("Студент вже відвідує цей гурток")
        return

    clubs = students[student]
    clubs.add(new_club)

    # students[student].add(new_club)


def remove_club_for_student(students: StudentsDict, student: str, club: str) -> None:
    """
    Видаляє гурток для вказаного учня.

    :param students: dict - Словник учнів та їх гуртків
    :param student: str - Ім'я учня
    :param club: str - Назва гуртка, який потрібно видалити
    :return: None
    """
    if not is_student_registered(students, student):
        print(f"Студент {student} не зареєстрований")
        return

    if club not in students[student]:
        print("Студент не відвідує даний гурток")
        return

    # видалення гуртка
    clubs = students[student]
    clubs.remove(club)


def get_students_by_clubs(students: StudentsDict, target_clubs: set[str]) -> list[str]:
    """
    Повертає список учнів, які відвідують ВСІ вказані гуртки.

    :param students: dict - Словник учнів та їх гуртків
    :param target_clubs: set - Множина гуртків для пошуку
    :return: list[str] - Список імен учнів, які відвідують ці гуртки
    """

    attenders = []  # студенти що відвідують усі гуртки

    for student in students:
        student_clubs = students[student]

        # гуртки з target_clubs які студент НЕ відвідує
        not_attended = target_clubs - student_clubs

        if len(not_attended) == 0:
            attenders.append(student)

    return attenders


def get_common_clubs_for_two_students(
    students: StudentsDict, student1: str, student2: str
) -> set[str]:
    """
    Повертає гуртки, які два учні відвідують разом.

    :param students: dict - Словник учнів та їх гуртків
    :param student1: str - Ім'я першого учня
    :param student2: str - Ім'я другого учня
    :return: set[str] - Множина спільних гуртків.
    """

    if not is_student_registered(students, student1):
        print(f"Студент {student1} не зареєстрований")
        return

    if not is_student_registered(students, student2):
        print(f"Студент {student2} не зареєстрований")
        return

    student1_clubs = students[student1]
    student2_clubs = students[student2]

    common_clubs = student1_clubs & student2_clubs

    return common_clubs


def print_all_info(students: StudentsDict) -> None:
    """
    Виводить всю інформацію про учнів та їхні гуртки.

    :param students: dict - Словник учнів та їх гуртків
    :return: None
    """

    for student in students:
        clubs = students[student]

        print(student)
        for club in clubs:
            print(f"   {club}")

        print()


def get_all_clubs(students: StudentsDict) -> set[str]:
    """
    Повертає множину всіх згаданих гуртків.

    :param students: dict - Словник учнів та їх гуртків
    :return: set[str] - Множина усіх гуртків, які відвідують будь-які учні
    """

    all_clubs = set()
    for club in students.values():
        # all_clubs = all_clubs.union(club)
        all_clubs |= club

    return all_clubs


def show_menu() -> None:
    print("\n=== Меню ===")
    print("1 — Додати учня")
    print("2 — Додати гурток учню")
    print("3 — Видалити гурток у учня")
    print("4 — Знайти учнів за набором гуртків (через кому)")
    print("5 — Спільні гуртки двох учнів")
    print("6 — Вивести всю інформацію")
    print("7 — Вивести список усіх гуртків")
    print("0 — Вихід")


def main():
    students: StudentsDict = {}  # 1. Початковий словник

    students = {
        "Степан": {"Плавання", "Іспанська"},
        "Марія": {"Python", "Танці"},
        "Софія": {"Плавання", "Танці", "Малювання"},
    }

    while True:  # 2. Нескінченний цикл
        show_menu()
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            name = input("Введіть ім'я учня: ")
            add_student(students, name)

        elif choice == "2":
            name = input("Ім'я учня: ")
            club = input("Назва гуртка: ")
            add_club_for_student(students, name, club)

        elif choice == "3":
            name = input("Ім'я учня: ")
            club = input("Назва гуртка для видалення: ")
            remove_club_for_student(students, name, club)

        elif choice == "4":
            clubs = input(
                "Введіть гуртки через кому (наприклад: 'Шахи, Плавання'): "
            ).split(", ")
            clubs = set(clubs)
            result = get_students_by_clubs(students, clubs)

            if not clubs:
                print("⚠️ Ви не вказали жодного гуртка.")
            elif result:
                print("✅ Учні, що відвідують усі ці гуртки:")
                for name in sorted(result):
                    print(f" • {name}")
            else:
                print("ℹ️ Не знайдено учнів за заданим набором гуртків.")

        elif choice == "5":
            name1 = input("Перше ім'я: ")
            name2 = input("Друге ім'я: ")
            common = get_common_clubs_for_two_students(students, name1, name2)
            if name1.strip() not in students:
                print(f"⚠️ Учня '{name1.strip()}' не знайдено.")
            if name2.strip() not in students:
                print(f"⚠️ Учня '{name2.strip()}' не знайдено.")
            if common:
                print("✅ Спільні гуртки:")
                for c in sorted(common):
                    print(f" • {c}")
            else:
                print(
                    "ℹ️ Спільних гуртків не знайдено або одного з учнів немає у списку."
                )

        elif choice == "6":
            print_all_info(students)

        elif choice == "7":
            clubs = get_all_clubs(students)
            if clubs:
                print("📚 Усі наявні гуртки:")
                for c in sorted(clubs):
                    print(f" • {c}")
            else:
                print("ℹ️ Поки що немає жодного гуртка.")

        elif choice == "0":
            print("👋 Вихід. До зустрічі!")
            break

        else:
            print("❌ Невірний вибір. Будь ласка, оберіть пункт з меню (0–7).")


if __name__ == "__main__":
    main()


# students = {
#     "Степан": {"Плавання", "Іспанська"},
#     "Марія": {"Python", "Танці"},
#     "Софія": {"Плавання", "Танці", "Малювання"}
# }
#
# students["Степан"].add("Малювання")
#
# student1_clubs = {"Плавання", "Іспанська"}
# student2_clubs = {"Плавання", "Танці", "Малювання"}
#
# common_clubs = student1_clubs.intersection(student2_clubs)
# common_clubs = student1_clubs & student2_clubs
#
# print(common_clubs)
#
# # total = 0
# # for num in nums:
# #     total += num
#
# all_clubs = set()
# for club in students.values():
#     #all_clubs = all_clubs.union(club)
#     all_clubs |= club
#
# print(all_clubs)
