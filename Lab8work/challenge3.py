from sense_hat import SenseHat
import numpy as np
from time import sleep

def add_dangerous_pixels(sense,nr_dang_pix):
	dangerous_coord = [] # list where all the x,y coordinates are stored
	for i in range(0,nr_dang_pix):
		##
		## randomly choose x,y coordinates for the dangerous pixels
		x = np.random.randint(0,8)
		y = np.random.randint(0,8)
		candidate_pixel = (x,y)
		##
	
	#		candidate_pixel = check_collision(candidate_pixel)
		dangerous_coord.append(candidate_pixel)
	return dangerous_coord

def check_collision(pixel):

	#goal_pixel = ([np.random.randint(0,8),np.random.randint(0,8)])
	for j in dangerous_coord:
		if(pixel == j):
			pixel = (np.random.randint(0,8),np.random.randint(0,8))
			check_collision(pixel)
	return pixel

def check_boundary(x,y):
	##
	## Add code to check if x,y are going beyond the limits of the matrix
	if(x > 7):
		x = 7
	elif(x < 0):
		x = 0
	if(y > 7):
		y = 7
	elif( y < 0):
		y = 0
	##
	return x,y

sense = SenseHat()
sense.clear()
number_of_dangerous_pixels = 4
dangerous_coord = add_dangerous_pixels(sense, number_of_dangerous_pixels)

## Adding dangerous pixels to the LED matrix:
r = (255,0,0)
for set in dangerous_coord:
	print (set)
	sense.set_pixel(set[0],set[1],r)

white=(255,255,255)
x,y=6,6 # location where the moving pixel is being 'spawned'
sense.set_pixel(x,y,white)
## Set wining pixel
goal_pixel = (np.random.randint(0,8),np.random.randint(0,8))
goal_pixel = check_collision(goal_pixel)
##
## Add code to generate "objective pixel"

##
sense.set_pixel(goal_pixel[0],goal_pixel[1],0,255,0)
alive=True # flag to check where the moving pixel is located

while alive:
	for event in sense.stick.get_events():

		if event.direction=='up':
			sense.set_pixel(x,y,0,0,0)
			y-=1
			x,y=check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if event.direction=='down':
			sense.set_pixel(x,y,0,0,0)
			y+=1
			x,y=check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if event.direction=='left':
			sense.set_pixel(x,y,0,0,0)
			x-=1
			x,y=check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if event.direction=='right':
			sense.set_pixel(x,y,0,0,0)
			x+=1
			x,y=check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if (x,y) in dangerous_coord:
			sense.show_message('Game over')
			print('Game Over')
			alive=False # Game is over, because you lost
		if (x,y) == (goal_pixel[0],goal_pixel[1]):
			sense.show_message('Victory')
			alive=False # Game is over, because you won.
