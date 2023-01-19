# -*- coding: cp1251 -*-


def fibanachi(i, n):
    print(i+n)
    if i+n <= 21:
        fibanachi(n, n+i)



fibanachi(0, 1)

input()