import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
type_count = df['Type1'].value_counts()

plt.barh(type_count.index, type_count.to_numpy(), align='center', alpha=0.7)
plt.xlabel('Type1')
plt.ylabel('Count')
plt.title('Count of Type1 in DataFrame')
plt.tight_layout()

plt.show()