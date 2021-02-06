from turtle import Turtle
PADDLE_LENGTH = 3


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=PADDLE_LENGTH)
        self.color('white')
        self.goto(x_pos, 0)

    def up(self):
        if self.ycor() < 270:
            self.forward(20)

    def down(self):
        if self.ycor() > -270:
            self.backward(20)
