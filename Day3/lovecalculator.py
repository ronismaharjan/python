print("Welcome to Love Calculator.")
name1 = str(input("Enter first name: ")).lower()
name2 = str(input("Enter Second Person Name: ")).lower()


letter_T = name1.count("t") + name2.count("t")
letter_R = name1.count("r") + name2.count("r")
letter_U = name1.count("u") + name2.count("u")
letter_E = name1.count("e") + name2.count("e")

# Total number of same letter for "true"
Total_For_True = str(letter_T + letter_R + letter_U + letter_E)
letter_L = name1.count("l") + name2.count("l")
letter_O = name1.count("o") + name2.count("o")
letter_V = name1.count("v") + name2.count("v")

#total  repeated number of  letter for "love"
Total_For_Love = str(letter_L + letter_O + letter_V + letter_E)

# final score
Total_Score_IN_TrueLove = int(Total_For_True + Total_For_Love)



if(Total_Score_IN_TrueLove < 10 or  Total_Score_IN_TrueLove > 90):
    print("your score is " + str(Total_Score_IN_TrueLove) + " you go together like coke and mentos.")

elif(Total_Score_IN_TrueLove > 40 and Total_Score_IN_TrueLove < 50):
    print("your score is " + str(Total_Score_IN_TrueLove) + " you are alright together.")
else:
    print("your score is " + str(Total_Score_IN_TrueLove) + " .")





