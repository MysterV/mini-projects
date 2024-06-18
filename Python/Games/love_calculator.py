# Don't question it
print('lovee calculator, because why not')
a = input('your name: ').lower()
b = input('their name: ').lower()
true = love = 0

string = a + b

for i in string:
    if i == 't':
        true += 1
    elif i == 'r':
        true += 1
    elif i == 'u':
        true += 1
    elif i == 'e':
        true += 1
        love += 1
    elif i == 'l':
        love += 1
    elif i == 'o':
        love += 1
    elif i == 'v':
        love += 1
        

print(f'{true}{love}')
