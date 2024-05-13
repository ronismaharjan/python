import random

#Function for choosing level of the game
def choose_level():
    attempts = 0
    level = input("Enter the Level. 'easy' or 'hard': ")

    if level == "easy":
        attempts = 10
    elif level == 'hard':
        attempts = 5
    else:
        print(f"You have entered wrong thing ")
    
    return attempts

def check_answer(guess, answer):
    if guess == answer:
        print(f"You won! The number was {number}")
        game_end = True  # Exit loop on correct guess
    else:
        if answer < guess:
            print("Your guess is higher.")
        else:
            print("Your guess is lower.")

#The game logic and function
def game():
    user_attempts = choose_level()
    number = random.randint(1, 100)
    game_end = False
    while user_attempts !=0 and not game_end :  # Loop runs only if attempts are left
        print(f"You have {user_attempts} attempts left.")
        user_guess = int(input("Guess the number: "))
        check_answer(user_guess, number)
        user_attempts -= 1

    if user_attempts == 0:
        print(f"You ran out of guesses. The number was {number}")
        



game()


