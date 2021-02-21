import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
df = read_csv('output2.csv', index_col=0)
print(df)
df.plot(xticks=range(4))
# df[['sepal_length', 'sepal_width']].plot()
# df.plot()
# df.plot(subplots=True, layout=(2,2))
plt.show()