# a simple game where you guess a number

import random
my_range = 1000
my_number = random.randint(1, my_range)

difficulties = {
    'easy': 30,
    'medium': 20,
    'hard': 13
}
difficulty = ''
while difficulty not in ('easy', 'medium', 'hard'):
    difficulty = input('Choose a difficulty: "easy", "medium", or "hard": ')
print(f'{difficulty}, great choice. Let the game begin.')

print(f'I have randomly chosen a number between 1 and {my_range}, try to guess it. You get {difficulty} shots.')

def guess(attempts):
    for i in range(1, attempts+1):
        choice = ''
        while not choice:
            choice = input(f'Attempt {i}/{attempts}: ')
        choice = int(choice)
        
        if choice == my_number:
            print(f'Congrats, the number was indeed {my_number}')
            return
        elif choice < my_number: print('More.')
        elif choice > my_number: print('Less.')
    else:
        print(f'You failed. The number was actually {my_number}')


guess(difficulties[difficulty])
