# Завдання 1
# Реалізуйте роботу банку. Усі дані зберігаються у
# словнику, де ключ – ім’я клієнта, значення – баланс на
# рахунку.
# Напишіть функцію, яка отримує словник з даними та
# зараховує гроші на баланс. Для цього вона запитує ім’я та
# суму у користувача, якщо користувача немає, то вносить його
# дані у словник, інакше додає суму до балансу.
# Напишіть іншу функцію, яка отримує словник з даними та
# знімає гроші з рахунку. Для цього вона запитує ім’я та суму у
# користувача, якщо користувача немає, то вивести відповідне
# повідомлення. Якщо на балансі не достатньо грошей, теж
# вивести повідомлення.
# Напишіть функцію main, яка організує роботу всієї
# програми, а саме матиме такий функціонал: поповнити
# рахунок, зняти кошти, завершити роботу

bank_accounts = {
    "Іван": 1500.00,
    "Марія": 3200.50,
    "Олег": 750.10,
    "Анна": 5400.00,
    "Петро": 120.00
}

def add_to_balance(bank_accounts):
    """
    функція, яка отримує словник з даними та
    зараховує гроші на баланс.

    Якщо користувача немає, то вносить його
    дані у словник, інакше додає суму до балансу.
    """

    client_name = input("Enter name: ")
    new_amount = float(input("Enter amount: "))

    if client_name not in bank_accounts:
        print(f"New client with {client_name} and amount {new_amount} was added")
        bank_accounts[client_name] = new_amount
    else:
        print(f"Amount for client {client_name} was increased to {new_amount}")
        bank_accounts[client_name] += new_amount
    return bank_accounts


def withdraw_amount(bank_accounts):
    """
    отримує словник з даними та
    знімає гроші з рахунку. Для цього вона запитує ім’я та суму у
    користувача, якщо користувача немає, то вивести відповідне
    повідомлення. Якщо на балансі не достатньо грошей, теж
    вивести повідомлення.

    """
    client_name = input("Enter name of client to withdraw: ")
    amount_to_withdraw = float(input("Enter amount to withdraw: "))

    if client_name not in bank_accounts:
        print(f"Client with {client_name} name was not found")
    elif bank_accounts[client_name] - amount_to_withdraw >=0:
        bank_accounts[client_name] -= amount_to_withdraw
        print(f"Amount for {client_name} was reduced by {amount_to_withdraw}")
    else:
        print(f"You current balance doesn't allow to withdraw amount {amount_to_withdraw}")

    return bank_accounts

def main() -> None:
    """
    Головна функція. Організовує всю роботу та запускає програму.

    """
    while True:

        action = input("Enter action Add/Withdraw/Finish you want to perform ")

        if action == "Add":
            print(f"Bank account was updated {add_to_balance(bank_accounts)}")
        elif action == "Withdraw":
            print(f"Bank account was updated {withdraw_amount(bank_accounts)}")
        elif action == "Finish":
            print(f"Program is finished")
            break
        else:
            print("Action is not allowed")

main()