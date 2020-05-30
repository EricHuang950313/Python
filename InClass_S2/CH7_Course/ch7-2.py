import numpy as np
x = np.random.random(10)
x *= 100
x = x.astype(int)
print(x)
print("max position:",np.argmax(x))  #-> print("max position:",np.argsort(x)[-1])
x[np.argmax(x)] = 0  #-> x[np.argsort(x)[-1]] = 0
print(x)