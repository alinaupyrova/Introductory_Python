lista = ["apple", "orange", "banana"]

def dodaj_znak(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].replace(lista[i], lista[i] + "!")
    return lista
