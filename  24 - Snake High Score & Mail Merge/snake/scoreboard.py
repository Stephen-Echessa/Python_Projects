from turtle import Turtle
FONT = ("Arial",10,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            contents = file.read()

        self.score = 0
        self.high_score = int(contents)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.goto(-30, 275)
        self.write(f"Score: {self.score} High Score: {self.high_score}", "center")

    def reset_score(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(-45,0)
    #     self.write("GAME OVER","center",font=FONT)

    def score_update(self):
        self.clear()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.score_update()
