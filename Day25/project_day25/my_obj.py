from turtle import Turtle
class State(Turtle):
    def __init__(self,state_data, state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(10)
        self.setposition(int(state_data.x), int(state_data.y))
        self.write(state)

