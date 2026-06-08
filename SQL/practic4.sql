-- ¾ Відділення (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор відділення.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва відділення.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE DEPARTMENTS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO DEPARTMENTS (NAME) VALUES
-- ('Cardiology'),
-- ('Neurology'),
-- ('Pediatrics'),
-- ('Oncology'),
-- ('Emergency Department'),
-- ('Radiology'),
-- ('Surgery'),
-- ('Orthopedics'),
-- ('Dermatology'),
-- ('Gynecology'),
-- ('Ophthalmology'),
-- ('Urology'),
-- ('Intensive Care Unit'),
-- ('Laboratory'),
-- ('Psychiatry'),
-- ('Endocrinology'),
-- ('Gastroenterology'),
-- ('Nephrology'),
-- ('Infectious Diseases'),
-- ('Rehabilitation');

-- ¾ Лікарі (Doctors)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- лікаря.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я лікаря.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Надбавка (Premium). Надбавка лікаря.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ставка (Salary). Ставка лікаря.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище лікаря.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.

-- CREATE TABLE DOCTORS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL,
-- 	PREMIUM INT NOT NULL CHECK(PREMIUM >=0) DEFAULT 0,
-- 	SALARY INT NOT NULL CHECK(SALARY >0),
-- 	SURNAME VARCHAR(100) NOT NULL,
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(ID)
-- )

-- INSERT INTO DOCTORS (NAME, PREMIUM, SALARY, SURNAME, DEPARTMENT_ID) VALUES
-- ('Ivan', 5000, 35000, 'Shevchenko', 1),
-- ('Olena', 4500, 32000, 'Koval', 2),
-- ('Petro', 6000, 40000, 'Bondarenko', 3),
-- ('Maria', 3000, 28000, 'Tkachenko', 4),
-- ('Andrii', 7000, 45000, 'Melnyk', 5),
-- ('Svitlana', 3500, 30000, 'Boyko', 6),
-- ('Mykola', 4000, 31000, 'Kravchenko', 7),
-- ('Iryna', 5500, 36000, 'Polishchuk', 8),
-- ('Vasyl', 4800, 33000, 'Savchenko', 9),
-- ('Natalia', 5200, 34000, 'Lysenko', 10),

-- ('Dmytro', 6200, 41000, 'Moroz', 11),
-- ('Tetiana', 4300, 29500, 'Marchenko', 12),
-- ('Yurii', 5100, 35500, 'Rudenko', 13),
-- ('Kateryna', 3900, 30500, 'Kostenko', 14),
-- ('Oleksandr', 7500, 47000, 'Danylchuk', 15),
-- ('Halyna', 3600, 29000, 'Mazur', 16),
-- ('Roman', 5800, 39000, 'Havryliuk', 17),
-- ('Anastasiia', 4100, 31500, 'Kozak', 18),
-- ('Serhii', 6400, 42500, 'Bilyk', 19),
-- ('Viktoria', 4700, 33500, 'Oliinyk', 20),

-- ('Maksym', 5300, 36500, 'Yaremchuk', 1),
-- ('Alina', 3400, 28500, 'Pavlenko', 2),
-- ('Volodymyr', 6900, 44000, 'Zakharchenko', 3),
-- ('Nadiia', 3700, 29800, 'Horbach', 4),
-- ('Taras', 5600, 37500, 'Klymenko', 5),
-- ('Oksana', 4400, 32500, 'Symonenko', 6),
-- ('Bohdan', 6100, 40500, 'Antonenko', 7),
-- ('Liudmyla', 3200, 27500, 'Chernenko', 8),
-- ('Artem', 5700, 38500, 'Yatsenko', 9),
-- ('Sofia', 4600, 33000, 'Panasenko', 10),

