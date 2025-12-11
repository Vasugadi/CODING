import numpy as np
#indexing and slicing in numpy
#slicing start stop and step
#
arr=np.array([[1,2,3,4,5],[6,7,8]])
print(arr)
print(arr[0])#first row
print(arr[1])#second row    
print(arr[1,2])#first and third column of all rows
print(arr[0,1:4])#first row, second to fourth column

#indexing+slicing +fancy indexing
#fancy indexing is used to access multiple elements of an array using a list of indices
print(arr[[0,1],[1,2]])#first row second column and second row
#boolean indexing
print(arr[arr>3])#all elements greater than 3
print(arr[arr%2==0])#all even elements
#boolean masking
mask=arr>3
print(arr[mask])#all elements greater than 3 using mask
mask=arr%2==0
print(arr[mask])#all even elements using mask