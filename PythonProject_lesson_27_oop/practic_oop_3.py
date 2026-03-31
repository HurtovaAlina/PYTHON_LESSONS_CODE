# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису
from typing import List

class Project:

    def __init__(
            self,
            name: str,
            budget: float,

    ):
        self.name = name
        self.budget = budget

        self.expenses: float = 0
        self.is_finished: bool = False
        self.duration: int = 0
        self.tasks: List[str] = []

    def show_info(self):
        print(f"Назва: {self.name}")
        print(f"Час виконання: {self.duration} днів")
        print("Необхідні задачі:")

        if self.tasks:
            for i in range(0,len(self.tasks)):
                print(f"{i}. {self.tasks[i]}")
        else:
            print("Немає задач")

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def divide_tasks(self, task: str, subtasks:List[str]):
        self.tasks.remove(task)
        self.tasks.extend(subtasks)

    def complete_task(self, task: str, expenses: float, time:int):
        self.tasks.remove(task)
        self.expenses += expenses
        self.duration += time
        self.budget -= expenses
        print(f"Task {task} was completed with duration {self.duration}")
        print(f"Your expenses {self.expenses}")
        print(f"Remaining budget {self.budget}")



project_1 = Project("new development", 30000)
project_1.show_info()
project_1.add_task("investigation")
project_1.add_task("prototype")
project_1.add_task("implementation")
project_1.add_task("testing")
project_1.add_task("user acceptance testing")

project_1.show_info()
subtasks = ["idea", "variants of realisation", "conception", "resume with customer"]
project_1.divide_tasks("investigation", subtasks)

project_1.show_info()

project_1.complete_task("idea", 200, 2)
