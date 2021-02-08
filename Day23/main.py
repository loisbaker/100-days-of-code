import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.write_level()
screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move(scoreboard.level)
    for car in car_manager.all_cars:
        # If the player crashes into a car:
        if player.xcor()-25 < car.xcor() and abs(player.ycor() - car.ycor()) < 27 and abs(player.xcor() - car.xcor()) < 25:
            game_is_on = False
            scoreboard.game_over()
            break
    # If player reaches the other side
    if player.ycor() > player.finish:
        scoreboard.level += 1
        scoreboard.write_level()
        player.refresh()

screen.exitonclick()
