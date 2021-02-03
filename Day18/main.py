import random
from turtle import Turtle, Screen
import colorgram

turtle = Turtle()
screen = Screen()
color_objects = colorgram.extract('hirst_image.jpg', 20)[5:]

spots_x = 10
spots_y = 20
screen.colormode(255)
turtle. speed(5)
turtle.penup()
for i in range(spots_y):
    for j in range(spots_x):
        color = random.choice(color_objects).rgb
        turtle.dot(10, color)
        turtle.forward(20)
    turtle.backward(20*spots_x)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)


#screen.exitonclick()