import math

a1 = eval(input("Please, enter the first term  of arithmetic sequence : a1 =  "))
r = eval(input("Please, enter the common difference:  r = "))
numberOfElements = eval(input("Please, enter the number of elements : "))
def sumaOfArithmeticSequence(a1, r, numberOfElements):
    sum = (2 * a1 + r * (numberOfElements - 1)/ 2) * numberOfElements
    return sum
print(sumaOfArithmeticSequence(a1, r, numberOfElements))

