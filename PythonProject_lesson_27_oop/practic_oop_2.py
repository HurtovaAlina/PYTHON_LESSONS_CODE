## Завдання 1 — Клас `BankCard` з лімітами та пін-кодом

# Створіть клас **BankCard** з атрибутами:
#
# *   `owner` — власник картки
# *   `balance` — поточний баланс
# *   `pin` — пін-код
# *   `daily_limit` — денний ліміт зняття грошей
# *   `withdrawn_today` — сума вже знятих за поточний день

class BankCard:

    def __init__(self, owner, balance, pin, daily_limit):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.daily_limit = daily_limit
        self.withdrawn_today = 0


# **Методи:**
#
# 1.  **Метод авторизації по пін-коду**
#     *   Логіка: перевіряє, чи співпадає введений код з піном картки. Якщо ні — доступ до операцій заборонено.
#     *   Параметри:
#         *   `self`
#         *   `entered_pin` — введений користувачем пін-код

    def auth(self, entered_pin):
        return self.pin == entered_pin

#
# 2.  **Метод поповнення рахунку**
#     *   Логіка: додає суму до балансу, але тільки якщо користувач уже авторизований.
#     *   Параметри:
#         *   `self`
#         *   `amount` — сума поповнення
    def add_money(self, amount):
        entered_pin = input("Enter pin to add amount ")
        if self.auth(entered_pin):
            self.balance += amount
            print(f"Added amount {amount} to your balance")
        else:
            print("Wrong PIN")
#
# 3.  **Метод зняття грошей**
#     *   Логіка:
#         *   перевірити, чи авторизований користувач
#         *   перевірити, чи вистачає грошей на балансі
#         *   перевірити, чи не буде перевищено `daily_limit`
#         *   якщо все ок — зменшити баланс і збільшити `withdrawn_today`
#     *   Параметри:
#         *   `self`
#         *   `amount` — сума для зняття
    def withdraw_money(self, amount):
        entered_pin = input("Enter pin to withdraw money ")
        if self.auth(entered_pin):
            if self.balance >= amount:
                if self.withdrawn_today + amount <= self.daily_limit:
                    self.balance -= amount
                    self.withdrawn_today += amount
                    print(f"Your balance was decreased on {amount}")
                    remaining = self.daily_limit - self.withdrawn_today
                    print(f"Remaining daily limit: {remaining}")
                else:
                    print(f"You can not withdraw - {self.withdrawn_today + amount} more than remaining  daily limit")
            else:
                print(f"It is not allowed to withdraw {amount} for current balance {self.balance}")
        else:
            print("Wrong PIN")

    def get_current_balance(self):
        print(f"Current balance {self.balance}")
#
# 4.  **Метод скидання денного ліміту** (наприклад, на початку нового дня)
#     *   Логіка: обнуляє `withdrawn_today`.
#     *   Параметри:
#         *   `self`

    def reset_daily_limit(self):
        self.withdrawn_today = 0
        print("Daily limit reset")

bank_account = BankCard("Alina", 5000, "2314", 3000)

bank_account.get_current_balance()

amount_to_add = float(input("Enter amount to add "))
bank_account.add_money(amount_to_add)

bank_account.get_current_balance()

amount_to_withdraw = float(input("Enter amount to withdraw "))
bank_account.withdraw_money(amount_to_withdraw)

bank_account.get_current_balance()

amount_to_withdraw = float(input("Enter amount to withdraw "))
bank_account.withdraw_money(amount_to_withdraw)

bank_account.reset_daily_limit()
