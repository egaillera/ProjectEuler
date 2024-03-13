'''
n! means n x (n-1) x (n-2) x ... x 3 x 2 x 1

Find the sum of the digits in the number 100!
'''
from time import time

start = time()
	
fact = 1
for i in range(1,101):
	fact = fact*i
	
str_fact = str(fact)

total= 0
for i in range(len(str_fact)):
	#print(str_fact[i])
	total = total + int(str_fact[i])
	

elapsed = time() - start
print("Solution: {0} \t Time elapsed: {1}".format(total, elapsed))