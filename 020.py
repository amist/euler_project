def digit_sum(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digits)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def get_answer():
    n = 100
    return digit_sum(factorial(n))

if __name__ == '__main__':
    print(get_answer())