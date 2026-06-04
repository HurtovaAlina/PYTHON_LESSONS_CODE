from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import dotenv
import os

dotenv.load_dotenv()

# отримуємо потрібні змінні з .env
host = os.getenv('HOST')
print(host)
port = os.getenv('PORT')
user = os.getenv('DB_USER')
password = os.getenv('PASSWORD')
# print(password)
db = os.getenv('DB')

db_uri = f"postgresql+psycopg2://{user}:{password}@{host}/{db}"

# створення підкючення (engine)
engine = create_engine(db_uri)

#створення сессії(session) на основі підключення (engine)
Session = sessionmaker(bind=engine) # клас з можливістю підключення до engine
session = Session() # конкретна сессія

# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))

# ▷ Вивести прізвища лікарів та їх спеціалізації;

def print_query(session, query):
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

def show_doctors(session):
    query = f"""
        SELECT NAME, SURNAME
        FROM DOCTORS
    """
    print("Вивести прізвища лікарів")
    print_query(session, query)

show_doctors(session)


# ▷ Вивести прізвища та зарплати (сума ставки та надбавки)
# лікарів, зарплатня яких > 40 000;
def show_salary(session, salary):
    query = f"""
            SELECT SURNAME, SALARY
            FROM DOCTORS
            WHERE SALARY >{salary}
        """
    print(f"Вивести прізвища та зарплати (сума ставки та надбавки) лікарів, зарплатня яких > {salary}")
    print_query(session, query)

show_salary(session, 40000)

# ▷ Вивести назви палат, які знаходяться у певному відділенні;
def show_ward_in_building(session, building):
    query = f"""
                SELECT NAME
                FROM WARDS
                WHERE BUILDING = {building}
            """
    print(f"Вивести назви палат, які знаходяться у певному відділенні {building}")
    print_query(session, query)

show_ward_in_building(session, 1)


# Вивести назви захворювань усіх ступенів тяжкості, крім 1-го та 2-го.;
def show_diseases(session, excluded_diseases):
    query = f"""
        SELECT NAME, SEVERITY
        FROM DISEASES
        WHERE SEVERITY NOT IN {excluded_diseases}
    """
    print(f"Вивести назви захворювань усіх ступенів тяжкості, крім {excluded_diseases}")
    print_query(session, query)


show_diseases(session, (1,2))

# Вивести кількість відділень у кожному корпусі.
def departments_qty_in_building(session):
    query = f"""
        SELECT BUILDING, COUNT(*) AS DEPARTMENTS_QTY
        FROM DEPARTMENTS
        GROUP BY BUILDING
        ORDER BY BUILDING
    """
    print("Вивести кількість відділень у кожному корпусі")
    print_query(session, query)

departments_qty_in_building(session)

# Назви палат в певному відділенні
def show_name_departments(session):
    query = f"""
        SELECT NAME
        FROM DEPARTMENTS
    """
    print_query(session, query)

def wards_in_buildig(session):
    show_name_departments(session)
    name_department = input("Enter department ")
    query = f"""
            SELECT *
            FROM WARDS W
            JOIN DEPARTMENTS D ON D.BUILDING = W.BUILDING
            WHERE D.NAME = '{name_department}'
        """
    print("Вивести Назви палат в певному відділенні")
    print_query(session, query)

wards_in_buildig(session)

# Вивести загальну суму фінансування для кожного корпусу.

def financing_amount(session):
    query = f"""
        SELECT BUILDING, SUM(FINANCING) AS TOTAL_FINANCING
        FROM DEPARTMENTS
        GROUP BY BUILDING
        ORDER BY BUILDING
    """
    print("Вивести загальну суму фінансування для кожного корпусу")
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(f'("building" {row._mapping["building"]}, "financing" {row._mapping["total_financing"]})')

financing_amount(session)

# Вивести назви відділень, які знаходяться у корпусі 3 з
# фондом фінансування у діапазоні від 120000 до 250000.
def departments_with_financing(session):
    building = input("Enter building ")
    print("Enter range of financing")
    start = input("Start value ")
    end = input("End value ")

    query = f"""
        SELECT NAME
        FROM DEPARTMENTS
        WHERE BUILDING = {building} AND FINANCING BETWEEN {start} AND {end}
    """
    print(f"Вивести назви відділень, які знаходяться у корпусі {building} з фондом фінансування у діапазоні "
          f"від {start} до {end}")
    print_query(session, query)

departments_with_financing(session)

# палати в будівлі з фінансуванням > 250 000

def wards_with_financing(session):
    financing = input("Enter financing ")
    query = f"""
        SELECT *
        FROM WARDS W
        JOIN DEPARTMENTS D ON D.BUILDING = W.BUILDING
        WHERE D.FINANCING > {financing}
    """
    print(f"Вивести Назви палат в будівлі з фінансуванням > {financing}")
    print_query(session, query)

wards_with_financing(session)
