import matplotlib.pyplot as plt
#matplot ---main package
#pyplot is a sub-package of matplotlib
#pyplot is used for creating static, animated, and interactive visualizations in Python
#plt is a commonly used alias for the pyplot module

x=['mon', 'tue', 'wed', 'thu', 'fri'] #x axis
y=[5, 7, 8, 6, 4] #y axis

# plt.plot(x, y) #plotting the graph
# plt.xlabel('Days')#x axis
# plt.ylabel('Values')
# plt.title('Sample Plot')
# plt.show() 


x=["jan","feb","mar","apr","may"]
y=[10,20,30,40,50]
plt.plot(x,y,color="red",marker="o",label="line 1")
plt.legend()
plt.xlabel("Months")
plt.ylabel("Values")
plt.title("Line Plot")
plt.grid(True)
plt.show()
