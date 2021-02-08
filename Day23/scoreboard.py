from turtle import Turtle
FONT1 = ("Courier", 24, "normal")
FONT2 = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()

    def write_level(self):
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-240, 240)
        self.clear()
        self.write(f'Level: {self.level}', font=FONT1)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align='center', font=FONT2)
