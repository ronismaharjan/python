# #Taking input from the user.
# year = int(input("Which year do you want to check: "))

# #Logic for checking the given year is leap or not.
# if year % 4 ==0:
#     if year % 100 ==0:
#         if year % 400 == 0:
#             print("It's a leap year")
#         else: 
#             print("It's not a leap year")
#     else:
#         print("It's a leap year")        
# else:
#     print("Not leap year")


#Fizz_Buzz debug
for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    else:
        if number % 3 == 0: 
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    
    
    
