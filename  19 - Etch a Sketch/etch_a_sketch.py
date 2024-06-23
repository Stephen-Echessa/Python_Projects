from turtle import Turtle,Screen

turtle_oniichan = Turtle()

def move_forwards():
    return turtle_oniichan.forward(10)

def move_backwards():
    return turtle_oniichan.backward(10)

def counter_clockwise():
    return turtle_oniichan.left(10)

def clockwise():
    return turtle_oniichan.right(10)

def clear():
    turtle_oniichan.home()
    return turtle_oniichan.clear()

screen = Screen()
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()