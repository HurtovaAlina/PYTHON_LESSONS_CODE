# 17. Менеджер завдань
# Клас Task: атрибути — назва (str), опис (str), статус (str): "нове" або "виконано".
# Клас TaskManager: список завдань.
# Методи: add_task(), remove_task(name), complete_task(name) — змінює статус на
# "виконано", show_all().
# Текстове меню (while True): 1 — Додати завдання (ввести назву і опис). 2 —
# Видалити завдання. 3 — Позначити як виконане. 4 — Показати всі завдання. 0 — Вийти.
from typing import List


class Task:

    def __init__(self, name: str, description: str, status: str = "new"):
        self.name = name
        self.description = description
        self.status = status



class TaskManager:

    def __init__(self):
        self.tasks: List[Task] = []


    def add_task(self, task:Task):
        for t in self.tasks:
            if t.name == task.name:
                print("Task already exists")
                return

        self.tasks.append(task)
        print(f"Task {task.name} was added")


    def remove_task(self):
        task_to_remove = input("Enter task to remove ").lower()

        for task in self.tasks:
            if task.name == task_to_remove:
                self.tasks.remove(task)
                print(f"Task {task_to_remove} was removed")
                return

        print("Task was not found")


    def complete_task(self):
        task_to_complete= input("Enter task to complete ").lower()

        for task in self.tasks:
            if task_to_complete == task.name:
                task.status = "completed"
                return

        print("Task doesn't exist")

    def show_all(self):
        if not self.tasks:
            print("No tasks")
            return

        for task in self.tasks:
            print(f"Name: {task.name}, "
                f"Description: {task.description}, "
                f"Status: {task.status}"
            )

tasks = TaskManager()

while True:
    action = input("Enter action "
        "\n1 - Add task\n"
        "2 - Remove task\n"
        "3 - Complete task\n"
        "4 - Show all tasks\n"
        "0 - Exit\n")

    if action == "1":
        task_name = input("Enter task name ").lower()
        description = input("Enter task description ").lower()
        tasks.add_task(Task(task_name, description))

    elif action == "2":
        tasks.remove_task()

    elif action == "3":
        tasks.complete_task()

    elif action == "4":
        tasks.show_all()

    elif action == "0":
        print("Program is finished")
        break
    else:
            print("Action is not allowed")


# 18. Бібліотечна система
# Клас Book: атрибути — назва (str), автор (str), is_available (bool, за замовчуванням
# True).
# Клас Library: список книг.
# Метод issue_book(title): позначає книгу як видану (is_available = False). Перевіряйте
# доступність.
# Метод return_book(title): повертає книгу (is_available = True).
# Текстове меню: 1 — Додати книгу. 2 — Видати книгу. 3 — Повернути книгу. 4 —
# Показати всі книги (з позначкою доступності). 5 — Пошук книги. 0 — Вийти.
# 19. Симулятор банкомату
# Клас Account: атрибути — власник (str), PIN (str), баланс (float).
# Клас ATM: список рахунків (dict або list).
# Метод find_account(owner): знаходить рахунок за ім'ям власника.
# Текстове меню: 1 — Створити рахунок (ввести ім'я, PIN, початковий баланс). 2 —
# Поповнити рахунок (ввести ім'я, PIN, суму). 3 — Зняти гроші (перевіряти PIN і наявність
# коштів). 4 — Показати баланс (після перевірки PIN). 0 — Вийти.
