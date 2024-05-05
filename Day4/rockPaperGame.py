import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# Paper
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
picks =[rock, paper, scissors]

computer = random.randint(0,2)

user=int(input("What do you choose? Type 0 for rock , 1 for paper and 2 for scissors: "))

if(user > 2):
    print("You have given wrong input read first")
else:
    print("User Pick: \n" + (picks[user])) 
    print("computer choose: \n" + picks[computer])
    if((picks[user]== picks[0] and picks[computer] == picks[2]) or (picks[user]==picks[2] and picks[computer] == picks[1]) or(picks[user]==picks[1]  and picks[computer]== picks[0]) ):
        print("You Win")


    elif(picks[user]== picks[computer]):
        print("It's a Draw")


    else:
        print("You Loose")


    



