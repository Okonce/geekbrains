'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''

people = int(input('Введите количество друзей: '))

adj_matrix = []
for i in range(people):
    a = [1] * people
    a[i] = 0
    adj_matrix.append(a)

handshake = 0
for n, i in enumerate(adj_matrix):
    handshake += sum(i[n:])

print(f"Всего  произведено {handshake} рукопожатий")
