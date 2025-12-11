#vectorization means replacing explicit loops with array expressions
list1=[1,2,3,4,5,6]
list2=[7,8,9,10,11,12]
result=[a+b for a,b in zip(list1,list2)]
print(result)

import numpy as np

arr=np.array([1,2,3,4,5,6])

result=arr*2

matrix=np.array([[1,2,3],[4,5,6]])

vector=np.array([10,20,30]) 
result2=matrix+vector

