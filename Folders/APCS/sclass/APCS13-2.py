import random

data = [x for x in range(1, 6)]
random.shuffle(data)

print("Before Sorting:", data)
for i in range(0, len(data)-1):
    for j in range(len(data)-1, i, -1):
        if data[j] < data[j-1]:
            abc = data[j]
            data[j] = data[j-1]
            data[j-1] = abc
            print("Sorting:", data)
print("After Sorting:", data)