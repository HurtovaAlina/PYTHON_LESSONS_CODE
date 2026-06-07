-- Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE DEPARTMENTS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	FINANCING INT NOT NULL CHECK(FINANCING >=0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO DEPARTMENTS (FINANCING, NAME) VALUES
-- (120000, 'Computer Science'),
-- (95000, 'Mathematics'),
-- (87000, 'Physics'),
-- (76000, 'Chemistry'),
-- (143000, 'Biology'),
-- (68000, 'History'),
-- (72000, 'Economics'),
-- (99000, 'Law'),
-- (81000, 'Psychology'),
-- (134000, 'Engineering'),
-- (59000, 'Philosophy'),
-- (88000, 'Foreign Languages'),
-- (101000, 'Architecture'),
-- (67000, 'Journalism'),
-- (115000, 'Medicine');

-- ¾ Факультети(Faculties)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор факультету.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Декан (Dean). Декан факультету.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнім.
-- ■ Назва (Name). Назва факультету.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE FACULTIES(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	DEAN VARCHAR(255) NOT NULL,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO FACULTIES (DEAN, NAME) VALUES
-- ('Dr. John Smith', 'Faculty of Computer Science'),
-- ('Prof. Emily Johnson', 'Faculty of Mathematics'),
-- ('Dr. Michael Brown', 'Faculty of Physics'),
-- ('Prof. Sarah Davis', 'Faculty of Chemistry'),
-- ('Dr. Daniel Wilson', 'Faculty of Biology'),
-- ('Prof. Olivia Martinez', 'Faculty of History'),
-- ('Dr. James Anderson', 'Faculty of Economics'),
-- ('Prof. Sophia Taylor', 'Faculty of Law'),
-- ('Dr. William Thomas', 'Faculty of Psychology'),
-- ('Prof. Isabella Moore', 'Faculty of Engineering'),
-- ('Dr. Benjamin Jackson', 'Faculty of Philosophy'),
-- ('Prof. Mia White', 'Faculty of Foreign Languages'),
-- ('Dr. Alexander Harris', 'Faculty of Architecture'),
-- ('Prof. Charlotte Martin', 'Faculty of Journalism'),
-- ('Dr. Ethan Thompson', 'Faculty of Medicine'),
-- ('Prof. Amelia Garcia', 'Faculty of Sociology'),
-- ('Dr. Henry Clark', 'Faculty of Political Science'),
-- ('Prof. Evelyn Lewis', 'Faculty of Arts'),
-- ('Dr. Sebastian Walker', 'Faculty of Information Technology'),
-- ('Prof. Abigail Hall', 'Faculty of International Relations');

-- ¾ Групи (Groups)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва групи.
-- ▷ Тип даних — varchar(10).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Рейтинг (Rating). Рейтинг групи.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 0 до 5.
-- ■ Курс (Year). Курс (рік), на якому навчається група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.

-- CREATE TABLE GROUPS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(10) NOT NULL UNIQUE,
-- 	RATING INT NOT NULL CHECK(RATING BETWEEN 0 AND 5),
-- 	YEAR INT NOT NULL CHECK(RATING BETWEEN 1 AND 5)
-- )

-- INSERT INTO GROUPS (NAME, RATING, YEAR) VALUES
-- ('CS101', 5, 1),
-- ('CS102', 4, 1),
-- ('CS201', 5, 2),
-- ('CS202', 3, 2),
-- ('CS301', 4, 3),
-- ('CS302', 5, 3),
-- ('CS401', 2, 4),
-- ('CS402', 4, 4),
-- ('CS501', 5, 5),
-- ('MTH101', 3, 1),
-- ('MTH201', 4, 2),
-- ('MTH301', 5, 3),
-- ('PHY101', 2, 1),
-- ('PHY201', 4, 2),
-- ('PHY301', 5, 3),
-- ('BIO101', 3, 1),
-- ('BIO201', 4, 2),
-- ('BIO301', 5, 3),
-- ('ENG101', 5, 1),
-- ('ENG201', 4, 2),
-- ('ENG301', 3, 3),
-- ('LAW101', 4, 1),
-- ('LAW201', 5, 2),
-- ('MED101', 5, 1),
-- ('MED201', 4, 2),
-- ('ART101', 2, 1),
-- ('ART201', 3, 2),
-- ('IT101', 5, 1),
-- ('IT201', 4, 2),
-- ('IT301', 5, 3);

-- ¾ Викладачі(Teachers)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- викладача.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Дата працевлаштування (EmploymentDate). Дата працевлаштування викладача.
-- ▷ Тип даних — date.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше 01.01.1990.
-- ■ Асистент (IsAssistant). Чи є викладач асистентом.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Професор (IsProfessor). Чи є викладач професором.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ім’я (Name). Ім’я викладача.
-- ▷ Тип даних — nvarchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Посада (Position). Посада викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Надбавка (Premium). Надбавка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ставка (Salary). Ставка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE TEACHERS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	EMPLOYMENT_DATE DATE NOT NULL CHECK(EMPLOYMENT_DATE > '1990-01-01'),
-- 	IS_ASSISTANT BOOLEAN NOT NULL DEFAULT FALSE,
-- 	IS_PROFESSOR BOOLEAN NOT NULL DEFAULT FALSE,
-- 	NAME VARCHAR(200) NOT NULL,
-- 	POSITION VARCHAR(200) NOT NULL,
-- 	PREMIUM INT NOT NULL CHECK(PREMIUM >=0) DEFAULT 0,
-- 	SALARY INT NOT NULL CHECK(SALARY > 0),
-- 	SURNAME VARCHAR(200) NOT NULL
-- )

