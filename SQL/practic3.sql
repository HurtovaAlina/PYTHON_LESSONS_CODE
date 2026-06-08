-- ¾ Відділення (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор відділення.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Корпус (Building). Номер корпусу, в якому знаходиться
-- відділення.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
-- ■ Фінансування (Financing). Фонд фінансування відділення.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва відділення.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE DEPARTMENTS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	BUILDING INT NOT NULL CHECK(1 <= BUILDING AND BUILDING <= 5),
-- 	FINANCING INT NOT NULL CHECK(FINANCING >=0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO DEPARTMENTS (BUILDING, FINANCING, NAME)
-- VALUES
-- (1, 260000, 'Radiology'),
-- (2, 175000, 'Urology'),
-- (3, 230000, 'Gynecology'),
-- (4, 210000, 'Endocrinology'),
-- (5, 145000, 'Nephrology'),
-- (1, 165000, 'Psychiatry'),
-- (2, 155000, 'Gastroenterology'),
-- (3, 185000, 'Pulmonology'),
-- (4, 195000, 'Immunology'),
-- (5, 205000, 'Rehabilitation');

-- ¾ Захворювання (Diseases)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- захво-рювання.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва захворювання.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Ступінь тяжкості (Severity). Ступінь тяжкості захворювання.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 1.
-- ▷ Значення за замовчуванням — 1.

-- CREATE TABLE DISEASES(
-- ID SERIAL NOT NULL PRIMARY KEY,
-- NAME VARCHAR(100) NOT NULL UNIQUE,
-- SEVERITY INT NOT NULL CHECK(SEVERITY>1) DEFAULT 1
-- )

-- INSERT INTO DISEASES(NAME, SEVERITY)
-- VALUES
-- ('Flu', 2),
-- ('Pneumonia', 5),
-- ('Diabetes', 4),
-- ('Hypertension', 3),
-- ('Asthma', 3),
-- ('Migraine', 2),
-- ('Bronchitis', 4),
-- ('Tuberculosis', 5),
-- ('COVID-19', 5),
-- ('Chickenpox', 2),
-- ('Hepatitis', 4),
-- ('Appendicitis', 4),
-- ('Arthritis', 3),
-- ('Anemia', 2),
-- ('Allergy', 2),
-- ('Stroke', 5),
-- ('Heart Failure', 5),
-- ('Gastritis', 2),
-- ('Sinusitis', 2),
-- ('Depression', 3);

-- ¾ Лікарі (Doctors)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- лікаря.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я лікаря.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Телефон(Phone). Телефонний номер лікаря.
-- ▷ Тип даних — char(10).
-- ▷ Може містити null-значення.
-- ■ Ставка (Salary). Ставка лікаря.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище лікаря.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE DOCTORS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(255) NOT NULL,
-- 	PHONE CHAR(10),
-- 	SALARY INT NOT NULL CHECK(SALARY >=0),
-- 	SURNAME VARCHAR(255) NOT NULL
-- )

-- INSERT INTO DOCTORS(NAME, PHONE, SALARY, SURNAME)
-- VALUES
-- ('John', '0501234567', 25000, 'Smith'),
-- ('Emily', '0502345678', 22000, 'Johnson'),
-- ('Michael', '0503456789', 40000, 'Brown'),
-- ('Sarah', '0504567890', 28000, 'Davis'),
-- ('David', '0505678901', 35000, 'Wilson'),
-- ('Anna', '0506789012', 21000, 'Taylor'),
-- ('Robert', '0507890123', 33000, 'Anderson'),
-- ('Laura', '0508901234', 26000, 'Thomas'),
-- ('Daniel', '0509012345', 31000, 'Jackson'),
-- ('Sophia', '0510123456', 27000, 'White'),
-- ('James', '0511234567', 45000, 'Harris'),
-- ('Olivia', '0512345678', 24000, 'Martin'),
-- ('William', '0513456789', 39000, 'Thompson'),
-- ('Emma', '0514567890', 32000, 'Garcia'),
-- ('Benjamin', '0515678901', 29000, 'Martinez'),
-- ('Mia', '0516789012', 23000, 'Robinson'),
-- ('Lucas', '0517890123', 36000, 'Clark'),
-- ('Charlotte', '0518901234', 25000, 'Rodriguez'),
-- ('Henry', '0519012345', 30000, 'Lewis'),
-- ('Amelia', '0520123456', 26000, 'Lee'),
-- ('Alexander', '0521234567', 47000, 'Walker'),
-- ('Evelyn', '0522345678', 24000, 'Hall'),
-- ('Matthew', '0523456789', 34000, 'Allen'),
-- ('Abigail', '0524567890', 28000, 'Young'),
-- ('Joseph', '0525678901', 41000, 'King'),
-- ('Harper', '0526789012', 22000, 'Wright'),
-- ('Samuel', '0527890123', 37000, 'Scott'),
-- ('Ella', '0528901234', 25000, 'Green'),
-- ('Sebastian', '0529012345', 43000, 'Baker'),
-- ('Grace', '0530123456', 27000, 'Adams');

-- ¾ Обстеження (Examinations)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- обсте-ження.
-- Практичне завдання
-- 5
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ День тижня (DayOfWeek). День тижня, коли проводиться обстеження.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 7.
-- ■ Час завершення (EndTime). Час завершення обстеження.
-- ▷ Тип даних для зберігання часу.
-- ▷ Не містить null-значення.
-- ▷ Має бути більше, ніж час початку обстеження.
-- ■ Назва (Name). Назва обстеження.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Час початку (StartTime). Час початку обстеження.
-- ▷ Тип даних для зберігання часу.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 8:00 до 18:00.

-- CREATE TABLE EXAMINATIONS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	DAYOFWEEK INT NOT NULL CHECK (DAYOFWEEK >= 1 AND DAYOFWEEK <= 7),
-- 	ENDTIME TIME NOT NULL CHECK(ENDTIME > STARTTIME),
-- 	NAME VARCHAR(100) NOT NULL UNIQUE,
-- 	STARTTIME TIME NOT NULL CHECK(STARTTIME >='8:00' AND STARTTIME <= '18:00')

-- )

