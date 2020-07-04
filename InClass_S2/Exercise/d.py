def mysum(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0]+mysum(L[1:])

print(mysum([1,2,3,4,5,6,7,8,9,10]))