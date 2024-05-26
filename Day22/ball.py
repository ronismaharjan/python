from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slow")
        self.move_x = 10
        self.move_y = 10

    def move_ball(self):
        new_xcor = self.xcor() + self.move_x
        new_ycor = self.ycor() + self.move_y
        self.goto(x=new_xcor, y=new_ycor)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
