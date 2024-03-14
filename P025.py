'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1
.
Hence the first  
12 terms will be:

	F1 = 1
	F2 = 1
	F3 = 2
	F4 = 3
	F5 = 5
	F6 = 8
	F7 = 13
	F8 = 21
	F9 = 34
	F10 = 55
	F11 = 89
	F12 = 144

The 12 th term, , is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''

a = 1
b = 1
c = 1
i = 3
while len(str(c)) < 1001:
	c = a + b
	if len(str(c)) == 1000:
		print ("F(%d) = %d" % (i,c))
		break
	a = b
	b = c
	i = i + 1
	
	
	
	