print("Welcome to the tip calculator")

# Taking the input form user 
bill = float(input("What was the total bill? "))
tipPercentage = int(input("What percentage tip would you give ? 10, 12, 15? "))
totalPeople = int(input ("How many you will split the bill: ")
)


# bill calculation function start from here
totalTipGiven = bill * tipPercentage / 100
totalBill = bill + totalTipGiven
billForEach = "{:.3f}".format(totalBill / totalPeople) you can use that #"{}".format() function to get the decimal




print("Each Person should pay " + "$" + str(billForEach))

