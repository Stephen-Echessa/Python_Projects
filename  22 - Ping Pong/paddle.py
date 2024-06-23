from mimetypes import init
from  turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.create_paddle(coordinates)

    def create_paddle(self, coordinates):
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.setpos(coordinates)

    def move_up(self):
        new_pos = self.pos() + (0,20)
        self.goto(new_pos)

    def move_down(self):
        new_pos = self.pos() - (0,20)
        self.goto(new_pos)
