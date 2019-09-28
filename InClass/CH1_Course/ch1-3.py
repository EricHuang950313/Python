l = [0, 9, 8, 8, 2, 2, 8, 7, 7, 8]

print(l[-4])
print(l[2:4])
print(l[:4])
print(l[4:])

del l[4:]
l += [1, 2, 3, 4, 5, 6]
print(l)