-- ('Denys', 6800, 43500, 'Kushnir', 11),
-- ('Yana', 3500, 29200, 'Kovtun', 12),
-- ('Ihor', 5900, 39500, 'Hnatyuk', 13),
-- ('Veronika', 4200, 31800, 'Tymoshenko', 14),
-- ('Pavlo', 6300, 42000, 'Stepanenko', 15),
-- ('Kristina', 3800, 29900, 'Karpenko', 16),
-- ('Ruslan', 5400, 37000, 'Shulha', 17),
-- ('Diana', 4000, 31200, 'Romaniuk', 18),
-- ('Yevhen', 7200, 46000, 'Fedorenko', 19),
-- ('Milana', 4500, 32800, 'Sydorenko', 20),

-- ('Oleh', 5100, 34500, 'Kucher', 1),
-- ('Anna', 3900, 30000, 'Levchenko', 2),
-- ('Stepan', 6500, 43000, 'Tereshchenko', 3),
-- ('Inna', 3600, 28900, 'Dubovyk', 4),
-- ('Vitalii', 7000, 45500, 'Kovalchuk', 5),
-- ('Larysa', 4100, 31700, 'Kryvenko', 6),
-- ('Vadym', 5600, 38200, 'Nosenko', 7),
-- ('Zhanna', 3300, 27600, 'Semenova', 8),
-- ('Oleksii', 6000, 40800, 'Taran', 9),
-- ('Tamara', 4700, 33400, 'Holub', 10),

-- ('Stanislav', 6200, 41800, 'Kysil', 11),
-- ('Nina', 3500, 29100, 'Babenko', 12),
-- ('Rostyslav', 5800, 39200, 'Lytvyn', 13),
-- ('Valeria', 4300, 32000, 'Kondratiuk', 14),
-- ('Hryhorii', 7100, 46200, 'Onyshchenko', 15),
-- ('Lesia', 3700, 29700, 'Yurchenko', 16),
-- ('Eduard', 5400, 37400, 'Chaika', 17),
-- ('Marta', 4000, 31100, 'Korniienko', 18),
-- ('Anton', 6700, 43800, 'Bohdanov', 19),
-- ('Polina', 4600, 32900, 'Savytska', 20);

-- ¾ Лікарі та спеціалізації (DoctorsSpecializations)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор лікаря
-- та спеціалізації.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ідентифікатор лікаря (DoctorId). Лікар.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор спеціалізації (SpecializationId). Спеціалізація.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE DOCTORS_SPECIALIZATIONS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	DOCTOR_ID INT NOT NULL,
-- 	FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS(ID),
-- 	SPECIALIZATION_ID INT NOT NULL,
-- 	FOREIGN KEY (SPECIALIZATION_ID) REFERENCES SPECIALIZATIONS(ID)
-- )

-- INSERT INTO DOCTORS_SPECIALIZATIONS (DOCTOR_ID, SPECIALIZATION_ID) VALUES

-- -- 1-10
-- (1, 1), (1, 27),
-- (2, 2),
-- (3, 3), (3, 27),
-- (4, 4),
-- (5, 5), (5, 19),
-- (6, 6),
-- (7, 7),
-- (8, 8),
-- (9, 9),

-- -- 11-20
-- (10, 10),
-- (11, 11),
-- (12, 12),
-- (13, 13),
-- (14, 14),
-- (15, 5), (15, 4),
-- (16, 15),
-- (17, 16),
-- (18, 17),
-- (19, 18),

-- -- 21-30
-- (20, 19),
-- (21, 27),
-- (22, 27),
-- (23, 5),
-- (24, 6),
-- (25, 7),
-- (26, 8),
-- (27, 9),
-- (28, 10),
-- (29, 11),

-- -- 31-40
-- (30, 12),
-- (31, 13),
-- (32, 14),
-- (33, 15),
-- (34, 16),
-- (35, 17),
-- (36, 18),
-- (37, 19),
-- (38, 20),
-- (39, 21),

-- -- 41-50
-- (40, 22),
-- (41, 23),
-- (42, 24),
-- (43, 25),
-- (44, 26),
-- (45, 27),
-- (46, 28),
-- (47, 29),
-- (48, 30),
-- (49, 1),

