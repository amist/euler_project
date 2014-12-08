import math

def fib():
	a, b = 0, 1
	while (True):
		a, b = b, a + b
		yield a
		
def num_of_digits(num):
	return int(math.floor(math.log10(num) + 1))
		
def solve_euler_025():
	fib_gen = fib()
	i = 0
	while (True):
		i += 1
		cur = fib_gen.next()
		if num_of_digits(cur) > 999:
			print i
			return
		
solve_euler_025()
