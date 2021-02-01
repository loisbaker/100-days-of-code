# Object examples

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red', 'green')
# timmy.forward(20)
#
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon', ['Pikachu', 'Charmander', 'Squirtle'])
table.add_column('type', ['electric', 'fire', 'water'])
table.align['type'] = 'l'
print(table.align)

