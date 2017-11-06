"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def lowdivnum():
	divflag = False
	count = 20 #start the count at 20 as that is the highest number we will divide by
	while count < 999999999: # while loop will let us escape when we find the lowest one
		for y in range(1, 20):
			if count % y != 0:
				divflag = True # if the flag is tripped, we don't have to check if it is a number we want
		if divflag == False:
			lownumber = count # if the flag wasn't tripped we've found it so set lownumber equal to count and escape
			break
		divflag = False
		count = count +	1
	return lownumber
	
print lowdivnum()

#232792560