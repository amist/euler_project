import copy
digits_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def factorial(n):
	if n < 0:
		raise Exception, 'n should be a non negative integer'
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

def get_digits_permutation(set, num):
	num -= 1
	ret = []
	for i in range(len(set)):
		ordinal = num / factorial(len(set) - 1)
		ret.append(set.pop(ordinal))
		num -= factorial(len(set)) * ordinal
	return ret

print ''.join([str(x) for x in get_digits_permutation(copy.copy(digits_set), 1000000)])