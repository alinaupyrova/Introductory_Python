import numpy as np

first_matrix = np.random.randint(low=10, high=50, size=(3,3))
second_matrix = np.random.randint(low=10, high=50, size=(4,4))

print("First_matrix : ", first_matrix)
print("Second_matrix : ", second_matrix)
print ("Description of first matrix : ")
for i in range (3):
    print("Min number in row", i, "is", np.min(first_matrix[i]))
for j in range (3):
    print("Min number in column ", j, "is", np.min(first_matrix[:, j]))

print("Description of second matrix : ")

for i in range (4):
    print("Min number in row", i, "is", np.min(second_matrix[i]))
for j in range (4):
    print("Min number in column ", j, "is", np.min(second_matrix[:, j]))