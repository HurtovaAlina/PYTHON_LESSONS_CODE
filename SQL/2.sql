-- SELECT * FROM STUDENTS

-- додати стовбчик
-- ALTER TABLE STUDENTS
-- ADD COLUMN BIRTHDAY DATE ---[назва стовбчика] [тип даних]

--видалити стовбчик
-- ALTER TABLE STUDENTS
-- DROP COLUMN BIRTHDAY

-- зміни змісту таблиці

-- зробити, що всі народилися в 2003-05-06
-- UPDATE STUDENTS
-- SET BIRTHDAY = '2003-05-06'

-- ті хто живе в Київі, дата народження 2001-02-28
-- UPDATE STUDENTS
-- SET BIRTHDAY = '2001-02-28'
-- WHERE CITY = 'Kyiv'

-- вивести рік народження
-- EXTRACT(YEAR FROM [стовбчик])

-- SELECT EXTRACT(YEAR FROM BIRTHDAY)
-- FROM STUDENTS

-- отримати вік на основі дати
-- SELECT AGE(BIRTHDAY)
-- FROM STUDENTS

-- лише рік
-- SELECT EXTRACT(YEAR FROM AGE(BIRTHDAY))
-- FROM STUDENTS

-- тексти
-- регулярні вирази

-- % -- будь-яка кількість будь-яких символів
-- вивести міста, які починаються на літеру К
-- SELECT CITY
-- FROM STUDENTS
-- WHERE CITY ILIKE 'K%'

-- містить К всередині
-- SELECT CITY
-- FROM STUDENTS
-- WHERE CITY ILIKE '%k%'

-- імʼя людини, яка містить два літери а
-- SELECT NAME
-- FROM STUDENTS
-- WHERE NAME ILIKE '%a%a%'

-- _ -- будь-який один символ
-- 3-я літера h
-- SELECT NAME
-- FROM STUDENTS
-- WHERE NAME ILIKE '__D%'

-- групування
-- групує данні за ознакою
-- вивести кількість сутдентів в кожному місті - згрупувати по містах
-- в SELECT можна використовувати або стовпчик для групування, або агрегатні функції
-- агрегатні функції: COUNT MIN MAX AVG SUM

-- SELECT CITY, COUNT(NAME), SUM(AVG_MARK)
-- FROM STUDENTS
-- GROUP BY CITY -- GROUP BY [стовпчик]


-- назва стовпчика
-- SELECT CITY, COUNT(*) AS "PEOPLE QTY"
-- FROM STUDENTS
-- GROUP BY CITY
