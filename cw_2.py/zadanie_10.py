h = int(input("Please, enter the height of your pyramid, h =  "))
while h > 10:
    h = input("Please, enter the height again, h = ")
a = "A"
for i in range(1, h + 1):
    print(i * a)
