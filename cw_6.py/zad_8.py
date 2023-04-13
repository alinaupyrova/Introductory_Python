import numpy as np

c=np.array([np.arange(3),np.arange(3),np.arange(3)])
print(c)
for i in range(3):
    print("Row", i + 1, ":", c[i])

    or 
    
    
mat = np.arange(9).reshape(3,3)
print(mat)
for i in range(3):
    print(mat[i])

