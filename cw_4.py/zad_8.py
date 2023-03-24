import numpy as np
n = eval(input("Please, enter the size of matrix:  "))
matrix = np.zeros((n , n))
direction = eval(input("Please, enter vertical - 1 or horizontal - 2 direction: "))
def foo8(matrix, direction):

    if direction == 1:
        if n % 2 != 0:
            print("Quantity does not allow operations!")
        return np.vsplit(matrix, n/2)
    elif direction == 2:
        if n % 2 != 0:
            print("Quantity does not allow operations!")
        return np.hsplit(matrix, n/2)
    else:
        print("The direction is not correct, please enter vertical or horizontal!")

print(foo8(matrix, direction))