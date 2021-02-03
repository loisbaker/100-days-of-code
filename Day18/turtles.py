from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()
turtle.shape('turtle')

# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# for i in range(50):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)

# for i in range(3, 11):
#     rgb = (random.randint(1, 100)/100, random.randint(1, 100)/100, random.randint(1, 100)/100)
#     turtle.pencolor(rgb)
#     for ii in range(i):
#         turtle.forward(100)
#         turtle.left(360/i)


def rand_colour():
    r = random.randint(1,100)/100
    g = random.randint(1, 100)/100
    b = random.randint(1,100)/100
    return (r, g, b)

# dirs = list(range(-180, 180, 1)) #[-180, -90, 0, 90]
# for _ in range(1000):
#     turtle.pencolor(rand_colour())
#     turtle.speed(5)
#     turtle.pensize(5)
#     turtle.right(random.choice(dirs))
#     turtle.forward(10)
num_circles = 100
for n in range(num_circles):
    turtle.setheading(n*360/num_circles)
    turtle.pencolor(rand_colour())
    turtle.speed(100)
    turtle.circle(100)



screen.exitonclick()