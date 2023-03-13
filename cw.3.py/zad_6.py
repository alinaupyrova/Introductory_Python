
import random

def guess_the_number(number):
    skore = 0
    random_number = random.randint(1, 10)
    for i in range(1, 6):
        print(input("Please, enter the number"))
        print("Random number is ", random_number)
        if(number == random_number):
            skore += 10
        elif(number != random_number):
            skore -= 1
            return skore
        print(guess_the_number(number))
