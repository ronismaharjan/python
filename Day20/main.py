from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
# Creating the snake and snake segment attach to each other


snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
game_is_on = True
while game_is_on:
    scoreboard.write_score()
    screen.update()
    time.sleep(0.1)
    snake.move()
# Collision detect
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.score += 1
        snake.add_segment()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake_segments[:0:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