-- INSERT INTO TEACHERS (
--     EMPLOYMENT_DATE,
--     IS_ASSISTANT,
--     IS_PROFESSOR,
--     NAME,
--     POSITION,
--     PREMIUM,
--     SALARY,
--     SURNAME
-- ) VALUES
-- ('2010-09-01', TRUE,  FALSE, 'Ivan',     'Assistant Lecturer',  500,  12000, 'Petrenko'),
-- ('2012-03-15', FALSE, TRUE,  'Olena',    'Professor',           2000, 25000, 'Kovalenko'),
-- ('2015-06-20', TRUE,  FALSE, 'Andrii',   'Assistant',           300,  11000, 'Shevchenko'),
-- ('2008-01-10', FALSE, TRUE,  'Mykola',   'Professor',           2500, 27000, 'Bondarenko'),
-- ('2018-11-05', TRUE,  FALSE, 'Iryna',    'Assistant Lecturer',  400,  13000, 'Tkachenko'),
-- ('2011-07-22', FALSE, TRUE,  'Sergii',   'Professor',           1800, 24000, 'Melnyk'),
-- ('2019-09-30', TRUE,  FALSE, 'Oleh',     'Assistant',           350,  12500, 'Danyliuk'),
-- ('2013-04-18', FALSE, TRUE,  'Nataliia',  'Professor',           2200, 26000, 'Rudenko'),
-- ('2020-02-12', TRUE,  FALSE, 'Dmytro',   'Assistant Lecturer',  450,  14000, 'Hrytsenko'),
-- ('2009-12-01', FALSE, TRUE,  'Tetiana',  'Professor',           3000, 28000, 'Kravchenko'),
-- ('2016-08-14', TRUE,  FALSE, 'Viktor',   'Assistant',           600,  15000, 'Lysenko'),
-- ('2014-10-25', FALSE, TRUE,  'Kateryna', 'Professor',           2100, 25500, 'Marchenko'),
-- ('2017-05-19', TRUE,  FALSE, 'Artem',    'Assistant Lecturer',  500,  13500, 'Zaitsev'),
-- ('2011-11-11', FALSE, TRUE,  'Yulia',    'Professor',           2300, 26500, 'Shevchuk'),
-- ('2021-03-03', TRUE,  FALSE, 'Bohdan',   'Assistant',           400,  14500, 'Moroz');

