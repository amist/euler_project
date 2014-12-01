boundary = 1000

def find_pythagorean_triplet():
	for a in range(1, boundary):
		for b in range(a, boundary):
			c = boundary - a - b
			if a ** 2 + b ** 2 == c ** 2:
				print(a * b * c)
				return
				
find_pythagorean_triplet()