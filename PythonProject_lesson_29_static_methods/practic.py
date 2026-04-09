from abc import ABC, abstractmethod
from enum import Enum


class Stat(Enum):
    intelligence = "intelligence"
    strength = "strength"
    dexterity = "dexterity"
    mana = "mana"
    defense = "defense"



class Character(ABC):

    def __init__(
            self,
            name: str,
            max_hp: int,
            intelligence: int,
            strength: int,
            dexterity: int,
            mana: int,
            defense: int,
            level: int = 1,
    ):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._level = level
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense

    @abstractmethod
    def attack(self):
        raise NotImplementedError

    def take_damage(self, damage: int):
        self._defense -= damage
        if damage > 0:
            self._hp -= damage

    def level_up(self):
        if self._level < 20:
            self._level += 1

    def increase_stat(self, stat: str):
        if stat == Stat.intelligence:
            self._intelligence +=1
        elif stat == Stat.strength:
            self._strength += 1
        elif stat == Stat.dexterity:
            self._dexterity += 1
        elif stat == Stat.mana:
            self._mana += 1
        elif stat == Stat.defense:
            self._defense += 1

    def rest(self):
        self._hp = self._max_hp

    def real_heal(self, heal_hp):
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp += self._max_hp


class Paladin(Character):

    def attack(self) -> int:
        if self._mana >= 5:
            self._mana -= 5
            return self._strength * 4
        return self._strength

    def shield(self) :
        self._defense += 4 + self._level

    def unshield(self):
        self._defense -= 4 + self._level

    def heal_ally(self, ally:Character):
        if isinstance(ally, Character):
            heal_hp = 5 + 2 * self._level + 0.5 * self._mana
            ally.real_heal(heal_hp)


class Mage(Character):

    def attack(self):
        if self._mana >= 3:
            self._mana -= 3
            return self._intelligence * 3
        return self._intelligence

    def fireball(self):
        if self._mana >= 5:
            self._mana -= 5
            return self._intelligence * 2 + 3
        return self._intelligence

    def heal_ally(self, ally):
        if isinstance(ally, Character):
            heal_hp = 3 + 2 * self._level + 0.5 * self._mana
            ally.real_heal(heal_hp)

class Warrior(Character):

    def attack(self) -> int:
        return self._strength * 4

    def power_strike(self, enemies):
        for enemy in enemies:
            if enemy._level < self._level:
                enemy._hp = 0


class Rogue(Character):

    def attack(self) -> int:
        return self._dexterity * 3


paladin_1 = Paladin("Paladin", 100, 10, 10, 10, 10, 10, 1)
paladin_1.level_up()
print(paladin_1._hp)
paladin_1.shield()
paladin_1.take_damage(10)
print(paladin_1._hp)

ally = Paladin("Ally", 5, 5, 5, 5, 5, 5, 1)
ally.unshield()
ally.take_damage(3)
print(ally._hp)

paladin_1.heal_ally(ally)
print(ally._hp)

mage = Mage("Mage", 200, 100, 10, 10, 50, 10, 2)
print(mage._hp)
mage.attack()


# Завдання 2
# Практичне завдання
# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana
# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить
# урону
#  heal_ally(ally) – лікує союзника на 3 + level +
# 3*intelligence
# Завдання 4
# Створіть дочірній клас Warrior
# Методи:
#  attack() – наносить 4*strength+3 урону
#  power_strike(enemies) – проходить по списку ворогів:
# якщо їхній рівень менший за рівень персонажа, то
# знищує його повністю
# Завдання 5
# Створіть дочірній клас Rogue
# Методи:
#  attack() – наносить strength+level урону
