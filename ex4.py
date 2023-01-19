# -*- coding: cp1251 -*-


def hello(i,n):
    if i <= n:
        print(i,"Привет!")
        i += 1
        hello(i, n)

    if i > n:
        input()
        exit()


i = 1
print("Введите число")
n = int(input())

hello(i, n)
