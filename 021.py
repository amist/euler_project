def get_divisors_sum(n):
    total = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            total += i
    return total

def get_answer():
    bound = 10001
    sums = {}

    for i in range(1, bound):
        sums[i] = get_divisors_sum(i)

    total = 0
    for i in range(2, bound):
        cur = sums[i]
        if cur < bound:
            if sums[cur] == i and cur != i:
                total += i
    return total

if __name__ == '__main__':
    print(get_answer())