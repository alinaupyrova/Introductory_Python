first case :
new_var = input("Please, enter some text :")
print(new_var.count(" "))

second case:
word = input("Please, enter the some words")
counter = 0
for i in range (word.__len__()):
    if word[i] == ' ':
       counter += 1

print(counter)
