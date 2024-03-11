
'''
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

from time import time

N = 20
paths_found = {}

x = 0
y = 0

n_paths = 0

'''
Function that works but it's not optimal: time of execution
is not affordable for N>15
'''
def move(x,y):
	
	global n_paths
	#print(x,y)

	if x == N & y == N:
		#print("------------")
		n_paths += 1

	if y < N:
		move(x,y+1)
	if x < N:	
		move(x+1,y)


'''
Function that calculates recusively the number of paths
from one given point (x,y) to (N,N)
'''
def pathcount(x,y):
   
   # If we've reached the final point, there is only
   # one path
   if ((x,y) == (N,N)):
      return 1
   # If we are outside the lattice, there is no path
   elif ((x > N) or (y > N)):
      return 0
   else:
      # If we have calculated the number of paths for this point,
      # that is already stored in d, we don't do it again 
      if ((x,y) in paths_found):
         return paths_found[(x,y)]
      else:
         # Calculate the two possible paths that start in this point:
         # one path starts by moving down an the other by going right. Store 
         # the number of paths found in paths_found
         number_of_paths = pathcount(x+1,y) + pathcount(x,y+1)
         paths_found[(x,y)] = number_of_paths
         return number_of_paths
	
start = time()	
#move(x,y)
n_paths = pathcount(0,0)
elapsed = time() - start

print("Solution: {0} \t Time elapsed: {1}".format(n_paths, elapsed))