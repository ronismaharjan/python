import colorgram
import turtle as t
import random

t.colormode(255)
colors_classes = colorgram.extract(
    r"C:\Users\Home\Desktop\python\Day18\image.png", 30)


def picking_color():
    color_list_classes = []
    for color_class in colors_classes:
        r = color_class.rgb.r
        g = color_class.rgb.g
        b = color_class.rgb.b
        generated_color = (r, g, b)
        color_list_classes.append(generated_color)

    return random.choice(color_list_classes)
    # return generated_color


timmi = t.Turtle()
timmi.setheading(225)
timmi.penup()
timmi.forward(300)
timmi.setheading(0)
timmi.speed("fastest")

for _ in range(10):
    for _ in range(10):
        timmi.showturtle()
        color = picking_color()
        previous_color = color
        if color == previous_color:
            color = picking_color()

        timmi.dot(20, *color)
        timmi.forward(50)
    timmi.hideturtle()
    timmi.left(90)
    timmi.forward(50)
    timmi.left(90)
    timmi.forward(50*10)
    timmi.setheading(0)


screen = t.Screen()
screen.exitonclick()
