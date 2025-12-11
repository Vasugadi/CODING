#pie chart
#pie chart helps the visualization of proportions
#it tells the contribution to the whole
import matplotlib.pyplot as plt

#plt.pie(values,labels=label_list,colors=color_list,autopct='%1.1f%%')
#autopct is used to format the percentage display on the pie chart
#%1.1f%% means to display one decimal place followed by a percent sign
regions=["north","South","east","west"]
revenu=[3000,2000,15000,1000]

plt.pie(revenu, labels=regions, autopct='%1.1f%%', colors=['gold','skyblue','lightcoral','lightsalmon'], startangle=140)
plt.title('Revenue by Region')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(loc='upper right')
plt.show()
