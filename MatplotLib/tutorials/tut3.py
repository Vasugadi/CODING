#bar plot
#bar plot helps in comparing different categories
import matplotlib.pyplot as plt
product=['A', 'B', 'C', 'D']
sales=[10, 15, 7, 12]
#to make a horizontal bar plot
#with h it acts as horizontal
#without h it acts as 
plt.barh(product, sales, color='blue',label='Sales Data',height=0.4)
plt.xlabel('Sales')
plt.ylabel('Products')
plt.title('Product Sales Comparison')
plt.legend(loc='upper left')
plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()