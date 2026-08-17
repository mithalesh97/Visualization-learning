import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y1 = np.array([10,20,15,10,40])
y2 = np.array([2,3,4,7,8])


#create the dictionary and just call the dictionary function
line_style = dict(marker='.',
                  markersize = 10,
                  markerfacecolor = 'red',
                  markeredgecolor = 'blue',
                  linestyle='solid',
                  linewidth = 2,
                  color = 'green')

plt.plot(x,y1,marker = 's',
         markersize = 10,
         markerfacecolor = 'red',
         markeredgecolor = 'green',
         linestyle='solid',
         linewidth = 2,
         color = 'black')

plt.plot(x, y2, **line_style) #type: ignore
plt.show()