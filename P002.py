a = 1
b = 2
n = 0
sum = 0
while n < 4000000:
  n = a + b
  a = b
  b = n
  if n%2 == 0:
    sum += n

print(sum + 2)
