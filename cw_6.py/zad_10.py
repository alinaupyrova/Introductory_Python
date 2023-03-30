import numpy as np

matrix = np.arange(81).reshape(9, 9)
print("Matrix 3 * 3 : \n", matrix)

matrix2 = matrix.reshape(3, 27)
print("Matrix 3 * 27 : \n ", matrix2)

matrix3 = matrix.reshape(27, 3)
print("Matrix 27 * 3 : \n " , matrix3)