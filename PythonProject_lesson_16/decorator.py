# Замикання
# def x():
#     pass
# def outer(k):
#
#     def inner(x):
#         return x * k
#
#     res = inner(5)
#     print(res)


# def outer(k):
#
#     def inner(x):
#         return x * k
#
#     return inner
#
# inner_func = outer(5)
# print(inner_func(10))

# def make_counter(start=0):
#     n = start
#
#     def inc(step=1):
#         nonlocal n
#         n += step
#         return n
#     return inc
#
# c = make_counter(10)
# print(c())
# print(c(2))
# print(c(3))
#
# c2 = make_counter()
# print(c2())
# print(c2())
# print(c2())

# def sendMsg(userTo, msgTxt, userFrom, lang):
#     print("Dear {}, Hello from {}. Welcome to {} world! {}".format(userTo, userFrom, lang, msgTxt))
#
#
#
# name = 's'
#
#
## sendMsg(name, "Python", "John", 'accept')

# Каррінг
# def sendMsg(userTo):
#     def setMsg(msgTxt):
#         def setUserFrom(userFrom):
#             def setLang(lang):
#                 print("Dear {}, Hello from {}. Welcome to {} world! {}".
#                        format(userTo, userFrom, lang, msgTxt))
#             return setLang
#         return setUserFrom
#     return setMsg

# set_mg = sendMsg("Den")
# ...
#..
# user_from = set_mg("Hello!")
# ..
# ..
# set_lang = user_from("John")
# ..
# ..
# set_lang("Python")
#
# sendMsg("Den")("Hello!")("John")("Python")
#
# set_lang = sendMsg("Den")("Hello!")("John")
#
# set_lang("Python")
# є дві посадові особи одна є працівником інше керівником, працівник отримує заяву її розглядає і робить по ній рішення
# потім заява передається керівнику він розглядає результат розгляду заяви і визначає чи погоджувати це рішення
# (accept/decline) та віддає супутнє повідомлення якщо заява прийнята

# def sendMsg(userTo):
#     def setMsg(msgTxt):
#         def setUserFrom(userFrom):
#             def setLang(lang):
#                 print("Dear {}, Hello from {}. Welcome to {} world! {}".
#                        format(userTo, userFrom, lang, msgTxt))
#             return setLang
#         return setUserFrom
#     return setMsg

# def employeeReview(employee):
#     def handle(app):
#         app_id, applicant, text = app

#         if len(text) < 10:
#             return (app, employee, "REJECT", "Текст заяви закороткий")

#         return (app, employee, "APPROVE", "Рекомендація на погодження")
#     return handle


# def managerDecision(manager):
#     def handle(review):
#         app, employee, decision, comment = review

#         if decision == "APPROVE":
#             return (app, manager, "ACCEPT", "Погоджено")

#         return (app, manager, "DECLINE", "Відхилено")

#     return handle

# def main():
#     employee = "Den"
#     manager = "Alice"

#     applications = [
#         [1, "John", "Прошу надати відпустку на 10 днів."],
#         [2, "Bob", "Дайте.."]
#     ]

#     reviewFn = employeeReview(employee)
#     finalFn = managerDecision(manager)

#     for app in applications:
#         review = reviewFn(app)
#         final = finalFn(review)

#         app_id, applicant, text = app
#         app2, employee_name, decision, employee_comment = review
#         app3, manager_name, status, manager_comment = final

#         print("\nЗаява: ", app_id, "від", applicant)
#         print("Працівник: ", employee_name, decision, " | ", employee_comment)
#         print("Керівник: ", manager_name, status, " | ", manager_comment)

#         if status == "ACCEPT":
#             msg = f"Ваша заява #{app_id} прийнята. {manager_comment}"
#             # sendMsg("Den")("Hello!")("John")("Python")
#             print(msg)
# if __name__ == '__main__':
#     main()

# Декоратори

# def hello():
#     print("Hi")

# x = hello
# x()

import functools
# functools.wraps
# functools.lru_cache()

# def action(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kwargs):
#         print("before")
#         fn(*args,**kwargs)
#         print("after")
#     return wrapper

# def say():
#     print("Hi")



# wrapper_say = action(say)

# wrapper_say()

# @action
# def say2(name):
#     """ is my super function """
#     print("Hi2 ", name)

# say2("Den")
# print(say2.__name__)
# print(say2.__doc__)

# def repeater(times):
#     def decorator(fn):
#         @functools.wraps(fn)
#         def wrapper(*args,**kwargs):
#             print(args, kwargs)
#             result = None
#             for _ in range(times):
#                 result = fn(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeater(2)
# def hi(name):
#     print("Hi ", name)

