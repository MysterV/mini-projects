import random as r
numbers = []
for _ in range(10):
    numbers.append(r.randint(1, 100))

print(numbers)



# max
a = 0
for _ in numbers:
    if _ > a:
        a = _
print(f'The lowest value: {a}')

#min
b = numbers[0]
for _ in numbers:
    if _ < b:
        b = _
print(f'The biggest value: {b}')
