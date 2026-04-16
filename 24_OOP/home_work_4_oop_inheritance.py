# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5
from abc import abstractmethod, ABC

class PetLevelValueError(ValueError):
    pass

class Pet (ABC):


    def __init__(self, name: str, satiety: int = 50, energy: int = 50):
        self._check_level(satiety)
        self._check_level(energy)

        self._name = name
        self._satiety = satiety
        self._energy = energy

    @staticmethod
    def _check_level(level):
        if not 0 <= level <= 100:
            raise PetLevelValueError("Level must be between 0 and 100")

    def sleep(self):
        self._energy = 100


    def eat(self, food_amount):
        if self._satiety + food_amount <=100:
            self._satiety += food_amount
        else:
            self._satiety = 100

    def __str__(self):
        return(f"Pet's name: {self._name}, satiety: {self._satiety}, energy: {self._energy}")

    @abstractmethod
    def play(self, activity_level):
        raise NotImplementedError


    def make_sound(self):
        pass

class Cat (Pet):


    def play(self, activity_level):
        if self._satiety > 60:
            self._energy = max(0, self._energy- 2*activity_level)
            self._satiety = max(0, self._satiety-activity_level)
        else:
            print("Cat wants to eat")


    def make_sound(self):
        print("Мяу")


    def catch_mouse(self, activity_level = 3, food_amount = 1):
        if self._energy > 30:
            print("Cat catching mouse")
            if self._satiety > 40:
                self.play(activity_level)
            else:
                print("Cat wants to eat")
                self.eat(food_amount)
        else:
            print("Cat is too tired and needs to sleep")
            self.sleep()

class Dog (Pet):

    def play(self, activity_level):
        if self._satiety > 15:
            self._energy = max(0, self._energy - activity_level//2)
            self._satiety = max(0, self._satiety - activity_level//2)
        else:
            print("Dog is too hungry to play")


    def make_sound(self):
        print("Гав")


    def fetch_ball(self):
        if self._satiety > 10:
            print("Catching ball")
            self._energy= max(0, self._energy - 5)
        else:
            print("Dog is too hungry")

cat = Cat("Tomas")
print(cat)
cat.make_sound()
print("Catching mouse")
cat.catch_mouse()
print(cat)
print("Playing")
cat.play(4)
print(cat)
cat.sleep()
cat.eat(20)
print(cat)
cat.play(4)
print(cat)

dog = Dog("Polkan", 70, -90)
print(dog)
