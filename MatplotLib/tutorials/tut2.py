#plt.plot(x,y, color='red',linestyle='dashed',linewidth=2,marker='o',label='Data Points')
import matplotlib.pyplot as plt
x=['mon', 'tue', 'wed', 'thu', 'fri'] #x axis
y=[5, 7, 8, 6, 4] #y axis
plt.plot(x, y, color='red',linestyle='dashed',linewidth=2,marker='o',label='Data Points')
plt.xlabel('Days')#x axis
plt.ylabel('Values')#y axis
plt.title('Sample Plot')#title
plt.legend(loc='upper left')#show legend
plt.grid(color='green', linestyle='--', linewidth=0.5)#show grid
plt.xlim(0, 4)#set x axis limit
plt.ylim(0, 10)#set y axis limit
plt.xticks(rotation=45)#rotate x axis labels
plt.yticks(rotation=45)#rotate y axis labels
plt.show()#display plot

#plt.grid() is help to add grid lines to the plot

#plt.xlim() is used to set the limits for the x-axis
#plt.ylim() is used to set the limits for the y-axis
#plt.xticks() is used to set the ticks for the x-axis
#plt.yticks() is used to set the ticks for the y-axis
plt.xticks([1,2,3,4],['m1','m2','m3','m4'])#set x axis ticks
plt.yticks([0,2,4,6,8,10],['0','2','4','6','8','10'])#set y axis ticks
plt.show()#display plot