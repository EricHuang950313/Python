times = int(input())
for i in range(times):
    a = input().split()
    if int(a[1])-int(a[0]) == int(a[2])-int(a[1]):
        print(a[0], a[1], a[2], a[3], int(a[3])+(int(a[1])-int(a[0])))
    else:
        print(a[0], a[1], a[2], a[3], round(int(a[3])*(int(a[1])/int(a[0]))))