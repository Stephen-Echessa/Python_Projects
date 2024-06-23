from random import randint
from turtle import Turtle,Screen
import turtle

is_race_on = False
all_turtles = []
screen = Screen()
screen.setup(width=600,height=600)
user_input = screen.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter a colour: ")
colors = ["blue","red","yellow","purple","black","green"]
height = -150

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    height += 50
    turtle.goto(x=-250,y=height)
    all_turtles.append(turtle) 

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:   
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            
            is_race_on = False 

        rand_distance = randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()