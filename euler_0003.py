"""


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# answer borrowed from
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
	
print prime_factors(600851475143)

# [71, 839, 1471, 6857L]  answer for largest prime facotr is 6857