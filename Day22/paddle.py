from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.initial_x_cor = position[0]
        self.initial_y_cor = position[1]
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x=self.initial_x_cor, y=self.initial_y_cor)

    def go_up(self):
        new_ypos = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_ypos)

    def go_down(self):
        new_ypos = self.ycor() - 30
        self.goto(self.xcor(), y=new_ypos)