# hi(name="Den")

# def call_count(fn):
#     count = 0

#     def wrapper():
#         nonlocal count
#         count += 1
#         print(fn.__name__, "called", count, "times")
#         return fn()

#     return wrapper

# @call_count
# def ping():
#     print("pong")

# ping()
# ping()
# ping()

# def action1(fn):
#     def wrapper(*args,**kwargs):
#         print("a1 before")
#         fn(*args,**kwargs)
#         print("a1 after")
#     return wrapper

# def action2(fn):
#     def wrapper(*args,**kwargs):
#         print("a2 before")
#         fn(*args,**kwargs)
#         print("a2 after")
#     return wrapper

# @action1
# @action2
# def ping():
#     print("pong")

# ping()

# @functools.lru_cache
# def add(a,b):
#     return a+b
#
# print(add(2,3)) # add 2 3 -> 5
# print(add(2,3))
# print(add(2,3))

# DECORATOR
#1.
def sayUserHello(user): # основна функція
    msg = "Hello, " + user

    def showMsf(): # вкладена функція є замиканням для основної, а змінна msg є для неї  nonlocal. Функція showMsf() має доступ до неї, щоб працювати з її значенням
        print(msg+"! Let's start...")

    showMsf()
print("1")
sayUserHello('admin') # Hello, admin! Let's start...

#Для того, щоб забезпечити бажаний результат (надання можливості змінювати значення нелокальних змінних усередині
# функції-замикання) нам потрібно перед ім'ям такої змінною додати ключове слово nonlocal
#2.
def sayUserHello(user):
    msg = "Hello, " + user # msg = "Student" -> буде передана з функції showMsf()

    def showMsf():
        nonlocal msg
        msg = "Student"
        print(msg + "! Let's start...")

    showMsf()
    print(msg) # Student! Let's start...
               # Student
print("2")
sayUserHello('admin') #-> admin wil lbe changed to Student inside showMsf()

#розглянемо ситуацію, коли наша охоплююча функція не викликає замикання, а повертає його, як результат своєї роботи.
#3.
def sayUserHello(user):
    msg = "Hello, " + user

    def showMsf():
        print(msg+"! Let's start...")

    return showMsf

# Оскільки тепер функція sayUserHello() повертає результат, то рядок коду із викликом функції sayUserHello() також
# буде змінено: ми створимо змінну, яка прийме результат її роботи — об'єкт функції.

result = sayUserHello('admin') # -> запишемо результат роботи функції в змінну
print("3")
result() # -> виклечемо функцію # Hello, admin! Let's start..

#Функція-замикання doExercise2() використовує у своєму тілі лише змінну var1 (аргумент охоплюючої функції
# doExercise1()). Тому значення змінної var1 буде «запам'ятоване» (незважаючи на те, що виконання функції
# doExercise1(2) було завершено).
#4.

def doExercise1(var1):
    var2 = 7
    def doExercise2(var3):
        return var1**var3
    return doExercise2

result = doExercise1(2) # створюється функція doExercise2 -> ця функція запам'ятовує var1 =2
#var1 = 2
#var2 = 7 (але ми його не використовуємо)

# повертається doExercise2 вона пам’ятає, що var1 = 2.
# Python шукає var1:
# Локально в doExercise2 → нема
# У зовнішній функції doExercise1 → є! (var1 = 2)
# Тому бере його звідти

print("4")
print(result(5)) #2**5 = 32      5 -> var3  2 -> var1
print(result(10)) #2**10 = 1024

# Лічильник
# 5.
def launchCounter():
    counter = 0 #Створюється змінна counter = 0

    def incrementCounter(): #Усередині створюється вкладена функція incrementCounter()
        nonlocal counter
        counter += 1
        return counter

    return incrementCounter #launchCounter() повертає саму функцію, а не число


n = launchCounter()
# Тепер n — це функція incrementCounter
print("5")
for i in range(5):
    print(n())

# Каррінг (також вживається термін «карирування») — це техніка перетворення функції від кількох аргументів
# на послідовність функцій, кожна з яких має лише один аргумент.

# Маємо функцію, яка приймає два аргументи: логін користувача, якому адресується повідомлення,
# і сам текст повідомлення:
def sendMsg(userTo, msgTxt):
    print("Dear {}, welcome to Python world! {}".format(userTo,msgTxt))

