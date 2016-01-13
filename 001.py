def get_answer():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
    
if __name__ == '__main__':
    print(get_answer())
    