"""
Sum square difference
Problem 6 

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

sumSquares = 0
squaredSum = 0

for x in range(1, 101):
	sumSquares = sumSquares + x**2
	squaredSum = squaredSum + x

squaredSum = squaredSum**2
difference = squaredSum - sumSquares

print "The squared sum of the first 100 natural numbers is " + str(squaredSum)
print "The sum of the squares of the first 100 natural numbers is " + str(sumSquares)
print "The difference between the sum of the squares and the square of the sums is " + str(difference)

#25164150

"""
The squared sum of the first 100 natural numbers is 25502500
The sum of the squares of the first 100 natural numbers is 338350
The difference between the sum of the squares and the square of the sums is 25164150
"""


