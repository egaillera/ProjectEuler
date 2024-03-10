'''
By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import math

def is_prime(x):

	if x == 1 or x == 2:
		return True
	
	if x%2 == 0:
		return False
	
	for i in range(3,int( math.sqrt(x) ) + 1,2):
		if x%i == 0:
			return False
			
	return True

pos = 1
x = 2	
while pos <= 10001:
	
	if is_prime(x):
		print ("The prime number %d is in position %d" % (x,pos))
		pos = pos + 1
		
	x = x + 1	
		
		
		
			
		