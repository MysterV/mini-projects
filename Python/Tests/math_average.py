heights = [123, 202, 125, 176, 189, 183, 181, 165, 147, 195, 148, 178, 160, 180, 190, 156]
sum = 0
for _ in heights:
    sum += _
average = sum / len(heights)
print(f'Average from manually generated heights is: {average}')

import random as r

sum_r = 0
for _ in range(ranga:=r.randint(1, 123456)):
    sum_r += r.randint(55, 300)
average_r = sum_r / ranga
print(f'Average from randomly generated heights is: {average_r}')


a = int(input('a = '))
b = int(input('b = '))
geo = (a*b)**0.5

print(f'Geometric average of a rectangle a x b: {geo}')


# power average

p = int(input('\nPower average time.\nPower: '))
n = int(input('n: '))
top = 0
for _ in range(n):
    top += int(input(f'a{_+1}: '))

print(f'The power average of these values is: {(top / n) ** (1/p)}')
