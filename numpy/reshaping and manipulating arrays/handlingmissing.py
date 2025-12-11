"""first value is missing
second value is missing
third value is missing
last value is missing
built-in missing value
np.nan--detect missing value
np.isnan()--check missing value
np.nan_to_num()--replace missing value with zero or any other number
np.isinfinite()--check if value is finite or not
np.isfinite()--check if value is finite or not
nan-not a number --missing or calc error or 

"""

import numpy as np
data=np.array([1,2,np.nan,4,5])
print(np.isnan(data)) #check missing value
print(np.nan==np.nan) #false