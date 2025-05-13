n = int(input('year '))
if n%400 == 0 or (n%4 == 0 and n%100 != 0):
    print('loop year')
else:
    print('not loop year')
