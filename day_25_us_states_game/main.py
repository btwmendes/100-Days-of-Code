import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# def get_mouse(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse)
# turtle.mainloop()

data = pd.read_csv("./50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another State's name?").title()
    if answer_state == "Exit":
        break
    state_lst = list(data.state)
    if answer_state in state_lst:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto((int(state_data['x']), int(state_data['y'])))
        t.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        # print(guessed_states)

learn_lst = [state for state in state_lst if state not in guessed_states]
# print(learn_lst)

for state in learn_lst:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data['state'] == state]
    t.goto((int(state_data['x']), int(state_data['y'])))
    t.pencolor("red")
    t.write(state)

new_data = pd.DataFrame(learn_lst)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()