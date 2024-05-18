from turtle import Turtle, Screen
# Creating a snake class
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:
    def __init__(self):

        self.snake_segments = []
        self.snake_x_cordinate = 0
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for _ in range(3):
            new_snake_segment = Turtle(shape="square")
            new_snake_segment.color("white")
            new_snake_segment.penup()
            new_snake_segment.speed("fastest")
            new_snake_segment.goto(x=self.snake_x_cordinate, y=0)
            self.snake_x_cordinate -= 20
            self.snake_segments.append(new_snake_segment)

    def move(self):

        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_num-1].xcor()
            new_y = self.snake_segments[segment_num-1].ycor()
            self.snake_segments[segment_num].goto(new_x, new_y)

        self.head.forward(20)

    def add_segment(self):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        new_snake_segment.speed("fastest")
        new_x = self.snake_segments[-1].xcor()
        new_y = self.snake_segments[-1].ycor()
        new_snake_segment.goto(x=new_x, y=new_y)

        self.snake_segments.append(new_snake_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
