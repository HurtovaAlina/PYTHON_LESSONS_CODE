# 6. Клас BankAccount — банківський рахунок
# Атрибути: номер рахунку (str), власник (str), баланс (float, за замовчуванням 0).
# Метод deposit(amount): поповнює баланс. Сума має бути більшою за 0.
# Метод withdraw(amount): знімає кошти. Забороняйте зняття більше, ніж є на
# рахунку.
# Метод get_balance(): виводить поточний баланс.
# 7. Клас Rectangle — прямокутник
# Атрибути: ширина (float), висота (float).
# Метод area(): повертає площу: ширина * висота.
# Метод perimeter(): повертає периметр: 2 * (ширина + висота).
# Метод resize(w, h): змінює розміри. Обидва значення мають бути > 0.
# 8. Клас Circle — коло
# Атрибути: радіус (float).
# Метод area(): повертає площу: π * r². Використайте math.pi.
# Метод circumference(): повертає довжину кола: 2 * π * r.
# 9. Клас Employee — співробітник
# Атрибути: ім'я (str), посада (str), зарплата (float).
# Метод display(): виводить усі дані про співробітника.
# Метод raise_salary(percent): підвищує зарплату на заданий відсоток. Перевіряйте
# percent > 0.
# 10. Клас Timer — таймер
# Атрибути: кількість секунд (int, за замовчуванням 0).
# Метод add(seconds): додає секунди. Значення має бути > 0.
# Метод subtract(seconds): віднімає секунди. Час не може стати від'ємним.
# Метод display(): виводить час у форматі "ГГ:ХХ:СС".

class Timer:

    def __init__(self, sec: int = 0):
        self.sec = sec


    def add_seconds(self, add_sec: int):
        if add_sec < 0:
            print("Value should be >0")
            return

        self.sec+=add_sec


    def subtract_seconds(self, subtr_sec):
        self.sec =max(0, self.sec-subtr_sec)



    def display(self):
        hours = self.sec // 3600  # ціла частка від ділення на 3600 - кількість повних годин
        minutes = (self.sec % 3600)//60 # залишок від ділення на 3600 - скільки хвилини, і скільки в них повних хвилин
        # (ціла частка від ділення на 60)
        if minutes == 0:
            secs = self.sec
        else:
            secs = self.sec % 60 #остача від ділення на 60 - скільки секунд

        print(f"time: {self.sec}\n"
              f"{hours:02}:{minutes:02}:{secs:02}")


time = Timer()
time.add_seconds(1000)
time.add_seconds(200)
time.add_seconds(30)
time.display()
time.subtract_seconds(1)
time.display()
time.subtract_seconds(2)
time.display()
