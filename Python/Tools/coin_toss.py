import random as r

gamble = 1

def coin_toss():
    global gamble
    answer = input('\nHeads or Tails? h/t ')
    c = r.randint(0, 1)
    win = 0

    if c == 0:
        print('Heads')
        if answer == 'h': win = 1
    else:
        print('Tails')
        if answer == 't': win = 1

    if win == 1:
        gamble *= 1.5
        print(f'Congrats! Your balance is now {gamble}')
    else:
        gamble *= 0.5
        print(f'You lose! Your balance is now {gamble}')

    if input('play again? y/n') == 'y': coin_toss()

coin_toss()
