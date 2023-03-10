

a = eval(input("Please, enter the number a, a = "))
def monotonicznosc(a):

    if(a > 0):
      return "Funkcja jest rosnaca"
    elif(a < 0):
       return "Funkcja jest malejąca"
    else:
        return "Funkcja jest stala"
print(monotonicznosc(a))