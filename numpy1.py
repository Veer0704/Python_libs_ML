import numpy as np
arr_1d = np.array([1,2,3,4])
print(arr_1d)
print(type(arr_1d))

# 2-d array printing

arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d)
print(arr_2d.ndim)

print(arr_2d.size) #total elements
print(arr_1d.size)
print(arr_2d.dtype) #datatype
print(arr_2d.shape) #row*columns