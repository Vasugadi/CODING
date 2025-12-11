import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize=(10,5)) #1 row, 2 columns figure size 10x5

x=[1, 2, 3, 4, 5]
y=[10, 20, 25, 30, 35]

ax[0].plot(x, y, color='blue', marker='o', label='Line 1')
ax[0].set_title('First Subplot')
ax[0].set_xlabel('X-axis')
ax[0].set_ylabel('Y-axis')
ax[0].legend()
ax[0].grid(True)

ax[1].bar(x, y, color='orange', label='Bar 1')
ax[1].set_title('Second Subplot')
ax[1].set_xlabel('X-axis')
ax[1].set_ylabel('Y-axis')
ax[1].legend()
ax[1].grid(True)



#title for all
fig.suptitle('Multiple Subplots Example', fontsize=16)

plt.tight_layout()
plt.show()