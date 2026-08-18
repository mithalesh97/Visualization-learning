import matplotlib.pyplot as plt
import numpy as np

#histogram is a graphical representation of the distribution of numerical data. It is an estimate of the probability distribution of a continuous variable. A histogram consists of rectangular bars, where each bar represents the frequency (or count) of data points that fall within a specific range (or bin).

Scores = np.random.normal(loc=75, scale=10, size=1000) #loc is the mean of the distribution, scale is the standard deviation, and size is the number of samples to generate.

plt.hist(Scores, bins=20, color='skyblue', edgecolor='black') #bins is used to set the number of bins (or intervals) for the histogram. In this case, we are setting it to 20.
plt.title('Distribution of Student Scores', fontsize=14, fontweight='bold', pad=15, color='darkblue')
plt.xlabel('Scores')
plt.ylabel('Frequency')

plt.show()