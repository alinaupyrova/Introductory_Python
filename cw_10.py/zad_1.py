import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.linspace(1,20,100)
y = 1/x
plt.plot(x, y,label = 'f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()