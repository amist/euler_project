def get_divisors_sum(n):
	total = 0
	for i in range(1, n/2 + 1):
		if n % i == 0:
			total += i
	return total
	
bound = 28123 + 1
sums = {}

for i in range(1, bound):
	sums[i] = get_divisors_sum(i)
	
abundants = []

for i in range(1, bound):
	if sums[i] > i:
		abundants.append(i)
		
abundant_sums = {}
for i in range(1, bound):
	abundant_sums[i] = False
	
for a in abundants:
	for b in abundants:
		if a + b < bound:
			abundant_sums[a + b] = True
			
sum = 0
for i in range(1, bound):
	if abundant_sums[i] == False:
		sum += i
		
print sum