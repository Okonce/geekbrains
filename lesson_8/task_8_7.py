'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class Complex:
    '''
    Комплексное число — это выражение вида a + bi, где a, b — действительные числа,
    а i — так называемая мнимая единица, символ, квадрат которого равен –1, то есть i2 = –1.
    Число a называется действительной частью, а число b — мнимой частью комплексного числа z = a + bi.
    Если b = 0, то вместо a + 0i пишут просто a. Видно, что действительные числа — это частный случай комплексных чисел.
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f'Комплесное число - {self.a} + {self.b}i'
        else:
            return f'Комплесное число - {self.a}'

    def __add__(self, other):
        '''
        Сложение и вычитание происходят по правилу (a + bi) ± (c + di) = (a ± c) + (b ± d)i
        :param other:
        :return: Complex(new_a, new_b)
        '''
        new_a = self.a+other.a
        new_b = self.b + other.b
        return Complex(new_a, new_b)

    def __mul__(self, other):
        '''
        умножение — по правилу (a + bi) · (c + di) = (ac – bd) + (ad + bc)i (здесь как раз используется, что i2 = –1)
        :param other:
        :return:
        '''
        new_a = self.a*other.a - self.b*other.b
        new_b = self.a*other.b + self.b*other.a
        return Complex(new_a, new_b)


complex_1 = Complex(2, 4)
complex_2 = Complex(1, 3)
print(complex_1)
print(complex_2)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
