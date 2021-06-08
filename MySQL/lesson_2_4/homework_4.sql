USE vk;

-- ii. Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке

SELECT DISTINCT firstname FROM users ORDER BY firstname;

-- iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false).
-- Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)

ALTER TABLE `profiles` ADD COLUMN is_active BIT DEFAULT 1;
UPDATE `profiles`
SET
    is_active = 0
-- WHERE DATE(birthday) > '2004-01-01';
WHERE (birthday + interval 18 YEAR) > NOW();

SELECT
  user_id,
  IF(
	TIMESTAMPDIFF(YEAR, birthday, NOW()) < 18,
	'0',
	'1'
  ) AS is_active
FROM
  `profiles`;

-- iv. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)

delete from messages
where DATE(created_at) > NOW()
;

ALTER TABLE messages
ADD COLUMN is_deleted BIT default 0;

UPDATE messages
SET messages.is_deleted = 1
WHERE created_at > NOW();

-- v. Написать название темы курсового проекта (в комментарии)
-- Модель хранения данных кинопоиска