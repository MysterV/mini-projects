# Higher or lower - a pointless game about pointing at things
# Theme: anime music

import random as r
from clear import clear

contenders = {
    'AKINO': 11400,
    'Animenz': 2190000,
    'Cateen': 1340000,
    'Fonzi M': 1520000,
    'King Gnu': 2520000,
    'RADWIMPS': 2920000,
    'SLSMusic': 490000,
    'Theishter': 1060000,
    'Torby Brand': 68800,
    'TRUE': 80600,
    'YOASOBI': 6600000,
    'Yuki Hayashi': 46900,
}

intro = '''Welcome to the game of Higher VS Lower, allow me to explain the rules:
You have to compare between 2 randomly chosen music creators, which one of them you think has more subscribers on YouTube. If you choose correctly, you get a point, if you guess wrong, you lose.
'''


def compare(a, b):
    if contenders[a] > contenders[b]:
        return 'a'
    elif contenders[a] < contenders[b]:
        return 'b'

def choose():
    chosen = r.choice(list(contenders))
    return chosen

b = choose()
score = 0
clear()
print(intro)

while True:
    a = b
    while b == a:
        b = choose()
    comparison = compare(a, b)

    print(f'Option A: {a}\nOption B: {b}')
    guess = input('Who do you think has more subscribers? a/b: ').lower()
    
    if guess == comparison:
        score += 1
        del contenders[a]
        clear()
        print(intro)
        print(f'Correct answer. Your score is {score}.')
        if len(contenders) == 1:
            print('Congrats, this is all. You have completed the game.')
            break
    else:
        print(f'You failed. Your final score is {score}')
        break
    
