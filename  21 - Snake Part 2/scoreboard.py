from turtle import Turtle
FONT = ("Arial",10,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.goto(-30,275)
        self.write("Score: ","center")
        self.write(self.score)

    def game_over(self):
        self.goto(-45,0)
        self.write("GAME OVER","center",font=FONT)

    def score_update(self):
        self.clear()
        self.score += 1
        self.write_score()
