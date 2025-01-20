placeholder = '[name]'

template = open('./Input/Letters/starting_letter.txt').read()
names = open('./Input/Names/invited_names.txt').readlines()

for name in names:
    name = name.rstrip()
    letter = open(f'./Output/ReadyToSend/to_{name.lower()}', 'w')
    letter.write(template.replace(placeholder, name))
