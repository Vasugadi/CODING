#matrix
#multi dimensional array

import numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(matrix.shape)#3 rows and 3 columns

#creating a array from a python list

import numpy as np
a=np.array([1,2,3,4,5])
print(a)

#with default values
c=np.ones((3,4))#3 rows and 4 columns
b=np.zeros((3,4))#3 rows and 4 columns
print(c)
print(b)
d=np.full((3,4),7)#3 rows and 4 columns with all values as 7
print(d)    #3 rows and 4 columns with all values as 7
e=np.eye(3)#3 rows and 3 columns with all values as 1
print(e)
f=np.random.random((3,4))#3 rows and 4 columns with random values
print(f)