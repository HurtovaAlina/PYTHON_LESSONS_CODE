-- Куратори (Curators)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор куратора.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я куратора.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Прізвище (Surname). Прізвище куратора.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE CURATORS (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL,
-- 	SURNAME VARCHAR(100) NOT NULL
-- )

-- INSERT INTO CURATORS (NAME, SURNAME) VALUES
-- ('Alexander', 'Ivanov'),
-- ('Maria', 'Peterson'),
-- ('Igor', 'Shevchenko'),
-- ('Natalie', 'Kovalenko'),
-- ('Andrew', 'Bondarenko'),
-- ('Helen', 'Tkachenko'),
-- ('Victor', 'Melnyk'),
-- ('Irene', 'Savchenko'),
-- ('Dmitry', 'Kravchenko'),
-- ('Svetlana', 'Oleynik'),
-- ('Maxim', 'Polishchuk'),
-- ('Julia', 'Lysenko'),
-- ('Sergey', 'Romanyuk'),
-- ('Catherine', 'Danyluk'),
-- ('Vladimir', 'Kozak'),
-- ('Tatiana', 'Gritsenko'),
-- ('Ruslan', 'Marchenko'),
-- ('Alina', 'Sydorenko'),
-- ('Bogdan', 'Yaremchuk'),
-- ('Ludmila', 'Fedorenko'),
-- ('Eugene', 'Chernenko'),
-- ('Oksana', 'Pavlenko'),
-- ('Artem', 'Gnatyuk'),
-- ('Veronica', 'Demchenko'),
-- ('Paul', 'Zakharenko'),
-- ('Anna', 'Klymenko'),
-- ('Nicholas', 'Tymoshenko'),
-- ('Sophia', 'Vlasenko'),
-- ('Yuriy', 'Kyrylenko'),
-- ('Daria', 'Levchenko');

