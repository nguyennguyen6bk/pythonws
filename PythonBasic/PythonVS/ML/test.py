import pandas as pd
import matplotlib.pyplot as plt
import os

dataFrame = pd.read_csv(".\\ML\\Advertising.csv")

X = dataFrame.values[:, 2]
Y = dataFrame.values[:, 4]

plt.scatter(X, Y, marker='o')
plt.show()