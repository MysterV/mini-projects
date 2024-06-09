import random as r

print('1')
for _ in range(2):
    a = r.randint(0, 5) + r. random()
    if a > 5: a = 5
    print(a)

print('\n2')
for _ in range(2):
    b = r.randint(1, 50) / 10
    print(b)

print('\n3')
for _ in range(2):
    b = r.randint(1, 5000000) / 1000000
    print(b)
