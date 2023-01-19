def osnovnaya(a):
    if a >= 0:
        print(a)
        a -= 2
        osnovnaya(a)


osnovnaya(25)

input()
