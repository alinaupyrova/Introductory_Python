import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def rzucaj(n):
    suma = []
    for i in range(n):
        rzut1 = np.random.randint(1, 7)
        rzut2 = np.random.randint(1, 7)
        suma.append(rzut1 + rzut2)
    plt.hist(suma, bins=range(2, 14), align='left', rwidth=0.8)
    plt.xlabel("Suma wyników")
    plt.ylabel("Liczba wystąpień")
    plt.title("Histogram sumy rzutów dwiema kostkami sześciennymi")
    plt.show()
    return suma

rzucaj(6)