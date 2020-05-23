import numpy as np
mylist = [[1,2],[3,4],[5,6],[7,8]]

x = np.array(mylist)  #array->list
print(x) # print array
print(x.shape) #長度
print(x.ndim)  #維度

mylist2 = x.tolist()  #list->array
print(mylist2) # print list