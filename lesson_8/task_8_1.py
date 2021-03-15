'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Data:

    def __init__(self, datum: str):
        self.datum = datum

    @classmethod
    def funtion_1(cls, datum):
        day, month, year = datum.split('-')
        return f'Data - {int(day)}, Month - {int(month)}, Year - {int(year)}'

    @staticmethod
    def funtion_2(day, month, year):
        if 0 < day <= 31:
            if 0 < month <= 12:
                if 1991 < year <= 2022:
                    print('All data correct')
                else:
                    print(f'Year {year} is not correct')
            else:
                print(f'Month {month} is not correct')
        else:
            print(f'Day {day} is not correct')


a = Data('24-05-1991')
print(a.funtion_1('24-05-1991'))
print(a.funtion_2(24, 5, 1991))