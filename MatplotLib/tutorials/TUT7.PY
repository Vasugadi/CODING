import matplotlib.pyplot as plt

#lt.subplot(nrows,ncols,index)

x=[1, 2, 3, 4, 5]
y=[10, 20, 25, 30, 35]
plt.subplot(1, 2,1) #1 row, 2 columns, first subplot
plt.plot(x, y, color='blue', marker='o', label='Line 1')


plt.subplot(1,2,2) #1 row, 2 columns, second subplot
plt.bar(x, y, color='orange', label='Bar 1')
plt.show()


#ooA
#fig,ax=plt.subplots(1,2)
#ax[0].plot(x,y,color='blue',marker='o',label='Line 1')
#ax[1].bar(x,y,color='orange',label='Bar 1')
#plt.show()


