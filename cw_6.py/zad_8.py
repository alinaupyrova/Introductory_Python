import numpy as np

c=np.array([np.arange(3),np.arange(3),np.arange(3)])
print(c)
for i in range(3):
    print("Row", i + 1, ":", c[i])


