import numpy as np
x = np.array([10,9,8,7,6])
x[0:3] += 3
x[-1] *= 5
print(x)

print("==============")

y = np.random.random(10) # 產生 0~1 之間的隨機值
y *= 100
y = y.astype(int)
print(y)

print("==============")

print(np.sort(y))
print(np.sort(y)[::-1])
print(np.argsort(y))
print("min position:",np.argsort(y)[0])
print("max position:",np.argsort(y)[-1])

print("==============")

p = y > 50
print(p)
print(sum(y))
for i in range(len(p)):
    if p[i] == True:
        print(y[i], end=" ")
