---- С-- зберігатиме таку інформацію:
-- ■ ПІБ студента;
-- ■ місто;
-- ■ країна;
-- ■ дата народження;
-- ■ електронна адреса;
-- ■ контактний телефон;
-- Практичне завдання
-- ■ назва групи;
-- ■ середня оцінка за рік з усіх предметів;
-- ■ назва предмета з мінімальною, середньою оцінкою;
-- ■ назва предмета з максимальною, середньою
-- оцінкою.

--DROP TABLE STUDENTS

-- CREATE TABLE STUDENTS(
-- 	ID SERIAL,
-- 	NAME VARCHAR(100),
-- 	CITY VARCHAR(30),
-- 	COUNTRY VARCHAR(40),
-- 	DOB INT,
-- 	EMAIL VARCHAR(50),
-- 	PHONE VARCHAR(11),
-- 	GROUP_NAME VARCHAR(20),
-- 	AVG_MARK INT,
-- 	MAX_MARK INT,
-- 	SUBJECT_MAX VARCHAR(20),
-- 	MIN_MARK INT,
-- 	SUBJECT_MIN VARCHAR(20)
-- )

--
--Відображати всієї інформації з таблиці зі студентами та оцінками.
-- SELECT *
-- FROM STUDENTS

--Відображати ПІБ усіх студентів.
-- SELECT NAME
-- FROM STUDENTS;

--Відображати усіх середніх оцінок
-- SELECT AVG_MARK
-- FROM STUDENTS;

-- SELECT MIN_MARK
-- FROM STUDENTS


--Показати ПІБ усіх студентів з мінімальною оцінкою,більшою, ніж зазначена.
-- SELECT ID, NAME
-- FROM STUDENTS
-- WHERE MIN_MARK > 60;

--Показати країни студентів. Назви країн мають бути унікальними.
-- SELECT DISTINCT COUNTRY
-- FROM STUDENTS

--Показати міста студентів. Назви міст мають бути унікальними.
-- SELECT DISTINCT CITY
-- FROM STUDENTS

--Показати назви груп. Назви груп мають бути унікальними.
-- SELECT DISTINCT GROUP_NAME
-- FROM STUDENTS;

--Показати назви усіх предметів із мінімальними середніми оцінками. Назви предметів мають бути унікальними.
-- SELECT DISTINCT SUBJECT_MIN, MIN_MARK
-- FROM STUDENTS

--виведіть студентів в містах Львів Одеса Дніпро
-- SELECT *
-- FROM STUDENTS
-- WHERE CITY = 'Lviv' OR CITY ='Odesa' OR CITY ='Dnipro'

-- вивести студентів з оцінками між 70 і 80
-- SELECT *
-- FROM STUDENTS
-- WHERE AVG_MARK>70 AND AVG_MARK< 80

-- SELECT *
-- FROM STUDENTS
-- WHERE AVG_MARK BETWEEN 70 AND 80

--вивести імʼя мінімальну і максимальну оцінку та різницю між ними
-- SELECT NAME, MIN_MARK, MAX_MARK, MAX_MARK - MIN_MARK AS DIFFERENCE
-- FROM STUDENTS;


--вивести людей, що живуть в Дніпрі або середня оцінка більша за 70
-- SELECT NAME, CITY, AVG_MARK
-- FROM STUDENTS
-- WHERE CITY = 'Dnipro' OR AVG_MARK > 70

-- SELECT NAME, MAX_MARK, MIN_MARK
-- FROM STUDENTS
-- WHERE MAX_MARK = MIN_MARK

SELECT NAME, MAX_MARK, MIN_MARK, MAX_MARK-MIN_MARK AS DIFF
FROM STUDENTS
WHERE MAX_MARK-MIN_MARK>10