-- -- 51-60
-- (50, 2),
-- (51, 3),
-- (52, 4),
-- (53, 5),
-- (54, 6),
-- (55, 7),
-- (56, 8),
-- (57, 9),
-- (58, 10),
-- (59, 11),
-- (60, 12);

-- ¾ Пожертвування (Donations)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор пожертвування.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Сума (Amount). Сума пожертвування.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Дата (Date). Дата пожертвування.
-- ▷ Тип даних для зберігання дати.
-- ▷ Не містить null-значення.
-- ▷ Не може бути більшою за поточну дату.
-- ▷ Значення за замовчуванням — поточна дата.
-- ■ Ідентифікатор відділення (DepartmentId). Відділення,
-- якому було надано пожертвування.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор спонсора (SponsorId). Спонсор, який
-- зробив пожертвування.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE DONATIONS (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	AMOUNT INT NOT NULL CHECK(AMOUNT > 0),
-- 	DONATION_DATE DATE NOT NULL CHECK(DONATION_DATE<=CURRENT_DATE),
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(ID),
-- 	SPONSOR_ID INT NOT NULL,
-- 	FOREIGN KEY (SPONSOR_ID) REFERENCES SPONSORS(ID)
-- )

-- INSERT INTO DONATIONS (AMOUNT, DONATION_DATE, DEPARTMENT_ID, SPONSOR_ID) VALUES
-- (5000, '2024-01-10', 1, 1),
-- (12000, '2024-02-15', 2, 2),
-- (8000, '2024-03-01', 3, 3),
-- (15000, '2024-03-20', 4, 4),
-- (7000, '2024-04-05', 5, 5),
-- (20000, '2024-04-18', 6, 6),
-- (9000, '2024-05-10', 7, 7),
-- (11000, '2024-05-22', 8, 8),
-- (6000, '2024-06-01', 9, 9),
-- (25000, '2024-06-15', 10, 10),

-- (13000, '2024-07-01', 11, 11),
-- (14000, '2024-07-18', 12, 12),
-- (9500, '2024-08-02', 13, 13),
-- (17000, '2024-08-19', 14, 14),
-- (30000, '2024-09-05', 15, 15),
-- (10000, '2024-09-20', 16, 16),
-- (11000, '2024-10-01', 17, 17),
-- (16000, '2024-10-18', 18, 18),
-- (8000, '2024-11-03', 19, 19),
-- (22000, '2024-11-20', 20, 20),

-- (7000, '2025-01-10', 1, 2),
-- (18000, '2025-01-25', 2, 3),
-- (9000, '2025-02-10', 3, 4),
-- (15000, '2025-02-28', 4, 5),
-- (12000, '2025-03-15', 5, 6),
-- (20000, '2025-03-30', 6, 7),
-- (14000, '2025-04-12', 7, 8),
-- (16000, '2025-04-25', 8, 9),
-- (10000, '2025-05-10', 9, 10),
-- (23000, '2025-05-25', 10, 11),

-- (19000, '2025-06-05', 11, 12),
-- (8000, '2025-06-18', 12, 13),
-- (17000, '2025-07-02', 13, 14),
-- (21000, '2025-07-15', 14, 15),
-- (25000, '2025-07-28', 15, 16),
-- (9000, '2025-08-10', 16, 17),
-- (15000, '2025-08-22', 17, 18),
-- (13000, '2025-09-05', 18, 19),
-- (24000, '2025-09-18', 19, 20),
-- (26000, '2025-10-01', 20, 1);

-- ¾ Спеціалізації (Specializations)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- спеці-алізації.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва спеціалізації.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE SPECIALIZATIONS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO SPECIALIZATIONS (NAME) VALUES
-- ('Cardiologist'),
-- ('Neurologist'),
-- ('Pediatrician'),
-- ('Oncologist'),
-- ('Surgeon'),
-- ('Orthopedist'),
-- ('Dermatologist'),
-- ('Gynecologist'),
-- ('Ophthalmologist'),
-- ('Urologist'),
-- ('Radiologist'),
-- ('Anesthesiologist'),
-- ('Psychiatrist'),
-- ('Endocrinologist'),
-- ('Gastroenterologist'),
-- ('Nephrologist'),
-- ('Infectious Disease Specialist'),
-- ('Rehabilitation Specialist'),
-- ('Emergency Physician'),
-- ('Intensivist'),

