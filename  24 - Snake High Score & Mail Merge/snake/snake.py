from turtle import Turtle

class Snake():
    def __init__(self):
        self.starting_positions = [(0,0),(-20,0),(-40,0)]
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in self.starting_positions:
            self.add_segment(pos)

    def add_segment(self,pos):
        turtle = Turtle()
        turtle.shape("square")
        turtle.shapesize(1)
        turtle.color("white")
        turtle.penup()
        turtle.goto(pos)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def move(self): 
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x,y)

        self.segments[0].forward(20) 

    def up(self):
        if self.segments[0].heading()!=270: 
            self.segments[0].setheading(90)
        
    def down(self):
        if self.segments[0].heading()!=90: 
            self.segments[0].setheading(270)
        
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading()!=180: 
            self.segments[0].setheading(0)
        