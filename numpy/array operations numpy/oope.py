import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print(arr+5)
print(arr-2)
print(arr*3)
print(arr/2)
print(arr**2)
print(arr>3)
print(arr<3)
print(arr>=3)
print(arr<=3)
print(arr==3)
print(arr!=3)
# print(np.sum(arr))
# print(np.sum(arr,axis=0))#column wise sum
# print(np.sum(arr,axis=1))#row wise sum
# print(np.mean(arr))
# print(np.mean(arr,axis=0))#column wise mean
# print(np.mean(arr,axis=1))#row wise mean
# print(np.min(arr))
# print(np.min(arr,axis=0))#column wise min
# print(np.min(arr,axis=1))#row wise min
# print(np.max(arr))
# print(np.max(arr,axis=0))#column wise max
# print(np.max(arr,axis=1))#row wise max
# print(np.std(arr))#standard deviation
# print(np.std(arr,axis=0))#column wise standard deviation
# print(np.std(arr,axis=1))#row wise standard deviation
# print(np.var(arr))#variance
# print(np.var(arr,axis=0))#column wise variance

# print(np.var(arr,axis=1))#row wise variance
# print(np.sqrt(arr))#square root
# print(np.exp(arr))#exponential
# print(np.log(arr))#natural logarithm
# print(np.log10(arr))#base 10 logarithm
# print(np.log2(arr))#base 2 logarit

#aggregation functions
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.sqrt(arr))