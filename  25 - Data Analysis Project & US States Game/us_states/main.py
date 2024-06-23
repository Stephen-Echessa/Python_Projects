import turtle
import pandas

screen = turtle.Screen()
df = pandas.DataFrame()

image = "blank_states_img.gif"
screen.title("US_States_Game")
screen.addshape(image)
turtle.shape(image)

correct_states_list = []
number_of_correct_guesses = 0

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

while len(correct_states_list) < 50:
    answer_state_input = screen.textinput(title=f"{number_of_correct_guesses}/50", prompt="Whats another state's name? ")
    answer_state = answer_state_input.title()

    if answer_state == "Exit":
        break

    if answer_state in states and answer_state not in correct_states_list:
        correct_states_list.append(answer_state)
        print(correct_states_list)

        correct_x_coor = int(data[data.state == answer_state].x)
        correct_y_coor = int(data[data.state == answer_state].y)

        states_turtle = turtle.Turtle()
        states_turtle.hideturtle()
        states_turtle.penup()
        states_turtle.goto(correct_x_coor, correct_y_coor)
        states_turtle.write(answer_state)

        number_of_correct_guesses += 1

states_to_learn_list = []
for state in states:
    if state not in correct_states_list:
        states_to_learn_list.append(state)

states_to_learn = pandas.DataFrame(states_to_learn_list)
states_to_learn.to_csv("states_to_learn.csv")

