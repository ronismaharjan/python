userBodYear = int(input("Enter your date of birth year: "))
if(userBodYear % 4 == 0):
    if(userBodYear % 100 == 0):
        if(userBodYear % 400 == 0):
            print(str(userBodYear) + " is a leap year.")
        else:
             print(str(userBodYear) + " is  a not leap year.")
    else:
           print(str(userBodYear) + " is  a leap year.")
        
else:
    print(str(userBodYear) + " is not a leap year.")
