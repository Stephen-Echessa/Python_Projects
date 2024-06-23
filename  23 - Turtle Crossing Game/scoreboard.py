from turtle import Turtle

FONT = ("Courier",18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

        self.hideturtle()
        self.penup()
        self.write_level()

    def write_level(self):
        self.goto(-240,270)
        self.write(f"Level: {self.level}",align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write_level()