--СТВОРИТИ ТАБЛИЦЮ
--CREATE TABLE PERSON (
--[НАЗВА СТОВПЧИКА] [ТИП ДАННИХ]
--ID ЦІЛЕ ЧИСЛО ВІД 1 І ЗБІЛЬШУЄТЬСЯ АВТОМАТИЧНО
--	ID SERIAL,
--	NAME VARCHAR(30), -- ТЕКСТ НЕ БІЛЬШЕ 30 СИМВОЛІВ
--	AGE INT,
--	CITY VARCHAR(20)
--);

--НАПОВНЕННЯ ТАБЛИЦІ ДАННИМИ
--INSERT INTO PERSON(NAME, AGE, CITY)
--VALUES
--('JOHN', 45, 'ODESA'),
--('MARY', 34, 'LVIV'),
--('SOPHIE', 25, 'DNIPRO');

--ЗАПИТИ (ОТРИМАННЯ ІНФОРМАЦІЇ)
--SELECT СТОВПЧИК1, СТОВПЧИК2, СТОВПЧИК3
--FROM ТАБЛИЦЯ
--WHERE УМОВА

-- ОТРИМАТИ ВСІ ДАННІ
-- SELECT ID, NAME, AGE, CITY
-- FROM PERSON;

-- ЩОБ НЕ ПЕРЕРАХОВУВАТИ ВСІ СТОВПЧИКИ -*
--SELECT *
--FROM PERSON;

--ДІСТАТИ ЛЮДЕЙ СТАРШЕ 30
-- SELECT NAME, AGE
-- FROM PERSON
-- WHERE AGE>40;

--ЛЮДИ ЯКІ ЖИВУТЬ В ДНІПРІ
-- SELECT *
-- FROM PERSON
-- WHERE CITY ='DNIPRO';

--ЛЮДИ ЯКІ ЖИВУТЬ В ДНІПРІ І ЛЬВОВІ
-- SELECT *
-- FROM PERSON
-- WHERE CITY ='LVIV' OR CITY='DNIPRO';
