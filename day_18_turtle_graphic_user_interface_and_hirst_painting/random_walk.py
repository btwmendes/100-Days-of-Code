from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(10)
tim.speed(10)

color_lst = ['chartreuse4',
             'red',
             'blue',
             'orange',
             'green',
             'gold',
             'purple',
             'DarkBlue',
             'IndianRed4',
             'DarkOrchid4']

directions = [0, 90, 180, 270]

def random_walk(num_of_moves):
    for i in range(num_of_moves):
        tim.color(random.choice(color_lst))
        tim.setheading(random.choice(directions))
        tim.forward(30)


random_walk(100)

screen = Screen()
screen.exitonclick()

