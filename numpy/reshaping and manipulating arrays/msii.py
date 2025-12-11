import numpy as np
arr=np.array([[1,2,3,np.nan,4,5,6]])
print(arr)
print(np.nan_to_num(arr,nan=9))  # Replace NaN with 0