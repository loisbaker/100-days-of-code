from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def turn_counter_clockwise():
    turtle.setheading(turtle.heading() + 10)


def turn_clockwise():
    turtle.setheading(turtle.heading() - 10)


def clear_turtle():
    turtle.reset()


screen.listen()

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_counter_clockwise, key="a")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=clear_turtle, key="c")

screen.exitonclick()
