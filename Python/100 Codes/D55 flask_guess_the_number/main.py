import random

from flask import Flask
import random as r

'''
A simple game about guessing a number, where you type in your guess into the URL bar, as though it is a subpage
'''

# Number picker
min = 1
max = 1
tries = -1  # if <0, infinite attempts

pick = random.randint(min, max)


# ===== Meaningless overcomplicating shit ======
def h(function):
    def wrapper(*args, **kwargs):
        output = f'<h{args[0]}>{function()}</h{args[0]}>'
        print(output)
        return output
    return wrapper


def b(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper


def i(function):
    def wrapper():
        return f'<i>{function()}</i>'
    return wrapper


# ===== Intro =====
app = Flask(__name__)


@app.route('/')
def hi():
    return f'Hello!!!!!\nWellcome to the death game :>\nPick a number between {min} and {max}'


@app.route('/<int:guess>')


def check(guess):
    @h
    def no_way():
        return 'N O   W A Y<br>CONGRATS!!1!1!!1!!'
    no_way(1)


    if guess == pick:
        return '<h2>You actually did it! You are insane, you know... <i>1 in a BILLION</i> chance</h2>' \
               '<img src="https://cdn.discordapp.com/emojis/1050670378562883584.gif?size=512" width=200>' \
               '<br>P.S. go <a href="https://torcado.com/windowkill/secret/">here</a> to claim your reward'
    elif guess > pick:
        return '<h2><i>Bad luck.</i> You, in fact, did not win the lottery. :<</h2>' \
               '<br>P.S. try lowering your expectations'
    elif guess < pick:
        return '<h2><i>Bad luck.</i> You, in fact, did not win the lottery. :<</h2>' \
               '<br>P.S. try aiming higher'


if __name__ == '__main__':
    app.run(debug=True)
