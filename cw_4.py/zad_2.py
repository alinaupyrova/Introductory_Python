import numpy as np
float_lista = [1.4, 3.2, 2.6]
float_lista = np.array(float_lista)
int_lista = float_lista.astype(np.int64)
print("Float array : ", float_lista)
print("Int array : ", int_lista)

OR 

lista = [1.4, 5.6, 7.9]
a = np.array(lista)
b = np.array(lista, dtype='int64')
print(a)
print(b)
