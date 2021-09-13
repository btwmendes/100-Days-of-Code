'''Phase 1: Extract the colors from your image and save it to a list in the (r,g,b) format.'''
# import colorgram
# # how to import new modules in pycharm
# # https://stackoverflow.com/questions/65634925/i-keep-getting-this-error-for-the-colorgram-module-in-python
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(0, 0, 0),
              (231, 153, 82), (119, 171, 203), (39, 110, 159), (240, 200, 80), (160, 59, 83), (200, 83, 111),
              (215, 132, 159), (23, 137, 102), (223, 83, 61), (119, 189, 154), (158, 164, 48), (188, 212, 222),
              (244, 156, 174), (47, 171, 134), (230, 197, 214), (28, 164, 194), (197, 221, 212), (161, 74, 52),
              (9, 102, 78), (242, 164, 153), (115, 43, 56), (108, 115, 171), (151, 214, 194), (148, 208, 225),
              (178, 181, 215), (42, 60, 103), (110, 46, 44), (34, 66, 83)]

'''Phase 2: Use the turtle module to create the art piece.'''
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()

start_x = -200
start_y = -200
tim.setposition(start_x, start_y)

for row in range(10):

    for moves in range(10):
        # print(tim.position())
        dot_color = random.choice(color_list)
        tim.dot(20, dot_color)
        tim.forward(50)
    start_y += 50
    tim.setposition(start_x, start_y)

screen.exitonclick()
