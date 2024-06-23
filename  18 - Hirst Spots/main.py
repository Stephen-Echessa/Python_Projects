from random import choice, randint
from turtle import Turtle,Screen, colormode

turtle_oniichan = Turtle()

def r():
    r = randint(0,255)
    return r

def g():
    g = randint(0,255)
    return g

def b():
    b = randint(0,255)
    return b

size_of_gap = 5

turtle_oniichan.speed("fastest")
turtle_oniichan.pensize(2)

for _ in range(int(360/size_of_gap)):
    red = r()
    green = g()
    blue = b()
    colormode(255)
    turtle_oniichan.color(red,green,blue)

    turtle_oniichan.circle(100)
    turtle_oniichan.setheading(turtle_oniichan.heading() + size_of_gap)

screen = Screen()
screen.exitonclick()