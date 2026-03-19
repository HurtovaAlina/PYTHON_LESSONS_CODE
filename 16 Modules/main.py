#1

"""
Функція обрахунку температури склянки води

"""
import math

def temperature_calculation(t_env: float, t_0: float, t: int, k: float)-> float:
    t_new = t_env +(t_0-t_env)*math.exp(-k*t)
    return round(t_new,2)

t_env = float(input("Enter temperature of environment: "))
t_0 = float(input("Enter temperature of water: "))
t = int(input("Enter time: "))

print("New temperature: ", temperature_calculation(t_env, t_0, t, k=0.05))

#2
"""
Функція запиту імені користувача

"""
import time

def ask_name(show_time):
    start_time = time.time()
    name = input("What is your name ")
    if show_time:
        end_time = time.time()
        time_of_work = end_time- start_time
        print(f"Time of work  {time_of_work:.4f} seconds")
    return  name


print("Name", ask_name(True))
print("Name", ask_name(False))


#3
"""
Розрахунок дедлайну

"""
import date_utils

deadline_date = input("Enter days to deadline in format YYYY-MM-DD ")
deadline = date_utils.check_deadline(deadline_date)
print("Days to deadline: ", deadline)
if deadline <7 :
    print("Warning: deadline is too close")