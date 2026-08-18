import matplotlib.pyplot as plt
import numpy as np

#Bar chart is a type of chart that represents data with rectangular bars. The length of each bar is proportional to the value it represents. Bar charts are commonly used to compare different categories or groups of data.

#lets create for the foods consumption

categories = np.array(['Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains'])
values = np.array([25, 30, 15, 20, 10])

# Create a bar chart using the bar() function. The first argument is the x-axis values (categories), and the second argument is the y-axis values (values).
plt.bar(categories, values, color='skyblue', edgecolor='black')

plt.grid(True, linestyle='--', color='gray', alpha=0.5) #alpha is used to set the transparency of the grid lines. A value of 0 means fully transparent, while a value of 1 means fully opaque.
plt.xticks(fontsize=10, color='green') # Set the font size and color of the x-axis tick labels.
plt.yticks(fontsize=10, color='green') # Set the font size and color of the y-axis tick labels.


plt.title('Food Consumption Bar Chart', fontsize=14, fontweight='bold', pad=15, color='darkblue')
plt.xlabel('Food Categories')
plt.ylabel('Consumption Values')
plt.show()