# # Завдання 1
# # Написати програму, яка за вибором користувача зводить введене ним число у ступінь від нульового до сьомого
# # включно.
# num = int(input("Enter number "))
# power = int(input("Enter pow from 0 to 7 "))
#
# if 0<= power <=7:
#     result = num ** power
#     print(result)
# else:
#     print("Wrong value of power!")
#
# # Завдання 2
# # Написати програму підрахунку вартості розмови для різних мобільних операторів. Користувач вводить вартість
# # розмови і вибирає з якого на який оператор він телефонує. Вивести вартість на екран.
#
# call_duration = float(input("Enter call duration, min "))
# provider = input("Enter provider Vodafone | Kyivstar | Life ")
# vodafone_price = 1.50
# kyivstar_price = 1.20
# life_price = 1.15
#
# if provider == "Vodafone":
#     cost = round(call_duration*vodafone_price, 2)
#     print("Cost: ", cost)
# elif provider == "Kyivstar":
#     cost = round(call_duration*kyivstar_price,2)
#     print("Cost: ", cost)
# elif provider == "Life":
#     cost = round(call_duration * life_price, 2)
#     print("Cost: ", cost)
# else:
#     print("Wrong data")
#
# # Завдання 3
# # Користувач вводить із клавіатури число в діапазоні від 1 до 100. Якщо число кратне 3 (ділиться на 3 без залишку)
# # потрібно вивести слово Fizz. Якщо число кратне 5 потрібно вивести слово Buzz. Якщо число кратне 3 і 5 потрібно
# # вивести Fizz Buzz. Якщо число не кратне не 3 і 5 потрібно вивести саме число.
# # Якщо користувач ввів значення не в діапазоні від 1 до 100 потрібно вивести повідомлення про помилку.
#
# number = int(input("Enter number "))
# if 1<= number <=100:
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# else:
#     print("Wrong number")
#
#
# # Завдання 4
# # Зарплата менеджера становить 200$ + відсоток від продажів, продажі до 500$ – 3%, від 500 до 1000 – 5%,
# # понад 1000 – 8%. Користувач вводить із клавіатури рівень продажів для трьох менеджерів.
# # Визначити їхню зарплату, визначити найкращого менеджера, нарахувати йому премію 200$,
# # вивести підсумки на екран.
#
# sales_1 = float(input("Enter sales for manager_1 "))
# sales_2 = float(input("Enter sales for manager_2 "))
# sales_3 = float(input("Enter sales for manager_3 "))
#
# salary_1 = 200.00
# salary_2 = 200.00
# salary_3 = 200.00
#
# if sales_1 < 500:
#     salary_1 = round(salary_1 + salary_1*0.03, 2)
#     print("Manager_1 salary ", salary_1)
# elif 500 <= sales_1 < 1000:
#     salary_1 = round(salary_1 + salary_1*0.05, 2)
#     print("Manager_1 salary ", salary_1)
# elif sales_1 >= 1000:
#     salary_1 = round(salary_1 + salary_1*0.08, 2)
#     print("Manager_1 salary ", salary_1)
#
# if sales_2 < 500:
#     salary_2 = round(salary_2 + salary_2*0.03, 2)
#     print("Manager_2 salary ", salary_2)
# elif 500 <= sales_2 < 1000:
#     salary_2 = round(salary_2 + salary_2*0.05, 2)
#     print("Manager_2 salary ", salary_2)
# elif sales_2 >= 1000:
#     salary_2 = round(salary_2 + salary_2*0.08, 2)
#     print("Manager_2 salary ", salary_2)
#
# if sales_3 < 500:
#     salary_3 = round(salary_3 + salary_3*0.03, 2)
#     print("Manager_3 salary ", salary_3)
# elif 500 <= sales_3 < 1000:
#     salary_3 = round(salary_3 + salary_3* 0.05, 2)
#     print("Manager_3 salary ", salary_3)
# elif sales_3 >= 1000:
#     salary_3 = round(salary_3 + salary_3*0.08, 2)
#     print("Manager_3 salary ", salary_3)
#
# max_salary = salary_1
# best_manager = "Manager_1"
# if salary_2> max_salary:
#     max_salary = salary_2
#     best_manager = "Manager_2"
# if salary_3> max_salary:
#     max_salary = salary_3
#     best_manager = "Manager_3"
# print("Best manager: ", best_manager)
# print("Max_salary ", max_salary)
# salary_with_bonus = max_salary + 200
# print("Salary with bonus ", salary_with_bonus)
#
# # Завдання 5
# # Користувач вводить суму кредиту і термін (у роках). Програма визначає процентну ставку і розраховує
# # загальну суму до виплати:
# # Для кредиту до 10 000$ на строк до 3 років – ставка 8%.
# # Для кредиту до 10 000$ на строк понад 3 роки – ставка 10%.
# # Для кредиту від 10 001$ до 50 000$ на строк до 3 років – ставка 12%.
# # Для кредиту від 10 001$ до 50 000$ на строк понад 3 роки – ставка 15%.
# # Для кредиту понад 50 000$ на будь-який термін – ставка 20%.
# # Програма виводить підсумкову суму до виплати і щомісячний платіж.
#
# sum_loan = float(input("Enter sum of loan "))
# term_loan = int(input("Enter term of loan, years "))
#
# rate = 0
#
# if sum_loan <= 10000:
#     if term_loan <=3:
#         rate = 0.08
#     else:
#         rate = 0.10
# elif 10001 <= sum_loan < 50000:
#     if term_loan <=3:
#         rate = 0.12
#     else:
#         rate = 0.15
# elif sum_loan > 50000:
#     rate = 0.20
# total = sum_loan + (sum_loan*rate)*term_loan
# sum_monthly = total/term_loan
#
# print(f"Rate: {rate*100}%")
# print("Total amount ", total)
# print("Monthly payment ", round(sum_monthly,2))
#
#
# # Завдання 6
# # Ви розробляєте програму для розрахунку вартості комплексного обіду в ресторані.
# # Меню складається з трьох категорій: закуска, основна страва і десерт. Залежно від вибору клієнта і його
# # статусу програма повинна розрахувати підсумкову вартість з урахуванням можливих знижок і спеціальних
# # пропозицій.
# # Умови:
# # Меню комплексного обіду.
# # Закуски:
# # Салат – 5$,
# # Суп – 7$.
# # Основні страви:
# # Курка – 10$,
# # Риба – 12$.
# # Десерти:
# # Морозиво – 3$,
# # Фрукти – 4$.
# # Знижки.
# # Якщо клієнт замовляє всі три позиції (закуску, основну страву і десерт), надається знижка 10% на
# # все замовлення.
# # Якщо сума замовлення перевищує 20$, знижка збільшується до 15%.
# # Для постійних клієнтів надається додаткова знижка 5%, яка підсумовується з іншими знижками.
# # Спеціальні пропозиції.
# # Якщо клієнт замовляє "Суп" і "Рибу", надається знижка 2$ на десерт.
# # Якщо клієнт замовляє "Курку" і "Морозиво", до замовлення додається безкоштовний напій (наприклад, "Чай").
# # Підсумкова вартість.
# # Програма повинна коректно застосувати всі знижки та спеціальні пропозиції, а потім розрахувати
# # підсумкову вартість замовлення.
#
# snack = input("Enter snack: salad | soup ")
# main_dish = input("Enter main dish: chicken | fish ")
# desert = input("Enter desert: ice cream | fruits ")
# client = input("Are you a client of restaurant? Y | N : ")
#
#
# snack_salad = 5.00
# snack_soup = 7.00
# main_chicken = 10.00
# main_fish = 12.00
# desert_fruits = 4.00
# desert_ice_cream = 3.00
# order_amount = 0
# discount = 0
#
# match snack:
#     case "salad": order_amount = order_amount + snack_salad
#     case "soup": order_amount = order_amount + snack_soup
# match main_dish:
#     case "chicken": order_amount = order_amount + main_chicken
#     case "fish": order_amount = order_amount + main_fish
# match desert:
#     case "ice cream": order_amount = order_amount + desert_ice_cream
#     case "fruits": order_amount = order_amount + desert_fruits
# #Якщо клієнт замовляє всі три позиції (закуску, основну страву і десерт), надається знижка 10% на
# # все замовлення.
# if snack and main_dish and desert:
#     discount = discount + 0.10
#     print(f"Discount 10% is applied for 3 dishes:  {discount*100}%")
# # Якщо сума замовлення перевищує 20$, знижка збільшується до 15%.
# if order_amount > 20:
#     discount = 0.15
#     print(f"Discount is increased to 15% for total order amount > 20$: {discount*100}%")
# # Для постійних клієнтів надається додаткова знижка 5%, яка підсумовується з іншими знижками.
# if client == "Y":
#     discount = discount + 0.05
#     print(f"Discount 5% is applied for client: {discount * 100}%")
# order_amount = round(order_amount - order_amount * discount, 2)
#
# # Спеціальні пропозиції
# # Якщо клієнт замовляє "Суп" і "Рибу", надається знижка 2$ на десерт.
# if snack == "soup" and main_dish == "fish" and desert != "":
#     order_amount = order_amount - 2
#     print(f"Discount -2$ was applied to desert")
# # Якщо клієнт замовляє "Курку" і "Морозиво", до замовлення додається безкоштовний напій (наприклад, "Чай").
# if main_dish == "chicken" and desert == "ice cream":
#     print("Free drink was added to the order")
# #Output
# if discount == 0.0:
#     print(f"You don't have applied discounts and your order amount: {round(order_amount, 2)}$")
# else:
#     print(f"Your order amount with applied discounts: {round(order_amount, 2)}$")