-- ('Allergist'),
-- ('Immunologist'),
-- ('Hematologist'),
-- ('Rheumatologist'),
-- ('Pulmonologist'),
-- ('Pathologist'),
-- ('Family Doctor'),
-- ('General Practitioner'),
-- ('Traumatologist'),
-- ('Plastic Surgeon');

-- ¾ Спонсори (Sponsors)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- спонсора.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва спонсора.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE SPONSORS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO SPONSORS (NAME) VALUES
-- ('MedLife Foundation'),
-- ('HealthCare Partners'),
-- ('Global Pharma Inc'),
-- ('BioMed Solutions'),
-- ('LifeLine Charity'),
-- ('Hope Medical Fund'),
-- ('United Health Group'),
-- ('MediTrust'),
-- ('PharmaCorp'),
-- ('GreenCross Sponsors'),

-- ('Starlight Health'),
-- ('AngelCare Foundation'),
-- ('NeoMed Systems'),
-- ('Vitality Support Fund'),
-- ('Doctors Without Borders Support UA'),
-- ('Prime Health Investments'),
-- ('Sunrise Medical Group'),
-- ('EuroMed Alliance'),
-- ('SmartHealth Sponsors'),
-- ('CareFirst Foundation');

-- ¾ Відпустки(Vacations)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- відпустки.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Дата завершення (EndDate). Дата завершення відпустки.
-- ▷ Тип даних для зберігання дати.
-- ▷ Не містить null-значення.
-- ▷ Має бути більшою за дату початку відпустки.
-- ■ Дата початку (StartDate). Дата початку відпустки.
-- ▷ Тип даних для зберігання дати.
-- ▷ Не містить null-значення.
-- ■ Ідентифікатор лікаря (DoctorId). Лікар, який у відпустці.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ

-- CREATE TABLE VACATIONS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	END_DATE DATE NOT NULL CHECK(END_DATE > START_DATE),
-- 	START_DATE DATE NOT NULL,
-- 	DOCTOR_ID INT NOT NULL,
-- 	FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS(ID)
-- )

-- INSERT INTO VACATIONS (START_DATE, END_DATE, DOCTOR_ID) VALUES
-- ('2024-01-05', '2024-01-20', 1),
-- ('2024-01-10', '2024-01-25', 2),
-- ('2024-02-01', '2024-02-14', 3),
-- ('2024-02-10', '2024-02-25', 4),
-- ('2024-03-01', '2024-03-15', 5),
-- ('2024-03-05', '2024-03-18', 6),
-- ('2024-03-10', '2024-03-25', 7),
-- ('2024-04-01', '2024-04-12', 8),
-- ('2024-04-10', '2024-04-22', 9),
-- ('2024-04-15', '2024-04-28', 10),

-- ('2024-05-01', '2024-05-15', 11),
-- ('2024-05-05', '2024-05-20', 12),
-- ('2024-05-10', '2024-05-25', 13),
-- ('2024-06-01', '2024-06-14', 14),
-- ('2024-06-05', '2024-06-18', 15),
-- ('2024-06-10', '2024-06-25', 16),
-- ('2024-07-01', '2024-07-12', 17),
-- ('2024-07-05', '2024-07-20', 18),
-- ('2024-07-10', '2024-07-25', 19),
-- ('2024-08-01', '2024-08-15', 20),

-- ('2024-08-05', '2024-08-18', 21),
-- ('2024-08-10', '2024-08-25', 22),
-- ('2024-09-01', '2024-09-14', 23),
-- ('2024-09-05', '2024-09-20', 24),
-- ('2024-09-10', '2024-09-25', 25),
-- ('2024-10-01', '2024-10-15', 26),
-- ('2024-10-05', '2024-10-18', 27),
-- ('2024-10-10', '2024-10-25', 28),
-- ('2024-11-01', '2024-11-14', 29),
-- ('2024-11-05', '2024-11-20', 30),

