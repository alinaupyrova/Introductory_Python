import numpy as np

def function(length_of_vector):
    arr = np.arange(length_of_vector, 0, -1)
    diagonal = np.diag([i for i in arr], 0)
    print(diagonal)
    function(4)