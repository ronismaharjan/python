userWeight = float(input("Enter your weight: "))
userHeight = float(input("Enter your Height: "))

userBmi = round((userWeight/userHeight ** 2), 2)

if(userBmi < 18.5):
    print("Your BMI is " + str(userBmi) +" You are underweight.")
elif(userBmi < 25):
    print("Your BMI is " + str(userBmi) + " You have normal weight.")
elif(userBmi < 30):
    print("Your BMI is " + str(userBmi) + " You are overweight.")
elif(userBmi < 35):
    print("Your BMI is " + str(userBmi) + " You are obese.")
else:
    print("Your BMI is " + str(userBmi) +" You are clinically obese.")

    
