boundary = 1000

def get_answer():
    for a in range(1, boundary):
        for b in range(a, boundary):
            c = boundary - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

if __name__ == '__main__':
    print(get_answer())