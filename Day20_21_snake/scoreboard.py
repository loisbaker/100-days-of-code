from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align='center', font=("Arial", 40, "normal"))