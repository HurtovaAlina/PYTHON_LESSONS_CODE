# Завдання 1
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off

from abc import ABC
from enum import Enum


class Status(Enum):
    on = "on"
    off = "off"
    working = "working"


class Robot(ABC):

    def __init__(
            self,
            name: str,
            battery_level: int,
            status: Status = Status.off
    ):
        self._name = name
        self._battery_level = battery_level
        self._status = status

    def info(self):
        print(f"Robot: {self._name} \n"
            f"Battery: {self._battery_level} \n"
            f"Status: {self._status}"
        )

    def charge(self, charge: int):
        if self._battery_level <100:
            self._battery_level = min(self._battery_level+charge, 100)

    def turn_on(self):
        self._status = Status.on

    def turn_off(self):
        self._status = Status.off

# # Завдання 2
# # Створіть дочірній клас CleaningRobot
# # Додаткові атрибути:
# #  dust_capacity – ємність контейнеру для пилу(за
# # замовчуванням 0%)
# #  water_capacity – ємність контейнеру для води(за
# # замовчуванням 100%)
# #  cleaning_mode – тип прибирання(вологе або сухе)
# # Методи:
# #  info() – додатково виводить інформацію про робота
# # Практичне завдання
# #  turn_on() – якщо контейнер для пилу повний або
# # контейнер для води порожній то виводить повідомлення,
# # інакше запускається turn_on() з класу Robot
# #  empty_dustbin() – очищає контейнер для пилу
# #  fill_water() – заповнює контейнер для води
# #  swap_mode() – змінює тип прибирання на протилежний
# #  clean(energy, dust, water=None) – чистить поверхню,
# # якщо прибирання сухе, то просто перенести пил у
# # контейнер(якщо місця не достатньо вивести помилку),
# # якщо прибирання вологе то додатково витратити воду.
# # Також зменшує рівень заряду на energy
#
class Cleaning_mode(Enum):
    wet = "wet"
    dry = "dry"

class CleaningRobot(Robot):

    def __init__(
            self,
            name: str,
            battery_level: int,
            cleaning_mode: Cleaning_mode = Cleaning_mode.dry,
            status: Status = Status.off,
            dust_capacity: int = 0,
            water_capacity: int = 100,
    ):
        super().__init__(name, battery_level, status)

        self._cleaning_mode = cleaning_mode
        self._dust_capacity = dust_capacity
        self._water_capacity = water_capacity

    def info(self):
        super().info()
        print(f"Cleaning mode: {self._cleaning_mode} \n"
            f"Dust capacity: {self._dust_capacity} \n"
            f"Water capacity: {self._water_capacity}"
        )

    def turn_on(self):
        if self._dust_capacity == 100:
            print("Dust container is full")
            return

        if self._cleaning_mode == Cleaning_mode.wet and self._water_capacity == 0:
            print("Water container is empty for wet cleaning")
            return
        super().turn_on()

    def empty_dustbin(self):
        self._dust_capacity = 0


    def fill_water(self):
        self._water_capacity = 100

    def swap_mode(self):
        if self._cleaning_mode == Cleaning_mode.wet:
            self._cleaning_mode = Cleaning_mode.dry
            print("Starting dry cleaning")
        else:
            self._cleaning_mode = Cleaning_mode.wet
            print("Starting wet cleaning")

    def clean(self, energy: int, dust: int, water=None):
        if self._status != Status.on:
            print("Robot must be ON")
            return

        self._status = Status.working

        if self._cleaning_mode == Cleaning_mode.dry:

            if self._dust_capacity+dust > 100:
                print("Dust container is full")
                return

            self._dust_capacity = min(self._dust_capacity + dust, 100)

        else:

            if water is None:
                print("Water amount required for wet cleaning")
                return

            if self._water_capacity < water:
                print("Not enough water")
                return

            self._water_capacity -= water

        self._battery_level = max(0, self._battery_level-energy)


cleaning_robot = CleaningRobot("Vasil", 100)
cleaning_robot.info()
cleaning_robot.turn_on()
cleaning_robot.clean(40, 50)
cleaning_robot.info()
cleaning_robot.swap_mode()
cleaning_robot.clean(70, 0, 60)
cleaning_robot.info()

