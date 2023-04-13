import numpy as np

def function(length_of_vector):
    arr = np.arange(length_of_vector, 0, -1)
    diagonal = np.diag([i for i in arr], 0)
    print(diagonal)
    function(4)
    
    np.arange([start, ]stop, [step, ]dtype=None)
    
    import numpy as np
    n = int(input("n = "))
    def foo(n):

    wec = np.arange(n, 0, -1)
    diagonal = np.diag(wec)
    print(diagonal)
print(foo(n))
