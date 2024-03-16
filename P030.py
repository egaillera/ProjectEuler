'''
Surprisingly there are only three numbers that can be written
 as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 
1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum 
of fifth powers of their digits.
'''
result = 0
 
# Upper limit is 9^5 + 9^5 + 9^5 + 9^5 + 9^5
for n in range(100,295245):
    sum_of_powers = 0
    for i in range(0,len(str(n))):
        sum_of_powers += (n // 10**i % 10)**5
    if sum_of_powers == n:
        print(f"found {n} that satisfy requirement")
        result += n

print(f"Solution: {result}")


