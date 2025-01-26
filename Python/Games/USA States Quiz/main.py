import turtle
import pandas

image = 'blank_states_img.gif'
states = pandas.read_csv('50_states.csv')
guessed_states = []

game = turtle.Screen()
game.title('USA States')
game.addshape(image)
game.setup(725, 491)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.up()
writer.speed(0)

def play():
    global guessed_states, game_on
    score = len(guessed_states)
    all_states = states.state.to_list()
    if score == 50:
        writer.goto(-100, 0)
        writer.write('You win!\nYou guessed all the states correctly', font=('Arial', 32, 'bold'))
        game_on = 0
        return

    answer = ''
    while not answer:
        answer = game.textinput(title=f'State Picker: {score}/50', prompt='Name?\n("exit" to exit)')
    if answer:
        answer = answer.title()

    if answer == 'Exit':
        missing_states = [i for i in all_states if i not in guessed_states]
        missing_states = pandas.DataFrame(missing_states)
        missing_states.to_csv('missed_states.csv')
        game_on = False
        return

    if answer in all_states:
        guessed_states.append(answer)
        stated = states[states.state == answer]
        writer.goto(int(stated.x.iloc[0]), int(stated.y.iloc[0]))
        writer.write(answer)


game_on = True
while game_on:
    play()
