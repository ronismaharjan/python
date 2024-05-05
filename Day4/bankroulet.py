
import random
usersName = input("Enter the names and separate by comma: ")

userNameLists = usersName.split(", ")
print(userNameLists)

guess = random.randint(0, 4)

print(usersNameLists[guess])