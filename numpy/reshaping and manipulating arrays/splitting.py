"""
Splitting arrays
np.split(array, indices_or_sections, axis=0)
np.vsplit(array, indices_or_sections)
np.hsplit(array, indices_or_sections)
"""

import numpy as np
arr=np.array([[10,20,30,40,50,60]] )
print("Original array:")
print(arr)
print("******************************")
print(np.split(arr,3,axis=1 ))#splits the array into 3 equal parts
#axis=1 means we are splitting column wise
print("******************************")
print(np.hsplit(arr,3))#splits the array into 3 equal parts
#hsplit is used to split the array horizontally
print("******************************")
print(np.vsplit(arr.T,2))#splits the array into 2 equal parts
#vsplit is used to split the array vertically
print("******************************")