# Завдання 3
# Створіть дочірній клас SecurityRobot
# Додаткові атрибути:
#  min_speed – мінімальна швидкість руху, щоб помітити
# об’єкт
#  alert_level – рівень небезпеки (low, middle, high)
#  dangerous_items – список небезпечних предметів(gun,
# knife, bat)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_off() – перед виключенням змінює рівень небезпеки
# на low
#  add_dangerous_item(item) – додає небезпечний предмет
#  remove_dangerous_item(item) – видаляє небезпечний
# предмет
#  detect(speed, item) – виявляє загрозу
# o якщо швидкість занизька, то ігноруємо
# o якщо швидкість велика, то рівень небезпеки
# middle
# o якщо це небезпечний предмет, то рівень
# небезпеки high
# Рівень небезпеки не може стати нижчим

class Alert(Enum):
    low = "low"
    middle = "middle"
    high = "high"

class SecurityRobot(Robot):

    def __init__(
            self,
            name: str,
            battery_level: int,
            min_speed: int,
            status: Status = Status.off,
            alert_level: Alert = Alert.low,
            dangerous_items: list[str] | None = None
    ):
        super().__init__(name, battery_level, status)

        self._min_speed = min_speed
        self._alert_level = alert_level

        if dangerous_items is None:
            self._dangerous_items = []
        else:
            self._dangerous_items = dangerous_items

    def info(self):
        super().info()
        print(f"Min speed: {self._min_speed} \n"
            f"Alert level: {self._alert_level.value} \n"
            f"Dangerous items: {self._dangerous_items}"
        )

    def turn_off(self):
        self._alert_level = Alert.low
        super().turn_off()

    def add_dangerous_item(self, item):
        if item not in self._dangerous_items:
            self._dangerous_items.append(item)

    def remove_dangerous_item(self, item):
        if item in self._dangerous_items:
            self._dangerous_items.remove(item)
        else:
            print("Item not found in dangerous items")

    def detect(self, speed, item):
        if speed < self._min_speed:
            return

        if self._alert_level == Alert.low  and speed > self._min_speed:
            self._alert_level = Alert.middle

        if item in self._dangerous_items:
            self._alert_level = Alert.high
            return

security_robot = SecurityRobot("Den", 100, 4)
security_robot.turn_on()
security_robot.info()
security_robot.add_dangerous_item("knife")
security_robot.detect(5, "knife")
security_robot.info()
security_robot.turn_off()
security_robot.add_dangerous_item("bat")
security_robot.add_dangerous_item("gun")
security_robot.info()
security_robot.remove_dangerous_item("bat")
security_robot.info()

# Завдання 4
# Створіть дочірній клас AssistantRobot
# Додаткові атрибути:
#  tasks – список завдань(за замовчуванням порожній)
#  current_task – поточне завдання(за замовчуванням None)
# Методи:
#  info() – додатково виводить інформацію про робота
#  add_task(task) – додає завдання до списку
#  change_task() – змінює поточне завдання, виводить на
# екран список завдань та просить користувача вибрати
# одне з них
#  execute_task() – виконує поточне завдання, видяляє його
# зі списку, та змінює current_task на наступне

class AssistantRobot(Robot):

    def __init__(
            self,
            name: str,
            battery_level: int,
            status: Status = Status.off,
            tasks: list[str] | None = None,
            current_task: str | None = None
    ):
        super().__init__(name, battery_level, status)

        self._current_task = current_task

        if tasks is None:
            self._tasks = []
        else:
            self._tasks = tasks


    def info(self):
        super().info()
        print(f"Tasks: {self._tasks} \n"
            f"Current task: {self._current_task}"
        )

    def add_task(self, task):
        if task not in self._tasks:
            self._tasks.append(task)

    def change_task(self):
        print(f"Tasks: {self._tasks}")
        current_task = input(f"Select the task from the list: {self._tasks} ")
        if self._current_task == current_task:
            print(f"Already working on task {current_task}")
        else:
            self._current_task = current_task

    def execute_task(self):
        print(f"Executing task {self._current_task}")
        index_current_task = self._tasks.index(self._current_task)
        self._tasks.remove(self._current_task)

        if self._tasks:
            if index_current_task < len(self._tasks):
                self._current_task = self._tasks[index_current_task]
            else:
                self._current_task = self._tasks[-1]
        else:
            self._current_task = None
            print("All tasks completed")

assistant_robot = AssistantRobot("Friend", 100)
assistant_robot.turn_on()
assistant_robot.info()
for i in range(1,4):
    task = input("Enter task ")
    assistant_robot.add_task(task)

assistant_robot.info()
assistant_robot.change_task()
assistant_robot.info()
for i in range(1, 4):
    assistant_robot.execute_task()
    assistant_robot.info()
