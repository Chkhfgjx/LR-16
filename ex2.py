def SumTo(a, summa):
    if a > 0:
        summa += a
        a -= 1
        SumTo(a, summa)

    if a == 0:
        print (summa)
        input()
        exit()

a = int(input())
summa = 0
SumTo(a, summa)




