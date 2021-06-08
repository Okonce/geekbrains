/* Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение” */

use shop;

-- 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными.
--   Заполните их текущими датой и временем.

-- ранее у меня было так

/* DROP TABLE IF EXISTS storehouses;
CREATE TABLE storehouses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Склады';*/

-- поменяем для задания 1

ALTER TABLE users CHANGE created_at created_at DATETIME;
ALTER TABLE users CHANGE updated_at updated_at DATETIME;

insert into users (name)
values ('assima');

select * from users;

update users
    SET created_at = NOW()
where created_at is null;

update users
    SET updated_at = NOW()
where updated_at is null;

select * from users;


-- 2. Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них
--   долгое время помещались значения в формате "20.10.2017 8:10". Необходимо преобразовать поля к типу DATETIME,
--   сохранив введеные ранее значения.

ALTER TABLE users CHANGE created_at created_at VARCHAR(100);
ALTER TABLE users CHANGE updated_at updated_at VARCHAR(100);

insert into users (created_at, updated_at)
values ('20.10.2017 8:10', '21.10.2017 18:10');

select * from users;

update users
    set created_at = STR_TO_DATE(created_at, '%d.%m.%Y %H:%i')
where id = 8;

update users
    set updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %H:%i')
where id = 8;

select * from users;

-- вернем как было раньше
ALTER TABLE users CHANGE created_at created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE users CHANGE updated_at updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

-- 3. В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры:
-- 0, если товар закончился и выше нуля, если на складе имеются запасы.
-- Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value.
-- Однако, нулевые запасы должны выводиться в конце, после всех записей.

INSERT INTO storehouses_products
  (value)
VALUES
  (0), (1),(0),(5),(6),(9);

(select * from storehouses_products
where value > 0
order by value)
union
select * from storehouses_products
where value = 0; -- я только так придумала

/* 4 (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае.
   Месяцы заданы в виде списка английских названий ('may', 'august')
*/

select * from users;
select * from users where MONTHNAME(birthday_at) in ('may', 'august');

/* 5 (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса.
   SELECT * FROM catalogs WHERE id IN (5, 1, 2);
   Отсортируйте записи в порядке, заданном в списке IN.
*/

SELECT * FROM catalogs;

 SELECT *
 FROM catalogs
 WHERE id IN (5, 1, 2)
 ORDER BY FIELD(id,5,1,2);

# 1. Подсчитайте средний возраст пользователей в таблице users

select avg(TIMESTAMPDIFF(YEAR, birthday_at, NOW())) as 'avr' FROM users;

# 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели.
# Следует учесть, что необходимы дни недели текущего года, а не года рождения.

select * from users;
SELECT COUNT(*), DAYNAME(birthday_at) as dayname FROM users group by dayname;
