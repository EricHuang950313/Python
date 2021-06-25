def avg(*ns):
    sum = 0
    for i in ns:
        sum += i
    print(sum/len(ns))


avg(1, 2, 3, 4)