-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.

-- SELECT *
-- FROM DEPARTMENTS
-- ORDER BY ID DESC

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв полів відповідно до назви таблиці.
-- SELECT NAME AS GROUP_NAME, RATING AS GROUP_RATING
-- FROM GROUPS

-- 3. Вивести для викладачів їх прізвища, відсоток ставки по відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки)
-- NUMERIC отримати дробові числа
-- NULLIF(x,0) → захист від ділення на 0

-- SELECT
--     SURNAME,
--     ROUND((PREMIUM::NUMERIC / SALARY) * 100, 2) AS premium_percent_of_salary,
--     ROUND((SALARY::NUMERIC / NULLIF(PREMIUM+SALARY, 0)) * 100, 2) AS salary_percent_of_premium
-- FROM TEACHERS;

-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».
-- || — оператор конкатенації рядків
-- SELECT
--     'The dean of faculty ' || NAME || ' is ' || DEAN || '.' AS result
-- FROM FACULTIES;

-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.

-- SELECT SURNAME, SALARY
-- FROM TEACHERS
-- WHERE SALARY > 20000

-- 6. Вивести назви кафедр, фонд фінансування яких менший, ніж 11000 або більший за 25000.

-- SELECT NAME, FINANCING
-- FROM DEPARTMENTS
-- WHERE FINANCING < 80000 OR FINANCING > 100000

-- 7. Вивести назви факультетів, окрім факультету «Computer Science».

-- SELECT NAME
-- FROM FACULTIES
-- WHERE NAME <> 'Faculty of Computer Science';

-- 8. Вивести прізвища та посади викладачів, які не є професорами.

-- SELECT SURNAME, POSITION
-- FROM TEACHERS
-- WHERE IS_PROFESSOR <> true

-- 9. Вивести прізвища, посади, ставки та надбавки асистентів, надбавка яких у діапазоні від 160 до 550.

-- SELECT SURNAME, POSITION, SALARY, PREMIUM
-- FROM TEACHERS
-- WHERE IS_ASSISTANT = true AND PREMIUM BETWEEN 600 AND 2000

-- 10. Вивести прізвища та ставки асистентів.
-- SELECT SURNAME, SALARY
-- FROM TEACHERS
-- WHERE IS_ASSISTANT = true

-- 11. Вивести прізвища та посади викладачів, які були прийняті на роботу до 01.01.2000.
-- SELECT SURNAME, POSITION, EMPLOYMENT_DATE
-- FROM TEACHERS
-- WHERE EMPLOYMENT_DATE < '2016-01-01'

-- 12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле назвіть «Name of Department».
-- NAME < 'Software Development' → всі назви, які в алфавіті йдуть до цієї кафедри
-- ORDER BY NAME → сортування за алфавітом

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE NAME < 'Economics'
-- ORDER BY NAME

-- 13. Вивести прізвища асистентів із зарплатою (сума ставки та надбавки) не більше 1200.
-- SELECT SURNAME, POSITION, SALARY+PREMIUM AS TOTAL_SALARY
-- FROM TEACHERS
-- WHERE IS_ASSISTANT = true AND SALARY+PREMIUM < 25000

-- 14. Вивести назви груп 5-го курсу з рейтингом у діапазоні від 2 до 4.

-- SELECT NAME, RATING, YEAR
-- FROM GROUPS
-- WHERE YEAR = 2 AND RATING IN(2,4)

-- 15. Вивести прізвища асистентів зі ставкою менше, ніж 550 або надбавкою менше, ніж 200.
-- SELECT SURNAME, SALARY, PREMIUM
-- FROM TEACHERS
-- WHERE  IS_ASSISTANT = true AND (SALARY < 13000) OR (PREMIUM <500)
