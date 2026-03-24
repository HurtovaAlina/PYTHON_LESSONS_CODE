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
    grid = [[EMPTY for _ in range(size)] for _ in range(size)]

    return grid


def print_grid(grid: list[list[Cell]]) -> None:
    """
    Виводить поточний стан сітки на екран у зручному для читання вигляді.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: None
    """
    for i in range(len(grid)):
        row = grid[i]

        row_str = " | ".join(str(cell) for cell in row)
        print(f"{row_str}")

        if i < len(grid) - 1:
            print("---+---+---")


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
    if grid[row][col] != EMPTY:
        return False

    grid[row][col] = symbol
    return True


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
    size = len(grid)

    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))

        if row < 0 or row >= size or col < 0 or col >= size:
            print("Неправильні індекси")
            continue

        if grid[row][col] != EMPTY:
            print("Клітинка занята")
            continue

        return row, col


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
    # 1. Перевірити кожний рядок: всі елементи однакові та не " ".
    for row in grid:
        symbol = row[0]

        if symbol == EMPTY:  # цей рядок точно не той що треба
            continue

        if row[0] == row[1] == row[2]:
            # в цьому рядки 3 однакових
            return symbol

    # 2. Перевірити кожний стовпець.
    for i in range(len(grid)):
        symbol = grid[0][i]

        if symbol == EMPTY:  # цей рядок точно не той що треба
            continue

        if grid[0][i] == grid[1][i] == grid[2][i]:
            # в цьому рядки 3 однакових
            return symbol

    # 3. Перевірити дві діагоналі.
    symbol = grid[1][1]

    if symbol == EMPTY:  # реможця немає
        return None

    if grid[0][0] == grid[1][1] == grid[2][2]:
        return symbol

    if grid[0][2] == grid[1][1] == grid[2][0]:
        return symbol

    return None


def has_empty_cells(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи є на сітці ще вільні (порожні) клітинки.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо є хоч одна порожня клітинка,
                    False, якщо поле повністю заповнене.
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == EMPTY:
                return True

    # не спрацював return True
    return False


def switch_player(player: Symbol) -> Symbol:
    """
    Змінює поточного гравця.

    :param player: Symbol - Поточний символ гравця ("X" або "O").
    :return: Symbol - Інший символ ("O" якщо був "X", і навпаки).
    """
    if player == CROSS:
        return ZERO

    return CROSS


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
    # 1. Створити порожню сітку.
    grid = create_grid()

    # 2. Встановити стартового гравця (наприклад, "X")
    current_player = CROSS

    while True:
        row, col = ask_user_move(current_player, grid)

        add_symbol_to_grid(grid, row, col, current_player)

        print_grid(grid)

        winner = check_winner(grid)
        if winner:
            print(f"Переміг {winner}")
            return

        if not has_empty_cells(grid):
            print("Всі клітинки зайняті, нічия")
            return

        current_player = switch_player(current_player)


main()
