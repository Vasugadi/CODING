"""stacking and splitting arrays
vertically
horizontally
vstack row wise
hstack column wise

"""

import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])

#stacking vertically
#stacking is done by np.vstack()
#it takes two arrays as input and stacks them vertically
#it returns a new array

new_arr=np.vstack((arr1,arr2))
print(new_arr)

#stacking horizontally
#stacking is done by np.hstack()
#it takes two arrays as input and stacks them horizontally
#it returns a new array

new_arr=np.hstack((arr1,arr2))
print(new_arr)