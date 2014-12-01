def calc_digits_sum(num):
	digits = [int(ch) for ch in [ch for ch in str(num)]]
	return sum(digits)
	
print calc_digits_sum(2 ** 1000)