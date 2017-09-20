# coding: utf-8
__author__ = 'Administrator'
# n=100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#     print("Sum of 1 until %d: %d" % (n,sum)


class A(object):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a+self.b

count = A('4',5)
print(count.add())