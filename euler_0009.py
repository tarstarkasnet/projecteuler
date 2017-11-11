"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

for i in range(1, 1000):
	for j in range(1, 1000):
		for k in range(1, 1000):
			if (i * i + j * j == k * k and i + j + k == 1000):
				print i,j,k


#The three numbers are 200 375 425
#180625 = 180635
#200 * 375 * 425 = 31875000