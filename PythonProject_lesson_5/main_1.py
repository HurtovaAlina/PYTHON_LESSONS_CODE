# if <condition>:
#     <code..> #True
# [elif] <condition>:
#     <code..> # False
# [elif] <condition>:  - x times
# [else]:
#     <code..>
# pass або (...) - пропустити зробити тіло пусте - для функції, класу

# age = 15
# if age >=18:
#     print("Ти повнолітній")
#     print("!!!")
# else:
#     print("Ти неповнолітній")
# print("The End")
#
# a = 0
# if a > 10:
#     pass

age = 5
if 0 < age <=14:
    print("Child")
elif 14 < age < 18:
    print("Teenager")
elif 18<= age < 65:
    print("Adult")
elif 65 <= age < 150:
    print("Very Old")
else:
    print("Error")
print("The End")

a = 0
if a > 10:
    pass

# вкладений if
n = 25

if n % 5 == 0:
    if n == 25:
        print("25!")
    else:
        print("not 25!")
else:
    print("n % 5 != 0!")
