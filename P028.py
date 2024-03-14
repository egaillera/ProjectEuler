'''
Starting with the number  and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

	21 22 23 24 25
	20  7  8  9 10
	19  6  1  2 11
	18  5  4  3 12
	17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
'''

import math

size = 1001

def walk_right(length,w,x,y):
	for i in range(0,length):
		m[x+1][y] = w + 1
		w = w + 1
		x = x + 1
		if (w == size*size):
			return w,x,y
	return w,x,y
		
def walk_down(length,w,x,y):
	for i in range(0,length):
		m[x][y-1] = w + 1
		w = w + 1
		y =  y - 1
	return w,x,y

def walk_left(length,w,x,y):
	for i in range(0,length):
		m[x-1][y] = w + 1
		w = w + 1
		x = x - 1
	return w,x,y

def walk_up(length,w,x,y):
	for i in range(0,length):
		m[x][y+1] = w + 1
		w = w + 1
		y =  y + 1
	return w,x,y

def print_matrix():
	print("############",end="")
	for y in range(size-1,-1,-1):
		print("\n")
		for x in range(size):
			print(m[x][y],end="\t")
	print("\n############")

# Inicializacion
m = [[0 for x in range(size)] for y in range(size)] 
m[int(size/2)][int(size/2)] = 1
l = 1
w = 1
x = int(size/2)
y = int(size/2)

while (1):
	w,x,y = walk_right(l,w,x,y)
	if (w==size*size):
		break
	w,x,y = walk_down(l,w,x,y)

	l = l + 1

	w,x,y = walk_left(l,w,x,y)
	w,x,y = walk_up(l,w,x,y)
	
	l = l + 1

print_matrix()

sum_first_diagonal = sum(m[i][i] for i in range(size))
sum_second_diagonal = sum(m[i][size-i-1] for i in range(size))

print("Suma diagonales (%d,%d): %d" % (sum_first_diagonal, sum_second_diagonal,
                                       sum_first_diagonal+sum_second_diagonal - 1))

