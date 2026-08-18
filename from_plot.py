import matplotlib.pyplot as plt
import numpy as np

# 1. Generate sample data
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([10, 20, 15, 10, 40])
y2 = np.array([2, 3, 4, 7, 8])

# 2. Define style configuration dictionaries
# (Using type annotations to keep Pylance happy)
y1_style: dict = dict(
    label='Primary Dataset',
    marker='s',
    markersize=10,
    markerfacecolor='red',
    markeredgecolor='green',
    linestyle='solid',
    linewidth=2,
    color='black'
)

y2_style: dict = dict(
    label='Secondary Dataset',
    marker='.',
    markersize=10,
    markerfacecolor='red',
    markeredgecolor='green',
    linestyle='solid',
    linewidth=2,
    color='darkblue'
)

# 3. Create the plot figure
plt.figure(figsize=(8, 5))

# 4. Plot data using dictionary unpacking
plt.plot(x, y1, **y1_style)
plt.plot(x, y2, **y2_style)

# 5. Decorate and customize the chart
plt.title('Customized Multi-Line Visualization', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('X-Axis Values (Independent Variable)', fontsize=11, labelpad=10)
plt.ylabel('Y-Axis Values (Dependent Variable)', fontsize=11, labelpad=10)

# 6. Add layout enhancements
plt.grid(True, linestyle=':', alpha=0.6)  # Subtle dotted background grid
plt.legend(loc='upper left', frameon=True) # Displays labels configured in dictionaries

# 7. Render and show chart
plt.tight_layout()  # Automatically adjusts padding around boundaries
plt.show()