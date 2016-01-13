dictionary = {}
dictionary[1] = 'one'
dictionary[2] = 'two'
dictionary[3] = 'three'
dictionary[4] = 'four'
dictionary[5] = 'five'
dictionary[6] = 'six'
dictionary[7] = 'seven'
dictionary[8] = 'eight'
dictionary[9] = 'nine'
dictionary[10] = 'ten'
dictionary[11] = 'eleven'
dictionary[12] = 'twelve'
dictionary[13] = 'thirteen'
dictionary[14] = 'fourteen'
dictionary[15] = 'fifteen'
dictionary[16] = 'sixteen'
dictionary[17] = 'seventeen'
dictionary[18] = 'eighteen'
dictionary[19] = 'nineteen'
dictionary[20] = 'twenty'
dictionary[30] = 'thirty'
dictionary[40] = 'forty'
dictionary[50] = 'fifty'
dictionary[60] = 'sixty'
dictionary[70] = 'seventy'
dictionary[80] = 'eighty'
dictionary[90] = 'ninety'
dictionary[100] = 'hundred'
dictionary[1000] = 'thousand'


def wordize(num):
    word = ''
    d1000 = int(num / 1000)
    d100 = int(num / 100) % 10
    d10 = int(num / 10) % 10
    d1 = num % 10
    w1000 = ''
    w100 = ''
    w10 = ''
    w1 = ''
    
    if d1000 == 1:
        w1000 = 'one ' + dictionary[1000]
    
    if d100 != 0:
        w100 = dictionary[d100] + ' ' + dictionary[100]
        
    if d10 != 1:
        if d10 != 0:
            w10 = dictionary[10 * d10]
        
        if d1 != 0:
            w1 = dictionary[d1]
    else:
        w10 = dictionary[num % 100]
    
    after1000 = ' and ' if w1000 != '' and (w100 != '' or w10 != '' or w1 != '') else ''
    after100 = ' and ' if w100 != '' and (w10 != '' or w1 != '') else ''
    after10 = '-' if w10 != '' and w1 != '' else ''
    
    word = w1000 + after1000 + w100 + after100 + w10 + after10 + w1
    
    return word

def letters_in_number(number):
    return len(number.replace(' ', '').replace('-', ''))

def get_answer():
    summation = 0
    for i in range(1001):
        summation += letters_in_number(wordize(i))
    return summation

if __name__ == '__main__':
    print(get_answer())