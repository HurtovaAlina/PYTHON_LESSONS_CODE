# Хрестики Нулики

# глобальні змінні
# хрестик
# нулик

# функції(підзадачі)
# створення сітки -- list[list[str]]

# добавити новий елемент на сітку(отримує координати та символ)

# спитати користувача куди добавити новий символ(отримує ім'я користувача)
# уточнює якщо клітинка занята

# перевірка(хто виграв)
# варіанти результату
#   * хрестик
#   * нулик
#   * None -- нічия

# перевірка чи гра все ще триває(чи є вільне місце)

# main -- головна функція, організовує вся роботуґзапускає програму


from typing import Literal

# Тип для символів на сітці
CROSS = "X"
ZERO = "O"
EMPTY = " "
Symbol = Literal["X", "O"]
Cell = Literal["X", "O", " "]  # " " — порожня клітинка


def create_grid(size: int = 3) -> list[list[Cell]]:
    """
    Створює і повертає порожню сітку для гри «Хрестики-нулики».

    :param size: int - Розмір квадратної сітки (типово 3x3)
    :return: list[list[Cell]] - Двовимірний список, що представляє ігрове поле.
             Кожна клітинка містить "X", "O" або " " (пробіл для порожньої).
    """

    grid = list()
    for i in range(size):
        row = list()
        for j in range(size):
            row.append(EMPTY)
        grid.append(row)
    return grid


def print_grid(grid: list[list[Cell]]) -> None:
    """
    Виводить поточний стан сітки на екран у зручному для читання вигляді.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: None
    """
    # ---+---+---
    #    | X | O
    # ---+---+---
    #  O |   | X
    for row in grid:
        print(" " + " | ".join(row) + "  ")
        print("---+" * (len(row) - 1), "---", sep="")


def add_symbol_to_grid(
    grid: list[list[Cell]], row: int, col: int, symbol: Symbol
) -> bool:
    """
    Додає новий символ на сітку за вказаними координатами.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :param row: int - Індекс рядка (0-based).
    :param col: int - Індекс стовпчика (0-based).
    :param symbol: Symbol - Символ гравця ("X" або "O").
    :return: bool - True, якщо хід успішний (клітинка була вільна),
                    False, якщо клітинка вже зайнята або координати некоректні.
    """

    l = len(grid)
    # 1. Перевірити, що row і col в межах розміру сітки.
    if row < 0 or row >= l or col < 0 or col >= l:
        print("Error, you are outside")
        return False
    # 2. Перевірити, що в цій клітинці зараз " " (порожньо).
    # 3. Якщо все ок — записати symbol у grid[row][col] і повернути True.
    if grid[row][col] == " ":
        grid[row][col] = symbol
        return True
    else:
        # 4. Інакше повернути False.
        print("This place is not empty")
        return False


def ask_user_move(player_name: str, grid: list[list[Cell]]) -> tuple[int, int]:
    """
    Запитує у користувача, куди поставити новий символ.

    Повинна:
    - запитати координати (рядок і стовпчик),
    - перевірити, що клітинка вільна,
    - у разі помилки (зайнята/некоректна) — попросити ввести ще раз.

    :param player_name: str - Ім'я поточного гравця (наприклад, "Гравець X").
    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: tuple[int, int] - Пара (row, col) з коректними координатами для ходу.
    """

    l = len(grid)
    # 1. В циклі питати в користувача рядок та стовпчик (через input()).
    while True:
        row = int(input(f" {player_name} Enter row "))
        col = int(input(f" {player_name} Enter column "))

        # 2. Якщо все добре — повернути (row, col).
        return (row, col)


