# creating variable to store the user input
user_number = str(input("Enter a number: \n"))

# putting the index of 0 in the first number variable as well as converting its type to integer
user_firstNumber = int (user_number[0])

# putting the index of 1 in the second number variable 
user_lastNumber = int(user_number[1])

# adding both number and converting its type to str to print with string
user_numberSum = str(user_firstNumber + user_lastNumber)

# printing the output 

print("The sum of " + str(user_firstNumber)+ " and " + str(user_lastNumber) + " is " + user_numberSum )

