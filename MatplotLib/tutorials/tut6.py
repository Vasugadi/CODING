#scatter plot
#scatter plot is used for visualizing the relationship between two continuous variables
import matplotlib.pyplot as plt

# x = [5, 10, 15, 20, 25]
# y = [10, 20, 25, 30, 35]
# plt.scatter(x, y, color='blue', marker='*', label='student data')
# plt.title('Scatter Plot Example')
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.legend(loc='upper left')
# plt.grid(True)
# plt.show()

plt.scatter([1, 2, 3, 4, 5], [50, 60, 70, 80, 90], color='blue', marker='*', label='student data')
plt.scatter([1, 2, 3, 4, 5], [30, 40, 50, 60, 70], color='red', marker='o', label='employee data')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

