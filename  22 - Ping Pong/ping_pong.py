import time
from  turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Scoreboard

R_COORDINATES = (350,0)
L_COORDINATES = (-350,0)

screen = Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

l_paddle = Paddle(L_COORDINATES)
r_paddle = Paddle(R_COORDINATES)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "i")
screen.onkey(r_paddle.move_down, "k")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when paddle misses
    if ball.xcor() > 380:
        ball.restart()
        score.l_point()

    if ball.xcor() < -380:
        ball.restart()
        score.r_point()

screen.exitonclick()