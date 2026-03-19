# Фінансова звітність для різних організацій
# Щороку ваша компанія надає різним державним організаціям фінансову звітність.
# Залежно від організації формати звітності різні. Використовуючи механізм декораторів,
# вирішіть питання звітності для організацій.
import datetime
import time


report = ["tax service", "government statistic", "pension fund"]

base_finance_report = [
    {"article":"income", "total_value":"income_value", "sub_articles": ["main_income","other_income"]},
    {"article":"expences", "total_value":"expences_value", "sub_articles": ["main_expences","salary", "other"] },
    {"article":"profit", "total_value":"profit_value", "sub_articles": ["main_profit","other_profit"]},
    {"article":"taxes", "total_value":"taxes_value", "sub_articles": ["vat","salary_tax", "profit_tax", "other"]},
    {"article":"other expences", "total_value":"other_expences_value", "sub_articles": ["extraordinary","financial"]}
]

def getReportForType(base_report, type):
    new_report = []
    for item in base_report:
        if type == "tax service" and item["article"] == "taxes":
            new_report.append(item)
        elif type == "government statistic" and (item["article"] == "income" or item["article"] == "expences"
                                                 or item["article"] == "profit"):
            new_report.append(item["total_value"])
        elif type == "pension fund":
            for i in item["sub_articles"]:
                    if i == "salary" or i == "salary_tax":
                        new_report.append(i)
    return new_report

def printBaseFinanceReport(report):
    for item in report:
        print(item, end ="\n")


def setReportDecoratorWrapper(report_type): # передаємо тип звітності у декоратор як параметр
    def typeOfReportDecorator(myFunction):
        print("Base finance report: ")
        printBaseFinanceReport(base_finance_report) # друкуємо загальний звіт
        print("This is report for {}".format(report_type))
        def getReport(*args): # звіт в залежності від типу
            print("Getting report...")
            report = myFunction(*args)
            return report
        return getReport
    return typeOfReportDecorator

report_type = input("Enter type of report: {} ".format(report))
result_report_type = setReportDecoratorWrapper(report_type)

result_report = result_report_type(getReportForType)
print(list(result_report(base_finance_report, report_type)))

#
# Аудит дій користувача
# У системі є функції, які виконують критичні операції (створення, видалення, зміна даних).
# Потрібно автоматично фіксувати в журналі хто виконав дію, яку саме дію, з якими параметрами і коли.
# Використовуючи декоратори, реалізуйте аудит для таких функцій.

actions = ["create", "delete", "update"]
log_action = []

def create():
    new_user_id = input("Enter new user ")
    print("New user is created")
    return new_user_id

def delete():
    deleted_user_id = input("Enter deleted user ")
    print("User was deleted")
    return deleted_user_id

def update():
    current_data = input("Enter data to update ")
    new_data = input("Enter new data ")
    print("Data was updated")
    return {"old": current_data, "new": new_data}

def performActionOfType(action_type):
    if action_type == "create":
        return create
    elif action_type == "delete":
        return delete
    elif action_type == "update":
        return update

def audit(action_type, user):
    def actionDecorator(myFunction):
        def performAction(*args, **kwargs):
            time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")
            action = myFunction(*args, **kwargs)
            log = {
                "user": user,
                "action": action_type,
                "time": time,
                "params": action
            }

            log_action.append(log)

            print("\n--- AUDIT LOG ---")
            print(log)
            return action
        return performAction()
    return actionDecorator

user = input("Enter user: ")
action_type = input("Select type of action: {} ".format(actions))

perform_action = audit(action_type, user)
result = perform_action(performActionOfType(action_type))


# Обмеження частоти запитів
# Ви розробляєте API, і деякі функції не можна викликати надто часто, щоб не
# перевантажувати систему. Потрібно обмежити кількість викликів однієї функції за певний проміжок
# часу для одного користувача. Використовуючи декоратори, реалізуйте rate limit для функцій.

def rate_limit(max_calls, period_seconds):
    calls = []
    def call_count(fn):
        def wrapper(*args):
            nonlocal calls
            start = datetime.datetime.now()
            calls = [t for t in calls if (start - t).total_seconds() < period_seconds]
            print(*calls)
            print("count of calls: ",len(calls))
            if len(calls) >= max_calls:
                print(f"Rate limit exceeded. Function was not called. Try later.")
                return None
            calls.append(start)
            return fn(*args)
        return wrapper
    return call_count

@rate_limit(max_calls=3, period_seconds=10)
def get_info():
    print("Getting info....")

for i in range(1, 6):
    get_info()
    time.sleep(2)
