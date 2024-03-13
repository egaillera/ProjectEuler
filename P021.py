'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than  
n which divide evenly into n). if d(a) = b and d(b) = a, where a <> b, then
a and b are an amicable par and each of a and b are called amicable numbers.

For example the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110;
therefore d(220)=284. The proper divisors of 284 are 1,2,4,71 and 142; so 
d(284)=220.

Evalute the sum of all the amicable numbers under 10000
'''
def d(x):
	s = 0
	for i in range(1,int(x/2) + 1):
		if x%i == 0:
			s = s + i
	return s		
		

myset = []		
for n in range(2,10001):
	p = d(n)
	if (d(p) == n) & (p != n):
		if n not in myset:
			myset.append(n)
		
		print(f"Found an amicable par: ({n},{p})")
		
print(f"List of amicables numbers below 10000: {myset}")
s = 0
for i in myset:
	s = s + i
	
print(f"Sum: {s}")