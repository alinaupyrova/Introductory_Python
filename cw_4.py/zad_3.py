import numpy as np
def arr_create(n):
    arr = np.arange(1, n * n + 1)
    return arr
n = int(input("Please, enter the number n = "))
arr = arr_create(n)
print("Array : ", arr)
print("Size of array is ", arr.shape)
