#!/usr/bin/python


import time


numberToWord = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
				   11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twelve',
				   30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}

def solve():
	return sum(sumOfWord(x) for x in xrange(1, 1001))

def sumOfWord(n):
	if n in numberToWord:
		if n == 100 or n == 1000:
			return len(numberToWord[1] + numberToWord[n])
		else:
			return len(numberToWord[n])
	else:
		if (n%100==0):
			return len(numberToWord[int(str(n)[0:1])] + numberToWord[100])
		else:
			s = ''
			if int(str(n)[-2:]) in numberToWord:
				s += numberToWord[int(str(n)[-2:])]
			else:
				s += numberToWord[int(str(n)[-1:])]
				n -= int(str(n)[-1:])
				s += numberToWord[int(str(n)[-2:])]
			n -= int(str(n)[-2:])
			if n != 0:
				s += 'and'
				s += numberToWord[int(str(n)[0:1])]
				s += numberToWord[100]
			return len(s)


if __name__ == '__main__':
	startTime = time.time()
	print solve()
	elapsedTime = time.time() - startTime
	print "Time: {0}".format(elapsedTime)