#Виклики
sendMsg('admin', 'Have a nice day!')
sendMsg('admin', 'See you!')
sendMsg('admin', 'Good luck!')
sendMsg('student', 'Good luck!')

# аргумент userTo часто повторюється. Було б зручно в цій ситуації мати можливість викликати цю функцію із
# встановленим (зафіксованим) першим аргументом «admin», вказуючи лише другий аргумент — текст повідомлення.

# КАРРІНГ
# 6.
def sendMsg(userTo):
    def setMsg(msgTxt):
        print("Dear {}, welcome to Python world! {}".format(userTo, msgTxt))
    return setMsg

print("6")
# Тепер створимо нову функцію для потрібного імені користувача:
userAdmin = sendMsg('admin')

# І викличемо її з потрібними аргументами-повідомленнями:
userAdmin('Have a nice day!')
userAdmin('See you!')
userAdmin('Good luck!')

# Для користувача-студента (якому потрібно надіслати лише одне вітання) будемо безпосередньо викликати функцію
# sendMsg() таким чином (тип користувача — студент є першим параметром функції ):
sendMsg('student')('Good luck!')

# Будь яка кількість аргументів
def sendMsg(userTo):
    def setMsg(msgTxt):
        def setUserFrom(userFrom):
            def setLang(lang):
                print("Dear {}, Hello from {}. Welcome to {} world! {}".
                       format(userTo, userFrom, lang, msgTxt))
            return setLang
        return setUserFrom
    return setMsg

print("7")
case1 = sendMsg('admin')('Good luck!') # передали параметри userTo, msgTxt
case2 = sendMsg('student')('See you!')('admin') # передали параметри userTo, msgTxt, userFrom
case1('teacher')('Python') # викликали sendMsg і додали параметри userFrom та lang
case2('C++') # викликали і додали параметр lang

# Карирування дозволяє нам легко створювати частково застосовані функції, які дозволяють спрощувати виклики
# за недостатнього або частково повторюваного набору аргументів. При таких ситуаціях можна просто передати
# частину аргументів (які, наприклад, повторюються) у функцію та отримати назад часткову функцію, яка прийматиме
# інші аргументи.

# ДЕКОРАТОР
# Декоратор — це функція-«обгортки», що дозволяє нам розширити функціональність вже існуючої функції без
# прямої зміни коду в її тілі.
# Використання декораторів показує, що функція може працювати з іншою функцією як із звичайними аргументами (даними).

def simpleDecorator(myFunction):
    print("Hello! I'm Decorator!")
    def simpleWrapper():
        print("Function starts working...")
        myFunction()
        print("See you!")
    return simpleWrapper

# Всередині simpleDecorator() ми визначаємо функцію-«обгортку» simpleWrapper().
# Функція simpleWrapper() «обертає» функцію-аргумент myFunction, тобто у своєму тілі містить рядки коду з
# новою функціональністю та виклик «декорованої» функції myFunction().
# Як результат декоратор повертає функцію-«обгортку».

def sayHi(): #функцію, код якої ми (з різних причин) не можемо змінювати
    print("Welcome!")

# Для зміни (доповнення, розширення) її функціональності ми її «декоруватимемо».
# Передамо її декоратору simpleDecorator(), який за допомогою функції-«обгортки» simpleWrapper() додасть нову
# поведінку і поверне нову версію нашої базової функції sayHi() з вже розширеною функціональністю.
print("8")
# 1. спосіб викликати декоратор
sayHiAdvanced = simpleDecorator(sayHi)
sayHiAdvanced()

# 2. спосіб
@simpleDecorator
def sayHi():
    print("Welcome!")

sayHi()

def sayBye():
    print("Buy!")

sayBye = simpleDecorator(sayBye)
sayBye()

# Тепер «декоруємо» нашу першу базову функцію sayHi() двома різними декораторами.
# Для цього спочатку створимо другий декоратор:

def simpleDecorator_v2(myFunction):
    print("Hello! I'm Second Decorator!")
    def simpleWrapper():
        print("Let's start...")
        myFunction()
        print("Good luck!")
    return simpleWrapper

print("9")
@simpleDecorator
@simpleDecorator_v2 # 2 декоратор буде запущений першим, а всередині буде 1 декоратор
def sayHi():
    print("Welcome!")

sayHi()

# Hello! I'm Second Decorator!
# Hello! I'm Decorator!
# Function starts working...
# Let's start...
# Welcome!
# Good luck!
# See you!

