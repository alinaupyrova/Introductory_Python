h = int(input("Please, enter the height (3, 9): "))
if h < 3 and h > 9:
    h = int(input("Please, enter again the height (3, 9): "))
for i in range(1, h + 1, 2):
    print(" " * ((h - i) // 2) + "o" * i)
for i in range(h-2, 0, -2):
    print(" " * ((h - i) // 2) + "o" * i)

