import time

factor = 1000


def timer(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        end = time.time()
        time_diff = end - start
        print(f'completed:\t{time_diff:.6f} seconds')
    return wrapper


def newline_at_the_end(function):
    def wrapper(*args):
        function(*args)
        print('')
    return wrapper


def logger(function):
    def wrapper(*args):
        if len(args) == 1:
            called = f'called:\t\t{function.__name__}({args[0]})'
        else:
            called = f'called:\t\t{function.__name__}{args}'
        result = f'returned:\t{function(*args)}'
        print(called)
        print(result)
    return wrapper


@newline_at_the_end
@timer
@logger
def fast(n):
    for i in range(n):
        i ** i


@newline_at_the_end
@timer
@logger
def slow(n):
    for i in range(n*10):
        i ** i


@newline_at_the_end
@logger
def a_function(a, b, c):
    return a * b * c


@timer
@logger
def insanely_slow(n):
    # Initially I made it n**100
    # but then I did the math, and realized that it makes the loop run 10^30 times
    # and it would try to calculate (10^30)^(10^30)
    # with such a number, the whole universe, and all parallel universes, and everything else that would ever follow,
    # would be long gone and forgotten before this code snippet is a 1/10^1000000000000000000000000th of the way there
    # so yeah... I don't think we need to go that far for this test
    # heck, even at 100n, we're already looking at a 7.5-minute run time, that's already overkill
    for i in range(n*100):
        i ** i


fast(factor)
slow(factor)
a_function(1, 2, 3)
insanely_slow(factor)



