def dis(a, b):
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(b)):
        b[i] = int(b[i])
    if a[0] < a[1]:
        return "Yes" if sum(b[a[0]:(a[1]+1)]) < a[2] else "No"
    else:
        return "Yes" if sum(b[a[1]:(a[0]+1)]) < a[2] else "No"

a = input().split()
b = input().split()

print(dis(a, b))