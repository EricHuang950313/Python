def Fab(n):
    if n > 2:
        return Fab(n-1)+Fab(n-2)
    else:
        return 1
print(Fab(8))

def getTotal(n):
    a1 = 1
    a2 = 1
    for i in range(3, n):
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    return a1+a2

print(getTotal(8))