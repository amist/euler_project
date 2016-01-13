def calc_digits_sum(num):
    digits = [int(ch) for ch in [ch for ch in str(num)]]
    return sum(digits)
    
def get_answer():
    return calc_digits_sum(2 ** 1000)

if __name__ == '__main__':
    print(get_answer())