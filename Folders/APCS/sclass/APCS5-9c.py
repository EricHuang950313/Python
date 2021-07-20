for i in range(5):
    l = [(i+1) for a in range(5)]
    l[i] = 0
    for j in range(5):
        print(l[j], end="")
    print() 