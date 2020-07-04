def Fabi(n):
    if n < 2:
        return 1
    else:
        return Fabi(n-1) + Fabi(n-2)
print(Fabi(3))
