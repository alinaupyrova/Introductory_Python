import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.arange(0,31,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label = 'sin(x)')
plt.plot(x,y2, label = 'cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x) , cos(x)')
plt.legend()
plt.show()
