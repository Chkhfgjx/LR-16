# -*- coding: cp1251 -*-

def stepen(a, b, x, step):
    if x <= b:
        step *= a
        x += 1

        stepen(a, b, x, step)

    if x > b:
        print(step)
        input()
        exit()

x = 1
step = 1
print("Введите число")
a = int(input())

print("Введите показатель степени")
b = int(input())
  
stepen(a, b, x, step)

