import turtle
import pandas

screen = turtle.Screen()
screen.title('US States game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.color('black')
writer.hideturtle()

answer_state = screen.textinput('Guess the state', 'What is the name of a state?').title()
state_data = pandas.read_csv('50_states.csv')
state_count = 0
keep_playing = True
correct_answers = []
while keep_playing:
    if answer_state == 'Exit':
        break
    if answer_state in state_data.state.values:
        state_count += 1
        correct_answers.append(answer_state)
        x_state = int(state_data.x[state_data.state == answer_state])
        y_state = int(state_data.y[state_data.state == answer_state])
        writer.goto(x_state, y_state)
        writer.write(f'{answer_state}', align='center')
    if state_count == 50:
        keep_playing = False
    else:
        answer_state = screen.textinput(f'State count: {state_count}/50 ', 'What is the name of another state?').title()

for correct_state in correct_answers:
    state_data = state_data[state_data.state != correct_state]


state_data.to_csv('state_to_learn.csv')


