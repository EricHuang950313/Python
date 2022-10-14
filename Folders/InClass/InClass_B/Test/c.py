def create_list(n):
    l = []
    a = 0
    for i in range(n):
        l += [list(range(a, n+a))]
        a += 1
    print(l)

create_list(5)