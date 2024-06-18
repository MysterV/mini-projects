import random as r

print('Welcome to the game of hangman!\nDue to a limited budget, we do not offer a graphical display.\nYou get 6 lives.\n')


words = ['python', 'never', 'mouse', 'ardvark', 'gonna', 'programming', 'two', 'give', 'camel', 'night', 'you', 'alien', 'day', 'up']
chosen = r.choice(words)
guess_list = []
already_guessed = []
guess_str = ''
lives = 6

# fill up the blanks
for _ in range(len(chosen)):
    guess_list += '_'
    guess_str += '_'


while lives > 0:
    # good ending
    if guess_str == chosen:
        print(f'\nYou win! The word was "{chosen}"')
        break

    # take the guess
    guess = input(f'{guess_str}  |  lives left: {lives}  |  Guess a letter: ').casefold()

    # make sure that the player doesn't guess a letter twice
    if guess in already_guessed:
        if guess in guess_list:
            print(f'You\'ve already guessed {guess}')
        else: print(f'You\'ve already tried {guess}')
        continue
    else: already_guessed += guess

    # check for wrong guess
    if guess not in chosen:
        lives -= 1
        pass
    
    # check for right guess
    for _ in range(len(chosen)):
        if chosen[_] == guess:
            guess_list[_] = guess


    # format the guess display
    guess_str = ''
    for _ in guess_list:
        guess_str += _

else:
    # bad ending
    print(f'\nYou lose! The word was "{chosen}"')
    
