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
print("������� �����")
a = int(input())

print("������� ���������� �������")
b = int(input())
  
stepen(a, b, x, step)

