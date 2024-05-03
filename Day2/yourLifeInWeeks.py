userAge = int(input("Enter your age: "))
userRemainingAge = 90 - userAge

userRemainingAgeInDays = userRemainingAge * 365 
userRemainingAgeInWeeks = userRemainingAge * 52
userRemainingAgeInMonths = userRemainingAge * 12

print("Welcome to Remaining Age calculator in weeks days and months until you reached 90 years")
print("you have " + str(userRemainingAgeInDays)+ " days, " + str(userRemainingAgeInWeeks) + " weeks, and "+ str(userRemainingAgeInMonths) + " months left")
