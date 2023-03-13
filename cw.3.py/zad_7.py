number = eval(input("Please, enter the positive number for calculating digital root, n = "))

def digital_root(number):
    sum = 0
    while number > 0:
         m = number % 10
         sum += m
         number //= 10

    return sum

print(digital_root(number))