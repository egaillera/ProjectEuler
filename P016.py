'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import math

total = 0
for c in str(pow(2,1000)):
    total = total + int(c)

print(total)
