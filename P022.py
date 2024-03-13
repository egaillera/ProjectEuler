'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing 
over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3+15+12+9+14=53, is the 938th name in the list. So, COLIN would obtain a score 
of 938x53 = 49714.

What is the total of all the name scores in the file?
'''


alp = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
	   'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26} 


def alph_value(s):
	value = 0
	for ch in s:
		value = value + alp[ch]
		
	return value
		

file = open('p022_names.txt', 'r') 
names = [name[1:-1] for name in file.read().split(',')]
file.close()
names.sort()

total = 0
i = 1
for name in names:
	print ("%s - %d" % (name,alph_value(name.lower())))
	total = total + i*alph_value(name.lower())
	i = i + 1
	
print(total)
	