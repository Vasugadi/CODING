# position number 

# numpy array uses zero based indexing
# positive indexing starts from 0
# negative indexing starts from -1

import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

print(arr[0])#first row
print(arr[1])#second row
print(arr[1,2])#second row third column
print(arr[0,1:3])#first row second to third column
print(arr[0:2,1])#first to second row second column
print(arr[:,1])#all rows second column
print(arr[1,:])#second row all columns

"""
print(arr[20])#index error it gives index out of bound error

"""

print(arr[1,2][1])#output 6 #first it access the element at index 1,2 which is 6 and then it access the index 1 of that element which is 6
#indexing of 1d array
a=np.array([1,2,3,4,5])
print(a[0])#first element
print(a[1])#second element
print(a[-1])#last element
print(a[-2])#second last element
print(a[1:4])#second to fourth element
print(a[:3])#first to third element
print(a[2:])#third to last element
print(a[:])#all elements
print(a[::2])#all elements with step 2
print(a[::-1])#all elements in reverse order

# boolean masking
print(a[a>3])#all elements greater than 3