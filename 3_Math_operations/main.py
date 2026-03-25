from datetime import datetime, time, timedelta

# Завдання 1:
# Користувач вводить:
# час відправлення: години h (0–23) і хвилини m (0–59)
# тривалість дороги: t хвилин (може бути більше 60 і навіть більше 1440)
# Потрібно вивести:
# час прибуття у форматі HH:MM
# скільки повних діб пройде під час дороги (0, 1, 2, …)
# Приклад
#
# Ввід: 23 50 і 125
# Прибуття: 01:55
# Діб пройшло: 0 (бо менше 24 год)

h = int(input("Enter hours of departure 0-23: "))
m = int(input("Enter minutes of departure 0-59: "))
d = int(input("Enter duration of way, minutes: "))

# 1 variant

time_of_departure = time(h, m)
print("Time of departure: ", time_of_departure)
day_of_departure = datetime.combine(datetime.today(), time_of_departure)
print("Day of departure: ", day_of_departure)
day_of_arrival = day_of_departure + timedelta(minutes=d)
print("Day of arrival", day_of_arrival)
print("Time of arrival: ", day_of_arrival.strftime("%H:%M"))
time_in_way = day_of_arrival - day_of_departure
print("Time in way", time_in_way)
print("Days in way: ", time_in_way.days)

# 2 variant
# start, min
# start_m = h * 60 + m
# # all minutes in way
# all_m = start_m + d
# arrival_min_in_day = all_m % 1440
# arrival_h = arrival_min_in_day // 60
# arrival_m = arrival_min_in_day % 60
#
# full_days_in_road = d // 1440
# print(f"Arrival : {arrival_h} : {arrival_m:02d}")
# print(f"Days in road : {full_days_in_road}")
#
# # Завдання 2:
# # Умова:
# # Користувач вводить 4-значне число (наприклад, 5831). Потрібно:
# # вивести окремо кожну цифру (по одній в рядок)
# # знайти суму цифр
# # сформувати число навпаки (5831 → 1385)
# # сформувати число з перших двох цифр і останніх двох цифр (наприклад 58 і 31)
# # number = int(input("Enter 4-digit number: "))
# # n4 = number % 10
# # n3 = (number//10) % 10
# # n2 = (number//100) % 10
# # n1 = (number//1000)
# # print(f"{n1} \n{n2} \n{n3} \n{n4}")
# # print("Sum: ", n1+n2+n3+n4)
# # print(f"{n4}{n3}{n2}{n1}")
# # n1_2 = str(n1)+str(n2)
# # n3_4 = str(n3)+str(n4)
# # print(int(n1_2), "and", int(n3_4))
#
#
# # Завдання 3:
# # Користувач вводить суму в гривнях (може бути дробова, наприклад 763.28). Треба:
# # перевести суму в копійки (ціле число)
# # порахувати, скільки потрібно купюр/монет, щоб видати цю суму мінімальною кількістю для номіналів:
# # грн: 200, 100, 50, 20, 10, 5, 2, 1
# # коп: 50, 25, 10, 5, 2, 1
# # Вивести кількість кожного номіналу та підсумкову кількість усіх купюр/монет.
# amount_of_money = float(input("Enter amount of money: "))
# amount_in_coins = round(amount_of_money*100, 2)
#
# # print("Amount in coins: ", amount_in_coins)
# total_banknotes = 0
# total_coins = 0
#
# b_200 = int(amount_in_coins // 20000)
# print("Banknotes 200 : ", b_200)
# total_banknotes += b_200
# rest_of_money = amount_in_coins-round(b_200*200*100,2)
# print("Rest of money : ", rest_of_money)
# b_100 = int(rest_of_money // 10000)
# print("Banknotes 100 : ", b_100)
# total_banknotes += b_100
# rest_of_money -= round(b_100*100*100,2)
# print("Rest of money : ", rest_of_money)
# b_50 = int(rest_of_money // 5000)
# print("Banknotes 50 : ", b_50)
# total_banknotes += b_50
# rest_of_money -= round(b_50*50*100,2)
# b_20 = int(rest_of_money // 2000)
# print("Banknotes 20 : ", b_20)
# total_banknotes += b_20
# rest_of_money -= round(b_20*20*100,2)
# b_10 = int(rest_of_money // 1000)
# print("Banknotes 10 : ", b_10)
# total_banknotes += b_10
# rest_of_money -= round(b_10*10*100,2)
# b_5 = int(rest_of_money // 500)
# print("Banknotes 5 : ", b_5)
# total_banknotes += b_5
# rest_of_money -= round(b_5*5*100,2)
# b_2 = int(rest_of_money // 200)
# print("Banknotes 2 : ", b_2)
# total_banknotes += b_2
# rest_of_money -= round(b_2*2*100,2)
# b_1 = int(rest_of_money // 100)
# print("Banknotes 1 : ", b_1)
# total_banknotes += b_1
# rest_of_money -= round(b_1*1*100,2)
# print("Rest of money in coins: ", rest_of_money)
# c_50 = int(rest_of_money // 50)
# print("Coins 50 : ", c_50)
# total_coins += c_50
# rest_of_money -= round(c_50*0.5*100,2)
# c_25 = int(rest_of_money // 25)
# print("Coins 25 : ", c_25)
# total_coins += c_25
# rest_of_money -= round(c_25*0.25*100,2)
# c_10 = int(rest_of_money // 10)
# print("Coins 10 : ", c_10)
# total_coins += c_10
# rest_of_money -= round(c_10*0.1*100,2)
# c_5 = int(rest_of_money // 5)
# print("Coins 5 : ", c_5)
# total_coins += c_5
# rest_of_money -= round(c_5*0.05*100,2)
# c_2 = int(rest_of_money // 2)
# print("Coins 2 : ", c_2)
# total_coins += c_2
# rest_of_money -= round(c_2*0.02*100,2)
# c_1 = int(rest_of_money // 1)
# print("Coins 1 : ", c_1)
# total_coins += c_1
# rest_of_money -= round(c_1*0.01*100,2)
# print("Rest of money : ", rest_of_money)
# print("Total banknotes : ", total_banknotes)
# print("Total coins : ", total_coins)
#
