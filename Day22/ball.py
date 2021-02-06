from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('purple')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.setheading(random.choice([10, 20, 30, 150, 160, 170, 190, 200, 210, 220, -10, -20, -30]))

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        heading = self.heading() #between 0 and 360
        if heading > 180:
            heading -= 360
        self.setheading(-heading)
        self.forward(10)

    def bounce_paddle(self):
        heading = self.heading()  # between 0 and 360
        self.setheading(180 - heading)
        self.forward(10)

    def refresh(self):
        self.goto(0, 0)
        self.setheading(random.choice([10, 20, 30, 150, 160, 170, 190, 200, 210, 220, -10, -20, -30]))