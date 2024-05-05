import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '@', '$', "^", "&", "*", "(", ")", "+"]

total_letters =int(input("How many letters do you want? \n"))
total_numbers  = int(input("How many numbers? \n"))
total_symbols = int(input("How many symbols? \n"))
import random
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '@', '$', "^", "&", "*", "(", ")", "+"]

total_letters = int(input("How many letters do you want? \n"))
total_numbers  = int(input("How many numbers? \n"))
total_symbols = int(input("How many symbols? \n"))

website = input("Enter website name: \n")
generatedPasswordChar = []
password =''

for letter in range(0, total_letters):
    generatedPasswordChar.append(random.choice(character))
for symbol in range(0, total_symbols):
    generatedPasswordChar.append(random.choice(symbols))
for number in range(0, total_numbers):
    generatedPasswordChar.append(random.choice(numbers))


random.shuffle(generatedPasswordChar)

for character in generatedPasswordChar:
    password += character


print(password)