import numpy as np
arr=np.array([1,2,3,4,5,6])
result=arr*2
print(result)
print(arr)

#1d to 2d
matrix=np.array([[1,2,3],[4,5,6]])
print(matrix)
vector=np.array([10,20,30])
result2=matrix+vector
print(result2)

#incompatible dimensions
matrix2=np.array([[1,2,3],[4,5,6]])
vector2=np.array([10,20])
#result3=matrix2+vector2 #error