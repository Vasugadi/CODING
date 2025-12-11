import numpy as np
#converion of data types in numpy using astype()
arr=np.array([[1.0,2.9,3.0,4.9,5.6,6.4]])
print(arr)
print(arr.dtype)#data type of the elements in the array
int_arr=arr.astype(np.int32)
print(int_arr)#converts the array to int32
print(int_arr.dtype)

