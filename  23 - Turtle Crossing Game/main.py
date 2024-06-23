import random
import time
from turtle import Screen

from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move_forwards,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car() 

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > player.finish_line_y:
        player.goto(player.starting_position)
        score.update_level()
        car_manager.update_car_speed()

screen.exitonclick()