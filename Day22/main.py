from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.go_up)
    screen.onkey(key="Down", fun=r_paddle.go_down)
    screen.onkey(key="w", fun=l_paddle.go_up)
    screen.onkey(key="s", fun=l_paddle.go_down)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()


screen.exitonclick()