-- ('2024-11-10', '2024-11-25', 31),
-- ('2024-12-01', '2024-12-15', 32),
-- ('2024-12-05', '2024-12-18', 33),
-- ('2024-12-10', '2024-12-25', 34),
-- ('2025-01-02', '2025-01-15', 35),
-- ('2025-01-10', '2025-01-25', 36),
-- ('2025-02-01', '2025-02-14', 37),
-- ('2025-02-05', '2025-02-20', 38),
-- ('2025-02-10', '2025-02-25', 39),
-- ('2025-03-01', '2025-03-14', 40),

-- ('2025-03-05', '2025-03-20', 41),
-- ('2025-03-10', '2025-03-25', 42),
-- ('2025-04-01', '2025-04-15', 43),
-- ('2025-04-05', '2025-04-18', 44),
-- ('2025-04-10', '2025-04-25', 45),
-- ('2025-05-01', '2025-05-14', 46),
-- ('2025-05-05', '2025-05-20', 47),
-- ('2025-05-10', '2025-05-25', 48),
-- ('2025-06-01', '2025-06-15', 49),
-- ('2025-06-05', '2025-06-18', 50),

-- ('2025-06-10', '2025-06-25', 51),
-- ('2025-07-01', '2025-07-14', 52),
-- ('2025-07-05', '2025-07-20', 53),
-- ('2025-07-10', '2025-07-25', 54),
-- ('2025-08-01', '2025-08-15', 55),
-- ('2025-08-05', '2025-08-18', 56),
-- ('2025-08-10', '2025-08-25', 57),
-- ('2025-09-01', '2025-09-14', 58),
-- ('2025-09-05', '2025-09-20', 59),
-- ('2025-09-10', '2025-09-25', 60);


-- ¾ Палати (Wards)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва палати.
-- ▷ Тип даних — varchar(20).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Ідентифікатор відділення (DepartmentId). Відділення,
-- де знаходиться палата.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE WARDS (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(20) NOT NULL UNIQUE,
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(ID)
-- )

-- INSERT INTO WARDS (NAME, DEPARTMENT_ID) VALUES
-- ('Ward A1', 1),
-- ('Ward A2', 1),
-- ('Ward A3', 1),

-- ('Ward B1', 2),
-- ('Ward B2', 2),
-- ('Ward B3', 2),

-- ('Ward C1', 3),
-- ('Ward C2', 3),
-- ('Ward C3', 3),

-- ('Ward D1', 4),
-- ('Ward D2', 4),
-- ('Ward D3', 4),

-- ('Ward E1', 5),
-- ('Ward E2', 5),
-- ('Ward E3', 5),

-- ('Ward F1', 6),
-- ('Ward F2', 6),
-- ('Ward F3', 6),

-- ('Ward G1', 7),
-- ('Ward G2', 7),
-- ('Ward G3', 7),

-- ('Ward H1', 8),
-- ('Ward H2', 8),
-- ('Ward H3', 8),

-- ('Ward I1', 9),
-- ('Ward I2', 9),
-- ('Ward I3', 9),

-- ('Ward J1', 10),
-- ('Ward J2', 10),
-- ('Ward J3', 10),

-- ('Ward K1', 11),
-- ('Ward K2', 11),
-- ('Ward K3', 11),

-- ('Ward L1', 12),
-- ('Ward L2', 12),
-- ('Ward L3', 12),

-- ('Ward M1', 13),
-- ('Ward M2', 13),
-- ('Ward M3', 13),

-- ('Ward N1', 14),
-- ('Ward N2', 14),
-- ('Ward N3', 14),

-- ('Ward O1', 15),
-- ('Ward O2', 15),
-- ('Ward O3', 15),

-- ('Ward P1', 16),
-- ('Ward P2', 16),
-- ('Ward P3', 16),

