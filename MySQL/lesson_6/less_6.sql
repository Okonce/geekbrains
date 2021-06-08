/* Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение. Агрегация данных”.
   Работаем с БД vk и данными, которые вы сгенерировали ранее:

   1. Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека,
   который больше всех общался с выбранным пользователем (написал ему сообщений).
   2. Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..
   3. Определить кто больше поставил лайков (всего): мужчины или женщины.
*/
set @user_id = 1;
select COUNT(*) as cnt, from_user_id from messages
where to_user_id = @user_id
group by from_user_id
order by cnt desc limit 1;

set @user_id = 1;
select * from messages
where to_user_id = @user_id
group by from_user_id;

select SUM(media_id) as cnt from likes
where user_id in (select user_id from profiles where TIMESTAMPDIFF(YEAR, birthday, NOW()) < 10);


select SUM(media_id) as cnt, (select gender from profiles where user_id = likes.user_id) as gender from likes
group by gender
order by cnt desc limit 1;


