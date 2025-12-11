#properties
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
shape =arr.shape #number of rows and columns
print(shape,"rows,columns")

size=arr.size #total number of elements in the array
print(size,"total elements")

ndim=arr.ndim #number of dimensions
print(ndim,"dimensions in the array")


dtype=arr.dtype #data type of the elements in the array
print(dtype,"data type of the elements in the array")

itemsize=arr.itemsize #size of each element in the array
print(itemsize,"size of each element in the array")

nbytes=arr.nbytes #total size of the array in bytes
print(nbytes,"total size of the array in bytes")

flat=arr.flat #returns a 1D iterator over the array
print(flat,"1D iterator over the array")









#operations