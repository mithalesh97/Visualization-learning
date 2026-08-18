import matplotlib.pyplot as plt
import numpy as np

#grid is a function that is used to add a grid to the plot. It helps in better visualization of the data points by providing reference lines. The grid can be customized in terms of line style, color, and transparency.
x = np.array([2020,2021,2022,2023])
y = np.array([10,20,30,40])

plt.grid(True, linestyle='--', color='gray', alpha=0.5) #alpha is used to set the transparency of the grid lines. A value of 0 means fully transparent, while a value of 1 means fully opaque.
plt.plot(x,y)
plt.show()