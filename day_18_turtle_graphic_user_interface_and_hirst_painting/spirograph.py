from turtle import Turtle, Screen
import random
import turtle
turtle.colormode(255)

tim = Turtle()
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(angle_shift):
    for _ in range(int(360/angle_shift)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(angle_shift)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()