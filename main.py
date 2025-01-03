import  turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

correct_answers = []
state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()

while len(correct_answers) < 50:
    answer_state = (
        screen.textinput(title=f"{len(correct_answers)}/50 States Correct:", prompt="What's another state's name?")).title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in correct_answers]
        states_to_learn_data = pandas.DataFrame(states_to_learn)
        states_to_learn_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in correct_answers:
        state_row = data[data.state == answer_state]
        state_index = state_row.index[0]
        state_turtle.goto(state_row['x'][state_index], state_row['y'][state_index])
        # state_turtle.goto(state_row['x'].item(), state_row['y'].item()) // easier way to get value
        state_turtle.write(answer_state, align="center", font=("Courier", 8, "normal"))
        correct_answers.append(answer_state)





# turtle.mainloop()
# Code for getting coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
