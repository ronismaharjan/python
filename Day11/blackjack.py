import random 
from art import logo


#Function to deal the card 
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    

    return sum(cards)

def compare(user_score, computer_score):
    if user_score  == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you loose"
    elif user_score == 0:
        return "you win"
    elif user_score > 21:
        return "loose"
    elif computer_score > 21 :
        return "you win"
    elif user_score > computer_score:
        return "you win"
    else: 
        return "you loose"


def play_game():
    
    #Variales of games
    computer_card = []
    player_card = []
    is_game_over = False
    
    print(logo)
    for num in range(2):
        computer_card.append(deal_card())
        player_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {player_card}, current score: {user_score}")
        print(f"computer first card: {computer_card[0]}")

        if computer_score == 0 or user_score ==0 or user_score > 21:
            is_game_over = True
        else:
            should_draw = input("Do you want to draw another card: ").lower()
            if should_draw == "y":
                player_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"your card {player_card} your score is {user_score}")
    print(f"computer card {computer_card} your score is {computer_score}")
    print(compare(user_score, computer_score))
  


while input("Do you want to continue 'y' or 'n': ").lower() == "y":
    play_game()