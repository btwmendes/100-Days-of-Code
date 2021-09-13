import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



tim.pensize(10)
tim.speed(10)
directions = [0, 90, 180, 270]

def random_walk(num_of_moves):
    for i in range(num_of_moves):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(30)


random_walk(100)

screen = Screen()
screen.exitonclick()

