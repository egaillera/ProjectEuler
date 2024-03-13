'''
How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

from datetime import timedelta,date
from dateutil.relativedelta import relativedelta

start_date = date(1900,12,1)
sundays = 0

for i in range(1,1201):
	months = relativedelta(months=i)
	if (start_date + months).weekday() == 6:
		sundays = sundays + 1
		
print(sundays)