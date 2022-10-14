num_list = [i for i in range(0, 2001, 100)]
print(num_list)

print()

copy = num_list[:] # all
print(copy)

print()

copy = num_list[::2] # interval 1, take 1
print(copy)

print()

copy = num_list[:3] # forward 3
print(copy)

print()

copy = num_list[-3:] # last 3
print(copy)

print()

copy = num_list[1:-1] # forward 2 to last 2
print(copy)

print()

copy = num_list[::-1] # last 1 to 1
print(copy)

print()
