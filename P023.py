'''
A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 
1+2+4+7+14=28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number that can 
be written as the sum of two abundant numbers is 24. By mathematical analysis, it 
can be shown that all integers greater than 28123 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum 
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
'''

def divisors(x):
	d = []
	for i in range(1,int(x/2 + 1)):
		if x%i == 0:
			d.append(i)
	return d
	
def abundant(x):
	if sum(divisors(x)) > x:
		return True
	else:
		return False

# Get the list of all abundants below 28123
ab_list = [x for x in range(1,28123) if abundant(x)]	

# Find all the sums of all abundants to each other
sums = []
j = 0
for i in range(0,len(ab_list)):
	for j in range(i,len(ab_list)):
		if ab_list[i]+ab_list[j] < 28123:
			sums.append(ab_list[i]+ab_list[j])
			#print "%d + %d = %d" % (ab_list[i],ab_list[j],ab_list[i]+ab_list[j])

# All the number between 1 and 28123
b = set(range(1,28123))

# All the numbers between 1 and 28123 that are the sum
# of two abundants
a = set(sums)

# b-a is the numbers between 1 and 28123 that are not 
# the sum of two abundants
print (sum(list(b-a)))
	