-- INSERT INTO EXAMINATIONS (DAYOFWEEK, STARTTIME, ENDTIME, NAME)
-- VALUES
-- (1, '08:00', '09:00', 'Cardiology Consultation 1'),
-- (1, '09:10', '10:10', 'Neurology Consultation 1'),
-- (1, '10:20', '11:20', 'Pediatrics Checkup 1'),

-- (2, '08:00', '09:00', 'Surgery Pre-op 1'),
-- (2, '09:10', '10:10', 'Traumatology Review 1'),
-- (2, '10:20', '11:20', 'Oncology Consultation 1'),

-- (3, '08:30', '09:30', 'Dermatology Checkup 1'),
-- (3, '09:40', '10:40', 'Ophthalmology Exam 1'),
-- (3, '10:50', '11:50', 'Cardiology Consultation 2'),

-- (4, '08:00', '09:00', 'Neurology Consultation 2'),
-- (4, '09:10', '10:10', 'Pediatrics Checkup 2'),
-- (4, '10:20', '11:20', 'Surgery Follow-up 1'),

-- (5, '08:00', '09:00', 'Traumatology Review 2'),
-- (5, '09:10', '10:10', 'Oncology Consultation 2'),
-- (5, '10:20', '11:20', 'Dermatology Checkup 2'),

-- (6, '08:30', '09:30', 'Ophthalmology Exam 2'),
-- (6, '09:40', '10:40', 'Cardiology Consultation 3'),
-- (6, '10:50', '11:50', 'Neurology Consultation 3'),

-- (7, '08:00', '09:00', 'Pediatrics Checkup 3'),
-- (7, '09:10', '10:10', 'Surgery Pre-op 2'),
-- (7, '10:20', '11:20', 'Traumatology Review 3'),

-- (1, '11:30', '12:30', 'Oncology Consultation 3'),
-- (2, '11:40', '12:40', 'Dermatology Checkup 3'),
-- (3, '11:50', '12:50', 'Ophthalmology Exam 3'),

-- (4, '12:00', '13:00', 'Cardiology Consultation 4'),
-- (5, '12:10', '13:10', 'Neurology Consultation 4'),
-- (6, '12:20', '13:20', 'Pediatrics Checkup 4'),

-- (7, '12:30', '13:30', 'Surgery Follow-up 2'),
-- (1, '13:40', '14:40', 'Traumatology Review 4'),
-- (2, '13:50', '14:50', 'Oncology Consultation 4');

-- ¾ Палати (Wards)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Корпус (Building). Номер корпусу, де знаходиться
-- палата.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
-- ■ Поверх (Floor). Номер поверху, на якому
-- знаходиться палата.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 1.
-- ■ Назва (Name). Назва палати.
-- ▷ Тип даних — varchar(20).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.



-- CREATE TABLE WARDS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	BUILDING INT NOT NULL CHECK(BUILDING BETWEEN 1 AND 5),
-- 	FLOOR INT NOT NULL CHECK(FLOOR >=1),
-- 	NAME VARCHAR(20) NOT NULL UNIQUE
-- )


