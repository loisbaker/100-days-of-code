from turtle import Turtle

class Net:
    def __init__(self):
        # First draw the central net
        net = Turtle()
        net.penup()
        net.hideturtle()
        net.color('white')
        net.goto(0, -290)
        net.pensize(4)
        net.setheading(90)
        while net.ycor() < 300:
            net.pendown()
            net.forward(20)
            net.penup()
            net.forward(20)
