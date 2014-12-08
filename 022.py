def get_word_value(word):
	word = word.lower()
	sum = 0
	for ch in word:
		sum += ord(ch) - 96
	return sum

f = open('p022_names.txt', 'r')
names = f.read()[1:-1].split('","')
names.sort()

total = 0
for i in range(len(names)):
	total += (i + 1) * get_word_value(names[i])
	
print total
