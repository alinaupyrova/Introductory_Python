import numpy as np

c = np.array([np.arange(3),np.arange(3),np.arange(3)])
print(c)
print("Elements : ")
for element in c.flat:
    print(element)
