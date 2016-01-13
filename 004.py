def is_palindrome(num):
    num = str(num)
    for i, ch in enumerate(num):
        if ch != num[-i - 1]:
            return False
    return True
    
def get_answer():
    highest = 0
    for i in range(1000):
        for j in range(1000):
            prod = i * j
            if prod > highest and is_palindrome(prod):
                highest = prod

    return highest

if __name__ == '__main__':
    print(get_answer())
