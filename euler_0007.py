"""
10001st prime
Problem 7 

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def primeGetter():
	h = 0
	primeflag = 0
	divJ = 2
	for primeN in range(2, 120000):
		primeflag = 0
		for divJ in range(2, primeN):
			if (primeN % divJ) == 0:
				primeflag = 1
				# print str(primeN) + " modulo " + str(divJ) + " is not prime" (error checking!)
				break
		if primeflag == 0:
			# print str(primeN) + " is prime" (error checking!)
			h = h + 1
			# print str(h) + " total primes found so far!"  (error checking!)
			if h == 10001:
				return primeN

print primeGetter()

#104743