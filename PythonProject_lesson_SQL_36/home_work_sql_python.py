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
db = os.getenv('DB_1')

db_uri = f"postgresql+psycopg2://{user}:{password}@{host}/{db}"

# створення підкючення (engine)
engine = create_engine(db_uri)

#створення сессії(session) на основі підключення (engine)
Session = sessionmaker(bind=engine) # клас з можливістю підключення до engine
session = Session() # конкретна сессія

def print_query(session, query):
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

def show_all_records(session, table):
    print(f"All records of: {table}")
    query = f"SELECT * FROM {table}"
    print_query(session, query)


def show_data_by_id(session, table, id_record):
    query = (f"SELECT * "
             f"FROM {table} "
             f"WHERE id = {id_record}")
    print_query(session, query)


def show_column_of_records(session, table, column):
    query = f"""
                    SELECT {column}
                    FROM {table};
                """
    print_query(session, query)


def update_record(session):
    table = input("Enter table name: ")
    show_all_records(session, table)
    id_record = input("Enter id of record to update: ")
    field_to_update = input("Enter field to update: ")
    new_value = input(f"Enter new value for the field {field_to_update}: ")
    query = f"""
                UPDATE {table}
                SET {field_to_update} = {new_value}
                WHERE id = {id_record} ;
            """
    print(f"Field {field_to_update} in table {table} was updated by {new_value}")
    query = text(query)
    session.execute(query)
    print("Updated record")
    show_data_by_id(session, table, id_record)


def delete_record_by_id(session):
    table = input("Enter table name: ")
    show_all_records(session, table)
    id_record = input("Enter id of record to delete: ")
    query = f"""
        DELETE FROM {table}
        WHERE ID = {id_record};
    """
    print(f"Record with {id_record} was deleted")
    query = text(query)
    session.execute(query)


def show_names_teachers_for_group(session, group):
    query = f"""
        SELECT T.NAME AS TEACHER_NAME, T.SURNAME AS TEACHER_SURNAME, G.NAME AS GROUP_NAME
        FROM TEACHERS T
        JOIN LECTURES L ON L.TEACHER_ID = T.ID
        JOIN GROUPS_LECTURES GL ON GL.LECTURE_ID = L.ID
        JOIN GROUPS G ON GL.GROUP_ID = G.ID
        WHERE G.NAME = '{group}'
    """
    print_query(session, query)

def show_departments_groups(session):
    query = """
        SELECT D.NAME AS DEPARTMENT, G.NAME AS GROUP_NAME
        FROM DEPARTMENTS D
        JOIN GROUPS G ON G.DEPARTMENT_ID = D.ID
    """
    print_query(session, query)

def show_subjects_for_teacher(session, name, surname):
    query = f"""
        SELECT T.NAME AS TEACHER_NAME, T.SURNAME AS TEACHER_SURNAME, S.NAME AS SUBJECT_NAME
        FROM TEACHERS T
        JOIN LECTURES L ON L.TEACHER_ID = T.ID
        JOIN SUBJECTS S ON S.ID = L.SUBJECT_ID
        WHERE T.NAME = '{name}' AND T.SURNAME = '{surname}'
    """
    print_query(session, query)

update_record(session)
delete_record_by_id(session)
show_all_records(session, "groups")

# вивести інформацію про всі навчальні групи,
show_all_records(session, "groups")

# ▷ вивести інформацію про всіх викладачів,
show_all_records(session, "teachers")

# ▷ вивести назви усіх кафедр,
show_column_of_records(session, "departments", "name")

# ▷ вивести імена та прізвища викладачів, які читають лекції в конкретній групі,
show_names_teachers_for_group(session, "AI-201")

# ▷ вивести назви кафедр і груп, які до них відносяться,
show_departments_groups(session)

# ▷ вивести назви предметів, які викладає конкретний викладач,
show_subjects_for_teacher(session, "Sarah", "Williams")
