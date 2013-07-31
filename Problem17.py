#!/usr/bin/python


import time


number_to_word = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
				   11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twelve',
				   30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}


def solve():
	return sum(sum_of_word(x) for x in xrange(1, 1001))


def sum_of_word(n):
	if n in number_to_word:
		if n == 100 or n == 1000:
			return len(number_to_word[1] + number_to_word[n])
		else:
			return len(number_to_word[n])
	else:
		if (n%100==0):
			return len(number_to_word[int(str(n)[0:1])] + number_to_word[100])
		else:
			s = ''
			if int(str(n)[-2:]) in number_to_word:
				s += number_to_word[int(str(n)[-2:])]
			else:
				s += number_to_word[int(str(n)[-1:])]
				n -= int(str(n)[-1:])
				s += number_to_word[int(str(n)[-2:])]
			n -= int(str(n)[-2:])
			if n != 0:
				s += 'and'
				s += number_to_word[int(str(n)[0:1])]
				s += number_to_word[100]
			return len(s)


if __name__ == '__main__':
	start_time = time.time()
	print solve()
	elapsed_time = time.time() - start_time
	print "Time: {0}".format(elapsed_time)