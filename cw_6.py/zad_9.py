import numpy as np

c = np.array([np.arange(3),np.arange(3),np.arange(3)])
print(c)
print("Elements : ")
for element in c.flat:
    print(element)
    
 or 
mat = np.arange(9).reshape(3,3)
for i in range(9):
    print(mat.flatten()[i])