-- ('Ward Q1', 17),
-- ('Ward Q2', 17),
-- ('Ward Q3', 17),

-- ('Ward R1', 18),
-- ('Ward R2', 18),
-- ('Ward R3', 18),

-- ('Ward S1', 19),
-- ('Ward S2', 19),
-- ('Ward S3', 19),

-- ('Ward T1', 20),
-- ('Ward T2', 20),
-- ('Ward T3', 20);

-- 1. Виведіть повні імена лікарів та їх спеціалізації.
-- SELECT
--     D.NAME,
--     D.SURNAME,
--     S.NAME AS SPECIALIZATION
-- FROM DOCTORS D
-- JOIN DOCTORS_SPECIALIZATIONS DS ON DS.DOCTOR_ID = D.ID
-- JOIN SPECIALIZATIONS S ON S.ID = DS.SPECIALIZATION_ID;

-- 2. Виведіть прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці 2025-06-08.
-- SELECT D.SURNAME, D.SALARY+D.PREMIUM
-- FROM DOCTORS D
-- JOIN VACATIONS V ON V.DOCTOR_ID = D.ID
-- WHERE V.START_DATE < '2025-06-08'AND V.END_DATE > '2025-06-08'


-- 3. Виведіть назви палат, які знаходяться у відділенні -- «Rehabilitation».
-- SELECT W.NAME, D.NAME
-- FROM WARDS W JOIN DEPARTMENTS D ON W.DEPARTMENT_ID = D.ID
-- WHERE D.NAME = 'Rehabilitation'

-- 4. Виведіть назви відділень без повторень, які спонсоруються компанією «United Health Group».
-- SELECT DISTINCT D.NAME, S.NAME
-- FROM DEPARTMENTS D
-- JOIN DONATIONS DON ON DON.DEPARTMENT_ID = D.ID
-- JOIN SPONSORS S ON DON.SPONSOR_ID = S.ID
-- WHERE S.NAME = 'United Health Group'

-- 5. Виведіть усі пожертвування з липня місяця 2025 року у вигляді: відділення, спонсор, сума пожертвування, дата
-- пожертвування.

-- SELECT D.NAME AS DEPARTMENT, S.NAME AS SPONSOR, DON.AMOUNT, DON.DONATION_DATE
-- FROM DEPARTMENTS D
-- JOIN DONATIONS DON ON DON.DEPARTMENT_ID = D.ID
-- JOIN SPONSORS S ON DON.SPONSOR_ID = S.ID
-- WHERE DON.DONATION_DATE >= '2025-07-01'

-- 6. Виведіть прізвища лікарів із зазначенням відділень, в яких вони проводять обстеження.
-- SELECT D.SURNAME AS DOCTOR, DEP.NAME AS DEPARTMENT
-- FROM DOCTORS D
-- JOIN DEPARTMENTS DEP ON D.DEPARTMENT_ID = DEP.ID
-- ORDER BY DEPARTMENT

-- 7. Виведіть назви відділень, які отримували пожертву-вання у розмірі понад 10000, із зазначенням їх лікарів.
-- SELECT *
-- FROM DONATIONS

-- SELECT D.NAME AS DEPARTMENTS, DON.AMOUNT, DOC.SURNAME AS DOCTOR
-- FROM DONATIONS DON
-- JOIN DEPARTMENTS D ON DON.DEPARTMENT_ID = D.ID
-- JOIN DOCTORS DOC ON DOC.DEPARTMENT_ID = D.ID
-- WHERE DON.AMOUNT > 20000

-- 8. Виведіть назви відділень, лікарів  з надбавкою менш ніж 4000.
-- SELECT * FROM DOCTORS

-- SELECT DEP.NAME AS DEPARTMENTS, D.SURNAME, D.PREMIUM
-- FROM DOCTORS D
-- JOIN DEPARTMENTS DEP ON D.DEPARTMENT_ID = DEP.ID
-- WHERE D.PREMIUM < 4000
-- ORDER BY DEPARTMENTS
