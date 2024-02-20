# Don't question it
print('lovee calculator, because why not')
a = input('your name: ').lower()
b = input('their name: ').lower()
true = love = 0

string = a + b

for _ in string:
    if _ == 't':
        true += 1
    elif _ == 'r':
        true += 1
    elif _ == 'u':
        true += 1
    elif _ == 'e':
        true += 1
        love += 1
    elif _ == 'l':
        love += 1
    elif _ == 'o':
        love += 1
    elif _ == 'v':
        love += 1
        

print(f'{true}{love}')
