"""


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""




def loopForPalis():
	sumhigh = 0
	for x in range(100, 999):
		for y in range(100, 999):
			loopSum = x *y
			sumStr = str(loopSum) #convert loopSum to a string so we can make the reverse
			sumRev = sumStr[::-1] #makes the reverse of the original string of the sum
			if sumStr == sumRev:  #compares if palindrome
				if loopSum > sumhigh:  #if it is a palindrome, then checks if it is bigger than the prior palindromes
					sumhigh = loopSum  #if it is bigger, we have a new champion
	return sumhigh

print loopForPalis()

#906609


