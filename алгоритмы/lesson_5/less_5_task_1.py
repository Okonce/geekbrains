from collections import defaultdict

my_dict = defaultdict(list)
number = int(input('Введите количество предприятий: '))
all_mean = 0

for num in range(1, number + 1):
    n = input(f'Введите наименование {num} предприятия: ')
    f = int(input(f'Введите прибыль {num} за 1ый квартал: '))
    s = int(input(f'Введите прибыль {num} за 2ый квартал: '))
    t = int(input(f'Введите прибыль {num} за 3ый квартал: '))
    q = int(input(f'Введите прибыль {num} за 4ый квартал: '))
    sum_ = f + s + t + q
    all_mean += sum_

    my_dict[n].extend([f, s, t, q, sum_])

all_mean_value = all_mean / number
print(f'Cредняя прибыль (за год для ВСЕХ предприятий) {all_mean_value}')

a, b = [], []
for k, v in my_dict.items():
    if v[-1] > all_mean_value:
        a.append(k)
    else:
        b.append(k)

print(f'Предприятия, у которых прибыль больше среднего {a}')
print(f'Предприятия, у которых прибыль ниже среднего {b}')