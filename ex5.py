import sys
sys.setrecursionlimit(1500)

def NOD(i, a, b):
    if i > 0:
        if (a % i == 0) and (b % i == 0):
            print(i)
            input()
            exit()
        
        i -= 1
        NOD(i, a, b)


b = 3430
a = 1365
i = a
NOD(i, a, b)
