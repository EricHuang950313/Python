import time
import numpy as np
n=10000000
mylist = list(range(1,n+1))
myarray = np.array(mylist) #convert list to numpy array
start_time = time.time()
sum(mylist)
end_time = time.time()
print('time cost of list sum :',end_time-start_time)
start_time = time.time()
myarray.sum()
end_time = time.time()
print('time cost of array sum :',end_time-start_time)
