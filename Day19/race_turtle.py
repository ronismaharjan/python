from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)

color = ["red", "orange", "yellow", "blue", "green", "purple"]
turtle_lists = []
turtle_positions = [0, 30, 60, 90, -30, -60]


def create_turtle():
    for index in range(len(color)):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.color(color[index])
        new_turtle.goto(x=-230, y=turtle_positions[index])
        turtle_lists.append(new_turtle)


winner = ""
is_race_on = False
create_turtle()
user_bet = ""
while user_bet not in color:
    user_bet = screen.textinput(title="Make Your Bet",
                                prompt="Which color turtle will win the race").lower()
is_race_on = True

while is_race_on:

    for racer in turtle_lists:
        if racer.xcor() >= 230:
            is_race_on = False
            winner = racer.color()[0]
        else:
            random_step = random.randint(0, 10)
            racer.forward(random_step)


if user_bet == winner:
    print(f"you win the bet.The winner is {winner} turtle.")
else:
    print(f"You loose. The winner is {winner} turtle.")
screen.exitonclick()
