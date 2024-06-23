from turtle import Turtle,Screen

turtle = Turtle()

turtle.setheading(turtle.heading() + 90)
turtle.forward(30)
if turtle.heading() == 90:
    turtle.setheading(turtle.heading() + 90)
else:
    turtle.forward(30)

screen = Screen()

screen.exitonclick()