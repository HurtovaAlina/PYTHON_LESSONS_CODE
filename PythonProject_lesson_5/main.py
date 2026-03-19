# умови
# == != < > <= >=
# if elif else -> true / false
# match

n1 = 5
n2 = 10
print(n1 == n2)
print(n1 != n2)
print(n1 < n2)
print(n1 > n2)
print(n1 <= n2)
print(n1 >= n2)
# порівнює по першій букві - якщо однакові, бере наступну букву і порівнює. Кожна буква має номер і вони
# порівнюються за номерами
print("bAllo" > "allox")

# and && - і то і то = вірно (обидві умови)
# or  || - або то або то = вірно (одна з умов)
# not  !

print(5 > 1 and 2 == 1)
# True and True -> True
# False and True -> False
# .. and .. -> False

n = 10
print(n > 0 and n <= 50)
print(0 < n <= 50)
print(n and True)
print(True and n)
# повернув правий елемент якщо лівий є вірний

print(n==5 and n)
# якщо перша умова не вірна, повертається False

print(n > 0 and n <= 50 and n != 20 and n != 15)

# or  логічне або, хочаб одне щось вірне. Зліва і зправа False -> False, хочаб один True -> True

# False or False -> False
#True or False -> True
# .. or .. -> True

is_admin = False
is_moderator = True
is_stuff = is_admin or is_moderator

print(is_stuff)

n1 = 5
print(n1 or False) # поверне завжди True
print(False or n1)

n2 = 0
print(False or n2)


# not заперечення
# not True -> False
# not False -> True
print(not 5)
print(not 0)
print(not (5>5 and 1 == 1))

n1 = 5
n2 = 5.1
n3 = 0
n4 = -6
n5 = "Hello!"

# 1. not
# 2. and
# 3. or

# True and True and False
