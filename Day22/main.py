# Pong game
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from net import Net
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)
net = Net()
ball = Ball()
screen.listen()

paddles = [Paddle(x_pos=-460), Paddle(x_pos=460)]
screen.onkey(paddles[0].up, 'w')
screen.onkey(paddles[0].down, 'a')
screen.onkey(paddles[1].up, 'Up')
screen.onkey(paddles[1].down, 'Down')

scoreboard = Scoreboard()


def play_pong():
    game_on = True
    at_least_one_hit = [0, 0]
    ball.refresh()
    while game_on:
        ball.move()
        time.sleep(ball.move_speed)
        screen.update()
        # If hits the wall:
        if abs(ball.ycor()) > 270:
            ball.bounce_wall()

        if ball.xcor() > 430:
            if paddles[1].distance(ball) < 50:
                ball.bounce_paddle()
                at_least_one_hit[1] += 1
            else:
                if at_least_one_hit[0] > 0:
                    scoreboard.scores[0] += 1
                scoreboard.write_score()
                game_on = False
        if ball.xcor() < -430:
            if paddles[0].distance(ball) < 50:
                ball.bounce_paddle()
                at_least_one_hit[0] += 1
            else:
                if at_least_one_hit[1] > 0:
                    scoreboard.scores[1] += 1
                scoreboard.write_score()
                game_on = False
    if max(scoreboard.scores) < 11:
        play_pong()


play_pong()





screen.update()








screen.exitonclick()