a = 10
b = 20

l = b
b = a
a = l # 把右邊丟進左邊

print("a:", a)
print("b:", b)

a, b = b, a
print("a:", a)
print("b:", b)