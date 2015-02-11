ordinal = 10001
target = ordinal * 600

# creating Sieve of Eratosthenes
# size = int(math.ceil(math.sqrt(target)))
size = target
sieve = [True] * (size + 1)
for i in range(2, size + 1):
    if sieve[i] == True:
        for j in range(2, int(size / i) + 1):
            sieve[j * i] = False

res = 0
i = 1
for j in range(2, size):
    if sieve[j] == True:
        if i == ordinal:
            res = j
            break
        i += 1

print res
