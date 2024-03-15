
'''
A unit fraction contains 1 in the numerator. The decimal representation 
of the unit fractions with denominators 2 to 10 are given:

	1/2 = 0.5
	1/3 = 0.(3)
	1/4 = 0.25
	1/5 = 0.2
	1/6 = 0.1(6)
	1/7 = 0.(142857)
	1/8 = 0.125
	1/9 = 0.(1)
	1/10 = 0.1

Where 0.1(6) means 0.16666 ... , and has a -digit recurring cycle. It can 
be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''
import math
from decimal import *

def detect_cycle(decimals,l_cycle):
	'''
	Divide the string in parts of l_cycle lenghth, and return True
	if all parts are the same
    '''
    
	# Divide the string in equal parts
	parts = [decimals[i:i+l_cycle] for i in range(0, len(decimals), l_cycle)]

	# Convert the list in a set: a set will eliminate duplicated elements, so
	# if the set equals 1, it means all the elements are the same and we have 
	# found the cycle
	if len(set(parts)) == 1:
		#print(f"Detected cycle of {l_cycle} chars")
		return True
	else:
		#print(f"No {l_cycle} chars cycle detected")
		pass


def analyze_number(d:str) -> int:
	#print(f"Analyzing {d}")

	# We need to try all possible strings moving to the right
	# to find a cycle. For instance if we have 12656565 
	# we try:
	# - 12656565 -> we don't find a cycle because of the inital 12
	# - 2656565 -> we don't find a cycle because of the initial 2
	# - 656565 -> we find a cycle of 2 chars
	for i in range(0,len(s)):
		#print(f"Trying with {s[i:]}")
		
		for j in range(1,int(len(s[i:])/2)):
			# Adjust the length of the string to be a multiple 
			# of the cycle we are trying
			rem = len(s[i:]) % j
			if rem != 0:
				number_to_try = s[i:-rem]
			else:
				number_to_try = s[i:]
			#print(f"Trying with {number_to_try}")
			if detect_cycle(number_to_try,j):
				return j

		#print("*********")

# Set a big precision to detect all decimals
getcontext().prec=10000

max_l_cycle = 0
found_d = 0
for d in range(1,1001):

	# Remove the fist two chars (0.) and the last one
	# to avoid rounding effects
	s = str(Decimal(1)/Decimal(d))[2:-1]
	
	l_cycle = analyze_number(s)
	print(f"For number {d} the cycle is {l_cycle}")
	if l_cycle:
		if l_cycle > max_l_cycle:
			max_l_cycle = l_cycle
			found_d = d

print(f"{found_d} is the number that generates a cycle of {max_l_cycle} decimals")






	





