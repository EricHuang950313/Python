for i in range(1, 11):
    print(i,":",end="")
    for j in range(1, 11):
        if i % j == 0:
            print( j, end=",")
    print()