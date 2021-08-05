import numpy as np

R = np.zeros((11,4))
Z = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
for i in range(11):
    R[i,:] = Z[i:i+4]
print(R)