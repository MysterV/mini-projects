import random as r

print('Choose:\n1 - rock\n2 - paper\n3 - scissors')
player = int(input())
computer = r.randint(1, 3)
print('I choose', ['rock', 'paper', 'scissors'][computer-1])

if computer == player: print('Draw')
elif player == 1:
    if computer == 3: print('You win')
    if computer == 2: print('You lose')
elif player == 2:
    if computer == 1: print('You win')
    if computer == 3: print('You lose')
elif player == 3:
    if computer == 2: print('You win')
    if computer == 1: print('You lose')
else:
    print('What were you thinking? Disqualified.')