-- ¾ Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — DECIMAL(10, 2).
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Ідентифікатор факультету (FacultyId). Факультет, до складу
-- якого належить кафедра.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE DEPARTMENTS (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	FINANCING DECIMAL(10, 2) NOT NULL CHECK(FINANCING >=0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE,
-- 	FACULTY_ID INT NOT NULL,
-- 	FOREIGN KEY (FACULTY_ID)REFERENCES FACULTIES(ID)
-- )

-- INSERT INTO DEPARTMENTS (FINANCING, NAME, FACULTY_ID) VALUES
-- (50000.00, 'Department of Software Engineering', 1),
-- (42000.00, 'Department of Artificial Intelligence', 1),
-- (38000.00, 'Department of Applied Mathematics', 2),
-- (36000.00, 'Department of Algebra and Geometry', 2),
-- (41000.00, 'Department of Quantum Physics', 3),
-- (39000.00, 'Department of Organic Chemistry', 4),
-- (45000.00, 'Department of Molecular Biology', 5),
-- (70000.00, 'Department of Surgery', 6),
-- (68000.00, 'Department of Internal Medicine', 6),
-- (25000.00, 'Department of World History', 7),
-- (22000.00, 'Department of Ancient Philosophy', 8),
-- (47000.00, 'Department of Finance and Banking', 9),
-- (52000.00, 'Department of Criminal Law', 10),
-- (31000.00, 'Department of English Linguistics', 11),
-- (29500.00, 'Department of Clinical Psychology', 12),
-- (80000.00, 'Department of Mechanical Engineering', 13),
-- (76000.00, 'Department of Civil Engineering', 13),
-- (64000.00, 'Department of Urban Architecture', 14),
-- (33000.00, 'Department of Media Studies', 15),
-- (49000.00, 'Department of International Economics', 16),
-- (35500.00, 'Department of Social Research', 17),
-- (34500.00, 'Department of Political Theory', 18),
-- (30000.00, 'Department of Pedagogy', 19),
-- (28000.00, 'Department of Fine Arts', 20),
-- (27000.00, 'Department of Music Theory', 21),
-- (43000.00, 'Department of Ecology', 22),
-- (56000.00, 'Department of Business Analytics', 23),
-- (61000.00, 'Department of Cyber Defense', 25),
-- (59000.00, 'Department of Data Analytics', 26),
-- (32000.00, 'Department of Agricultural Technology', 28);

-- ¾ Факультети (Faculties)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- факультету.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування факультету.
-- ▷ Тип даних — DECIMAL(10, 2).
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва факультету.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE FACULTIES(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	FINANCING DECIMAL(10,2) NOT NULL CHECK(FINANCING>=0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE

-- )

-- INSERT INTO FACULTIES (FINANCING, NAME) VALUES
-- (150000.00, 'Faculty of Computer Science'),
-- (120000.50, 'Faculty of Mathematics'),
-- (98000.75, 'Faculty of Physics'),
-- (110500.00, 'Faculty of Chemistry'),
-- (130000.00, 'Faculty of Biology'),
-- (145000.20, 'Faculty of Medicine'),
-- (89000.00, 'Faculty of History'),
-- (76000.40, 'Faculty of Philosophy'),
-- (102300.00, 'Faculty of Economics'),
-- (118000.00, 'Faculty of Law'),
-- (99000.99, 'Faculty of Linguistics'),
-- (87000.00, 'Faculty of Psychology'),
-- (160000.00, 'Faculty of Engineering'),
-- (142500.00, 'Faculty of Architecture'),
-- (95000.00, 'Faculty of Journalism'),
-- (125000.00, 'Faculty of International Relations'),
-- (113400.50, 'Faculty of Sociology'),
-- (108000.00, 'Faculty of Political Science'),
-- (97000.25, 'Faculty of Education'),
-- (88000.80, 'Faculty of Arts'),
-- (92000.00, 'Faculty of Music'),
-- (104500.00, 'Faculty of Environmental Studies'),
-- (119000.00, 'Faculty of Business Administration'),
-- (111100.00, 'Faculty of Information Technology'),
-- (99050.00, 'Faculty of Cybersecurity'),
-- (134000.00, 'Faculty of Data Science'),
-- (87050.00, 'Faculty of Tourism'),
-- (93000.00, 'Faculty of Agriculture'),
-- (101000.00, 'Faculty of Geology'),
-- (127500.00, 'Faculty of Aviation');

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
-- ■ Курс (Year). Курс (рік), на якому навчається група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
-- ■ Ідентифікатор кафедри (DepartmentId). Кафедра, до складу
-- якої належить група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE GROUPS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(10) NOT NULL UNIQUE,
-- 	YEAR INT NOT NULL CHECK(YEAR BETWEEN 1 AND 5),
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(ID)
-- )

-- INSERT INTO GROUPS (NAME, YEAR, DEPARTMENT_ID) VALUES
-- ('CS-101', 1, 1),
-- ('CS-102', 2, 1),
-- ('CS-103', 3, 1),

-- ('AI-201', 1, 2),
-- ('AI-202', 2, 2),
-- ('AI-203', 3, 2),

-- ('MA-301', 1, 3),
-- ('MA-302', 2, 3),
-- ('MA-303', 3, 3),

-- ('ALG-401', 1, 4),
-- ('ALG-402', 2, 4),
-- ('ALG-403', 3, 4),

-- ('PHY-501', 1, 5),
-- ('PHY-502', 2, 5),
-- ('PHY-503', 3, 5),

-- ('CHE-601', 1, 6),
-- ('CHE-602', 2, 6),
-- ('CHE-603', 3, 6),

-- ('BIO-701', 1, 7),
-- ('BIO-702', 2, 7),
-- ('BIO-703', 3, 7),

-- ('MED-801', 1, 8),
-- ('MED-802', 2, 8),
-- ('MED-803', 3, 8),

-- ('HIS-901', 1, 9),
-- ('HIS-902', 2, 9),
-- ('HIS-903', 3, 9),

-- ('PHI-1001', 1, 10),
-- ('PHI-1002', 2, 10),
-- ('PHI-1003', 3, 10),

-- ('ECO-1101', 1, 11),
-- ('ECO-1102', 2, 11),
-- ('ECO-1103', 3, 11),

-- ('LAW-1201', 1, 12),
-- ('LAW-1202', 2, 12),
-- ('LAW-1203', 3, 12),

-- ('LING-1301', 1, 13),
-- ('LING-1302', 2, 13),
-- ('LING-1303', 3, 13),

-- ('PSY-1401', 1, 14),
-- ('PSY-1402', 2, 14),
-- ('PSY-1403', 3, 14),

-- ('ENG-1501', 1, 15),
-- ('ENG-1502', 2, 15),
-- ('ENG-1503', 3, 15),

-- ('ARCH-1601', 1, 16),
-- ('ARCH-1602', 2, 16),
-- ('ARCH-1603', 3, 16),

-- ('JOUR-1701', 1, 17),
-- ('JOUR-1702', 2, 17),
-- ('JOUR-1703', 3, 17),

-- ('IR-1801', 1, 18),
-- ('IR-1802', 2, 18),
-- ('IR-1803', 3, 18),

-- ('SOC-1901', 1, 19),
-- ('SOC-1902', 2, 19),
-- ('SOC-1903', 3, 19),

-- ('PED-2001', 1, 20),
-- ('PED-2002', 2, 20),
-- ('PED-2003', 3, 20),

-- ('ART-2101', 1, 21),
-- ('ART-2102', 2, 21),
-- ('ART-2103', 3, 21),

-- ('MUS-2201', 1, 22),
-- ('MUS-2202', 2, 22),
-- ('MUS-2203', 3, 22),

-- ('ENV-2301', 1, 23),
-- ('ENV-2302', 2, 23),
-- ('ENV-2303', 3, 23),

-- ('BUS-2401', 1, 24),
-- ('BUS-2402', 2, 24),
-- ('BUS-2403', 3, 24),

-- ('IT-2501', 1, 25),
-- ('IT-2502', 2, 25),
-- ('IT-2503', 3, 25),

-- ('SEC-2601', 1, 26),
-- ('SEC-2602', 2, 26),
-- ('SEC-2603', 3, 26),

-- ('DATA-2701', 1, 27),
-- ('DATA-2702', 2, 27),
-- ('DATA-2703', 3, 27),

-- ('TOUR-2801', 1, 28),
-- ('TOUR-2802', 2, 28),
-- ('TOUR-2803', 3, 28),

-- ('AGR-2901', 1, 29),
-- ('AGR-2902', 2, 29),
-- ('AGR-2903', 3, 29),

-- ('GEO-3001', 1, 30),
-- ('GEO-3002', 2, 30),
-- ('GEO-3003', 3, 30);

-- ¾ Групи та куратори (GroupsCurators)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
-- куратора.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ідентифікатор куратора (CuratorId). Куратор.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор групи (GroupId). Група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE GROUPS_CURATORS (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	CURATOR_ID INT NOT NULL,
-- 	FOREIGN KEY (CURATOR_ID)REFERENCES CURATORS(ID),
-- 	GROUP_ID INT NOT NULL,
-- 	FOREIGN KEY (GROUP_ID) REFERENCES GROUPS(ID)
-- )

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (1, 1), (1, 2), (1, 3);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (2, 4), (2, 5), (2, 6);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (3, 7), (3, 8), (3, 9);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (4, 10), (4, 11), (4, 12);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (5, 13), (5, 14), (5, 15);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (6, 16), (6, 17), (6, 18);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (7, 19), (7, 20), (7, 21);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (8, 22), (8, 23), (8, 24);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (9, 25), (9, 26), (9, 27);

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (10, 28), (10, 29), (10, 30);

-- ¾ Групи та лекції (GroupsLectures)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
-- лекції.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ідентифікатор групи (GroupId). Група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор лекції (LectureId). Лекція.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE GROUPS_LECTURES (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	GROUP_ID INT NOT NULL,
-- 	FOREIGN KEY (GROUP_ID) REFERENCES GROUPS(ID),
-- 	LECTURE_ID INT NOT NULL,
-- 	FOREIGN KEY (LECTURE_ID) REFERENCES LECTURES(ID)
-- )

-- INSERT INTO GROUPS_LECTURES (GROUP_ID, LECTURE_ID) VALUES

-- -- Group 1
-- (1, 1), (1, 2), (1, 3), (1, 4),

-- -- Group 2
-- (2, 2), (2, 3), (2, 5), (2, 6),

-- -- Group 3
-- (3, 3), (3, 4), (3, 7), (3, 8),

-- -- Group 4
-- (4, 4), (4, 5), (4, 9), (4, 10),

-- -- Group 5
-- (5, 5), (5, 6), (5, 11), (5, 12),

-- -- Group 6
-- (6, 6), (6, 7), (6, 13), (6, 14),

-- -- Group 7
-- (7, 7), (7, 8), (7, 15), (7, 16),

-- -- Group 8
-- (8, 8), (8, 9), (8, 17), (8, 18),

-- -- Group 9
-- (9, 9), (9, 10), (9, 19), (9, 20),

-- -- Group 10
-- (10, 10), (10, 11), (10, 21), (10, 22),

-- -- Group 11
-- (11, 11), (11, 12), (11, 23), (11, 24),

-- -- Group 12
-- (12, 12), (12, 13), (12, 25), (12, 26),

-- -- Group 13
-- (13, 13), (13, 14), (13, 27), (13, 28),

-- -- Group 14
-- (14, 14), (14, 15), (14, 29), (14, 30),

-- -- Group 15
-- (15, 15), (15, 16), (15, 31), (15, 32),

-- -- Group 16
-- (16, 16), (16, 17), (16, 33), (16, 34),

-- -- Group 17
-- (17, 17), (17, 18), (17, 35), (17, 36),

-- -- Group 18
-- (18, 18), (18, 19), (18, 37), (18, 38),

-- -- Group 19
-- (19, 19), (19, 20), (19, 39), (19, 40),

-- -- Group 20
-- (20, 20), (20, 21), (20, 41), (20, 42);

-- ¾ Лекції (Lectures)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор лекції.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Аудиторія (LectureRoom). Аудиторія, в якій проходить
-- лекція.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Ідентифікатор предмета (SubjectId). Предмет, з якого читається лекція.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор викладача (TeacherId). Викладач, який веде
-- лекцію.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE LECTURES (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	LECTURE_ROOM VARCHAR(100) NOT NULL,
-- 	SUBJECT_ID INT NOT NULL,
-- 	FOREIGN KEY (SUBJECT_ID) REFERENCES SUBJECTS(ID),
-- 	TEACHER_ID INT NOT NULL,
-- 	FOREIGN KEY (TEACHER_ID) REFERENCES TEACHERS(ID)
-- )

-- INSERT INTO LECTURES (LECTURE_ROOM, SUBJECT_ID, TEACHER_ID) VALUES
-- ('A101', 1, 1),
-- ('A102', 2, 2),
-- ('A103', 3, 3),
-- ('A104', 4, 4),
-- ('A105', 5, 5),
-- ('A106', 6, 6),
-- ('A107', 7, 7),
-- ('A108', 8, 8),
-- ('A109', 9, 9),
-- ('A110', 10, 10),

-- ('B201', 11, 11),
-- ('B202', 12, 12),
-- ('B203', 13, 13),
-- ('B204', 14, 14),
-- ('B205', 15, 15),
-- ('B206', 16, 16),
-- ('B207', 17, 17),
-- ('B208', 18, 18),
-- ('B209', 19, 19),
-- ('B210', 20, 20),

-- ('C301', 21, 21),
-- ('C302', 22, 22),
-- ('C303', 23, 23),
-- ('C304', 24, 24),
-- ('C305', 25, 25),
-- ('C306', 26, 26),
-- ('C307', 27, 27),
-- ('C308', 28, 28),
-- ('C309', 29, 29),
-- ('C310', 30, 30),

-- ('D401', 31, 1),
-- ('D402', 32, 2),
-- ('D403', 33, 3),
-- ('D404', 34, 4),
-- ('D405', 35, 5),
-- ('D406', 36, 6),
-- ('D407', 37, 7),
-- ('D408', 38, 8),
-- ('D409', 39, 9),
-- ('D410', 40, 10),

-- ('E501', 41, 11),
-- ('E502', 42, 12),
-- ('E503', 43, 13),
-- ('E504', 44, 14),
-- ('E505', 45, 15),
-- ('E506', 46, 16),
-- ('E507', 47, 17),
-- ('E508', 48, 18),
-- ('E509', 49, 19),
-- ('E510', 50, 20),

-- ('F601', 51, 21),
-- ('F602', 52, 22),
-- ('F603', 53, 23),
-- ('F604', 54, 24),
-- ('F605', 55, 25),
-- ('F606', 56, 26),
-- ('F607', 57, 27),
-- ('F608', 58, 28),
-- ('F609', 59, 29),
-- ('F610', 60, 30),

-- ('G701', 61, 1),
-- ('G702', 62, 2),
-- ('G703', 63, 3),
-- ('G704', 64, 4),
-- ('G705', 65, 5),
-- ('G706', 66, 6),
-- ('G707', 67, 7),
-- ('G708', 68, 8),
-- ('G709', 69, 9),
-- ('G710', 70, 10),

-- ('H801', 71, 11),
-- ('H802', 72, 12),
-- ('H803', 73, 13),
-- ('H804', 74, 14),
-- ('H805', 75, 15),
-- ('H806', 76, 16),
-- ('H807', 77, 17),
-- ('H808', 78, 18),
-- ('H809', 79, 19),
-- ('H810', 80, 20);


-- ¾ Предмети (Subjects)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор предмета.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва предмета.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE SUBJECTS (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO SUBJECTS (NAME) VALUES
-- ('Introduction to Programming'),
-- ('Data Structures and Algorithms'),
-- ('Database Systems'),
-- ('Operating Systems'),
-- ('Computer Networks'),
-- ('Software Engineering'),
-- ('Artificial Intelligence'),
-- ('Machine Learning'),
-- ('Deep Learning'),
-- ('Discrete Mathematics'),
-- ('Linear Algebra'),
-- ('Calculus'),
-- ('Probability Theory'),
-- ('Statistics'),
-- ('Physics Fundamentals'),
-- ('Organic Chemistry'),
-- ('Biology Basics'),
-- ('Human Anatomy'),
-- ('World History'),
-- ('Philosophy of Science'),
-- ('Economics Principles'),
-- ('Business Management'),
-- ('Marketing Basics'),
-- ('Financial Accounting'),
-- ('Law Fundamentals'),
-- ('Psychology Introduction'),
-- ('Sociology Basics'),
-- ('Cybersecurity Principles'),
-- ('Web Development'),
-- ('Mobile Application Development');

-- INSERT INTO SUBJECTS (NAME) VALUES
-- ('Advanced Algorithms'),
-- ('Algorithm Design Techniques'),
-- ('Compiler Construction'),
-- ('Distributed Systems'),
-- ('Cloud Computing'),
-- ('Parallel Computing'),
-- ('Big Data Analytics'),
-- ('Data Mining'),
-- ('Natural Language Processing'),
-- ('Computer Vision'),
-- ('Robotics Fundamentals'),
-- ('Embedded Systems'),
-- ('Internet of Things'),
-- ('Information Security'),
-- ('Cryptography'),
-- ('Ethical Hacking Basics'),
-- ('Penetration Testing'),
-- ('Network Security'),
-- ('Digital Forensics'),
-- ('Software Testing'),
-- ('Quality Assurance'),
-- ('UI/UX Design'),
-- ('Human-Computer Interaction'),
-- ('Game Development'),
-- ('3D Modeling Basics'),
-- ('Computer Graphics'),
-- ('Mathematical Analysis'),
-- ('Differential Equations'),
-- ('Numerical Methods'),
-- ('Graph Theory'),
-- ('Operations Research'),
-- ('Optimization Methods'),
-- ('Microeconomics'),
-- ('Macroeconomics'),
-- ('International Economics'),
-- ('Corporate Finance'),
-- ('Investment Analysis'),
-- ('Taxation Systems'),
-- ('Public Administration'),
-- ('Political Systems'),
-- ('Comparative Politics'),
-- ('Social Psychology'),
-- ('Developmental Psychology'),
-- ('Educational Psychology'),
-- ('Linguistics Theory'),
-- ('Applied Linguistics'),
-- ('Translation Studies'),
-- ('Environmental Science'),
-- ('Geology Basics'),
-- ('Astronomy Introduction'),
-- ('Bioinformatics');

-- ¾ Викладачі(Teachers)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- викладача.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Ставка (Salary). Ставка викладача.
-- ▷ Тип даних — DECIMAL(10, 2).
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE TEACHERS (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL,
-- 	SALARY DECIMAL(10, 2) NOT NULL CHECK (SALARY >0),
-- 	SURNAME VARCHAR(100) NOT NULL
-- )

-- INSERT INTO TEACHERS (NAME, SALARY, SURNAME) VALUES
-- ('John', 1500.00, 'Smith'),
-- ('Emily', 1700.50, 'Johnson'),
-- ('Michael', 1600.00, 'Brown'),
-- ('Sarah', 1800.75, 'Williams'),
-- ('David', 2000.00, 'Jones'),
-- ('Anna', 1550.25, 'Garcia'),
-- ('Robert', 2100.00, 'Miller'),
-- ('Laura', 1900.00, 'Davis'),
-- ('James', 1750.00, 'Rodriguez'),
-- ('Olivia', 1650.00, 'Martinez'),
-- ('William', 2200.00, 'Hernandez'),
-- ('Sophia', 1850.50, 'Lopez'),
-- ('Daniel', 1950.00, 'Gonzalez'),
-- ('Emma', 1600.75, 'Wilson'),
-- ('Joseph', 2050.00, 'Anderson'),
-- ('Mia', 1725.00, 'Thomas'),
-- ('Alexander', 2300.00, 'Taylor'),
-- ('Isabella', 1750.50, 'Moore'),
-- ('Matthew', 1980.00, 'Jackson'),
-- ('Ava', 1820.00, 'Martin'),
-- ('Ethan', 2400.00, 'Lee'),
-- ('Charlotte', 1700.00, 'Perez'),
-- ('Benjamin', 2600.00, 'Thompson'),
-- ('Amelia', 1755.00, 'White'),
-- ('Lucas', 2250.00, 'Harris'),
-- ('Harper', 1800.00, 'Sanchez'),
-- ('Henry', 1955.50, 'Clark'),
-- ('Evelyn', 2000.00, 'Ramirez'),
-- ('Sebastian', 2150.00, 'Lewis'),
-- ('Grace', 1900.00, 'Robinson');

-- 1. Виведіть усі можливі пари рядків викладачів і груп.
-- SELECT C.NAME AS CURATOR, G.NAME AS GROUP
-- FROM CURATORS C
-- JOIN GROUPS_CURATORS GC ON GC.CURATOR_ID = C.ID
-- JOIN GROUPS G ON GC.GROUP_ID = G.ID

-- 2. Виведіть назви факультетів, фонд фінансування кафедр
-- яких менше фонду фінансування факультету.
-- SELECT F.NAME AS FACULTY, F.FINANCING AS FACULTY_FINANCING,
-- 	D.NAME AS DEPARTMENT, D.FINANCING AS DEPARTMENT_FINANCING
-- FROM FACULTIES F
-- JOIN DEPARTMENTS D ON F.ID = D.FACULTY_ID
-- WHERE D.FINANCING < F.FINANCING

-- 3. Виведіть прізвища кураторів груп і назви груп, які вони курирують.
-- SELECT C.NAME AS CURATOR, G.NAME AS GROUP
-- FROM CURATORS C
-- JOIN GROUPS_CURATORS GC ON GC.CURATOR_ID = C.ID
-- JOIN GROUPS G ON G.ID = GC.GROUP_ID

-- 4. Виведіть імена та прізвища викладачів, які читають лекції у групі «AI-201».


-- SELECT T.NAME AS TEACHER_NAME, T.SURNAME AS TEACHER_SURNAME, G.NAME AS GROUP_NAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON L.TEACHER_ID = T.ID
-- JOIN GROUPS_LECTURES GL ON GL.LECTURE_ID = L.ID
-- JOIN GROUPS G ON GL.GROUP_ID = G.ID
-- WHERE G.NAME = 'AI-201'


-- 5. Виведіть прізвища викладачів і назви факультетів, на яких
-- вони читають лекції.
-- SELECT T.SURNAME AS TEACHER, F.NAME AS FACULTY
-- FROM TEACHERS T
-- JOIN LECTURES L ON L.TEACHER_ID = T.ID
-- JOIN GROUPS_LECTURES GL ON L.ID = GL.LECTURE_ID
-- JOIN GROUPS G ON G.ID = GL.GROUP_ID
-- JOIN DEPARTMENTS D ON D.ID = G.DEPARTMENT_ID
-- JOIN FACULTIES F ON F.ID = D.FACULTY_ID

-- 6. Виведіть назви кафедр і назви груп, які до них належать.
-- SELECT D.NAME AS DEPARTMENT, G.NAME AS GROUP_NAME
-- FROM DEPARTMENTS D
-- JOIN GROUPS G ON G.DEPARTMENT_ID = D.ID

-- 7. Виведіть назви предметів, які викладає викладач «Sarah Williams».
-- SELECT S.NAME AS SUBJECT, T.SURNAME AS TEACHER_SURNAME, T.NAME AS TEACHER_NAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON L.TEACHER_ID = T.ID
-- JOIN SUBJECTS S ON S.ID = L.SUBJECT_ID
-- WHERE T.NAME = 'Sarah' AND T.SURNAME = 'Williams'

-- 8. Виведіть назви кафедр, на яких викладається дисципліна «Financial Accounting».
-- SELECT D.NAME AS DEPARTMENT, S.NAME AS SUBJECT
-- FROM SUBJECTS S
-- JOIN LECTURES L ON L.SUBJECT_ID = S.ID
-- JOIN GROUPS_LECTURES GL ON GL.LECTURE_ID = L.ID
-- JOIN GROUPS G ON GL.GROUP_ID = G.ID
-- JOIN DEPARTMENTS D ON G.DEPARTMENT_ID =D.ID
-- WHERE S.NAME = 'Financial Accounting'


-- 9. Виведіть назви груп, що належать до факультету «Computer Science».

-- SELECT G.NAME AS GROUP_NAME, F.NAME AS FACULTY
-- FROM GROUPS G
-- JOIN DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID
-- JOIN FACULTIES F ON D.FACULTY_ID = F.ID
-- WHERE F.NAME = 'Faculty of Computer Science'

-- 10. Виведіть назви груп 3-го курсу, а також назви факультетів,
-- до яких вони належать.
-- SELECT G.NAME AS GROUP_NAME, F.NAME AS FACULTY, G.YEAR
-- FROM GROUPS G
-- JOIN DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID
-- JOIN FACULTIES F ON D.FACULTY_ID = F.ID
-- WHERE G.YEAR = 3

-- 11. Виведіть повні імена викладачів і лекції, які вони читають
-- (назви предметів та груп). Зробіть відбір по тим лекціям,
-- які проходять в аудиторії «B206».

-- SELECT T.NAME AS TEACHER_NAME, T.SURNAME AS TEACHER_SURNAME,
-- L.LECTURE_ROOM, S.NAME AS SUBJECT, G.NAME AS GROUP_NAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON T.ID = L.TEACHER_ID
-- JOIN SUBJECTS S ON S.ID = L.SUBJECT_ID
-- JOIN GROUPS_LECTURES GL ON GL.LECTURE_ID = L.ID
-- JOIN GROUPS G ON GL.GROUP_ID = G.ID
-- WHERE L.LECTURE_ROOM = 'B206'
