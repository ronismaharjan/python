from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=0, y=278)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}",
                   move=False, font=("Arial", 16, "normal"), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over",
                   move=False, font=("Arial", 16, "normal"), align="center")
