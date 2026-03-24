"""
модуль для роботи з геометричними фігурами

"""

pi = 3.14


def get_circle_area(radius: float) -> float:
    """
    Рахує радіус кола
    :param radius: радіус кола
    :return: площа кола
    """
    print("Circle area")
    return pi * radius**2


def get_circle_perimetr(radius: float) -> float:
    print("Circle perimetr")
    return 2 * pi * radius


if (
    __name__ == "__main__"
):  # перевіряє чи файл запущений НЕ через імпорт, а напряму є головним (тоді якщо файл,
    # запущений через імпорт - все, що після  if __name__ == "__main__" не буде запущено)
    print("Hello from geometry")
    radius = float(input("Enter radius: "))

    res = get_circle_perimetr(radius)
    print(f"Perimeter: {res}")
