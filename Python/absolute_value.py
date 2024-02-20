from math import fabs
a = -10
b = 5

print(fabs(a))
print(fabs(b))

def absolute(n):
    if n < 0: return -n
    else: return n
    
print(absolute(a))
print(absolute(b))
