def even_fib_up_to_n(n):
	a, b = 1, 1
	while (True):
		a, b = b, a+b
		if a % 2 == 0:
			yield a
		if b > n:
			raise StopIteration
			
sum = 0
for i in even_fib_up_to_n(4000000):
	sum += i
print sum