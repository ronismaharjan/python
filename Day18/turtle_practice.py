from turtle import Turtle, Screen
my_turtle = Turtle()
my_turtle.color("red")


# def draw_square():
#     for _ in range(4):
#         my_turtle.forward(100)
#         my_turtle.right(90)
for _ in range(15):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()


my_screen = Screen()

my_screen.exitonclick()