def check_winner(grid: list[list[Cell]]) -> Symbol | None:
    """
    Перевіряє, чи є переможець на поточній сітці.

    Перевіряються:
    - усі рядки,
    - усі стовпці,
    - дві діагоналі (головна і побічна).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: Optional[Symbol] - "X", якщо виграв хрестик,
                                "O", якщо виграв нулик,
                                None, якщо переможця ще немає.
    """

    l = len(grid)

    # --- Рядки ---
    # 1. Перевірити кожний рядок: всі елементи однакові та не " ".
    for row in grid:
        first_el = row[0]
        if first_el != EMPTY and all(cell == first_el for cell in row):
            return first_el  # Якщо знайдено три однакові символи ("X" або "O") — повернути X або О.

    # --- Стовпці ---
    # 2. Перевірити кожний стовпець.
    for col in range(l):
        first_el = grid[0][col]
        if first_el != EMPTY and all(grid[row][col] == first_el for row in range(l)):
            return first_el  # Якщо знайдено три однакові символи ("X" або "O") — повернути X або О.

    # 3. Перевірити дві діагоналі.
    # --- Головна діагональ ---
    first_el = grid[0][0]
    if first_el != EMPTY and all(grid[i][i] == first_el for i in range(l)):
        return first_el  # Якщо знайдено три однакові символи ("X" або "O") — повернути X або О.

    # --- Побічна діагональ ---
    first_el = grid[0][l - 1]
    if first_el != EMPTY and all(grid[i][l - 1 - i] == first_el for i in range(l)):
        return first_el  # Якщо знайдено три однакові символи ("X" або "O") — повернути X або О.

    return None  # Якщо переможця немає — повернути None.


def has_empty_cells(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи є на сітці ще вільні (порожні) клітинки.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо є хоч одна порожня клітинка,
                    False, якщо поле повністю заповнене.
    """
    for row in grid:
        if EMPTY in row:
            return True
    return False


def is_game_over(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи гра завершена.

    Гра завершується, якщо:
    - є переможець, або
    - немає вільних клітинок (нічия).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо гра завершена, False інакше.
    """
    # 1. Використати check_winner().
    if check_winner(grid):
        print("Winner is ", check_winner(grid), " Congrats!!! ", current_player)
        return True  # 3. Повернути True, якщо є переможець або немає порожніх клітинок.
    elif (
        not has_empty_cells(grid) and check_winner(grid) is None
    ):  # 2. Використати has_empty_cells().
        print("Draw in the game")
        return True  # 3. Повернути True, якщо є переможець або немає порожніх клітинок.
    else:
        return False


def switch_player(player: Symbol) -> str:
    """
    Змінює поточного гравця.

    :param player: Symbol - Поточний символ гравця ("X" або "O").
    :return: Symbol - Інший символ ("O" якщо був "X", і навпаки).
    """
    # повернути "O" якщо player == "X", і "X" якщо player == "O".
    return ZERO if player == CROSS else CROSS


def main() -> None:
    """
    Головна функція. Організовує всю роботу гри та запускає програму.

    Алгоритм:
    1. Створити порожню сітку.
    2. Встановити стартового гравця (наприклад, "X").
    3. У циклі:
       - вивести сітку;
       - запитати хід у поточного гравця;
       - додати символ до сітки;
       - перевірити, чи є переможець;
       - перевірити, чи ще є вільні клітинки;
       - при завершенні гри вивести результат (хто виграв або нічия);
       - переключити гравця.
    """


player_x = input("Enter name of the 1 player ")
player_o = input("Enter name of the 2 player ")

# 1. Створити порожню сітку.
grid = create_grid(3)
print_grid(grid)
# 2. Встановити стартового гравця (наприклад, "X").
print("Enter symbol to start game  X or O ")
symbol = input("Enter symbol to start ")

while symbol not in ("X", "O"):
    print("Wrong symbol! Enter X or O.")
    symbol = input("Enter symbol to start ")

if symbol == CROSS:
    current_player = player_x
else:
    current_player = player_o
# 3. У циклі:
while True:
    #        - запитати хід у поточного гравця;
    row, col = ask_user_move(current_player, grid)
    #        - додати символ до сітки;
    add_symbol_to_grid(grid, row, col, symbol)
    #        - вивести сітку;
    print_grid(grid)
    #        - перевірити, чи є переможець;
    #        - при завершенні гри вивести результат (хто виграв або нічия);
    if not is_game_over(grid):
        # - переключити гравця.
        symbol = switch_player(symbol)
        if symbol == CROSS:
            current_player = player_x
        else:
            current_player = player_o
    else:
        break
