def triangulars():
    counter = 0
    summation = 0
    while (True):
        counter += 1
        summation += counter
        yield summation

def get_divisors(n):
    divs = []
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            divs.append(i)
    divs.append(n)
    return divs

def get_answer():
    trian = triangulars()
    while (True):
        cur = next(trian)
        divs = get_divisors(cur)
        #print cur, '->', divs
        if len(divs) > 500:
            return cur

# 842161320 is not correct
print(get_answer())
#print get_divisors(842161320)
#print len(get_divisors(842161320))
