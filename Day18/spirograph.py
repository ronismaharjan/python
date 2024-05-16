import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        current_color = random_color()
        tim.color(current_color)
        tim.circle(50)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
