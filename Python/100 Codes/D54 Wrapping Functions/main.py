import time


def timer(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        time_diff = end - start
        print(f'{function.__name__}\tfinished in: {time_diff} seconds')
    return wrapper


@timer
def slow():
    for i in range(1000):
        a = i ** i


@timer
def fast():
    for i in range(10000):
        a = i ** i


slow()
fast()