-- INSERT INTO WARDS(BUILDING, FLOOR, NAME)
-- VALUES
-- (1, 1, 'Cardio A'),
-- (1, 2, 'Cardio B'),
-- (1, 3, 'Cardio C'),
-- (1, 4, 'ICU 1'),
-- (1, 5, 'ICU 2'),

-- (2, 1, 'Surgery A'),
-- (2, 2, 'Surgery B'),
-- (2, 3, 'Trauma 1'),
-- (2, 4, 'Trauma 2'),
-- (2, 5, 'Recovery'),

-- (3, 1, 'Pediatrics A'),
-- (3, 2, 'Pediatrics B'),
-- (3, 3, 'Neonatal'),
-- (3, 4, 'Infectious A'),
-- (3, 5, 'Infectious B'),

-- (4, 1, 'Neurology A'),
-- (4, 2, 'Neurology B'),
-- (4, 3, 'Psych Ward 1'),
-- (4, 4, 'Psych Ward 2'),
-- (4, 5, 'Rehab'),

-- (5, 1, 'Oncology A'),
-- (5, 2, 'Oncology B'),
-- (5, 3, 'Chemotherapy'),
-- (5, 4, 'Radiology A'),
-- (5, 5, 'Radiology B'),

-- (1, 1, 'Emergency 1'),
-- (2, 1, 'Emergency 2'),
-- (3, 1, 'Emergency 3'),
-- (4, 1, 'Emergency 4'),
-- (5, 1, 'Emergency 5'),
-- (2, 3, 'Dialysis'),
-- (3, 2, 'Endoscopy');

-- Завдання 2
-- Для бази даних «Таблиця» створіть такі запити:
-- 1. Вивести вміст таблиці палат.
-- SELECT *
-- FROM WARDS
-- 2. Вивести прізвища та телефони усіх лікарів.

-- SELECT SURNAME, PHONE
-- FROM DOCTORS

-- 3. Вивести усі поверхи без повторень, де розміщуються
-- палати.

-- SELECT DISTINCT FLOOR
-- FROM WARDS

-- 4. Вивести назви захворювань під назвою « Name of
-- Disease» та ступінь їхньої тяжкості під назвою «Severity
-- of Disease».

-- SELECT NAME AS NAME_OF_DISEASE, SEVERITY AS SEVERITY_OF_DISEASE
-- FROM DISEASES

-- 5. Вивести назви відділень, які знаходяться у корпусі 5
-- з фондом фінансування меншим, ніж 30000.
-- SELECT *
-- FROM DEPARTMENTS

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE FINANCING < 200000

-- 6. Вивести назви відділень, які знаходяться у корпусі 3 з
-- фондом фінансування у діапазоні від 12000 до 15000.

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE BUILDING = 3 AND FINANCING BETWEEN 120000 AND 250000

-- 8. Вивести назви палат, які знаходяться у корпусах 4 та
-- 5 на 1-му поверсі.

-- SELECT NAME, BUILDING, FLOOR
-- FROM WARDS
-- WHERE (BUILDING = 4 OR BUILDING =5) AND FLOOR = 1  -- BUILDING IN(4,5)

-- 9. Вивести назви, корпуси та фонди фінансування відділень, які знаходяться у корпусах 3 або 6 та мають
-- фонд фінансування менший, ніж 11000 або більший
-- за 25000.

-- SELECT NAME, BUILDING, FINANCING
-- FROM DEPARTMENTS
-- WHERE (BUILDING = 3 OR BUILDING = 6) AND (FINANCING < 170000 OR FINANCING > 250000)

-- 10. Вивести прізвища лікарів, зарплата (сума ставки та
-- надбавки 120) яких перевищує 1500.

-- SELECT *
-- FROM DOCTORS

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY > 25000

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY > 25000 + SALARY * 0.2

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY +120 > 25000

-- 11. Вивести прізвища лікарів, у яких половина зарплати
-- перевищує триразову надбавку у вигляді 500.

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE (SALARY/2) > (5000*3)

-- 12. Вивести назви обстежень без повторень, які проводяться у перші три дні тижня з 12:00 до 15:00.
-- SELECT *
-- FROM EXAMINATIONS


-- SELECT DISTINCT NAME, DAYOFWEEK, STARTTIME
-- FROM EXAMINATIONS
-- WHERE DAYOFWEEK IN(1,2,3)
-- 	AND STARTTIME >= '12:00'
-- 	AND ENDTIME <= '15:00'


-- 13. Вивести назви та номери корпусів відділень, які знаходяться у корпусах 1, 3, 8 або 10.

-- SELECT NAME, BUILDING
-- FROM WARDS
-- WHERE BUILDING IN (1,3,8, 10)

