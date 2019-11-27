from sense_hat import SenseHat
from time import sleep
from PIL import Image
import numpy as np
#import scipy.io

def load_image(values,sense):
## ##
	#count = 0
	for i in range(0, 7):
		for j in range(0,7):
		#	for k in range(0,2):
		#		print values[i][j][k]
			sense.set_pixel(i,j,values[i][j])
			#count = count+1
		#sense.set_pixels(values[])
## ##

def clear_leds(sense):
##
	sense.clear()
##

path_to_file = "/home/pi/Downloads/8lab/45608329_363300120878491_1050549915429634048_n.jpg"          #path to image
im = Image.open(path_to_file)                #store the image
rgb_im=im.convert('RGB')                     #convert to an RGB image
values=np.array(rgb_im)                      #store the rgb values as an array

##print(values)
sense=SenseHat()

load_image(values,sense)

sense.flip_v()
sense.set_rotation(270)
