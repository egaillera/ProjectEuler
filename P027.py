'''
Euler discovered the remarkable quadratic formula:

	n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive 
integer values 0 <= n <= 39. However, when n=40, 40^2+40+41 = 40(40+1) + 41 is 
divisible by 41, and certainly when n=41, 41^2+41+41 is clearly divisible by 41.

The incredible formula n^2 -79n + 1601 was discovered, which produces 80 primes 
for the consecutive values 0 <= n <= 79. The product of the coefficients, -79 and
-1601, is -126479.

Considering quadratics of the form:

	n^2 + an + b, where |a| < 1000 and |b| <= 1000

Find the product of the coefficients, a and b, for the quadratic expression that 
produces the maximum number of primes for consecutive values of n , starting with n=0.

'''

import math

def is_prime(x):
	if x%2 == 0:
		return False
	for i in range(3,int( math.sqrt(x) ) + 1):
		if x%i == 0:
			return False
	return True

max_primes = [0,0,0]
for a in range(-1000,1000):
	for b in range(-1001,1001):
		n = 0
		while is_prime(abs(n*n + a*n + b)):
			n = n + 1
		if n > max_primes[2]:
			max_primes = [a,b,n]
		
print ("a = %d, b = %d, n = %d" % (max_primes[0],max_primes[1],max_primes[2]))
print(f"Resultado a*b = {max_primes[0]*max_primes[1]}")