#histograms
#histograms are used for visualizing the distribution of a dataset
import matplotlib.pyplot as plt
scores=[45, 67, 23, 89, 12, 34, 56, 78, 90, 100]
#we can give the bins =4 or etc then the histogram will have that many bars its automatically calculated by matplotlib
plt.hist(scores, bins=[0,20,40,60,80,100], color='purple', edgecolor='black', alpha=0.7)
plt.title('Score Distribution')
plt.xlabel('Score Ranges')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

#here the height of the bar represents the number of studentss in
#that range
