import sqlalchemy
import psycopg2
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import dotenv
import os # бібліотека для роботи з операційною системою

# читаємо .env
dotenv.load_dotenv()

# отримуємо потрібні змінні з .env
host = os.getenv('HOST')
print(host)
port = os.getenv('PORT')
user = os.getenv('DB_USER')
password = os.getenv('PASSWORD')
# print(password)
db = os.getenv('DB')

# шлях (uri) до бази даних
db_uri = f"postgresql+psycopg2://{user}:{password}@{host}/{db}"

# створення підкючення (engine)
engine = create_engine(db_uri)

#створення сессії(session) на основі підключення (engine)
Session = sessionmaker(bind=engine) # клас з можливістю підключення до engine
session = Session() # конкретна сессія

# отримання таблиць з бази даних
# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))

# запуск sql запиту
city = "Lviv"
query = f"""
    SELECT *
    FROM STUDENTS
    WHERE CITY = '{city}'
"""
# підправити текст
query = text(query)

# запуск
result = session.execute(query)

# виведення результатів (рядків)
for row in result:
    print(row)
