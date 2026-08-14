import matplotlib.pyplot as plt

# 1. Prepare the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create the plot
plt.plot(x, y, marker='o', color='blue', linestyle='-')

# 3. Add labels and a title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot')

# 4. Display the chart
plt.show()
