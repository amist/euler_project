import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]
a = {}
for j in primes:
	a[j] = 0

for i in range(2, 21):
	b = {}
	num = i
	for j in primes:
		b[j] = 0
		while num % j == 0:
			b[j] += 1
			num = num / j
		if b[j] > a[j]:
			a[j] = b[j]
	
res = 1
for j in primes:
	res *= math.pow(j, a[j])
print int(res)