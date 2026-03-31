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
from typing import List, Dict

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
        if expenses > self.budget:
            print("Not enough budget!")
            return

        self.tasks.remove(task)
        self.expenses += expenses
        self.duration += time
        self.budget -= expenses
        print(f"Task {task} was completed with duration {self.duration}")
        print(f"Your expenses {self.expenses}")
        print(f"Remaining budget {self.budget}")

        if not self.tasks:
            self.is_finished = True

    def add_budget(self, additional_budget: float):
        self.budget +=additional_budget
        print(f"Budget was increased, new budget: {self.budget}")



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

project_1.add_budget(450)

# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

class Phone:

    def __init__(self, max_memory: float):
        self.max_memory = max_memory
        self.used_memory: float = 0
        self.is_on: bool = False
        self.apps: Dict[str, float] = {}

    def show_memory_info(self):
        print(f"Загальна пам'ять: {self.max_memory} GB")
        print(f"Використано: {self.used_memory} GB")
        print(f"Вільно: {self.max_memory - self.used_memory} GB")

        if self.apps:
            print("\nЗапущені додатки:")
            for app, memory in self.apps.items():
                print(f"- {app}: {memory} GB")
        else:
            print("\nНемає запущених додатків")

    def install_new_app(self, app_name, app_memory):
        if app_memory + self.used_memory > self.max_memory:
            print(f"You don't have enough memory")
            return
        self.apps[app_name] = app_memory
        self.used_memory += app_memory
        print(f"App {app_name} was successfully installed")

    def remove_app(self, app_name):
        if app_name not in self.apps:
            print(f"App {app_name} was not found")
            return
        self.used_memory -= self.apps[app_name]
        self.apps.pop(app_name)
        print(f"App {app_name} was removed")


    def update_app(self, app, memory):
        if memory != self.apps[app]:
            self.used_memory -= self.apps[app]
            print(f"Updated app with new memory {memory}")
            self.apps[app] = memory
            self.used_memory += memory


phone_1 = Phone(512)
phone_1.show_memory_info()
phone_1.install_new_app("game", 12)
phone_1.show_memory_info()
phone_1.update_app("game", 15)
phone_1.show_memory_info()
phone_1.remove_app("calculator")
phone_1.remove_app("game")
phone_1.show_memory_info()
