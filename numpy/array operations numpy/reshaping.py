import numpy as np
#reshapeing the array create a view of the original array
arr=np.array([[1,2,3,4,5,6]])
#reshaping the array
print(arr.shape)
reshaped_arr=arr.reshape(2,3)
print(reshaped_arr)
print(reshaped_arr.shape)

#flattening the array create a copy of the original array
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)#(2,3)
flattened_arr=arr.flatten()
print(flattened_arr)

#raveling the array create a view of the original array
raveled_arr=a.ravel()
print(raveled_arr)

"""ravel =effects the original array
    
    flatten =does not effects the original array
    
    reshape =does not effects the original arrayf"""