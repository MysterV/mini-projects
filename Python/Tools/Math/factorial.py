def factorial(n):
    if n<0: return 'Nope. Try again'
    if n==0 or n==1: return 1
    if n>=2: return n*factorial(n-1)

print(factorial(int(input('what number to take factorial of? '))))
