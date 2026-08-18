import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020,2021,2022,2023])
y = np.array([10,20,30,40])
z = np.array([5,15,2,3])

plt.plot(x,y)
plt.plot(x,z)
plt.title('Multi-Line Plot Example', fontsize=14, fontweight='bold', pad=15, color='darkblue')
plt.xlabel('Year')
plt.ylabel('Value')

#tick marks
plt.xticks(x, rotation=45, fontsize=10, color='green')
plt.yticks(fontsize=10, color='green')

#tick parameters is used to customize the appearance of ticks on the axes. It allows you to control the size, color, direction, and other properties of the ticks. In this case, we are setting the tick parameters for both the x-axis and y-axis.
plt.tick_params(axis='x', direction='inout', length=6, width=2, colors='purple', grid_color='gray', grid_alpha=0.5)
plt.tick_params(axis='y', direction='inout', length=6, width=2, colors='purple', grid_color='gray', grid_alpha=0.5)

# Add a grid to the plot for better readability. The grid lines are styled with a dashed line, a light gray color, and partial transparency (alpha=0.5).
plt.grid(True, linestyle='--', color='gray', alpha=0.5)
plt.show()