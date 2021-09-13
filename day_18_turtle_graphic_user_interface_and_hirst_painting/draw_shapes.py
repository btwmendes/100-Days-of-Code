# draw shapes
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
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

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(color_lst))
    draw_shape((shape_side_n))


screen = Screen()
screen.exitonclick()