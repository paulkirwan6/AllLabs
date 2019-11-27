import time

seconds_total = int(input('Enter number of seconds: '))

while seconds_total > 0:
	minutes = int(round(seconds_total/60))
	seconds = int(seconds_total%60)

	# If either minutes or seconds variables are < 10, add a leading 0
	# Makes printouts all the same length, not a necessary step
	if minutes < 10:
		minutes = str(0) + str(minutes)
	if seconds < 10:
		seconds = str(0) + str(seconds)

	print(str(minutes) + ":" + str(seconds))

	seconds_total -=1
	time.sleep(1)