#Завдання 6*.
# Умова
# Користувач вводить ціле число n від 1 до 10000(сума для зняття).Програма має “видати” цю суму
# і показати її: цифрами словами(у дужках)
# Приклад: Введіть суму для зняття: 1981
# Знято: 1981(тисяча дев'ятсот вісімдесят один)

amount = int(input("Enter amount to withdraw from 1 to 10 000 "))
n5 = amount % 10
n4 = (amount // 10) % 10
n3 = (amount // 100) % 10
n2 = (amount // 1000) % 10
n1 = amount // 10000

n1_amount = ""
n2_amount = ""
n3_amount = ""
n4_amount = ""
n5_amount = ""

#print(f"{n1}, \n{n2}, \n{n3}, \n{n4}, \n{n5}")
if amount <= 10000 and isinstance(amount, int):
    if n1 == 1:
        n1_amount = "десять тисяч гривень"
    else:
        if n2 > 0:
            match n2:
                case 1:
                    n2_amount = "тисяча"
                case 2:
                    n2_amount = "дві тисячі"
                case 3:
                    n2_amount = "три тисячі"
                case 4:
                    n2_amount = "чотири тисячі"
                case 5:
                    n2_amount = "пʼять тисяч"
                case 6:
                    n2_amount = "шість тисяч"
                case 7:
                    n2_amount = "сім тисяч"
                case 8:
                    n2_amount = "вісім тисяч"
                case 9:
                    n2_amount = "девʼять тисяч"
        if n3 > 0:
            match n3:
                case 1:
                    n3_amount = "сто"
                case 2:
                    n3_amount = "двісті"
                case 3:
                    n3_amount = "триста"
                case 4:
                    n3_amount = "чотириста"
                case 5:
                    n3_amount = "пʼятсот"
                case 6:
                    n3_amount = "шістсот"
                case 7:
                    n3_amount = "сімсот"
                case 8:
                    n3_amount = "вісімсот"
                case 9:
                    n3_amount = "девʼятсот"
        if n4 == 1 and n5 == 0:
            n4_amount = "десять"
        if n4 == 1 and n5 > 0:
            match n5:
                case 1:
                    n4_amount = "одинадцять"
                case 2:
                    n4_amount = "дванадцять"
                case 3:
                    n4_amount = "тринадцять"
                case 4:
                    n4_amount = "чотирнадцять"
                case 5:
                    n4_amount = "пʼятнадцять"
                case 6:
                    n4_amount = "шістнадцять"
                case 7:
                    n4_amount = "сімнадцять"
                case 8:
                    n4_amount = "вісімнадцять"
                case 9:
                    n4_amount = "девʼятнадцять"
        if 1 < n4 <=9:
            match n4:
                case 2:
                    n4_amount = "двадцять"
                case 3:
                    n4_amount = "тридцять"
                case 4:
                    n4_amount = "сорок"
                case 5:
                    n4_amount = "пʼятдесят"
                case 6:
                    n4_amount = "шістдесят"
                case 7:
                    n4_amount = "сімдесят"
                case 8:
                    n4_amount = "вісімдесят"
                case 9:
                    n4_amount = "девʼяносто"
        if 9 >= n5 >= 1 != n4:
            match n5:
                case 1:
                    n5_amount = "один"
                case 2:
                    n5_amount = "два"
                case 3:
                    n5_amount = "три"
                case 4:
                    n5_amount = "чотири"
                case 5:
                    n5_amount = "пʼять"
                case 6:
                    n5_amount = "шість"
                case 7:
                    n5_amount = "сім"
                case 8:
                    n5_amount = "вісім"
                case 9:
                    n5_amount = "девʼять"
    print(f"{amount} : ({n1_amount} {n2_amount} {n3_amount} {n4_amount} {n5_amount} UAH)")
else:
    print("Wrong amount")
