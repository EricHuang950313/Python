def mysum(L):
    if len(L) == 1:
        return L[0]
    else:
        return int(L[0])*int(mysum(L[1:]))

print(mysum("525"))