#Якщо ж функція, яку потрібно «декорувати», має повертати значення, то його також має повертати і функція-«обгортка».
def simpleDecorator_v3(myFunction):
    print("Hello! I'm Third Decorator!")
    def simpleWrapper():
        print("Function starts working...")
        resutl = myFunction() # враппер повертає змінну, в яку записаний  результат роботи функцїі
        print("See you!")
        return resutl
    return simpleWrapper # декоратор має повернути враппер

def calculateSum():
    print("Welcome! Let's calculate...")
    x = int(input("x: "))
    y = int(input("y: "))
    return x+y

calculateSum = simpleDecorator_v3(calculateSum)
print("10")
print(calculateSum())

# передача аргументів у функцію, що декорується:
def simpleDecorator_v4(myFunction):
    print("Hello! I'm Fourth Decorator!")
    def simpleWrapper(argX, argY):
        print("I've got {}, {}. Function starts working...".format(argX, argY))
        resutl = myFunction(argX, argY)
        print("See you!")
        return resutl
    return simpleWrapper

def calculateSum_v1(a, b):
    print("Welcome! Let's calculate...")
    x = int(input("x: "))
    y = int(input("y: "))
    return x+y+a+b

calculateSum_v1 = simpleDecorator_v4(calculateSum_v1)
print("11")
print(calculateSum_v1(3, 4))

# а чи можна передавати аргументи самому декоратору? Адже ми знаємо, як аргумент декоратор має приймати
# базову функцію. А якщо нам потрібні якісь додаткові дані, наприклад, для управління
# логікою роботи самого декоратора?
#Для вирішення цього завдання нам потрібно додати ще один рівень абстракції — створити«обгортку» для самого
# декоратора і передати цій функції потрібні додаткові аргументи.
#Обов'язкова умова: ця функція-«обгортка» для декоратора має повертати декоратор в результаті своєї роботи.

def decoratorWrapper(argForDec): # у враппер для декоратора ми можемо передати аргументи, які використовує декоратор
    print("I've got arg = {} for decorator!".format(argForDec))

    def simpleDecorator_v5(myFunction): # в декоратор ми передаємо функцію
        print("Hello! I'm Decorator with arg = {}!".format(argForDec))

        def simpleWrapper(argX, argY): # в функцію ми передаємо її аргументи
            print("Hi! I am Funcion. I've got {}, {}."
                   "Function starts working...".format(argX, argY))
            result = myFunction(argX, argY) + argForDec # 2+4+3+4+10
            print("See you!")
            return result # враппер має повернути результат виконання функції
        return simpleWrapper # декоратор повертає враппер
    return simpleDecorator_v5 # враппер для декоратора повертає декоратор

def calculateSum_v1(a, b):
    print("Welcome! Let's calculate...")
    x = int(input("x: "))
    y = int(input("y: "))
    return x+y+a+b

print("12")
decoratorWithArg_1 = decoratorWrapper(10)

calculateSum_v1 = decoratorWithArg_1(calculateSum_v1)
print(calculateSum_v1(3, 4))

print("13")
#Припустимо, що ми маємо список із цінами на товари в доларах.
pricesUSD = [100.34, 35, 67.99, 25.5]
print(pricesUSD)

def toPriceNew(priceList): #І функція, яка переводить ціну товару в доларах у відповідний гривневий еквівалент:
    return list(map(lambda x: x*27.5, priceList))

#Однак зараз на всі товари діє знижка (наприклад, 15%) і нам потрібно перевести ціни в гривні та ще
# додатково врахувати знижку.
#Знижка — непостійна характеристика товару, тому змінювати код функції toPriceNew() немає сенсу.
# Знижку передавати як аргумент

def setDiscountDecoratorWrapper(disc): # передаємо дисконт у декоратор як параметр
    def changePriceDecorator_v1(myFunction):
        print("Hello! Let's change your prices...")

        def simpleWrapper(argList):
            print("I've got list of prices with {} elements. Function starts working...".
                   format(len(argList)))
            result = myFunction(argList) #функція toPriceNew, яка переводить ціну товару в доларах у гривневий еквівалент
            resutlwithDisc = list(map(lambda x: x*(1-disc), result)) # приміняємо дисконт
            print("Let's set a discount..")
            return resutlwithDisc
        return simpleWrapper
    return changePriceDecorator_v1

discount = float(input("Discount value: ex. 1 -> 100% "))
changePriceDecorator_v2 = setDiscountDecoratorWrapper(discount) # передаємо дисконт у враппер декоратора

pricesToGRN = changePriceDecorator_v2(toPriceNew) # в декоратор маємо передати основну функцію для розрахунку
print(pricesToGRN(pricesUSD))

