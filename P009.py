'''
A Pythagorean triplet is a set of three natural numbers, a<b<c,for which,

		a^2 + b^2 = c^2

For example: 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a+b+c = 1000.
Find the product abc.

'''

import itertools

def check_pythagorean(a,b,c):
	
	l = [a,b,c]
	l.sort()
	
	if (l[0]*l[0] + l[1]*l[1] == l[2]*l[2]):
		return True
	else:
		return False	

# Combinations of 1000 elements taken 3 at a time
for tp in itertools.combinations(range(1000),3):
	if tp[0]+tp[1]+tp[2] == 1000:
		if check_pythagorean(tp[0],tp[1],tp[2]):
			print(tp)
			print(str(tp[0]*tp[1]*tp[2]))
			exit()

	