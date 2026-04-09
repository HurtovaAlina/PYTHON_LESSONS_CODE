from abc import ABC, abstractmethod

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
        damage -= self._defense
        if damage > 0:
            self._hp -= damage

    def level_up(self):
        if self._level < 20:
            self._level += 1

    def increase_stat(self, stat: str):
        if stat == "intelligence":
            self._intelligence +=1
        elif stat == "strength":
            self._strength += 1
        elif stat == "dexterity":
            self._dexterity += 1
        elif stat == "mana":
            self._mana += 1
        elif stat == "defense":
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

    def shield(self) -> int:
        self._defense += 4 + self._level

    def unshield(self):
        self._defense -= 4 + self._level

    def heal_ally(self, ally):
        if isinstance(ally, Character):
            ally._hp += 5 + 2 * self._level + 0.5 * self._mana


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
