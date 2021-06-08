'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
from collections import Counter

string = 'BCAADDDCCACACAC'

freq = sorted(Counter(string).items(), key=lambda x: x[1], reverse=True)
nodes = freq

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))


# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечаниe: в сумму не включаем пустую строку и строку целиком;

def count_substrings(s: str, verbose=False):

    s_length = len(s)
    substr_list = set()

    for i in range(s_length):
        for j in range(s_length - 1 if i == 0 else s_length, i, -1):
            sub = s[i:j]
            if verbose:
                print(sub)
            substr_list.add(hash(sub))

    return len(substr_list)


# print(count_substrings('hello'))
print(count_substrings('hello', True))