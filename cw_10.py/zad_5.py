import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("iris .data", sep=",", names=["sepal length", "sepal width", "3", "4", "5"])
color = np.random.randn(150)
x = df["sepal length"]
y = df["sepal width"]
plt.scatter(x, y, s=10 * abs(x - y), c=color)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.colorbar()
plt.show()
