from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()

screen.listen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.score_update()
        snake.extend()

    #Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()