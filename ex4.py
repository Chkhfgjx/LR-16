# -*- coding: cp1251 -*-


def hello(i,n):
    if i <= n:
        print(i,"������!")
        i += 1
        hello(i, n)

    if i > n:
        input()
        exit()


i = 1
print("������� �����")
n = int(input())

hello(i, n)
