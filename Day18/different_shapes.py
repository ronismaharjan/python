from turtle import Turtle, Screen
import random


def draw(side):

    sides = 3
    while sides != side:
        r = random.random()
        g = random.random()
        b = random.random()
        current_angle = 360/sides
        for _ in range(sides):
            t1.color(r, g, b)
            t1.forward(100)
            t1.right(current_angle)
        sides += 1


t1 = Turtle()

draw(20)

screen = Screen()
screen.exitonclick()
