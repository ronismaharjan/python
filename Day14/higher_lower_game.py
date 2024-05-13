from art import logo, vs_icon
from game_data import data
import random 

def format_data(account):
    """Formate the data for the game"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return (f"{account_name}, a {account_desc}, from {account_country}") 

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#Score keeping
score = 0
game_should_continue = True

#Generate random data
account_b = random.choice(data)

#Make the game repeatable
while game_should_continue:
    #Display the art
    print(logo)
    
#Making the account at B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b == random.choice(data)

    #Format account data.
    print(f"Compare A:{format_data(account_a)}")
    print(vs_icon)
    print(f"Against B:{format_data(account_b)}")

    #Ask user for a guess
    user_guess = input("Who has the more followers: ").lower()

    #Check if user is correct

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    #Use if else statement to check if user is correct
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    #Give user feedback on their game
    if is_correct:

        score += 1
        print(f"you are right and your score is {score}")
    else:
        print(f"You are wrong and your score is {score}")
        game_should_continue = False






