#np.isinfinite() 10^1000
import numpy as  np
arr=np.array([1,2,3,4,5,6,7,8,9,-np.inf,np.inf])
print(arr)
print(np.isinf(arr))  # Check for infinite values
cleaned_arr=np.nan_to_num(arr, posinf=1000, neginf=-1000)
print(cleaned_arr)  # Replace inf with large finite numbers