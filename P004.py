'''
A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91*99

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(x):
	
	str_x = str(x)
	half_len = int(len(str_x)/2)
	offset = 0
	if len(str_x) % 2 != 0:
		offset = 1
	
	if str_x[:half_len] == str_x[half_len+offset:][::-1]:
		return True
	else:
		return False

max_pal = 0
for i in range(999,99,-1):
	for j in range(999,99,-1):
		prod = i*j
		if is_palindrome(prod):
			if prod > max_pal:
				max_pal = prod
			
print(max_pal)
		
		