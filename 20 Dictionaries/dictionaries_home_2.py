# Завдання 1
# Є словник з курсами валют, де ключ – назва валюти,
# значення – курс до гривні. Користувач вводить назву валюти,
# суму та назву нової валюти, в яку треба перевести суму.
# Підказка 1: для того щоб перевести, скажімо, 10 доларів у
# євро, спочатку треба перевести 10 доларів у гривні, після чого
# гривні переводити у євро.
# Підказка 2: щоб можна було переводити долари у
# гривні(або гривні у долари), потрібно щоб у словнику була
# інформація скільки гривень в 1 гривні

currencies = {
    "USD": 41.2,
    "EUR": 44.5,
    "PLN": 10.3,
    "GBP": 52.1,
    "UAH": 1
}

def currency_check(currency, currencies):

    if currency == "":
        raise ValueError("Currency can not be empty")

    if not currency.isalpha():
        raise ValueError("Currency must be letters")

    if currency not in currencies:
        raise KeyError(f"Currency {currency} is not supported")

    return currency


def currency_exchange():
    currency_name = input("Enter currency ").upper()
    currency_name = currency_check(currency_name, currencies)

    currency_name_to_change = input("Enter currency do you want to change ").upper()
    currency_name_to_change = currency_check(currency_name_to_change, currencies)

    if currency_name == currency_name_to_change:
        print("Currencies are the same")
        return

    currency_amount = float(input("Enter currency amount do you want to change "))

    if currency_amount <= 0:
        raise ValueError("Currency can not be negative or zero")

    print(f"Changing currency {currency_amount} from {currency_name} to {currency_name_to_change}")
    hryvna = currencies[currency_name]*currency_amount

    changed_currency = round(hryvna/currencies[currency_name_to_change],2)

    return changed_currency

try:
    print(currency_exchange())

except ValueError as e:
    print("Value error:", e)

except KeyError as e:
    print("Key error:", e)



# Завдання 2
# Напишіть функцію, яка отримує 2 множини з іменами
# працівників, які працюють в офісі та віддалено. Виведіть на
# екран:
#  Імена усіх працівників
#  Імена працівників, які працюють і в офісі, і віддалено
#  Відсоток працівників, які працюють і в офісі, і
# віддалено

office = {"Ivan", "Oleg", "Anna", "Maria"}
remote = {"Anna", "Petro", "Oleg", "Max"}

def get_all_employees(office, remote):
    return office.union(remote)

def get_employees_office_remote_both(office, remote):
    return office.intersection(remote)

all_employees = get_all_employees(office, remote)
print("All employees ", all_employees)
remote_office_employees = get_employees_office_remote_both(office, remote)
print("Employees working in office and remote ", remote_office_employees)

try:
    qty_all_employees = len(all_employees)
    qty_remote_office_employees = len(remote_office_employees)
    percent = round((qty_remote_office_employees/qty_all_employees)*100, 2)
except ZeroDivisionError as error:
    print("Zero division: ", error)
    percent = 0

print(f"Percent of employees working in office and remote in total amount of employees - {percent}%")
