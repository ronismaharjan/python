import turtle
import pandas
from my_obj import State

# Create a screen
screen = turtle.Screen()
screen.title("U.S Game")

# # Load the image
image_path = "Day25/project_day25/blank_states_img.gif"
screen.addshape(image_path)

# # Create a turtle and set its shape to the loaded image
turtle.shape(image_path)

# Importing the data form the csv file 
data = pandas.read_csv("Day25/project_day25/50_states.csv")

# Variables for guess game
all_states = (data["state"]).to_list()
user_correct_answer =[]
guessed = 0

# GameLoop
is_game_on = True
while is_game_on:
    user_guess = screen.textinput(title = f'{guessed}/{len(all_states)}', prompt="whats the state name").capitalize()
    if user_guess not in user_correct_answer:
        if user_guess in all_states:     
            state_data= data[data.state == user_guess]
            t = State(state_data, user_guess)
            user_correct_answer.append(user_guess)
            guessed += 1

    if len(user_correct_answer) == len(all_states) or user_guess =="Exit":
        is_game_on=False
        print("close")

if not is_game_on:
    # Checking for remaining states
    remained_state =[]
    for index in range(len(all_states)):
        if all_states[index] not in user_correct_answer:
            remained_state.append(all_states[index])
        
    remaining_state_dict = {
        "states":remained_state
    }

    # Creating the dataframe of remaining states 
    remaining_state_data_frame = pandas.DataFrame(remaining_state_dict)
    
    # Creating a csv file named "states_to_learn.csc"
    remaining_state_data_frame.to_csv("Day25\project_day25\states_to_learn.csv")
        
    







screen.exitonclick()
# Exit when the screen is clicked
# screen.exitonclick()
