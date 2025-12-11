"""
np.concatenate((arr1, arr2, ...))
axis=0  # vertical stacking (row-wise)
axis=1  # horizontal stacking (column-wise)

    """




import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
new_arr=np.concatenate((arr,arr2),axis=0)
print(new_arr)