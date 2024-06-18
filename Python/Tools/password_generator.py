from assets import alphabet, digits, special_characters
import random as r

length = int(input('Length of the password: '))
n_digits = int(input('Number of digits: '))
n_special_characters = int(input('Number of special characters: '))


# some apps and websites don't support these characters in passwords
if n_special_characters > 0:
    if input('Include quotes (\', ")? y/n ') != 'y':
        special_characters.remove("'")
        special_characters.remove('"')
    if input('Include question mark (?)? y/n ') != 'y':
        special_characters.remove('?')
    if input('Include backslash (\\)? y/n ') != 'y':
        special_characters.remove('\\')


chars = []
for _ in range(length):
    if n_special_characters != 0:
            n_special_characters -= 1
            chars += r.choice(special_characters)
    elif n_digits != 0:
        n_digits -= 1
        chars += r.choice(digits)
    else:
        chars += r.choice(alphabet)


password = ''
for _ in range(length):
    choice = r.choice(chars)
    chars.remove(choice)
    password += choice


print('\n' + password)
