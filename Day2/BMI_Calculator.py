heightInMeter =float(input('Enter your height in meter: '))
weightInKg = float(input("Enter your weight in kg: "))

# function to calculate bmi
bmi = int(weightInKg/heightInMeter ** 2)

print("Your BMI is: " + str(bmi))