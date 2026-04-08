# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.

class CreditCardPayment:

    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount):
        print(f"оплата карткою {amount} {self._currency}")


class PayPalPayment:

    def __init__(self, currency: str):
        self._currency = currency


    def pay(self, amount):
        print(f"оплата PayPal {amount} {self._currency}")


class CryptoPayment:

    def __init__(self, currency: str):
        self._currency = currency

    def pay(self, amount):
        print(f"оплата криптогаманцем {amount} {self._currency}")

def  create_payment() -> CreditCardPayment | PayPalPayment | CryptoPayment | None:

    type_of_payment = input("Enter payment CreditCard | PayPal | Crypto ").lower()

    if type_of_payment == "creditcard":
        currency = input("Enter currency ")
        return CreditCardPayment(currency)

    elif type_of_payment == "paypal":
        currency = input("Enter currency ")
        return PayPalPayment(currency)

    elif type_of_payment == "crypto":
        currency = input("Enter currency ")
        return CryptoPayment(currency)

    else:
        print("Invalid type of payment")
        return None


payments = []

for _ in range(3):
    payment = create_payment()
    if payment:
        payments.append(payment)

for payment in payments:
    payment.pay(1000)
