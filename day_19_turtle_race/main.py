'''Turtle Race'''
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_spot = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for i, color in enumerate(colors):
    name = Turtle(shape='turtle')
    name.penup()
    name.color(color)
    y_start = starting_spot[i]
    name.goto(x=-230, y=y_start)
    all_turtles.append(name)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
