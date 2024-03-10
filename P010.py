'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from time import time 

def is_prime(x):
	
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif (x % 2 == 0) or (x % 3 == 0):
		return False
	
	i = 5
	while i*i <= x:
		if (x % i == 0)  or (x % (i + 2) == 0):
			return False
		# Because all primes > 3 can be represented
		# as 6n-1 or 6n+1
		i = i + 6 
	return True	 	

start = time()	
total = 5
i = 5
while i <= 2000000:
	if is_prime(i):
		total = total + i
	i = i + 2

elapsed = time() - start		

print(f"Solution: {total}. Time elapsed: {elapsed} seconds")