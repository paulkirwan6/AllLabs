import time

seconds_total = int(raw_input('Enter number of seconds:	'))  # Get input from user

i = 0  # start counter

while i < seconds_total:
	minutes = int(round((seconds_total-i)/60))  # Get number of minutes
	seconds = int((seconds_total-i)%60)         # Get number of seconds
	
	# If either minutes or seconds variables are < 10, add a leading 0
	# Makes printouts all the same length, not a necessary step
	if minutes < 10:
		minutes = str(0) + str(minutes)
	
	if seconds < 10:
		seconds = str(0) + str(seconds)

	print(str(minutes) + ":" + str(seconds))  # Print counter value to screen

	i+=1  # Increment counter
	time.sleep(1)  # sleep for 1 second

