# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує
# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали
# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()

from abc import ABC
from typing import List


class Passenger:

    def __init__(self, name: str, destination: str):
        self._name = name
        self._destination = destination

    def __str__(self):
        return f"{self._name} -> {self._destination}"


class Transport(ABC):

    def __init__(self, speed: int):

        if speed > 0:
            self._speed = speed
        else:
            raise ValueError("Speed must be more than 0")

    def move(self, destination: str, distance: float) -> float:
        time = distance / self._speed
        print(f"Move to {destination}. Time: {time:.2f}")
        return time


class Bus(Transport):

    def __init__(self, passengers: List[Passenger] | None, capacity: int, speed: float):

        super().__init__(speed)

        if passengers is None:
            self._passengers = []
        else:
            self._passengers = passengers

        self._capacity = capacity


    def __str__(self):
        passengers_str = ", ".join(str(p) for p in self._passengers)
        return f"Passengers: [{passengers_str}], Capacity: {self._capacity}, Speed: {self._speed}"


    def board_passenger(self, passenger: Passenger):
        if len(self._passengers) < self._capacity:
            self._passengers.append(passenger)
        else:
            print("Bus is full")


    def move(self, destination: str, distance: float):
        leaving_passengers = []
        passengers_copy = self._passengers.copy()
        for passenger in passengers_copy:
            if passenger._destination == destination:
                leaving_passengers.append(passenger)
                self._passengers.remove(passenger)
        print(f"{len(leaving_passengers)} passengers left at {destination}")
        super().move(destination, distance)


passenger_1 = Passenger("Alina", "City")
passenger_2 = Passenger("Alisa", "Village")
passenger_3 = Passenger("Dan", "City")

bus_1 = Bus([], 4, 60)
bus_1.board_passenger(passenger_1)
bus_1.board_passenger(passenger_2)
bus_1.board_passenger(passenger_3)

print(bus_1)

bus_1.move("City", 234.6)
print(bus_1)
