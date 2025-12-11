#saving the figure
import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5]
y=[10, 20, 25, 30, 35]
plt.plot(x, y, color='blue', marker='o', label='Line 1')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
plt.show()