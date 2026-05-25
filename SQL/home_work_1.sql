-- ALTER DATABASE PEOPLE
-- RENAME TO CATS;

-- DROP DATABASE CATS;

-- Створіть однотабличну базу даних «Овочі та фрукти»,
-- яка зберігатиме таку інформацію:
-- ■ Назва;
-- ■ Тип (овоч або фрукт);
-- ■ Колір;
-- ■ Калорійність;
-- ■ Короткий опис.

-- CREATE TABLE FRUITS_VEGETABLES(
-- 	ID SERIAL,
-- 	NAME VARCHAR(30),
-- 	TYPE VARCHAR(20),
-- 	COLOUR VARCHAR(20),
-- 	ENERGY INT,
-- 	DESCRIPTION VARCHAR(400)
-- )

-- INSERT INTO FRUITS_VEGETABLES(NAME, TYPE, COLOUR, ENERGY, DESCRIPTION)
-- VALUES
-- ('Apple', 'Fruit', 'Red', 52, 'Sweet and crunchy fruit'),
-- ('Banana', 'Fruit', 'Yellow', 89, 'Soft tropical fruit rich in potassium'),
-- ('Orange', 'Fruit', 'Orange', 47, 'Citrus fruit with vitamin C'),
-- ('Pear', 'Fruit', 'Green', 57, 'Juicy fruit with soft texture'),
-- ('Grape', 'Fruit', 'Purple', 69, 'Small sweet berries growing in clusters'),
-- ('Watermelon', 'Fruit', 'Green', 30, 'Large fruit with red juicy flesh'),
-- ('Cherry', 'Fruit', 'Red', 50, 'Small sweet fruit with a pit'),
-- ('Strawberry', 'Fruit', 'Red', 33, 'Popular berry with sweet taste'),
-- ('Pineapple', 'Fruit', 'Brown', 50, 'Tropical fruit with juicy yellow flesh'),
-- ('Kiwi', 'Fruit', 'Brown', 61, 'Small fruit with green interior'),
-- ('Mango', 'Fruit', 'Orange', 60, 'Sweet tropical fruit'),
-- ('Peach', 'Fruit', 'Orange', 39, 'Soft fruit with fuzzy skin'),
-- ('Lemon', 'Fruit', 'Yellow', 29, 'Sour citrus fruit'),
-- ('Plum', 'Fruit', 'Purple', 46, 'Juicy fruit with smooth skin'),
-- ('Apricot', 'Fruit', 'Orange', 48, 'Small sweet orange fruit'),

-- ('Tomato', 'Vegetable', 'Red', 18, 'Popular vegetable used in salads'),
-- ('Cucumber', 'Vegetable', 'Green', 15, 'Fresh vegetable with high water content'),
-- ('Carrot', 'Vegetable', 'Orange', 41, 'Crunchy root vegetable'),
-- ('Potato', 'Vegetable', 'Brown', 77, 'Starchy vegetable used worldwide'),
-- ('Onion', 'Vegetable', 'White', 40, 'Vegetable with strong smell and taste'),
-- ('Garlic', 'Vegetable', 'White', 149, 'Aromatic vegetable used for seasoning'),
-- ('Broccoli', 'Vegetable', 'Green', 34, 'Healthy green vegetable'),
-- ('Pepper', 'Vegetable', 'Yellow', 20, 'Sweet bell pepper'),
-- ('Eggplant', 'Vegetable', 'Purple', 25, 'Vegetable with soft interior'),
-- ('Cabbage', 'Vegetable', 'Green', 25, 'Leafy vegetable often used in salads'),
-- ('Pumpkin', 'Vegetable', 'Orange', 26, 'Large vegetable used in soups'),
-- ('Radish', 'Vegetable', 'Red', 16, 'Small spicy root vegetable'),
-- ('Spinach', 'Vegetable', 'Green', 23, 'Leafy vegetable rich in iron'),
-- ('Corn', 'Vegetable', 'Yellow', 86, 'Sweet vegetable with kernels'),
-- ('Beetroot', 'Vegetable', 'Purple', 43, 'Root vegetable with dark red color');

-- Створіть наступні запити для таблиці з інформацією про
-- овочі та фрукти із попереднього завдання:
-- ■ Відображення всієї інформації з таблиці овочів та фруктів;

-- SELECT * FROM FRUITS_VEGETABLES

-- ■ Відображення усіх овочів;

-- SELECT NAME FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Vegetable'

-- ■ Відображення усіх фруктів;

-- SELECT NAME FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Fruit'

-- ■ Відображення усіх назв овочів та фруктів;

-- SELECT NAME FROM FRUITS_VEGETABLES

-- ■ Відображення усіх кольорів. Кольори мають бути унікальними;

-- SELECT DISTINCT COLOUR FROM FRUITS_VEGETABLES

-- ■ Відображення фруктів певного кольору;

-- SELECT NAME FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Fruit' AND COLOUR = 'Orange'

-- ■ Відображення овочів певного кольору

-- SELECT NAME FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'Vegetable' AND COLOUR = 'Green'