-- 14. Вивести назви захворювань усіх ступенів тяжкості,
-- крім 1-го та 2-го.

-- SELECT NAME, SEVERITY
-- FROM DISEASES
-- WHERE SEVERITY NOT IN (1,2)

-- 15. Вивести назви відділень, які не знаходяться у
-- першому або третьому корпусі.

-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING NOT IN (1,3)

-- 16. Вивести назви відділень, які знаходяться у першому
-- або третьому корпусі.

-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (1,3)

-- 17. Вивести прізвища лікарів, що починаються з літери
-- «N».
-- SELECT *
-- FROM DOCTORS


-- SELECT SURNAME
-- FROM DOCTORS
-- WHERE SURNAME LIKE 'L%'


-- Вивести кількість палат у кожному корпусі.

-- SELECT COUNT(ID), BUILDING
-- FROM WARDS
-- GROUP BY BUILDING

-- Вивести кількість палат на кожному поверсі.

-- SELECT COUNT(*) AS WARDS_QTY, FLOOR
-- FROM WARDS
-- GROUP BY FLOOR
-- ORDER BY FLOOR


-- Вивести середній фонд фінансування для кожного корпусу.
-- SELECT AVG(FINANCING) AS AVG_FINANCE, BUILDING
-- FROM DEPARTMENTS
-- GROUP BY BUILDING
-- ORDER BY BUILDING

-- Вивести максимальний фонд фінансування серед відділень у кожному корпусі.
-- SELECT MAX(FINANCING) AS MAX_FINANCE, BUILDING
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести мінімальний фонд фінансування серед відділень у кожному корпусі.

-- SELECT BUILDING, MIN(FINANCING) AS MIN_FINANCE
-- FROM DEPARTMENTS
-- GROUP BY BUILDING
-- ORDER BY BUILDING


financing


-- Вивести кількість відділень у кожному корпусі.

-- SELECT BUILDING, COUNT(*) AS DEPARTMENTS_QTY
-- FROM DEPARTMENTS
-- GROUP BY BUILDING
-- ORDER BY BUILDING

-- Вивести кількість захворювань для кожного ступеня тяжкості.
-- SELECT *
-- FROM DISEASES

-- SELECT SEVERITY, COUNT(*) AS DISEASES_QTY
-- FROM DISEASES
-- GROUP BY SEVERITY
-- ORDER BY SEVERITY

-- Вивести середню зарплату лікарів залежно від наявності телефону.
-- UPDATE DOCTORS
-- SET PHONE = NULL
-- WHERE ID IN (2,5,6,7,8);

-- SELECT *
-- FROM DOCTORS

-- SELECT AVG(SALARY) AS AVG_SALARY, PHONE IS NULL AS WITHOUT_PHONE
-- FROM DOCTORS
-- GROUP BY PHONE IS NULL

-- Вивести середню зарплату лікарів у кожному корпусі.


-- Вивести максимальну зарплату лікарів у кожному корпусі.\


-- Вивести кількість обстежень для кожного дня тижня.
-- SELECT DAYOFWEEK, COUNT(*) AS EXAMINATIONS_PER_DAY
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести найраніший час початку обстежень для кожного дня тижня.
-- SELECT DAYOFWEEK, MIN(STARTTIME)
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести найпізніший час завершення обстежень для кожного дня тижня.
-- SELECT DAYOFWEEK, MAX(ENDTIME)
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести кількість лікарів із зарплатою понад 2000 у кожному корпусі.

-- SELECT COUNT(*)
-- FROM DOCTORS
-- WHERE SALARY > 40000

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY= (SELECT MAX(SALARY)
-- 	FROM DOCTORS)

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY = (
-- 	SELECT MIN(SALARY)
-- 	FROM DOCTORS
-- )
-- SELECT *
-- FROM DOCTORS

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY > (
-- 	SELECT AVG(SALARY)
-- 	FROM DOCTORS
-- )

-- SELECT NAME, STARTTIME
-- FROM EXAMINATIONS
-- WHERE STARTTIME = (
-- 	SELECT MIN(STARTTIME)
-- 	FROM EXAMINATIONS
-- )

-- SELECT NAME, ENDTIME
-- FROM EXAMINATIONS
-- WHERE ENDTIME = (
-- 	SELECT MAX(ENDTIME)
-- 	FROM EXAMINATIONS
-- )

-- палата в будівлі з фінансуванням > 200 000
SELECT *
FROM WARDS W
JOIN DEPARTMENTS D ON D.BUILDING = W.BUILDING
WHERE D.FINANCING > 250000
