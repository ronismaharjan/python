# functions.py

import math
from alphabets import alphabets

def paint_calc(height, width, coverage):
    number_of_cans = math.ceil((height * width) / coverage)
    print("You have to buy " + str(number_of_cans) + " cans.")

def prime_num_checker(number):
    count = 0
    divisible_number = []
    for num in range(2, number):
        if number % num == 0:
            divisible_number.append(num)
            count += 1
    
    if count < 1:
        print("The number " + str(number) + " is a prime number. It is divisible by \n" + str(divisible_number))
    else:
        print("The number " + str(number) + " is not a prime number. It is divisible by \n" + str(divisible_number))

def caesar(text, shift, direction):
    end_text = ""
    for letter in text:
        index = alphabets.index(letter)
        if(direction == "encode"):
            end_text += alphabets[(index + shift)]
        elif(direction == "decode"):
            end_text += alphabets[(index - shift)]
    print("The " + direction +" text is : " + end_text)