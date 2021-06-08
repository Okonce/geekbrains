# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.

n = int(input())
hour, minute, sec = 0, 0, 0
if n > 60:
    if n > 3600:
        hour = n // 3600
        minute = n % 3600 // 60
        sec = n - hour*3600 - minute*60
    elif n == 3600:
        hour = 1
    else:
        minute = n // 60
        sec = n - minute*60
elif n == 60:
    minute = 1
elif n < 60:
    sec = n

# print("{:0>2}:{:0>2}:{:0>2}".format(hour,minute,sec))
print(f'{hour:02}:{minute:02}:{sec:02}')