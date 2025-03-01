# Rules of prime
# >1
# not divisible by any number other than 1 and itself

def isprime_slow(n):
    n = int(n)
    if n <= 1: return False
    
    # this runs n-2 times
    for i in range(2, n):
        if n%i == 0: return False

    return True



def isprime_medium(n):
    n = int(n)
    if n <= 1: return False

    # this runs sqrt(n) times
    # if we divide n by any number bigger than the square root of n, it will never be a prime
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
        
    return True



def isprime_fast(n):
    n = int(n)
    if n == 2: return True
    elif n <= 1 or n%2 == 0: return False

    # this runs 0.5*sqrt(n) times
    # since not divisible by 2, only need to check for odd numbers
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return False

    return True


number = input('Give me a number and I will check if it is prime: ')
print('Slow code says:\t', isprime_slow(number))
print('Medium code says:\t', isprime_medium(number))
print('Fast code says:\t', isprime_fast(number))
