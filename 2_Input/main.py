# Завдання 1
# Користувач вводить з клавіатури три числа. Необхідно знайти суму чисел, добуток чисел.
# Результат обчислень вивести на екран.
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
sum = n1 + n2 + n3
mult = n1 * n2 * n3
print(f"Sum = {sum}")
print(f"Mult = {mult}")

# Завдання 2
# Напишіть програму, що обчислює площу ромба. Користувач з клавіатури вводить довжину двох його діагоналей.
length_diag_1 = int(input("Enter length 1, sm: "))
length_diag_2 = int(input("Enter length 2, sm: "))
square = (length_diag_1 * length_diag_2) / 2
print("Romb square = ", square, "sm2")

# Завдання 3
# Користувач вводить з клавіатури три числа. Перше число - зарплата за місяць, друге число — сума місячного платежу
# за кредитом у банку, третє число — заборгованість за комунальні послуги.
# Необхідно вивести на екран суму, яка залишиться у користувача після всіх виплат.
salary = float(input("Enter salary : "))
credit = float(input("Enter credit : "))
debts = float(input("Enter debts : "))
sum_to_spend = salary - credit - debts
print(f"Sum to spend: {sum_to_spend}")

# Завдання 4
# Напишіть програму, яка обчислює вартість поїздки на автомобілі.
# Користувач вводить відстань у кілометрах, витрату палива на 100 кілометрів і ціну за літр бензину.
# Програма повинна вивести підсумкову вартість поїздки.
way = float(input("Enter way length, km : "))
petrol = float(input("Enter petrol volume in liters for 100 km : "))
petrol_price = float(input("Enter price of liter of petrol : "))
cost = (petrol / 100) * way * petrol_price
print(f"Cost of way {way} km : {cost}")

# Завдання 5
# Користувач вводить загальну суму рахунку в ресторані та кількість осіб, які будуть ділити рахунок.
# Напишіть програму, яка розраховує суму чайових (15% від загальної суми) і загальну суму, включаючи чайові.
# Потім програма повинна розділити загальну суму з чайовими на кількість осіб і вивести, скільки кожна
# людина має заплатити.
sum_of_bill = float(input("Enter sum of bill : "))
persons = int(input("Enter amount of persons: "))
sum_of_tips = sum_of_bill * 15 / 100
bill_with_tips = sum_of_bill + sum_of_tips
payment_per_person = bill_with_tips / persons
print(
    f"Payment per person for {persons} persons for common bill including tips {bill_with_tips:.2f}$: "
    f"{payment_per_person:.2f}$"
)

# Завдання 6
# Користувач вводить вартість оренди автомобіля за день, кількість днів оренди та суму застави, яку потрібно внести.
# Напишіть програму, яка розраховує загальну вартість оренди (з урахуванням застави) і виводить суму, яку необхідно
# заплатити користувачеві після повернення автомобіля (припускаючи, що застава повертається повністю).
# Програма повинна також розділити підсумкову суму оренди (без застави) на кількість днів і вивести вартість оренди
# за один день.
rent_price_per_day = float(input("Enter price of rent per day : "))
days_of_rent = int(input("Enter day of rent: "))
deposit = float(input("Enter deposit : "))
full_cost_of_rent = rent_price_per_day * days_of_rent + deposit
cost_of_rent_excl_dep = full_cost_of_rent - deposit
cost_of_rent_day = cost_of_rent_excl_dep / days_of_rent
print(
    f"Cost of rent after deposit refund: {cost_of_rent_excl_dep:.2f}$ "
    f"\nCost of rent per day: {cost_of_rent_day:.2f}$"
)
