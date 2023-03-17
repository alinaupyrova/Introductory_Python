import numpy as np

def potegowanie(a, n):
    powers = np.logspace(1, n, num=n, base=a, dtype="int64")
    return powers
a = eval(input("Please, enter the number n = "))
n = eval(input("Please, enter the number k = "))

print(potegowanie(a, n))
