# Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min
# Приклад рецептів:
# Recipe("Піца",
# Домашнє завдання
#  ["борошно", "вода", "дріжджі", "томат", "сир"],
#  "Готуємо тісто, додаємо інгредієнти та запікаємо",
#  30)
#
#  Recipe("Салат",
#  ["томат", "огірок", "зелень", "олія"],
#  "Нарізаємо овочі, додаємо зелень та поливаємо
# олією",
#  10)
#
#  Recipe("Суп",
#  ["вода", "картопля", "морква", "м'ясо"],
#  "Варимо всі інгредієнти до готовності",
#  45)

class Recipe:

    def __init__(self, name: str, ingredients: list, text: str, time: int):
        self._name = name
        self._ingredients = ingredients
        self._text = text
        self._time = time

    def __str__(self):
        return f"Name of the dish: {self._name}"

    def __contains__(self, item):
        return item in self._ingredients

    def __gt__(self, other):
        if isinstance(other, Recipe):
            return self._time > other._time
        raise TypeError(f"не можна порівнювати Recipe та {type(other)}")

    def __lt__(self, other):
        if isinstance(other, Recipe):
            return self._time < other._time
        raise TypeError(f"не можна порівнювати Recipe та {type(other)}")

    def __iter__(self):
        return iter(self._ingredients)

    def display_info(self):
        print(f"Recip: {self._name}")
        print("Ingredients: ")

        for ingredient in self._ingredients:
            print(ingredient)

        print(f"Text of recip: {self._text}")
        print(f"Time: {self._time}")

recipe_pizza = Recipe("Pizza",["борошно", "вода", "дріжджі", "томат", "сир"],
                      "Готуємо тісто, додаємо інгредієнти та запікаємо", 30)

recipe_salad = Recipe("Salad", ["томат", "огірок", "зелень", "олія"],
                      "Нарізаємо овочі, додаємо зелень та поливаємо олією", 10)

recipe_soup = Recipe("Soup", ["вода", "картопля", "морква", "м'ясо"],
                     "Варимо всі інгредієнти до готовності", 45)

recipes = []
recipes.append(recipe_pizza)
recipes.append(recipe_salad)
recipes.append(recipe_soup)

print("All recipes:")
for recipe in recipes:
    print(recipe)

print("Recipe with \"томат\" in ingredients:")
for recipe in recipes:
    if "томат" in recipe:
        print(recipe)

print("Recipe with mim time")
recipe_min_time = min(recipes)
recipe_min_time.display_info()
