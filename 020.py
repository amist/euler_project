def digit_sum(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digits)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

n = 100
print digit_sum(factorial(n))
