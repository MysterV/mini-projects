import math
import sys

import prettytable

a_table = prettytable.PrettyTable()
a_table.add_column('Name',['Max', 'Matt', 'Mab', 'Mel', 'Mi', 'Morty'])
a_table.add_column('Pet name', ['Paw', 'Piss', 'Pet', 'Put', 'Pero', 'Power'])
a_table.align = 'r'

a_table.del_row(3)
print(a_table)

a_table.clear()
a_table.add_column('A', [])
a_table.add_column('B', [])
a_table.align = 'l'
print(a_table)

for i in range(1,15):
    a_table.add_row([f'{i**(1/i**i):.2f}', i**i])

print(a_table)

sys.set_int_max_str_digits(100000)
for i in range(2, 100):
    a_table.add_column(f'{i}', [
        i,
        10 ** 100,
        10 ** (1100),
        math.factorial(100),
        i - 1,
        i ** (1/i),
        i ** 1.0000001 + 1,
        i ** 2 + 2,
        i**2 + 5*i + 176,
        i ** 10 + 3,
        i ** 999,
        i ** i + 4,
        i ** (i ** 2),
        i ** 100 * i
        # these seem to make the program freeze for some reason
        # 10 ** (10 ** 100),
        # i ** (i ** i),
        # i ** (i ** (i ** (i ** i))),
    ])

print(a_table)
a_table.clear()
print(a_table)