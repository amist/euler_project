import math

def get_answer():
    target = 600851475143

    # creating Sieve of Eratosthenes
    size = int(math.ceil(math.sqrt(target)))
    sieve = [True] * (size + 1)
    for i in range(2, size + 1):
        if sieve[i] == True:
            for j in range(2, int(size / i) + 1):
                sieve[j * i] = False

    biggest_prime = 0
    for i in range(size, 2, -1):
        if sieve[i] == True:
            if target % i == 0:
                biggest_prime = i
                return biggest_prime

if __name__ == '__main__':
    print(get_answer())