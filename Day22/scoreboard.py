from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.penup()
        self.hideturtle()
        self.sety(180)
        self.scores = [0, 0]
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'{self.scores[0]}     {self.scores[1]}', align='center', font=("Courier", 100, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align='center', font=("Courier", 40, "normal"))