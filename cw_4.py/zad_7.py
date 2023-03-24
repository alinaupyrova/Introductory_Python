import numpy as np

n = eval(input("Please, enter the size of your matrix: "))


def foo7(n):
    matrix = np.zeros((n, n), dtype = int)
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 2
            elif i+j == n-1:
                matrix[i][j] = 6
            elif i+j == n or n-2:
                matrix[i][j] = 4
    print(matrix)
foo7(n)
