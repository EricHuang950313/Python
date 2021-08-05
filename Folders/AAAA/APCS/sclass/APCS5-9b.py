x = 1
for i in range(1, 6):
    if i % 2 == 0:
        x = 0
    else:
        x = 1
    for j in range(i):
        if x == 0:
            print(1, end="")
            x = 1
        else:
            print(0, end="")
            x = 0
    print()