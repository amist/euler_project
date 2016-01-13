import math

def fib():
    a, b = 0, 1
    while (True):
        a, b = b, a + b
        yield a

def num_of_digits(num):
    return int(math.floor(math.log10(num) + 1))

def get_answer():
    fib_gen = fib()
    i = 0
    while True:
        i += 1
        cur = next(fib_gen)
        if num_of_digits(cur) > 999:
            return i

if __name__ == '__main__':
    print(get_answer())