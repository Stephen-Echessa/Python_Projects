import colorgram
from turtle import Turtle,Screen
import random

colors = colorgram.extract('hirst spots.jpeg', 25)
rgb_list = []
y = -225
x = -225

turtle = Turtle()
screen = Screen()

turtle.speed("fastest")
screen.colormode(255)

turtle.penup()
turtle.hideturtle()
turtle.goto(x, y)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_list.append(new_color)

print(rgb_list)

for vertical in range(10):
    for horizontal in range(10):
        turtle.begin_fill()
        turtle.dot(28)
        random_color = random.choice(rgb_list)
        turtle.color(random_color)
        turtle.end_fill()

        turtle.forward(49)

    y += 50
    turtle.goto(x, y)

screen.exitonclick()

