import math

a = eval(input("Podaj dlugosc jednego boku trojkata prostokatnego: a = "))
b = eval(input("Podaj dlugosc jednego boku trojkata prostokatnego: b = "))


def długość_przeciwprostokątnej(a, b):
    c = math.sqrt(a * a + b * b)
    return c
    print(długość_przeciwprostokątnej(a,b))
