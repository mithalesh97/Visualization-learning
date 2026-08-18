import matplotlib.pyplot as plt
import numpy as np

#pie chart is a circular statistical graphic, which is divided into slices to illustrate numerical proportion. In a pie chart, the arc length of each slice (and consequently its central angle and area) is proportional to the quantity it represents.

#different example of pie chart
categories = ['Freshmen', 'Sophomore', 'Junior', 'Senior']
values = np.array([25, 30, 15, 20])

plt.pie(values,
        labels = categories,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'],
        wedgeprops={'edgecolor':'black'},
        explode=(0.1, 0, 0, 0),                #wedgeprops is used to customize the appearance of the wedges in the pie chart. In this case, we are setting the edge color of the wedges to black.
        shadow=True)                            #explode is used to "explode" or offset a slice of the pie chart. In this case, we are exploding the first slice (Freshmen) by 0.1 units.
plt.title('Student Distribution by Year', fontsize=14, fontweight='bold', pad=15, color='darkblue')

plt.show()