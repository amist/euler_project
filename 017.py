dict = {}
dict[1] = 'one'
dict[2] = 'two'
dict[3] = 'three'
dict[4] = 'four'
dict[5] = 'five'
dict[6] = 'six'
dict[7] = 'seven'
dict[8] = 'eight'
dict[9] = 'nine'
dict[10] = 'ten'
dict[11] = 'eleven'
dict[12] = 'twelve'
dict[13] = 'thirteen'
dict[14] = 'fourteen'
dict[15] = 'fifteen'
dict[16] = 'sixteen'
dict[17] = 'seventeen'
dict[18] = 'eighteen'
dict[19] = 'nineteen'
dict[20] = 'twenty'
dict[30] = 'thirty'
dict[40] = 'forty'
dict[50] = 'fifty'
dict[60] = 'sixty'
dict[70] = 'seventy'
dict[80] = 'eighty'
dict[90] = 'ninety'
dict[100] = 'hundred'
dict[1000] = 'thousand'


def wordize(num):
	word = ''
	d1000 = num / 1000
	d100 = (num / 100) % 10
	d10 = (num / 10) % 10
	d1 = num % 10
	w1000 = ''
	w100 = ''
	w10 = ''
	w1 = ''
	
	if d1000 == 1:
		w1000 = 'one ' + dict[1000]
	
	if d100 != 0:
		w100 = dict[d100] + ' ' + dict[100]
		
	if d10 != 1:
		if d10 != 0:
			w10 = dict[10 * d10]
			
		if d1 != 0:
			w1 = dict[d1]
	else:
		w10 = dict[num % 100]
		
	after1000 = ' and ' if w1000 != '' and (w100 != '' or w10 != '' or w1 != '') else ''
	after100 = ' and ' if w100 != '' and (w10 != '' or w1 != '') else ''
	after10 = '-' if w10 != '' and w1 != '' else ''
	
	word = w1000 + after1000 + w100 + after100 + w10 + after10 + w1
	
	return word
	
def letters_in_number(number):
	return len(number.replace(' ', '').replace('-', ''))
	
summation = 0
for i in range(1001):
	summation += letters_in_number(wordize(i))
print summation
