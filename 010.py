target = 2000000

# creating Sieve of Eratosthenes
#size = int(math.ceil(math.sqrt(target)))
size = target
sieve = [True] * (size + 1)
for i in range(2, size + 1):
    if sieve[i] == True:
        for j in range(2, int(size / i) + 1):
            sieve[j * i] = False

summation = 0
for i in range(2, size):
    if sieve[i] == True:
        summation += i
print summation
