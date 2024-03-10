'''
The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of the number 600851475143?

'''

import math

N = 600851475143

def is_prime(x):
	'''
	Return True is x is prime. Calcuation by brute force
	'''
	for i in range(2,int(math.sqrt(x))):
		if x%i == 0:
			return False
	return True

# Look for prime factors starting by 3, and skipping evens
for i in range(3,int(N/2),2):
	if is_prime(i):
		while N%i == 0:
			print(i)
			N = N / i
			if N == 1:
				print("Largest prime factor: " + str(i))
				quit()


			
		
