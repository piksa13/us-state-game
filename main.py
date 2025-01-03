import  turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

game_is_on = True
correct_answers = []
score = 0
state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()

answer_state = (screen.textinput(title="Guess the State:", prompt="What's another state's name?")).title()
while game_is_on:
    if answer_state in states_list:
        state_row = data[data.state == answer_state]
        state_index = state_row.index[0]
        state_turtle.goto(state_row['x'][state_index], state_row['y'][state_index])
        # state_turtle.goto(state_row['x'].item(), state_row['y'].item()) // easier way to get value
        state_turtle.write(answer_state, align="center", font=("Courier", 8, "normal"))
        correct_answers.append(answer_state)
        score += 1
        if score == 50:
            game_is_on = False
    answer_state = (
        screen.textinput(title=f"{score}/50 States Correct:", prompt="What's another state's name?")).title()



turtle.mainloop()

# Code for getting coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
