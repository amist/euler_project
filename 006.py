def get_answer():
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(101):
        sum_of_squares += i ** 2
        square_of_sum += i
    square_of_sum = square_of_sum ** 2

    dif = square_of_sum - sum_of_squares
    return dif

if __name__ == '__main__':
    print(get_answer())