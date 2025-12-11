"""
np.insert(arr, index, values, axis=None)
"""
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print("Original array:")
print(arr)
#insert 10 at index 1
new_arr=np.insert(arr,1,10,axis=0)#inserts a new row at index 1
print("Array after inserting 10 at index 1 along axis 0:")
print(new_arr)

####### using axis=none
a=np.array([[1,2,3],[4,5,6]])
print("Original array:")
print(a)
#insert 10 at index 1
new_a=np.insert(a,1,10,axis=None)#inserts a new row at index 1
print("Array after inserting 10 at index 1 along axis 0:")
print(new_a)