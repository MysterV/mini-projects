'''simple calculator, which features:
- [/] operations on multiple values at once
- [x] adding, 
- [x] subtracting, 
- [x] multiplying, 
- [x] dividing, 
- [x] roots, 
- [x] powers,
- [x] absolute value,
- [x] rounding up the result to any number of digits,
'''

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def root(a, b): return a ** (1/b)
def power(a, b): return a ** b
def absolute(a):
    if a>=0: return a
    else: return -a
def remainder(a, b): return a % b
def quotient(a, b): return a // b
def myround(a, decimal_point):
    a = (a * 10**decimal_point)
    if a % 1 >= 0.5: a += 1
    a = a // 1
    a = a / 10**decimal_point
    return a

operation_map = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "root": root,
    "^": power,
    "absolute": absolute,
    "%": remainder,
    "//": quotient,
    "round": myround,
}

for i in operation_map:
    print(i, end='\t')
old_result = 0

while True ^ ~(True | (False & False)):    
    # first number
    if old_result: a = old_result
    else:
        a = float(input('\na: '))

    # operator
    chosen_operation = input('Choose type of operation: ')
    operation = operation_map[chosen_operation]
    
    # second number
    if chosen_operation == 'absolute': result = operation(a)
    else:
        b = float(input('b: '))
        result = operation(a, b)
    
    # format result
    if result % 1 == 0:
        result = int(result)

    print(result)
    
    if input('Continue calculating? y/n: ') != 'y':
        break
    else: 
        if input('Reuse the result? y/n: ') == 'y':
            old_result = result
        else: 
            old_result = 0

