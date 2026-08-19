import matplotlib.pyplot as plt
import numpy as np

#sub plots means creating multiple plots in a single figure. It allows you to visualize different datasets or different aspects of the same dataset side by side for comparison.

x = np.array([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
figures,axes = plt.subplots(2, 2)  # (rows, columns, index)

axes[0, 0].plot(x, x**3, color = 'red')
axes[0, 0].set_title('Cubic Function')
axes[0, 1].bar(x, x**2, color = 'blue')
axes[0, 1].set_title('Square Function')
axes[1, 0].plot(x, x**4, color = 'green')
axes[1, 0].set_title('Quartic Function')
axes[1, 1].pie([1, 2, 3, 4], labels=['A', 'B', 'C', 'D'], colors=['red', 'blue', 'green', 'orange'])
axes[1, 1].set_title('Quintic Function')

plt.show()