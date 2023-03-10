

a_1 = eval(input("Podaj liczbe a dla pierwszej prostej : a_1 = "))
a_2 = eval(input("Podaj liczbe a dla drugiej prostej : a_2 = "))

def rownoległe_czy_prostopadłe(a_1, a_2):
    if(a_1 == a_2):
        return "Równolegle"
    elif(a_1 * a_2 == -1):
        return "Prostopadłe"
    else:
        return "Dwie proste a nie rownolegle, a nie prostopadle"

print(rownoległe_czy_prostopadłe(a_1, a_2))

