def get_word_value(word):
    word = word.lower()
    word_total = 0
    for ch in word:
        word_total += ord(ch) - 96
    return word_total

def get_answer():
    f = open('p022_names.txt', 'r')
    names = f.read()[1:-1].split('","')
    names.sort()

    total = 0
    for i in range(len(names)):
        total += (i + 1) * get_word_value(names[i])

    return total
    
if __name__ == '__main__':
    print(get_answer())