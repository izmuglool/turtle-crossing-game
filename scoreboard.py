from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-240, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="Center", font=("Courier", 15, ""))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="Center", font=("Courier", 20, ""))