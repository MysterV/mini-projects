a = 2
while a != 0:
    a = 0
    print('Test')

b = [0]

for _ in b:
    b.append(len(b))
    print(_)
    if len(b) >= 100: break
