lista = []
while True:
    a = input("Please, enter the number or end: ")
    if a == 'end':
        break
    elif a.isdigit():
        number = int(a)
        lista.append(number)
        print("You add the number", number)
    else:
        print("error,enter the number or end")
print(lista)
append - записує наприклад якесь значення на кінець нашої listy 
