-- SELECT *
-- FROM STUDENTS

-- Завдання 1
-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою
-- у вказаному діапазоні.

-- SELECT NAME, MIN_MARK
-- FROM STUDENTS
-- WHERE MIN_MARK BETWEEN 50 AND 70


-- ■ Показати інформацію про студентів, яким виповнилося 20 років.

-- SELECT NAME, EXTRACT(YEAR FROM AGE(BIRTHDAY)) AS AGE
-- FROM STUDENTS
-- WHERE EXTRACT(YEAR FROM AGE(BIRTHDAY)) >= 20;  -- WHERE AGE(BIRTHDAY) > INTERVAL '20 YEARS'

-- ■ Показати інформацію про студентів з віком, у вказаному діапазоні.
-- SELECT NAME, EXTRACT(YEAR FROM AGE(BIRTHDAY)) AS AGE
-- FROM STUDENTS
-- WHERE EXTRACT(YEAR FROM AGE(BIRTHDAY)) BETWEEN 20 AND 25


-- ■ Показати інформацію про студентів із конкретним
-- ім’ям. Наприклад, показати студентів з ім’ям Борис.
-- SELECT NAME
-- FROM STUDENTS
-- WHERE NAME LIKE '%Alina%'

-- Змінити тип даних в колонці
-- ALTER TABLE STUDENTS
-- ALTER COLUMN BIRTHDAY: DATE
-- USING BIRTHDAY::DATE

-- ■ Показати інформацію про студентів, в номері яких
-- є три пʼятірки.
-- SELECT NAME, PHONE
-- FROM STUDENTS
-- WHERE PHONE LIKE '%5%5%5%'

-- ■ Показати електронні адреси студентів, що починаються з конкретної літери.
-- SELECT NAME, EMAIL
-- FROM STUDENTS
-- WHERE EMAIL ILIKE 'I%'

-- Завдання 2
-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- ■ Показати мінімальну середню оцінку по всіх студентах.

-- SELECT MIN(AVG_MARK) AS MIN_AVG_MARK
-- FROM STUDENTS

-- ■ Показати максимальну середню оцінку по всіх студентах.
-- SELECT MAX(AVG_MARK) AS MAX_AVG_MARK
-- FROM STUDENTS

-- ■ Показати статистику міст. Має відображатися назва
-- міста та кількість студентів з цього міста.
-- SELECT CITY, COUNT(NAME)
-- FROM STUDENTS
-- GROUP BY CITY

-- ■ Показати статистику студентів. Має відображатися
-- назва країни та кількість студентів з цієї країни.
-- SELECT COUNTRY, COUNT(NAME)
-- FROM STUDENTS
-- GROUP BY COUNTRY

-- ■ Показати кількість студентів з мінімальною середньою
-- оцінкою з математики.
-- SELECT SUBJECT_MIN, COUNT(NAME) AS MIN_MARK_SUBJ
-- FROM STUDENTS
-- WHERE SUBJECT_MIN = 'Math'
-- GROUP BY SUBJECT_MIN

-- ■ Показати кількість студентів з максимальною середньою оцінкою з математики.
-- SELECT SUBJECT_MAX, COUNT(NAME) AS MAX_MARK_SUBJ
-- FROM STUDENTS
-- WHERE SUBJECT_MAX = 'Math'
-- GROUP BY SUBJECT_MAX

-- ■ Показати кількість студентів у кожній групі.
-- SELECT GROUP_NAME, COUNT(NAME)
-- FROM STUDENTS
-- GROUP BY GROUP_NAME

-- ■ Показати середню оцінку групи.
-- SELECT GROUP_NAME, AVG(AVG_MARK)
-- FROM STUDENTS
-- GROUP BY GROUP_NAME

-- вивести максимальну серед максимальних середніх
-- SELECT MAX(AVG_MARK)
-- FROM STUDENTS


-- SELECT *
-- FROM STUDENTS
-- WHERE AVG_MARK = (
-- 	SELECT MAX(AVG_MARK)
--  	FROM STUDENTS
-- 	 )



-- вивести групи і середні оцінки
-- WITH GROUP_INFO AS (
-- 	SELECT GROUP_NAME, AVG(AVG_MARK) AS GROUP_MARK
-- 	FROM STUDENTS
-- 	GROUP BY GROUP_NAME
-- )
-- SELECT GROUP_NAME, GROUP_MARK
-- FROM GROUP_INFO
-- WHERE GROUP_MARK = (
-- 	SELECT MAX(GROUP_MARK)
-- 	FROM GROUP_INFO
-- )

--ВИВЕСТИ СТУДЕНТІВ ЯКІ НАВЧАЮТЬСЯ В ГРУПІ З НАЙВИЩОЮ СЕРЕДНЬОЇ ОЦІНКОЮ

-- WITH GROUP_INFO AS (
-- 	SELECT GROUP_NAME, AVG(AVG_MARK) AS GROUP_MARK
-- 	FROM STUDENTS
-- 	GROUP BY GROUP_NAME
-- )
-- SELECT *
-- FROM STUDENTS
-- WHERE GROUP_NAME = (
-- 	SELECT GROUP_NAME
-- 	FROM GROUP_INFO
-- 	WHERE GROUP_MARK = (
-- 		SELECT MAX(GROUP_MARK)
-- 		FROM GROUP_INFO
-- 	)
-- )
