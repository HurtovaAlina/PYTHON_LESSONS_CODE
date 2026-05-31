-- SELECT *
-- FROM FRUITS_VEGETABLES


-- Завдання 1
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Відображення усіх овочів з калорійністю, менше вказаної.
-- SELECT NAME, ENERGY
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Vegetable' AND ENERGY < 40

-- ■ Відображення усіх фруктів з калорійністю у вказаному
-- діапазоні.
-- SELECT NAME, ENERGY
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Fruit' AND (ENERGY BETWEEN 40 AND 50)

-- ■ Відображення усіх овочів, у назві яких є вказане слово.
-- Наприклад, слово: капуста.
-- SELECT NAME
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Vegetable' AND NAME ILIKE '%tomato%'

-- ■ Відображення усіх овочів та фруктів, у короткому описі
-- яких є вказане слово. Наприклад, слово: гемоглобін.
-- SELECT NAME, DESCRIPTION
-- FROM FRUITS_VEGETABLES
-- WHERE DESCRIPTION ILIKE '%sweet%'

-- ■ Показати усі овочі та фрукти жовтого або червоного
-- кольору.
-- SELECT NAME, COLOUR
-- FROM FRUITS_VEGETABLES
-- WHERE COLOUR IN ('Red', 'Yellow')

-- Завдання 2
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Показати кількість овочів.
-- SELECT COUNT(*)
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Vegetable'

-- ■ Показати кількість фруктів.
-- SELECT COUNT(*)
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Fruit'

-- ■ Показати кількість овочів та фруктів заданого кольору.
-- SELECT COUNT(*)
-- FROM FRUITS_VEGETABLES
-- WHERE COLOUR = 'Red'

-- ■ Показати кількість овочів та фруктів кожного кольору.
-- SELECT COUNT(*), COLOUR
-- FROM FRUITS_VEGETABLES
-- GROUP BY COLOUR

-- ■ Показати колір мінімальної кількості овочів та фруктів.
-- SELECT COLOUR
-- FROM FRUITS_VEGETABLES
-- GROUP BY COLOUR
-- HAVING COUNT(*) = (
--     SELECT COUNT(*)
--     FROM FRUITS_VEGETABLES
--     GROUP BY COLOUR
--     ORDER BY COUNT(*)
--     LIMIT 1
-- );


-- ■ Показати колір максимальної кількості овочів та фруктів.

-- SELECT COLOUR
-- FROM FRUITS_VEGETABLES
-- GROUP BY COLOUR
-- HAVING COUNT(*) = (
--     SELECT COUNT(*)
--     FROM FRUITS_VEGETABLES
--     GROUP BY COLOUR
--     ORDER BY COUNT(*) DESC
--     LIMIT 1
-- );

-- ■ Показати мінімальну калорійність овочів та фруктів.
-- SELECT MIN(ENERGY)
-- FROM FRUITS_VEGETABLES


-- ■ Показати максимальну калорійність овочів та фруктів.
-- SELECT MAX(ENERGY)
-- FROM FRUITS_VEGETABLES

-- ■ Показати середню калорійність овочів та фруктів.
-- SELECT AVG(ENERGY)
-- FROM FRUITS_VEGETABLES

-- ■ Показати фрукт з мінімальною калорійністю.
-- SELECT NAME, ENERGY
-- FROM FRUITS_VEGETABLES
-- WHERE ENERGY = (
--     SELECT MIN(ENERGY)
--     FROM FRUITS_VEGETABLES
-- );

-- ■ Показати фрукт з максимальною калорійністю.
-- SELECT NAME, ENERGY
-- FROM FRUITS_VEGETABLES
-- WHERE ENERGY = (
--     SELECT MAX(ENERGY)
--     FROM FRUITS_VEGETABLES
-- );
