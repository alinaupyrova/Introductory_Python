
def print_A(size):
    if size < 3:
        print("Wielkość musi być większa niż 2.")
        return

    for i in range(size):
        if i == 0:
            print(" " * (size - 1) + "*")
        elif i == 1:
            print(" " * (size - 2) + "* " + "*")
        elif i == 2:
            print(" " * (size - 3) + "*" * (3 * i - 1))
        else:
            print(" " * (size - i-1) + "*" + " " * (2 * i - 1) + "*")

size = int(input("Podaj wielkość litery A: "))
print_A(size)