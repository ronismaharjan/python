import turtle as tu
import random
t = tu.Turtle()
tu.colormode(255)
direction = [0, 90, 180, 270]


def random_walk(num_of_walks):

    t.pensize(10)
    for _ in range(num_of_walks):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.forward(20)
        t.setheading(random.choice(direction))
        t.color(r, g, b)
        t.speed(10)


random_walk(500)

screen = tu.Screen()
screen.exitonclick()
