'''
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is.,
    (1+2+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025-385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum
'''

from functools import reduce

r = range(1,101)

sum_of_squares = reduce( (lambda x, y: x + y), map((lambda x: x **2), r) ) 
total_sum = reduce( (lambda x, y: x + y), r )
square_of_sum = total_sum*total_sum

print(square_of_sum - sum_of_squares)
