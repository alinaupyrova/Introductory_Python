h = int(input("Please, enter the height of your diamond, h =  "))
if h < 3 or h > 9:
    h = input("Please, enter the height again, h = ")
for i in h:
    for j in h - 1:
        if h == 2:
            print("o")

