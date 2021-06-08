# a = [135, 45934, True, 'Hello']

# for i in a:
#     print(i)

# b = a.__iter__()
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

# iter_a = a.__iter__()
# while True:
#     try:
#         print(iter_a.__next__())
#     except StopIteration:
#         break

class Iterator:

    def __init__(self, start=0):
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= 10:
            return self.i
        else:
            raise StopIteration

    def __iter__(self):
        return self

obj = Iterator(start=0)
for el in obj:
    print(el)