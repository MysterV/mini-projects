# Rules of prime
# - whole number >1
# - not divisible by any number other than 1 and itself

number = int(input('Give me a number and I will check if it is a prime: '))


def logger(function):
    def wrapper(*args):
        result = function(*args)
        # if prime => True
        # if not primeable (n<=1) => False, -1
        # if not prime => False, divisor
        if type(result) == bool:
            if result == True:
                print(f'{function.__name__}\tsays:\tprime')
        elif type(result) == tuple:
            if result == (False, -1):
                print(f'{function.__name__}\tsays:\tnot primeable')
            elif result[0] == False:
                print(f'{function.__name__}\tsays:\tnot prime, divisible by {result[1]}')
        else:
            print(f'{function.__name__}\tsays:\t{result}')
    return wrapper


@logger
def isprime_slow(n: int):
    if n <= 1: return False, -1
    
    # this runs n-2 times
    for i in range(2, n):
        if n%i == 0: return False, i

    return True


# beyond this point everything runs at O(sqrt(n)), but there are still ways for a minor improvement
@logger
def isprime_medium(n: int):
    if n <= 1: return False, -1

    # this runs sqrt(n) times
    # if we divide n by any number bigger than the square root of n, it will never be a prime
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False, i
        
    return True


@logger
def isprime_fast(n: int):
    if n <= 1: return False, -1
    if n == 2: return True
    if n%2 == 0: return False, 2
    

    # this runs 0.5*sqrt(n) times
    # since not divisible by 2, we skip even numbers
    # which halves the amount of values
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return False, i

    return True


@logger
def isprime_faster(n: int):
    if n <= 1: return False, -1
    if n in (2, 3): return True
    for i in (2,3):
        if n%i == 0: return False, i

    # this runs 0.33*sqrt(n) times
    # since not divisible by 3, skip every odd number divisible by 3
    # that brings the numbers left to check down to 0.5 * 0.667 = 0.33
    for i in range(5, int(n**0.5)+1, 6):
        if n%i == 0: return False, i
        elif n%(i+2) == 0: return False, i+2

    return True


isprime_slow(number)
isprime_medium(number)
isprime_fast(number)
isprime_faster(number)

