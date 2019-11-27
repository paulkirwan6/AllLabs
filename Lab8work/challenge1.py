from sense_hat import SenseHat 
from time import sleep

def clear_leds(sense):

	sense.clear()

sense = SenseHat()
clear_leds(sense)

sense.set_pixels
## Insert code HERE ##
## Commands for image
X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

house = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, X, O, O, O, O, X, O,
O, X, O, O, O, O, X, O,
O, X, O, X, X, O, X, O,
O, X, O, X, X, O, X, O,
O, X, O, X, X, O, X, O,
O, O, O, X, X, O, O, O
]

sense.set_pixels(house)

## Added code ends HERE ##
#sense.flip_v()                 #flips it vertically

angle=0

while True:
	if angle>270:
		angle=0
	sense.set_rotation(angle)
	sleep(1)
    	angle+=90

