import numpy as np

arr_1d=np.array([1,2,3,4,5,6])
arr_2d=np.array([[1,2,3],[4,5,6]])
arr_3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_1d)
print(arr_2d)
print(arr_3d)
print(arr_1d.shape,"shape of 1d array")
print(arr_2d.shape,"shape of 2d array")
print(arr_3d.shape,"shape of 3d array")
print("*************")
print(arr_1d.size,"size of 1d array")
print(arr_2d.size,"size of 2d array")
print(arr_3d.size,"size of 3d array")
print("*************")
print(arr_1d.dtype,"datatype of 1d array")
print(arr_2d.dtype,"datatype of 2d array")
print(arr_3d.dtype,"datatype of 3d array")
print("*************")

print(arr_1d.itemsize,"itemsize of 1d array")
print(arr_2d.itemsize,"itemsize of 2d array")
print(arr_3d.itemsize,"itemsize of 3d array")
print("*************")
print(arr_1d.nbytes,"nbytes of 1d array")
print(arr_2d.nbytes,"nbytes of 2d array")
print(arr_3d.nbytes,"nbytes of 3d array")


print("*************")    
      
print(arr_1d.ndim,"dimension of 1d array")
print(arr_2d.ndim,"dimension of 2d array")
print(arr_3d.ndim,"dimension of 3d array")
print("*************")

# to change data type of array
#using astype() method
arr_1d_float=arr_1d.astype(np.float64)
print(arr_1d_float)
print(arr_1d_float.dtype)

#to convert 1d array to 2d array
arr_1d_to_2d=arr_1d.reshape(2,3)
print(arr_1d_to_2d)