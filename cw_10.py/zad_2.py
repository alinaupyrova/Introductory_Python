import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.arange(0,21,1)
y = 1/x
plt.plot(x, y,'g>:', label = 'f(x) = 1/x')
plt.xlabel('x')
plt.axis([0,20,0,1])
plt.ylabel('f(x)')
plt.legend()
plt.title("Wykres funkcji f(x) dla x [1,20]")
plt.show()