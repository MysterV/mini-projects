import random as r
numbers = []
n = int(input('How many numbers? '))
biggest = int(input('What\'s the max value? '))
for _ in range(n):
    numbers.append(r.randint(0, biggest))

print(numbers, '\n')


# simple sorting algorithmm, idk the name

for _ in range(len(numbers)-1):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers)
    
