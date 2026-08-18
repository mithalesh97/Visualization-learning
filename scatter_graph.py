import matplotlib.pyplot as plt
import numpy as np

#scatter graph is a type of plot that uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.

#relation between students' study hours and their scores
study_hours1 = np.array([1, 1, 3, 4, 5, 6, 7, 8, 8, 10])
scores1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

study_hours2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scores2 = np.array([15, 25, 35, 45, 55, 65, 75, 85, 95, 105])

plt.scatter(study_hours1, scores1, color='blue', marker='o', s=100, alpha=0.7, edgecolors='black', label='Group 1') #s is used to set the size of the markers. In this case, we are setting the size of the markers to 100.
plt.scatter(study_hours2, scores2, color='red', marker='s', s=100, alpha=0.7, edgecolors='black', label='Group 2') #s is used to set the size of the markers. In this case, we are setting the size of the markers to 100.
plt.title('Study Hours vs Scores', fontsize=14, fontweight='bold', pad=15, color='darkblue')
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.legend()
plt.show()