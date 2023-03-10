lista = ["apple", "orange", "banana"]

def dodaj_znak(lista):
    for i in range(len(lista)):
        lista[i] += "!"
    return lista

print(dodaj_znak(lista)) 